---
title: Support and Troubleshooting | Veeam Kasten
url: https://docs.kasten.io/latest/operating/support
hostname: kasten.io
description: If you have questions or need support, please refer to [Veeam Kasten
sitename: docs.kasten.io
date: "2026-01-01"
fingerprint: "2efaf549410420e7"
---
Version: 9.0.9 (latest)

# Support and Troubleshooting

If you have questions or need support, please refer to Veeam Kasten Community Support or open a case via https://my.veeam.com.

## Supported Kubernetes Versions

Veeam Kasten currently supports deployments running on the following certified Kubernetes distributions and respective OpenShift versions:

Veeam Kasten does not support distribution versions that are no longer actively supported by their respective vendor or community.

| Kubernetes | RedHat Openshift | Notes | 
|---|---|---|
| 1.36 |  |  | 
| 1.35 | 4.22 |  | 
| 1.34 | 4.21 |  | 
| 1.33 | 4.20 |  | 
| 1.32 | 4.19 | Kubernetes version \*only\* supported when deployed as an OpenShift cluster | 
| 1.31 | 4.18 | Kubernetes version \*only\* supported when deployed as an OpenShift cluster | 
| 1.30 | 4.17 | Kubernetes version \*only\* supported when deployed as an OpenShift cluster | 
| 1.29 | 4.16 | Kubernetes version \*only\* supported when deployed as an OpenShift cluster | 

## Gathering Debugging Information

Admin users running 4.5.7 or later can get support logs from the
  `System Information` page under the \[Settings\] menu in the
  navigation sidebar.

Alternatively, if you run into problems with Veeam Kasten, please run
  these commands on your cluster as a first step to get information to
  support. The script assumes that your default `kubectl` context is
  pointed to the cluster you have installed Veeam Kasten on and that Veeam
  Kasten is installed in the `kasten-io` namespace.

```
$ curl -s https://docs.kasten.io/downloads/9.0.9/tools/k10_debug.sh | bash;
```
By default, the debug script will generate a compressed archive file
  `k10_debug_logs.tar.gz` which will have separate log files for Veeam
  Kasten services.

If you installed Veeam Kasten in a different namespace or want to log to a different file you can specify additional option flags to the script:

```
$ curl -s https://docs.kasten.io/downloads/9.0.9/tools/k10_debug.sh | \
    bash -s -- -n <k10-namespace> -o <logfile-name>;
```
See the script usage message for additional help.

The debug script can optionally gather metrics from the Prometheus
  server installed by Veeam Kasten, by specifying the `--prom-duration`
  flag with a value indicating the desired duration (e.g. "1d",
  "3h25m"). The start time of the metric collection is implicitly
  assumed to be the current time less the specified duration, but can be
  adjusted with the `--prom-start-time` flag to specify a time in the
  past. The format is either the simple duration string that is accepted
  by the duration flag, or a string that is parsable with the `date`
  command, which could be a timestamp or a free form relative or absolute
  time specification. For example:

```
$ curl -s https://docs.kasten.io/downloads/9.0.9/tools/k10_debug.sh | \
    bash -s -- --prom-duration 4h30m --prom-start-time "-2 days -3 hours"
```
would collect 270 minutes of metrics starting from 51 hours in the past.

Metrics capture only works with the Prometheus instance installed by
    Veeam Kasten. The specified duration directly impacts the size of the
    captured metrics data so constrain the duration accordingly. One can
    also consider using the `--prom-metrics-only` flag to separate the
    collection of metrics from the collection of the logs.

The collected logs also contain a `# K10: Prometheus Health Check`
  section with a curated set of metrics to evaluate storage and retention
  health of the Prometheus instance.

### Changing the Log Level

Veeam Kasten services log at `info` by default. Raising the level to `debug`,
  for the whole installation or for a single service, before gathering debugging
  information often gives support the detail they need. Only `info` and `debug`
  are supported, in any letter case. A missing or empty global level uses `info`
  without a warning. Any other value is treated as `info`, and the service logs
  a warning naming the value it received.

Live changes and per-service overrides require
  `features.restartlessLogLevelChange=true`. New installations enable this
  feature by default. When upgrading an older installation with
  `--reuse-values`, Helm retains the old defaults, which may not include this
  feature. Enable it explicitly once:

```
$ helm upgrade k10 kasten/k10 --namespace kasten-io --reuse-values \
    --set features.restartlessLogLevelChange=true
```
Enabling the feature restarts the pods. Wait for that rollout to complete before making live changes.

#### For All Services

Set the `logLevel` Helm value:

```
$ helm upgrade k10 kasten/k10 --namespace kasten-io --reuse-values \
    --set logLevel=debug
```
This restarts the Veeam Kasten pods, because some components, such as init containers, read the level only at startup.

To change the level without a restart, edit the `loglevel` key of the
  `k10-config` ConfigMap. Running services pick up the new level within seconds:

```
$ kubectl --namespace kasten-io patch configmap k10-config \
    --type merge --patch '{"data":{"loglevel":"debug"}}'
```
The chart renders this key, so the next `helm upgrade` puts back the value of
  `logLevel`. Set `logLevel` for a level that has to outlive an upgrade.

#### For a Single Service

Use the `logLevelOverrides` Helm value, keyed by service name. The override takes
  effect within seconds and does not restart the service:

```
$ helm upgrade k10 kasten/k10 --namespace kasten-io --reuse-values \
    --set logLevelOverrides.executor=debug
```
To remove an override while reusing values, set it to an empty string:

```
$ helm upgrade k10 kasten/k10 --namespace kasten-io --reuse-values \
    --set-string logLevelOverrides.executor=
```
Setting the override to `null` does not remove it: with `--reuse-values`,
  Helm restores the previous override from the installed release, although
  `helm get values` no longer lists it. Use the empty string command above to
  remove an existing override.

An unsupported level, or the name of a service that does not read its level from the ConfigMap, fails the install or upgrade. The error lists the supported levels or service names, respectively. An override for a service that is switched off is left out.

The same can be done without Helm by adding a `loglevel.<service>` key to the
  `k10-config` ConfigMap:

```
$ kubectl --namespace kasten-io patch configmap k10-config \
    --type merge --patch '{"data":{"loglevel.executor":"debug"}}'
```
A key added this way stays until it is removed by hand, so an unrelated
  `helm upgrade` does not reset it. Naming the same service in
  `logLevelOverrides` takes over from then on.

#### What Follows the Level

- Pods that Veeam Kasten starts for a single operation, such as data movement, get the level of the service that started them. This includes a file-level recovery session and the mount process that serves it.
- 
    Veeam Kasten does not add the inherited `LOG_LEVEL` environment value to
    pods using other images. Explicit pod settings are preserved.
- 
    For operation processes that use `LOG_LEVEL`, an explicit value in an
    ActionPodSpec or pod-spec override takes precedence over the inherited
    environment value. The datamover daemon uses a generated `--log-level` command-line argument; changing `LOG_LEVEL` alone does not override that
    argument.
- The Kanister controller follows the level like the other services.
- The `insights` service keeps the level it started with.

#### Turning It Off

Set `features.restartlessLogLevelChange` to `false` to have every service read
  the level once at startup, as in earlier releases. Per-service overrides are
  then left out of the ConfigMap and come back when the value is set to `true`
  again.

### Application Debug Information

If you are having issues with a particular application, please also gather the following information.

```
## Get Application Information
$ kubectl get pvc -oyaml --namespace <APP NAMESPACE>
$ kubectl api-resources --verbs=list --namespaced -o name | \
    xargs -n 1 kubectl get --show-kind --ignore-not-found --namespace <APP NAMESPACE>
```
Please also get the Helm status:

```
## If deployed via Helm
$ helm status <RELEASE NAME> --namespace=<APP NAMESPACE>
```
## Veeam Kasten Tools

The `k10tools` binary has commands that can help with validating if a cluster
  is setup correctly before installing Veeam Kasten and for debugging Veeam
  Kasten's micro services.

To learn more about this, see Veeam Kasten Tools.

## Storage Class Validation

`k10tools` provides an option to validate storage classes via
  CSI Capabilities Check or
  Generic Volume Snapshot Capabilities Check commands. It is also possible for admin users to validate
  storage classes from the Veeam Kasten dashboard, under the
  `System Information` page of the `Settings` menu in the navigation
  sidebar. The state "Unknown" is shown until validation is run.

## Security Disclosures

We value the critical role that the security community plays in helping us protect the confidentiality, integrity, and availability of our software, services, and information. If you have information about security vulnerabilities that affect Kasten software, services, or information, please report it via our vulnerability disclosure program.
