| Proxmox | Datacenter | Manager |     |
| ------- | ---------- | ------- | --- |
Documentation
|     |         | Release | 1.1.9 |
| --- | ------- | ------- | ----- |
|     | Proxmox | Support | Team  |
Wednesday,14October2026

TABLE OF CONTENTS
1 Introduction 2
1.1 WhatisProxmoxDatacenterManager?. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 FeatureOverview. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 TechnologyStack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 GettingHelp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.1 EnterpriseSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.2 CommunitySupportForum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.3 MailingLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.4 BugTracker . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 License . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Installation 5
2.1 SystemRequirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.1 MinimumServerRequirements,forEvaluation . . . . . . . . . . . . . . . . . . 5
2.1.2 RecommendedServerSystemRequirements . . . . . . . . . . . . . . . . . . . 5
2.1.3 SupportedWebBrowsersforAccessingtheWebInterface . . . . . . . . . . . . 5
2.2 InstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.1 PrepareInstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.2 PrepareaUSBFlashDriveasInstallationMedium . . . . . . . . . . . . . . . . . 6
2.2.3 InstructionsforGNU/Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.4 InstructionsformacOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2.5 InstructionsforWindows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2.6 UsetheInstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.7 InstallProxmoxDatacenterManagerUnattended . . . . . . . . . . . . . . . . . 8
2.2.8 InstallProxmoxDatacenterManageronDebian . . . . . . . . . . . . . . . . . . 8
2.3 DebianPackageRepositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.1 RepositoryFormats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.2 DebianBaseRepositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.3 ProxmoxDatacenterManagerEnterpriseRepository . . . . . . . . . . . . . . . 10
2.3.4 ProxmoxDatacenterManagerNo-SubscriptionRepository . . . . . . . . . . . 10
2.3.5 ProxmoxDatacenterManagerTestRepository . . . . . . . . . . . . . . . . . . . 10
2.3.6 ProxmoxDatacenterManagerDebugSymbolRepository . . . . . . . . . . . . 11
2.3.7 SecureApt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3 GraphicalUserInterface 13
3.1 Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2 Login . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3 UserInterfaceOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4 Sidebar. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.1 Dashboard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4.2 Views . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4.3 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.4 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.5 Administration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
i

3.4.6 SDN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.7 Ceph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.8 Guests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.9 Remotes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 SDNIntegration 20
4.1 StatusOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.2 EVPNIntegration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.2.1 Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5 Remotes 22
5.1 ResourceOperation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
5.2 DataCollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
5.3 ProxmoxVERemote . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
5.4 ProxmoxBackupServerRemote . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5.5 ConnectionandCertificateTroubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . 23
6 Ceph 24
6.1 ClusterOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
6.2 ClusterDetail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
6.2.1 Dashboard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
6.2.2 Monitors,Managers,OSDs,Pools,CephFS,andFlags . . . . . . . . . . . . . . . 25
6.3 OpenWebUI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
6.4 Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7 Guests 27
7.1 ListandTreeView . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.2 Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.3 GuestActions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.4 Snapshots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.5 Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
8 AutomatedInstallations 30
8.1 Overview. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
8.2 PreparedAnswers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
8.2.1 Targetfilter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
8.2.2 Templating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.2.3 SubscriptionKey . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.3 Authenticationtokenmanagement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.4 PreparinganISO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
9 Views 33
9.1 ResourceSelection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
9.1.1 FilterTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
9.2 CustomizableDashboard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
9.2.1 Widgets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
9.2.2 MapWidget . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
9.3 AccessControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
10 SubscriptionRegistry 35
10.1 KeyPool . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
10.2 NodeSubscriptionStatus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
10.3 AssignmentandClearing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
10.4 Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
11 Authentication&AccessControl 38
11.1 UserConfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
11.2 APITokens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
11.3 AccessControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
ii

11.3.1 Privileges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
11.3.2 AccessRoles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
11.3.3 ObjectsandPaths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
11.3.4 Configuration&Management. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
11.3.5 APITokenPermissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
11.4 Two-FactorAuthentication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
11.4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
11.4.2 AvailableSecondFactors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
12 HostSystemAdministration 42
12.1 ZFSonLinux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
12.1.1 Hardware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
12.1.2 ZFSAdministration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
12.2 HostBootloader . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
12.2.1 PartitioningSchemeUsedbytheInstaller . . . . . . . . . . . . . . . . . . . . . . 48
12.2.2 SynchronizingtheContentoftheESPwithproxmox-boot-tool . . . . . . . 48
12.2.3 DeterminewhichBootloaderisUsed . . . . . . . . . . . . . . . . . . . . . . . . 50
12.2.4 Grub . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
12.2.5 Systemd-boot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
12.2.6 EditingtheKernelCommandline . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
12.2.7 OverridetheKernel-VersionfornextBoot . . . . . . . . . . . . . . . . . . . . . 52
12.2.8 SecureBoot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
12.3 CertificateManagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
12.3.1 CertificatesfortheAPIandSMTP . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
12.3.2 UploadCustomCertificate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
12.3.3 TrustedcertificatesviaLet’sEncrypt(ACME) . . . . . . . . . . . . . . . . . . . . 56
12.3.4 ACMEHTTPChallengePlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
12.3.5 ACMEDNSAPIChallengePlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
12.3.6 AutomaticrenewalofACMEcertificates . . . . . . . . . . . . . . . . . . . . . . . 58
12.3.7 ManuallyChangeCertificateovertheCommandLine . . . . . . . . . . . . . . . 58
12.4 ServiceDaemons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
12.4.1 proxmox-datacenter-api . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
12.4.2 proxmox-datacenter-privileged-api . . . . . . . . . . . . . . . . . . . . . 59
12.5 Command-lineTools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
12.5.1 proxmox-datacenter-manager-client . . . . . . . . . . . . . . . . . . . . . 59
12.5.2 proxmox-datacenter-manager-admin . . . . . . . . . . . . . . . . . . . . . 59
13 FAQ 60
13.1 WhatdistributionisProxmoxDatacenterManager(PDM)basedon? . . . . . . . . . . 60
13.2 WillProxmoxDatacenterManagerrunona32-bitprocessor? . . . . . . . . . . . . . . 60
13.3 HowlongwillmyProxmoxDatacenterManagerversionbesupported? . . . . . . . . 60
13.4 HowcanIupgradeProxmoxDatacenterManagertothenextpointrelease?. . . . . . 60
13.5 IsthereadedicatedsubscriptionfortheProxmoxDatacenterManager? . . . . . . . . 61
13.6 HowcanIgetEnterpriseSupportfortheProxmoxDatacenterManager?. . . . . . . . 61
13.7 HowcanIgetaccesstotheProxmoxDatacenterManagerEnterpriseRepository? . . 61
A CommandSyntax 62
A.1 proxmox-datacenter-manager-admin . . . . . . . . . . . . . . . . . . . . . . . . . . 62
A.2 proxmox-datacenter-manager-client . . . . . . . . . . . . . . . . . . . . . . . . . 67
B ConfigurationFiles 104
B.1 remotes.cfg. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
B.1.1 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
B.2 views.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
B.2.1 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
C Roadmap 106
C.1 ReleaseHistory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
C.1.1 ProxmoxDatacenterManager1.1 . . . . . . . . . . . . . . . . . . . . . . . . . . 107
iii

C.1.2 ProxmoxDatacenterManager1.0 . . . . . . . . . . . . . . . . . . . . . . . . . . 112
D MarkdownPrimer 123
D.1 MarkdownBasics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
D.1.1 Headings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
D.1.2 Emphasis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
D.1.3 Links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
D.1.4 Lists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
D.1.5 Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
D.1.6 BlockQuotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
D.1.7 CodeandSnippets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
E GNUFreeDocumentationLicense 126
iv

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Copyright(C)2023-2026,ProxmoxServerSolutionsGmbH
Version1.1.9--Wednesday,14October2026
Permissionisgrantedtocopy,distributeand/ormodifythisdocumentunderthetermsoftheGNU
FreeDocumentationLicense,Version1.3oranylaterversionpublishedbytheFreeSoftwareFoun-
dation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
licenseisincludedinthesectionentitled”GNUFreeDocumentationLicense”.
TABLEOFCONTENTS 1

CHAPTER
ONE
INTRODUCTION
1.1 What is Proxmox Datacenter Manager?
ProxmoxDatacenterManagerisacentralizedmanagementplatformdesignedtooverseeProxmox
VirtualEnvironmentandProxmoxBackupServerinstancesacrossdisjointedlocations. Itprovides
aunifiedviewofallregisteredresources,includingnodes,virtualmachines,containers,storages,
andbackupdatastores,regardlessoftheirgeographiclocation.
Thissolutionsupportsmanagingbothsingle-nodeinstallationsandcomplexclusters. Inthecon-
textofProxmoxDatacenterManager,theseconnectedinstancesarereferredtoasremotes.
The platform allows for active resource control, enabling administrators to execute power oper-
ations, apply system updates, and perform live migrations across the infrastructure. It acts as
ahigh-levelcontrolplanewhileprovidingaseamlesstransition(”escapehatch”)tothenativeweb
interfacesofindividualremotesforgranularconfiguration. Thisarchitectureensuresalooselycou-
pledsystemwherethecentralmanagerdoesnotbecomeabottleneckorasinglepointoffailure
fortheoperationoftheunderlyingremotes.
1.2 Feature Overview
ProxmoxDatacenterManagerprovidesthefollowingcorecapabilities:
• CentralizedInventory: Connectandmanageascalablenumberofindependentnodesand
clusters(”Datacenters”)fromasingleinterface.
2

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• UnifiedResourceMonitoring: Viewthestatus,health,andloadofglobalresources,includ-
ingnodes,virtualguests,andstoragebackends.
• Global Dashboard: A high-level dashboard visualizes the state of all remotes, highlighting
potentialissuessuchashighresourceconsumption(CPU&memory)orfailedtasks.
• TaskAggregation: Centralizedaccesstotasklogsacrosstheentireinfrastructureforauditing
andtroubleshooting.
• LifecycleManagement: Performbasicpoweroperations(start,stop,reboot,shutdown)on
nodesandvirtualguestsdirectlyfromthecentralview.
• Update Management: Monitor available updates and security patches across the server
fleet.
• Cross-ClusterMigration: Executelivemigrationsofvirtualguestsbetweennodes,support-
ingtransferswithinthesameremote(cluster)oracrossdifferentremotes.
• Advanced Access Control: Supports enterprise authentication standards, including
LDAP/ActiveDirectoryandOpenIDConnect(SSO),integratedwithagranularpermissionsys-
tem.
• CertificateManagement: IntegratedACMEsupport(e.g., Let’sEncrypt)forautomatedcer-
tificatemanagement.
1.3 Technology Stack
ProxmoxDatacenterManagerreliesonamodern,secure,andperformanttechnologystack:
• CoreLanguage: TheprojectisprimarilydevelopedintheRustprogrammingLanguage,en-
suringmemorysafetyandhighperformance.
• BackendArchitecture:
• ThebackendexposesaJSON-basedRESTAPI.
• Itutilizesadual-daemonarchitecturestandardforProxmoxprojects:
1. MainAPIDaemon: Runsasanunprivilegedusertohandleexternalrequests,minimiz-
ingtheattacksurface.
2. PrivilegedDaemon: RunsasrootandlistensexclusivelyonalocalUNIXsockettoexe-
cutesystem-leveloperations.
• The backend leverages the existing, battle-tested REST/API stack from Proxmox Backup
Server.
• CommunicationoccursoverTCPport443(HTTPS).
• FrontendArchitecture:
– ThewebinterfaceisaSinglePageApplication(SPA)writteninRustusingtheYewframe-
work.
– ItiscompiledtoWebAssembly(Wasm),offeringhighperformanceandtypesafetysim-
ilartothebackend.
– TheUIcomponentsarebuiltupontheproxmox-yew-widget-toolkit,enablingaconsistent
lookandfeelacrosstheProxmoxecosystem.
1.3. TechnologyStack 3

ProxmoxDatacenterManagerDocumentation,Release1.1.9
1.4 Getting Help
1.4.1 EnterpriseSupport
CustomerswithanactiveBasic,Standard,orPremiumsubscriptionfortheirProxmoxremotesgain
accesstotheProxmoxDatacenterManagerEnterpriseRepositoryandtechnicalsupport.
Formoreinformation,pleasevisithttps://www.proxmox.comorcontact<mailto:sales@proxmox.
com>.
1.4.2 CommunitySupportForum
TheProxmoxCommunityForumisaprimaryresourceforuserdiscussionsandknowledgesharing.
ModeratedbytheProxmoxsupportteam,itconnectsaglobaluserbaseandservesasanextensive
databaseofsolutionsandconfigurations.
1.4.3 MailingLists
ProxmoxDatacenterManagerisopen-sourcesoftware. Thedevelopmentmailinglististheprimary
communicationchannelforcontributingdevelopers:
Mailinglistfordevelopers
PDMDevelopmentList
1.4.4 BugTracker
Proxmoxmaintainsapublicissuetrackerathttps://bugzilla.proxmox.com. Thissystemtracksbug
reportsandfeaturerequests. Userscansubscribetoissuestoreceivenotificationsregardingthe
statusandresolutionofsubmittedissues.
1.5 License
Copyright(C)2023-2026,ProxmoxServerSolutionsGmbH
ThissoftwareiswrittenbyProxmoxServerSolutionsGmbH<support@proxmox.com>.
Proxmox Datacenter Manager is free and open-source software: you can use it, redistribute it,
and/ormodifyitunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedbythe
FreeSoftwareFoundation,eitherversion3oftheLicense,or(atyouroption)anylaterversion.
Thisprogramisdistributedinthehopethatitwillbeuseful,butWITHOUTANYWARRANTY;with-
outeventheimpliedwarrantyof MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.
SeetheGNUAfferoGeneralPublicLicenseformoredetails.
YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicensealongwiththisprogram.
Ifnot,seeAGPL3.
1.4. GettingHelp 4

CHAPTER
TWO
INSTALLATION
ProxmoxDatacenterManagercaneitherbeinstalledwithagraphicalinstallerorontopofDebian
fromtheprovidedpackagerepository.
2.1 System Requirements
We recommend using high quality server hardware when running Proxmox Datacenter Manager
inproduction. WhilenomanagedremoteorresourcedependsonProxmoxDatacenterManager
torun,youmightfindthatProxmoxDatacenterManagerwillbecomeaconvenientandcriticaltool
inyouroperationsfastenough.
2.1.1 MinimumServerRequirements,forEvaluation
Theseminimumrequirementsareforevaluationpurposesonlyandshouldnotbeusedinproduc-
tion.
• CPU:64bit(x86-64orAMD64),1+Cores
• Memory(RAM):1GiBRAM
• Harddrive: morethan10GBofspace.
• Networkcard(NIC)
2.1.2 RecommendedServerSystemRequirements
• CPU:ModernAMDorIntel64-bitbasedCPU,withatleast2cores
• Memory: minimum4GiBfortheOS.
• OSstorage:
– 40GB,ormore,freestoragespace
– UseahardwareRAIDwithbatteryprotectedwritecache(BBU)oraredundantZFSsetup
(ZFSisnotcompatiblewithahardwareRAIDcontroller).
• RedundantMulti-GBit/snetworkinterfacecards(NICs)
2.1.3 SupportedWebBrowsersforAccessingtheWebInterface
To access the server’s web-based user interface, we recommend using one of the following
browsers:
• Firefox,areleasefromthecurrentyear,orthelatestExtendedSupportRelease
• Chrome,areleasefromthecurrentyear
• Microsoft’scurrentlysupportedversionofEdge
• Safari,areleasefromthecurrentyear
5

ProxmoxDatacenterManagerDocumentation,Release1.1.9
2.2 Installation Medium
ProxmoxDatacenterManagercanbeinstalledviadifferentmethods. Therecommendedmethodis
theusageofaninstallationmedium,tosimplyboottheinteractiveinstaller.
2.2.1 PrepareInstallationMedium
DownloadtheinstallerISOimagefromhttps://www.proxmox.com/downloads.
TheProxmoxDatacenterManagerinstallationmediumisahybridISOimage. Itworksintwoways:
• AnISOimagefilereadytoburntoaDVD.
• Arawsector(IMG)imagefilereadytocopytoaUSBflashdrive(USBstick).
UsingaUSBflashdrivetoinstallProxmoxDatacenterManageristherecommendedwaysinceitis
thefasterandmorefrequentlyavailableoptionthesedays.
2.2.2 PrepareaUSBFlashDriveasInstallationMedium
Theflashdriveneedstohaveatleast2GBofstoragespace.
(cid:174) Note
Do not use UNetbootin. It does not work with the Proxmox Datacenter Manager installation
image.
(cid:489) Important
ExistingdataontheUSBflashdrivewillbeoverwritten. Therefore,makesurethatitdoesnot
containanystillneededdataandunmountitafterwardsagainbeforeproceeding.
2.2.3 InstructionsforGNU/Linux
OnUnix-likeoperatingsystemsusetheddcommandtocopytheISOimagetotheUSBflashdrive.
FirstfindthecorrectdevicenameoftheUSBflashdrive(seebelow). Thenruntheddcommand.
Dependingonyourenvironment,youwillneedtohaverootprivilegestoexecutedd.
# dd bs=1M conv=fdatasync if=./proxmox-datacenter-manager_*.iso of=/dev/XYZ
(cid:174) Note
Be sure to replace /dev/XYZ with the correct device name and adapt the input filename (if)
path.
(cid:1002) Caution
Beverycareful,anddonotoverwritethewrongdisk!
2.2. InstallationMedium 6

ProxmoxDatacenterManagerDocumentation,Release1.1.9
FindtheCorrectUSBDeviceName
TherearetwowaystofindoutthenameoftheUSBflashdrive. Thefirstoneistocomparethelast
linesofthedmesgcommandoutputbeforeandafterpluggingintheflashdrive. Thesecondway
istocomparetheoutputofthelsblkcommand. Openaterminalandrun:
# lsblk
ThenpluginyourUSBflashdriveandrunthecommandagain:
# lsblk
Anewdevicewillappear. Thisistheoneyouwanttouse. Tobeontheextrasafesidecheckifthe
reportedsizematchesyourUSBflashdrive.
2.2.4 InstructionsformacOS
Opentheterminal(queryTerminalinSpotlight).
Convertthe.isofileto.dmgformatusingtheconvertoptionof hdiutil,forexample:
# hdiutil convert proxmox-datacenter-manager_*.iso -format UDRW -o proxmox-datacenter-manager_
,→*.dmg
(cid:174) Note
macOStendstoautomaticallyadd.dmgtotheoutputfilename.
Togetthecurrentlistofdevicesrunthecommand:
# diskutil list
NowinserttheUSBflashdriveandrunthiscommandagaintodeterminewhichdevicenodehas
beenassignedtoit. (e.g.,/dev/diskX).
# diskutil list
# diskutil unmountDisk /dev/diskX
(cid:174) Note
replaceX withthedisknumberfromthelastcommand.
# sudo dd if=proxmox-datacenter-manager_*.dmg bs=1M of=/dev/rdiskX
(cid:174) Note
rdiskX,insteadofdiskX,inthelastcommandisintended. Itwillincreasethewritespeed.
2.2.5 InstructionsforWindows
UsingEtcher
Etcherworksoutofthebox. DownloadEtcherfromhttps://etcher.io. Itwillguideyouthroughthe
processofselectingtheISOandyourUSBflashdrive.
2.2. InstallationMedium 7

ProxmoxDatacenterManagerDocumentation,Release1.1.9
UsingRufus
Rufusisamorelightweightalternative,butyouneedtousetheDDmodetomakeitwork. Down-
loadRufusfromhttps://rufus.ie/. Eitherinstallitorusetheportableversion. Selectthedestination
driveandthedownloadedProxmoxISOfile.
(cid:489) Important
OnceyouclickStart, youhavetoclickNoonthedialogaskingtodownloadadifferentversion
ofGrub. InthenextdialogselectDDmode.
2.2.6 UsetheInstallationMedium
Insert the created USB flash drive (or DVD) into your server. Continue by reading the installer
chapter,whichalsodescribespossiblebootissues.
Usingourprovideddiskimage(ISOfile)istherecommendedinstallationmethod,asitincludesa
convenientinstaller,acompleteDebiansystemaswellasallnecessarypackagesfortheProxmox
DatacenterManager.
Once you have created an installation_medium, the booted installer will guide you through the
setup process. It will help you to partition your disks, apply basic settings such as the language,
timezoneandnetworkconfiguration,andfinallyinstallallrequiredpackageswithinminutes.
Asanalternativetotheinteractiveinstaller,advancedusersmaywishtoinstallProxmoxDatacenter
Managerunattended.
WithsufficientDebianknowledge,youcanalsoinstallProxmoxDatacenterManagerontopofDe-
bianyourself.
2.2.7 InstallProxmoxDatacenterManagerUnattended
ItispossibletoinstallProxmoxDatacenterManagerautomaticallyinanunattendedmanner. This
enablesyoutofullyautomatethesetupprocessonbare-metal. Oncetheinstallationiscomplete
and the host has booted up, automation tools like Ansible can be used to further configure the
installation.
Thenecessaryoptionsfortheinstallermustbeprovidedinananswerfile. Thisfileallowstheuse
offilterrulestodeterminewhichdisksandnetworkcardsshouldbeused.
Tousetheautomatedinstallation,itisfirstnecessarytoprepareaninstallationISO.Formoredetails
andinformationontheunattendedinstallationseeourwiki.
2.2.8 InstallProxmoxDatacenterManageronDebian
Proxmox ships as a set of Debian packages which can be installed on top of a standard Debian
installation. AfterconfiguringtheDebianPackageRepositories,youneedtorun:
# apt update
# apt install proxmox-datacenter-manager-container-meta
Theabovecommandskeepthecurrent(Debian)kernelandinstallaminimalsetofrequiredpack-
ages.
YoucaninstalltheProxmoxdefaultkernelwithZFSsupportbyusingtheregularmeta-package:
# apt update
# apt install proxmox-datacenter-manager-meta
2.2. InstallationMedium 8

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:1002) Caution
InstallingProxmoxDatacenterManagerontopofanexistingDebianinstallationlookseasy,but
itassumesthatthebasesystemandlocalstoragehavebeensetupcorrectly. Ingeneralthisis
nottrivial, especiallywhenLVMorZFSisused. Thenetworkconfigurationiscompletelyupto
youaswell.
(cid:174) Note
YoucanaccessthewebinterfaceoftheProxmoxDatacenterManagerwithyourwebbrowser,
usingHTTPSonport8443. Forexampleathttps://<ip-or-dns-name>:8443
2.3 Debian Package Repositories
All Debian based systems use APT_ as a package management tool. The lists of repositories are
definedin/etc/apt/sources.list andthe.listor.sourcesfilesfoundinthe/etc/apt/
sources.d/ directory. Updates can be installed directly with the apt command-line tool, or via
theGUI.
2.3.1 RepositoryFormats
APT_repositoriescanbeconfiguredintwodistinctformats,theoldsinglelineformatandthenewer
deb822format. Nomatterwhatformatyouchoose,apt updatewillfetchtheinformationfrom
allconfiguredsources.
SingleLine
Singlelinerepositoriesaredefinedin.listfileslistonepackagerepositoryperline,withthemost
preferredsourcelistedfirst. Emptylinesareignoredanda#characteranywhereonalinemarks
theremainderofthatlineasacomment.
deb822Style
Thenewerdeb822multilineformatisusedin.sourcesfiles. Eachrepositoryconsistsofastanza
with multiple key value pairs. A stanza is simply a group of lines. One file can contain multiple
stanzasbyseparatingthemwithablankline. Youcanstilluse#tocommentoutlines.
(cid:174) Note
ModernizingyourrepositoriesisrecommendedunderDebianTrixie,asaptwillcomplainabout
olderrepositorydefinitionsotherwise. Youcan runthecommandapt modernize-sources
tomodernizeyourexistingrepositoriesautomatically.
2.3.2 DebianBaseRepositories
YouwillneedaDebianbaserepositoryasaminimumtogetupdatesforallpackagesprovidedby
Debianitself:
2.3. DebianPackageRepositories 9

ProxmoxDatacenterManagerDocumentation,Release1.1.9
|     | Listing | 1: File: | /etc/apt/sources.list.d/debian. |     |
| --- | ------- | -------- | ------------------------------- | --- |
sources
Types: deb
URIs: http://deb.debian.org/debian/
| Suites:     | trixie trixie-updates                          |                   |     |     |
| ----------- | ---------------------------------------------- | ----------------- | --- | --- |
| Components: | main contrib                                   | non-free-firmware |     |     |
| Signed-By:  | /usr/share/keyrings/debian-archive-keyring.gpg |                   |     |     |
Types: deb
URIs: http://security.debian.org/debian-security/
Suites: trixie-security
| Components: | main contrib                                   | non-free-firmware |     |     |
| ----------- | ---------------------------------------------- | ----------------- | --- | --- |
| Signed-By:  | /usr/share/keyrings/debian-archive-keyring.gpg |                   |     |     |
In addition, you need a package repository from Proxmox to get Proxmox Datacenter Manager
updates.
2.3.3 ProxmoxDatacenterManagerEnterpriseRepository
Thisisthestable,recommendedrepository. ItisavailableforallusersfulfillingtheProxmoxData-
centerManagersubscriptionrequirements. Itcontainsthemoststablepackages,andissuitablefor
productionuse. Thepdm-enterpriserepositoryisenabledbydefault:
|     | Listing | 2:  | File: | /etc/apt/sources.list.d/ |
| --- | ------- | --- | ----- | ------------------------ |
pdm-enterprise.sources
Types: deb
URIs: https://enterprise.proxmox.com/debian/pdm
Suites: trixie
| Components: | pdm-enterprise                                  |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Signed-By:  | /usr/share/keyrings/proxmox-archive-keyring.gpg |     |     |     |
Thechange-loganddetailsofeachpackagecanbeviewedinthewebUI.
Pleasenotethatyouneedavalidsubscriptionkeytoaccessthisrepository,andforthatyourremote
| nodesneedBasicorhighersubscriptions. |     |     | SeetheFAQfordetails. |     |
| ------------------------------------ | --- | --- | -------------------- | --- |
(cid:174) Note
YoucandisablethisrepositorybyaddingthelineEnabled: falsetothestanza.
2.3.4 ProxmoxDatacenterManagerNo‐SubscriptionRepository
Asthenamesuggests,youdonotneedasubscriptionkeytoaccessthisrepository. Itcanbeused
fortestingandnon-productionuse. Itisnotrecommendedtouseitonproductionservers,because
thesepackagesarenotalwaysheavilytestedandvalidated.
Werecommendtoconfigurethisrepositoryin/etc/apt/sources.list.d/proxmox.sources.
|     | Listing | 3: File: | /etc/apt/sources.list.d/proxmox. |     |
| --- | ------- | -------- | -------------------------------- | --- |
sources
Types: deb
URIs: http://download.proxmox.com/debian/pdm
Suites: trixie
| Components: | pdm-no-subscription                             |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Signed-By:  | /usr/share/keyrings/proxmox-archive-keyring.gpg |     |     |     |
2.3.5 ProxmoxDatacenterManagerTestRepository
Thisrepositorycontainsthelatestpackagesandisheavilyusedbydeveloperstotestnewfeatures.
2.3. DebianPackageRepositories 10

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:193) Warning
thepdm-testrepositoryshould(asthenameimplies)onlybeusedtotestnewfeaturesorbug
fixes.
You can access this repository by adding the following stanza to /etc/apt/sources.list.d/
proxmox.sources:
Listing4: sources.listentryforpdm-test
Types: deb
URIs: http://download.proxmox.com/debian/pdm
Suites: trixie
Components: pdm-test
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
2.3.6 ProxmoxDatacenterManagerDebugSymbolRepository
Debugsymbolpackages,named<package>-dbgsym,containthedetacheddebuginformationfor
thematchingbinarypackage. Theyarenotneededfornormaloperation,butlettoolssuchasgdb,
systemd-coredump or crash produce useful backtraces when analyzing a crash or hang. They
areprovidedinadedicatedrepository,separatefromtheregularones,fortheDebianBookworm
andTrixiebasedProxmoxDatacenterManagerreleases(andnewer).
Listing5: sources.listentryforpdm-dbgsym
Types: deb
URIs: https://dbgsym.proxmox.com/debian/pdm
Suites: trixie
Components: pdm-dbgsym
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
After enabling the repository, install the -dbgsym package that matches the binary you want to
debug.
2.3.7 SecureApt
TheReleasefilesintherepositoriesaresignedwithGnuPG.APTisusingthesesignaturestoverify
thatallpackagesarefromatrustedsource.
IfyouinstallProxmoxDatacenterManagerfromanofficialISOimage,theverificationkeyisalready
installed.
IfyouinstallProxmoxDatacenterManagerontopofDebian,downloadandinstallthekeywiththe
followingcommands:
# wget https://enterprise.proxmox.com/debian/proxmox-archive-keyring-trixie.gpg -O /usr/share/
,→keyrings/proxmox-archive-keyring.gpg
(cid:174) Note
ThewgetcommandaboveaddsthekeyringforProxmoxreleasesbasedonDebianTrixie. Once
theproxmox-archive-keyringpackageisinstalled,itwillmanagethisfile. Atthatpoint,thehashes
belowmaynolongermatchthehashesofthisfile,askeysfornewProxmoxreleasesgetadded
orremoved. Thisisintended,aptwillensurethatonlytrustedkeysarebeingused. Modifying
thisfileisdiscouragedonce‘proxmox-archive-keyring‘isinstalled.
VerifytheSHA256checksumafterwardswiththeexpectedoutputbelow:
2.3. DebianPackageRepositories 11

ProxmoxDatacenterManagerDocumentation,Release1.1.9
# sha256sum /usr/share/keyrings/proxmox-archive-keyring.gpg
136673be77aba35dcce385b28737689ad64fd785a797e57897589aed08db6e45 /usr/share/keyrings/proxmox-
,→archive-keyring.gpg
andthemd5sum,withtheexpectedoutputbelow:
# md5sum /usr/share/keyrings/proxmox-archive-keyring.gpg
77c8b1166d15ce8350102ab1bca2fcbf /usr/share/keyrings/proxmox-archive-keyring.gpg
(cid:174) Note
Make sure that the path that you download the key to, matches the path specified in the
Signed-By: linesinyourrepositorystanzasfromabove.
2.3. DebianPackageRepositories 12

CHAPTER
THREE
GRAPHICAL USER INTERFACE
ProxmoxDatacenterManagementoffersanintegrated,web-basedinterfacetomanagetheserver.
Thismeansthatyoucancarryoutalladministrationtasksthroughyourwebbrowser,andthatyou
don’t have to worry about installing extra management tools. The web interface also provides
a built-in console, so if you prefer the command line or need some extra control, you have this
option.
The web interface can be accessed via https://youripaddress:8443. The default login is root, and
thepasswordiseithertheonespecifiedduringtheinstallationprocessorthepasswordoftheroot
user,incaseofinstallationontopofDebian.
(cid:174) Note
Mostofthedescriptionsbelowwillfocusontheuserinterfacesetto”English”,whichusesthe
left-to-right text direction. If you use a language with a text direction from right-to-left, then
someelementswillappearontherightwhenthedescriptionsays”left”andviceversa.
3.1 Features
• ModernmanagementinterfaceforProxmoxDatacenterManager
• CustomizableViews.
• Managementofremotes,resources,users,permissions,etc.
• SecureHTML5console
• Supportformultipleauthenticationsources
• Supportformultiplelanguages
• Based on Yew, a modern Rust framework for creating multi-threaded, front-end web apps
withWebAssembly.
13

ProxmoxDatacenterManagerDocumentation,Release1.1.9
3.2 Login
When you connect to the web interface, you will first see the login window. Proxmox Datacenter
Managersupportsvariouslanguagesandauthenticationbackends(Realms),bothofwhichcanbe
selectedhere.
(cid:174) Note
For convenience, you can save the username on the client side, by selecting the ”Save User
name”checkboxatthebottomofthewindow.
3.3 User Interface Overview
TheProxmoxDatacenterManagergraphicalinterfacecanberoughlysplitintothreedifferentsec-
tion:
• Header: Onthelefttheheadershowsthecurrentversioninformation. Inthemiddleasearch
barisfoundthathelpsyoufinddifferentremotesandresources. Whileontherightyoucan
toggle the dark mode of the theme, go to the user documentation, open a list of tasks and
openamenutoconfigurethethemeandlanguagethatisusedaswellaslogout.
• Sidebar: Belowtheheaderontheleftthesidebarcontainsthemainmenuwiththedifferent
menuoptionslisted.
• MainPanel: Thebiggestpartoftheinterfaceistakenupbythemainpanel. Itscontentwill
changedependingonthemenuselectedinthesidebar. Tostart,thedashboardwillbeshown.
3.4 Sidebar
Inthesidebar,ontheleftsideofthepage,youcanseevariousitemsrelatingtospecificmanage-
mentactivities.
3.2. Login 14

ProxmoxDatacenterManagerDocumentation,Release1.1.9
3.4.1 Dashboard
Thedashboardgivesanoverviewofallconfiguredremotesandresources. Includingwhetherre-
motes and their resources are up and running. Allowing you to tell at a glimpse how many VMs
andCTsarerunningorstoppedacrossyourdatacenterandthestateofallconfigureddatastores.
Informationonrunningtasks,CPUandmemoryusage,softwaredefinednetworking(SDN)zones
andthesubscriptionstatusisshownaswell.
3.4.2 Views
Viewsessentiallyallowyoutocreateacustomdashboard. Youcancreateanewviewbycopyingan
existingvieworcreatingitasanemptyview. Thenasetoffilterscanbeappliedtoaview,soitwill
onlyincludeinformationonspecificresourcesorremotes. Aftercreatinganewview,selectitfrom
thesidebartoseewhatitlookslike. Fromthereyoucanalsoadjustitslayoutandwidgets.
3.4. Sidebar 15

ProxmoxDatacenterManagerDocumentation,Release1.1.9
3.4.3 Notes
Inthenotessectionyoucankeeptrackofinformationthatmightbeusefultootheradministrators
oryourselfinthefuture. Toformatthenotes,Markdowncanbeused. Notesaresharedacrossall
datacenterusersthathavebeengrantedaccesstothem.
3.4.4 Configuration
To configure your Proxmox Datacenter Manager, navigate to the ”Configuration” menu. It allows
you to change the time and timezone, the DNS server and the its network interfaces. A second
tabmakestheWebAuthnTwoFactorAuthentication(TFA)settingsavailable. Therearealsoseveral
sub-menus:
• AccessControl: Manageusers,APItokens,TFAsettings,tokenanduserpermissionsaswell
asauthenticationrealms.
• Certificates: SetupcustomTLSorautomatedACMEcertificates.
• Subscription: To get proper support and access to the enterprise repository for your Prox-
moxDatacenterManager,youcanusethismenutocheckthesubscriptionstatus.
3.4.5 Administration
The administration menu can be used to get an overview of the Proxmox Datacenter Manager
nodeitself. Throughthesub-menu”Shell”youcanaccessthehost’sshell. Severaltabsallowyou
tomanagedifferentaspectsofthenode,suchas:
• NodeStatus: SeetheCPUutilization,memoryusageandothermetricsoftheProxmoxDat-
acenterManager. Hereyoucanalsoaccesspackageversionsandthesystemreportofyour
host,aswellasrebootorturnofthehost.
• Updates: Manageandinstallupdates.
• Repositories: Add,enableandinspectupdaterepositories.
• Syslog: Accessthehostssystemlog.
• Tasks: Anoverviewofalltasksofthehost.
3.4.6 SDN
ThismenuprovidesanoverviewofallSDNzonesacrossallconfiguredProxmoxVEremotes. The
EVPNmenucanbeusedtosetupEVPNzonesacrossmultipleremotesviaasingleinterface. More
detailedinformationonhowtouseProxmoxDatacenterManager’sSDNintegrationcanbefound
intheSDNIntegrationsection.
3.4. Sidebar 16

ProxmoxDatacenterManagerDocumentation,Release1.1.9
3.4.7 Ceph
This menu collects the Ceph clusters of all connected hyper-converged Proxmox VE remotes for
read-onlymonitoring. SeetheCephsectionfordetails.
3.4.8 Guests
Thismenuprovidesasinglecross-remotelistofallQEMUandLXCguests,withtextfiltering,sorting,
thecommonper-guestactions,andsnapshotmanagement. SeetheGuestssectionfordetails.
3.4.9 Remotes
Remotesallowsyoutoconfigurenewremotesaswellasmanageexistingone. The”Remotes”menu
itselfprovidesdifferenttabstoprovideaunifiedviewofyourentiredatacenter:
3.4. Sidebar 17

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Configuration: Showsalistofconfiguredremotesandsomebasicinformationonthem. It
alsoallowsconfiguringnewremotes.
• Tasks: Anoverviewofalltasksacrosstheentiredatacenterthatcanbefiltered.
• Updates: Allowsmanagingupdatesandpackageversionsforallremotes.
• Firewall: Shows a list of configured firewall rules and settings for each Proxmox VE remote
cluster,itsnodes,andguests.
Allconfiguredremotesarealsolistedhereinthesidebar. Eachmenuentryprovidesasplitpanel
thatcontainsthemostimportantinformationforeachremoteinaneasytonavigateinterface.
ForProxmoxVEremotesthisincludesanoverviewofallnodesandguestsinacluster. Byselecting
a guest or a node in the tree on the right, you can access its more detailed tabs on the left. For
nodesyoucangetanoverviewoftheirmetrics,aread-onlyviewoftheirnotesandupdatesaswell
3.4. Sidebar 18

ProxmoxDatacenterManagerDocumentation,Release1.1.9
asaccesstoa”Shell”tab. Thislasttabsgivesyouaccesstothenodesshell,makingmanagement
easy.
ProxmoxBackupServerremotesshowanoverviewofalltheirdatastoresontheleft. Ifyouselect
thenodeitself,youcanseeanoverviewofitsmostimportantmetricsandaseparatetabthatshows
availableupdates. WhenselectingadatastoreitsusageanddiskI/Oareshownfirst. Asecondtab
providesadetailedviewofitscontentbynamespace.
3.4. Sidebar 19

CHAPTER
FOUR
SDN INTEGRATION
TheProxmoxDatacenterManagerallowsmanagingSDNzonesandvnetsacrossmultipleremotes
andprovidesanoverviewofthecurrentstateofSDNentities.
4.1 Status Overview
The status overview shows the current status (available / error / unknown) of all zones on all re-
motes. This is equivalent to the status shown in the SDN overview of the Proxmox VE Web UI. A
summaryisalsoshownonthedashboard,allowinguserstoquicklyidentifyifthereareanyerro-
neousSDNzonesonanyremote.
4.2 EVPN Integration
The EVPN overview shows an aggregated overview of the contents of EVPN zones / routing table
instancesofallconfiguredclusters.
(cid:174) Note
Currently,theintegrationoperatesundertheassumptionthatEVPNcontrollerswiththesame
ASNareinterconnectedandpartofthesameoverlaynetwork. ZonesandVnetswiththesame
ASN:VNItagwillgetautomaticallymergedintheoverviewtrees.
The EVPN integration respects the ‘Route Target Import’ field of an EVPN zone and assumes any
Zones/VnetswiththatRouteTargetareimportedaswell.
4.2.1 Definitions
Currently,theSDNstackinProxmoxVEusesthetermsZonesandVNets,whicharespecifictothe
Proxmox VE stack. The following definitions try to make the relationship of those entities to the
morecommonlyuseddefinitionsinRFC7432andRFC9136clearer:
AEVPNzonerepresentsaroutingtableinstance(identifiedbyitsASN:VNItag). Thisisalsoknown
asanIP-VRFItisassociatedwithaVXLANVNI(theVRF-VXLANtagofazone)andalsoreferredtoas
L3VNI.
AvnetinanEVPNzonerepresentsabridgingtable(identifiedbyitsASN:VNItag). Thisisalsoknown
asaMAC-VRF.OneIP-VRFcancontainmultipleMAC-VRFs. AnalogoustoaEVPNzoneitisassociated
withaVXLANVNI(thetagofavnet)andalsoreferredtoasL2VNI.
20

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Remotes
Thisviewprovidesanoverviewofwhichzonesareavailableonaremoteandwhichvnetsitcontains.
Itshowsthevnetsthatarelocallyconfiguredonthatremote,aswellasthevnetsthatgetimported
either automatically (due to matching ASN:VNI tags) or manually (due to being specified in the
‘RouteTargetImport’ setting). Vnetsthatarenot local toa remoteareshownslightly greyedout,
sotheycanbedistinguishedeasily.
Itcontainsthefollowingcolumns:
• Name: Thenameoftheremote/zone/vnet
• L3VNI:TheVRF-VXLANtagconfiguredinthezone
• L2VNI:Thetagconfiguredinthevnet
• External: WhetherthisVNetislocallyconfiguredorfromanotherremote
• Imported: Whether this VNet was manually imported, due to a respective ‘Route Target Im-
port’entry
IP‐VRF
This view provides an overview of all available IP-VRFs and their contents. This view shows only
VNetsthatarenaturallypartofanIP-VRFduetotheirzonehavingthesameASN:VNIcombination.
ItcanbeusedtoseewhichVNetswouldgetimportedwhenspecifyingtherespectiveASN:VNIin
the‘RouteTargetImport’field.
Itcontainsthefollowingcolumns:
• Name: Thenameoftheremote/zone/vnet
• ASN:TheVRF-VXLANtagconfiguredinthezone
• VNI:TheL3VNI(forzones)orL2VNI(forvnets)
• Zone: Thenameofthezonethatcontainsthevnet
• Remote: Thenameoftheremotethatcontainsthezone(andthereforevnet).
StatusPanel
SelectingazoneorvnetshowsthecurrentstatusoftheIP-VRF/MAC-VRFfortheselectedzone/
vnetonagivennode. ThenodecanbeselectedviathedropdownintheEVPNstatuspanel.
For zones it shows the contents of the IP-VRF, as seen by the kernel. This means that routes for
guests located on the note do not show up in the IP-VRF status, since they are handled by the
connected route for the subnet. For vnets it shows the type 2 routes, as learned via BGP, so all
guestsareincludedinthisview.
Thefollowingpropertiesareshownforentriesinthezone:
• Destination: TheCIDRofthedestinationforthisroutingtableentry
• Nexthops: Thenexthopsforthisroute,forvnetsthisisusuallythelocalbridge-forexternally
learnedroutes(e.g. defaultroutes)theIPofthenexthop
• Protocol: Theprotocolviawhichthisrouteswaslearned
• Metric: Themetric(orcost)ofaroute,lowercostroutesarepreferredoverhighercostroutes
Thefollowingpropertiesareshownforentriesinthevnet:
• IPAddress: TheIP-Addressfromthetype-2route
• MACAddress: TheMAC-Addressfromthetype-2route
• via: Thenexthopforthetype-2route
4.2. EVPNIntegration 21

CHAPTER
FIVE
REMOTES
ProxmoxDatacenterManagerallowsyoutoaddarbitraryProxmoxVEnodesorclustersandProx-
mox Backup Server instances as remotes. This allows for a structured, unified overview of every
host,VM,container,anddatastoreacrossdifferentlocations.
5.1 Resource Operation
ThroughtheProxmoxDatacenterManager,administratorscanmanagethelifecycleofvirtualwork-
loads at scale. Supported operations include starting, stopping, and rebooting guests across the
inventorywithouttheneedtologintoindividualnodes.
Additionally,theplatformsupportslivemigrationofguests. Thiscapabilityextendstomigrations
between independent clusters, facilitating load balancing and planned maintenance while main-
taininghighavailability.
5.2 Data Collection
Collecting data like RRD metrics, worker task status, logs, and other operational information is
a primary function of Proxmox Datacenter Manager. The system aggregates metrics to provide
insightintousage,performance,andinfrastructuregrowth.
Thisallowsforintrospectionintotheserverfleet,providingacentraloverviewbutalsoallowingyou
toexplorespecificremotesorresources. DashboardsandRRDgraphsvisualizethisdatatoassist
indetectingtrends,optimizingresourceallocation,andplanningfuturecapacity.
5.3 Proxmox VE Remote
ProxmoxVEremotesintegratevirtualizationclustersandindependentnodesintothecentralman-
agement view. Once added, the interface displays the hierarchy of hosts, virtual machines, con-
tainers,andstorageresources,searchableviathecentralinterface.
SpecificmanagementcapabilitiesavailableforProxmoxVEremotesinclude:
• UpdateManagement: Acentralizedpanelprovidesanoverviewofavailableupdatesacross
theinfrastructureandallowsfortherolloutofpatchesdirectlyfromtheDatacenterManager
interface.
• SDN Capabilities: Administrators can configure EVPN zones and VNets across multiple re-
motestomanagenetworkoverlaysandadministrativetasks.
22

ProxmoxDatacenterManagerDocumentation,Release1.1.9
5.4 Proxmox Backup Server Remote
Proxmox Backup Server instances can be managed as remotes to oversee backup infrastructure
alongside virtualization hosts. The interface provides a consolidated overview of different datas-
tores,displayingcontentandstorageutilization.
Metrics from Proxmox Backup Server remotes are integrated directly into the central dashboard
widgets,includingRRDgraphsforperformanceandusagemonitoring.
5.5 Connection and Certificate Troubleshooting
Proxmox Datacenter Manager validates a remote’s TLS certificate against the system certificate
store. Iftheremotepresentsapubliclytrustedcertificate,forexampleoneissuedbyLet’sEncrypt
throughACME,nofurthertrustconfigurationisneededandcertificaterenewalsarehandledtrans-
parently.
Whenaremote’scertificateisnotinthesystemtruststore,aswiththedefaultself-signedProxmox
certificates,ProxmoxDatacenterManagerinsteadpinsthefingerprintyouacceptedwhenadding
theremote. Ifsucharemotelaterrenewsorrotatesitscertificate,thepinnedfingerprintnolonger
matchesthepresentedoneandeveryconnectiontothatremotefails. Thewebinterfaceandthe
command-linetoolssurfacethisasanerrorsuchas:
connection failed: Could not establish a TLS connection. Check whether the fingerprint matches
or the certificate on the remote is valid. OpenSSL Error: error:0A000086:SSL routines:
tls_post_process_server_certificate:certificate verify failed
Themostcommoncauseisalegitimatecertificaterenewalontheremote. Itcanalsoindicatean
expiredorotherwiseinvalidcertificateor,ifthechangeisunexpected,aman-in-the-middleattack,
soconfirmthenewcertificatethroughatrustedchannelbeforeacceptingit.
Torecover, re-probethecertificatethattheremotecurrentlypresentsandupdatethestoredfin-
gerprint:
• Inthewebinterface,opentheaffectedremoteandusetheCheckCertificateaction. Itcon-
tactsthenode, showsthecertificatepresentednow, andletsyouupdatethepinnedfinger-
print once you have confirmed the change. If the remote now uses a certificate that the
systemtruststoreaccepts,youcaninsteadclearthestoredfingerprinttorelyonthattrust.
• On the command line, inspect the presented certificate with
proxmox-datacenter-manager-client remote probe-certificate <remote>
<node>, then store the verified value with proxmox-datacenter-manager-client
remote set-fingerprint <remote> <node> <fingerprint> (omit the fingerprint to
clearthepin).
ThesystemjournalontheProxmoxDatacenterManagerhostrecordsadditionaldetail,including
thefingerprintthattheremotepresentedandtheonethatwasexpected.
5.4. ProxmoxBackupServerRemote 23

CHAPTER
SIX
CEPH
ProxmoxDatacenterManagercanmonitortheCephclustersofconnectedhyper-convergedProx-
mox VE remotes. The ”Ceph” entry in the sidebar collects the Ceph clusters across all configured
remotes,sothehealth,capacity,andservicestateofseveralclusterscanbereviewedfromasingle
place.
The Ceph integration is read-only: it surfaces the state of a cluster for monitoring and triage but
doesnotcreate,change,ordestroyCephresources. Usethe”OpenWebUI”button(seebelow)to
jumptothecluster’sownProxmoxVEinterfaceforanymanagementoperation.
6.1 Cluster Overview
TheoverviewlistseachdetectedCephclusterasonerowwiththefollowingcolumns:
• Health: theoverallCephhealthstatus,withthenumberofactivehealthchecksinparenthe-
ses. Thecelliscoloredsothatawarningorerrorstandsout.
• NameandRemote: theclusternameandtheProxmoxVEremotethatbacksit.
• CapacityandAvailable: therawtotalandfreecapacityofthecluster.
• Usage: athreshold-coloredmeterwiththeusedpercentage.
• OSDs: theobjectstoragedaemoncounts,phrasedas{up} up, {in}/{total} insothe
runningcount,whichistheavailabilityconcern,andthein-clusterfraction,whichisthedata-
placementconcern,stayreadableinonecell.
24

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Monitors: themonitorquorum,phrasedas{in quorum} / {total} in quorum.
• Activity: a short status such as ”Near full”, ”Degraded”, or ”Recovering” when the cluster is
notinacleanstate.
Selectaclustertoopenitsdetailpanel.
6.2 Cluster Detail
Thedetailpanelpresentsoneclusteracrossseveraltabs.
6.2.1 Dashboard
TheDashboardtabistheat-a-glancesummaryofthecluster:
• Health: the health status together with a plain-language assessment of whether data is at
risk, the recovery progress when a recovery is in flight, and the list of active Ceph health
checks.
• Capacity: thecluster-wideusagemeter.
• Services: thecountofmonitorsinquorum,managers,OSDs,pools,andplacementgroups,
plustherunningCephversion. Amixed-versionclusterismarkedassuch.
• Members: theProxmoxVEremotes,andtheirnodes,thatbackthiscluster.
• Performance: clientandrecoverythroughput,shownwhilethereisactivity.
6.2.2 Monitors,Managers,OSDs,Pools,CephFS,andFlags
6.2. ClusterDetail 25

ProxmoxDatacenterManagerDocumentation,Release1.1.9
TheremainingtabseachlistoneclassofCephcomponent:
• Monitors: themonitorswiththeirhost,quorumstatus,address,andversion.
• Managers: theCephmanagersandthemetadataservers,eachwithhost,state,address,and
version.
• OSDs: theOSDs,eitherasahostorOSDtreeorasaflatlist,withtheirupandinstatus,device
class,usage,placement-groupcount,andlatency.
• Pools: thepoolswiththeirtype,sizeandminimumsize,placement-groupcount,usage,au-
toscalemode,CRUSHrule,andassignedapplication.
• CephFS:theCephfilesystemswiththeirdataandmetadatapools.
• Flags: thecluster-wideOSDflagsthatarecurrentlyset.
6.3 Open Web UI
The”OpenWebUI”buttonintheclusterdetailheaderopensthebackingProxmoxVEnode’snative
Cephpanelinanewtab,onthesubviewthatmatchesthecurrentlyselectedtab. Useittoperform
anymanagementoperationthattheread-onlyProxmoxDatacenterManagerviewdoesnotoffer.
6.4 Permissions
ViewingaclusterrequirestheResource.Auditprivilegeonthebackingremote. Clusterswhose
remotetheusermaynotauditareomittedfromtheoverview.
6.3. OpenWebUI 26

CHAPTER
SEVEN
GUESTS
The”Guests”entryinthesidebarprovidesasingle, cross-remoteviewofeveryQEMUvirtualma-
chineandLXCcontainerthatProxmoxDatacenterManagerknowsabout. Itcollectstheguestsof
all configured Proxmox VE remotes into one list, so the whole fleet can be searched, sorted, and
actedonwithoutfirstnavigatingtotheowningremote.
Itcoversthemostcommonday-to-daytasks,includingtheper-guestpoweractionsandsnapshot
management.
7.1 List and Tree View
Atoggleinthetoolbarswitchesbetweentwopresentationsofthesamedata:
• List: aflat,sortabletableofallguests. Thisisthedefault. Itshowstheguestname,ID,status,
remote, node, tags, CPU usage, memory usage, uptime, and a column of per-guest actions.
Clickacolumnheadertosortbyit,includingbyCPUormemoryusage.
• Tree: the guests grouped by remote, each remote a collapsible parent with its guest count.
Thecolumnsarethesameexceptthattheremoteisimpliedbythegroup,soitisnotrepeated
perrow.
27

ProxmoxDatacenterManagerDocumentation,Release1.1.9
7.2 Filtering
The ”Filter” box narrows the list as you type. A bare word matches as a substring against every
visiblecolumn,suchasthename,ID,status,type,node,remote,ortags.
Atermcanalsobequalifiedwithafield:valueprefixtorestrictittoasinglecolumn. Thesup-
portedqualifiersare:
• tag: --aguesttag
• remote: --theremotename
• node: --thenodename
• status: --therunstatus,suchasrunningorstopped
• type: --theguesttype,qemuorlxc
Multiple terms are combined with a logical AND and separated by spaces, so tag:prod
status:running matches only running guests that carry the prod tag. Matching is case-
insensitive. Thisisthesamequalifiersyntaxastheglobalsearchfieldintheheader.
7.3 Guest Actions
Theactionscolumnoffersthecommonlife-cycleoperationsforeachguest,enabledaccordingto
itscurrentstate:
• Start: poweronastoppedguest.
• Resume: resume a paused or suspended QEMU virtual machine, complementing the start,
shutdown, and stop actions. Offered only for QEMU guests in a paused, suspended, or
prelaunchstate.
• Shutdown: gracefullyshutdownarunningguest.
• Snapshots: openthesnapshotmanagementdialogfortheguest(seebelow).
• Migrate: migratethe guest to another node, within the same remote(cluster) or acrossre-
motes. Notofferedfortemplates.
• OpeninPVEUI:opentheguestinthebackingProxmoxVEwebinterfaceinanewtab.
7.4 Snapshots
Snapshot management is available for both QEMU and LXC guests, either from the ”Snapshots”
actionintheguestlistorfromthe”Snapshots”tabinaguest’sdetailpanel.
7.2. Filtering 28

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Thedialoglistsaguest’ssnapshotsasaparent/childtreethatreflectshoweachsnapshotwastaken
fromtheonebeforeit. ThecurrentrunningstateisshownasaNOWentryattheappropriateplace
inthetree. Foreachsnapshotthedialogshowsthename,thetimeitwastaken,whetheritincludes
theguestRAM(forQEMUguests),anditsdescription.
Thefollowingoperationsareavailable:
• TakeSnapshot: createanewsnapshotofthecurrentstate. ForQEMUgueststhememory
canoptionallybeincluded.
• EditDescription: changethedescriptionofanexistingsnapshot.
• Rollback: reverttheguesttotheselectedsnapshot.
• Delete: removetheselectedsnapshot.
7.5 Permissions
Theguestlistshowstheresourcestheusermayaudit,andeveryactioniscarriedoutagainstthe
backingremote,wheretheremote’sownprivilegesapply. Anoperatorthereforeneedstheappro-
priatepermissiononthetargetguest’sremoteforanactiontosucceed.
7.5. Permissions 29

CHAPTER
EIGHT
AUTOMATED INSTALLATIONS
TheProxmoxDatacenterManagerprovidesintegrationwiththeautomatedinstallerforallProxmox
products.
Adetaileddocumentationofallavailableoptionscanbefoundonourdedicatedwikipage.
8.1 Overview
The overview shows all past and ongoing installations done using the Proxmox Datacenter Man-
ager. Itallowsaccesstotherawsysteminformationdataassentbytheautomatedinstallerbefore
theactualinstallation,and(ifconfigured)post-installationnotificationhookdata,containingexten-
siveinformationaboutthenewlyinstalledsystem.
8.2 Prepared Answers
This view provides an overview over all defined answer files and allows editing, copying into new
answersanddeletingthem. Foraquickoverview, itshowswhetheranansweristhedefaultand
whattargetfiltershavebeendefinedforthatparticularconfiguration.
8.2.1 Targetfilter
Targetfilterallowyoutocontrolwhatsystemsshouldmatch.
Filters are key-value pairs in the format key=format, with keys being JSON Pointers, and match
systemsbasedtheidentifyinginformationsentbytheinstallerasJSONdocument. Anexampleof
suchadocumentisprovidedonthewiki.
JSONPointersallowforidentifyingspecificvalueswithinaJSONdocument. Forexample,tomatch
onlyProxmoxVEinstallationsbytheproductname,afilterentrylike/product/product=pvecan
beused.
Values are globs and use the same syntax as the automated installer itself. The following special
characterscanbeusedinfilters:
• ?--matchesanysinglecharacter
• *--matchesanynumberofcharacters,canbenone
• [a],[abc],[0-9]--matchesanysinglecharacterinsidethebrackets,rangesarepossible
• [!a]--negatethefilter,anysinglecharacterbuttheonesspecified
Apreparedanswercanbealsosetasdefault,inwhichcaseitwillbeusedifnoothermorespecific
answermatchesbasedonitsconfiguredtargetfilters.
30

ProxmoxDatacenterManagerDocumentation,Release1.1.9
8.2.2 Templating
CertainfieldssupporttemplatingviaMiniJinja(aJinja2-inspiredtemplatingengine)andsequential
counters. Counters are automatically incremented each time an answer file is served to a client,
allowingforeasyprovisioningofuniquefields,suchasper-systemhostnames.
Thefollowingcounterisautomaticallydefinedwhencreatinganewpreparedanswerconfiguration:
• installation_nr-Counterofthenumberofinstallationsdonewiththisparticularanswer
configuration.
Thismechanismallowstemplatingonthefollowingfieldsforpreparedanswerconfigurations:
• Administratoremailaddress
• Hostname/FQDN
• NetworkIPaddress(CIDR)
• Networkgateway
• DNSServeraddress
Thetemplatingcontextprovidedforeachfieldcontainsthesysteminformationdataassentbythe
automatedinstalleronanswerretrieval,aswellasalltemplatecounters.
Forexample,toprovideauniquehostnametoeachtargetsystem,thefollowingtemplatecanbe
usedfortheHostname/FQDNfield:
{{ product.product }}{{ installation_nr }}.example.com
MiniJinjafeaturesawiderangeofbuilt-infilters,whichareenabledbydefault,similartoJinja2.
8.2.3 SubscriptionKey
ApreparedanswercancarryanoptionalProxmoxsubscriptionkey. Whenset,thenewlyinstalled
noderegistersthatsubscriptionautomaticallyaspartoftheinstallation,sonoseparateoperator
stepisneededtobringthenodeunderavalidsubscription.
8.3 Authentication token management
TousetheautomatedinstallerintegrationofProxmoxDatacenterManager,aninstallationprocess
must authenticate itself. This also provides for an additional scoping mechanism for prepared
answerconfigurations.
Theautomatedinstallerintegrationusesadedicatedtokenmechanism,separatefromthenormal
APItokens. SeetheexampleunderPreparinganISOonhowtoincludesuchatokenintheISOwhen
preparingit.
8.4 Preparing an ISO
TouseaninstallationISOofaProxmoxproductwiththeProxmoxDatacenterManagerfunctional-
ity,theISOmustbeappropriatelypreparedtofetchananswerviaHTTPfromtheProxmoxData-
centerManagerusingtheproxmox-auto-install-assistanttool,availablefromtheProxmox
VEpackagerepositories.
The target URL for the automated installer must point to https://<pdm>/api2/json/
auto-install/answer,where<pdm>istheaddressunderwhichtheProxmoxDatacenterMan-
agerisreachablefromthesystemstobeinstalled.
Forexample:
8.3. Authenticationtokenmanagement 31

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-auto-install-assistant prepare-iso /path/to/source.iso \
--fetch-from http \
--url 'https://datacenter.example.com/api2/json/auto-install/answer' \
--cert-fingerprint
,→'ab:cd:ef:12:34:56:78:90:a1:b2:c3:d4:e5:f6:7a:8b:9c:0d:aa:bb:cc:dd:ee:ff:21:43:65:87:09:af:bd:ce
,→' \
--answer-auth-token 'mytoken:ee2a5901-1910-4eb0-b0a2-c914f4adbb75'
8.4. PreparinganISO 32

CHAPTER
NINE
VIEWS
Viewsallowyoutoaddaninteractiveviewonaselectedsetofresources.
9.1 Resource Selection
Theresourceselectioniscontrolledbyaninclude-excludefiltersystem.
Youdefinewhatresourcestoconsiderforincludingwhichthengetpassedthroughanexcludelist
tosinglespecifictypesoutagain.
Thiswayyoucan, forexample, easilyconfiguretoincludeallvirtualmachineresources, butthen
excludeanysuchVMthatresidesonaspecificremote.
9.1.1 FilterTypes
Thefollowinglistsoffiltertypesareavailabletobeusedinincludeorexcludelists.
• Theresource-typefilterallowsyoutofilterbyaspecificresourcetype. Thefollowingtypesare
available:
– datastore: AProxmoxBackupServerdatastore.
– lxc: ALXCcontainer.
– node: AProxmoxVEorProxmoxBackupServernode.
– qemu: AQEMUvirtualmachine.
– sdn-zone: ASDNzone.
– storage: AProxmoxVEstorage
• The resource-pool filter allows you to include or exclude only resources that are located in a
specificresourcepool-name.
• Thetagfilterallowsyoutofilterresourcesthataretaggedwithaspecifictag-name.
• Theremotefilterallowsyoutofilterresourceslocatedonaspecificremote.
• Theresource-idfilterallowsyoutofilterresourceswithaspecificID.
Each filter can be prefixed with an optional <match-behavior>: prefix. Currently there is only the
exactmatchingbehavioravailable. Thisbehavioristhedefaultifnoprefixisprovided.
9.2 Customizable Dashboard
You can create customizable dashboards for a views from a set of pre-defined widgets. Only re-
sources matching your include minus the ones matching your exclude filters will be displayed in
thesewidgets.
33

ProxmoxDatacenterManagerDocumentation,Release1.1.9
9.2.1 Widgets
Thefollowingwidgetsareavailable:
• The nodes widget shows a status overview of the Proxmox VE and Proxmox Backup Server
nodes,andcanbelimitedtoasingleremotetype.
• Theguestswidgetshowsastatusoverviewofthevirtualguests,andcanbelimitedtoQEMU
virtualmachinesorLXCcontainers.
• Thepbs-datastoreswidgetshowstheusageandstatusofProxmoxBackupServerdatastores.
• The remotes widget lists the configured remotes and their status. It can also show a wizard
foraddinganewremote.
• Thesubscriptionwidgetshowsthesubscriptionstatusoftheremotes.
• ThesdnwidgetshowsthestatusoftheSoftware-DefinedNetworking(SDN)zones.
• Theleaderboardwidgetranksresourcesbyametric,suchasguestornodeCPUornodemem-
oryusage,andliststhetopconsumers.
• Thetask-summary widgetsummarizesrecenttasks,groupedbyachosencriterion.
• Theresource-treewidgetshowstheselectedresourcesinahierarchicaltree.
• The node-resource-gauge widget displays a single node resource, such as CPU, memory, or
storage,asagaugechart,andcanbelimitedtoasingleremotetype.
• Themapwidgetplotstheremotesonaninteractiveworldmapattheirconfiguredgeographic
location. Markersarecoloredbytheremote’sstatus,andmarkersthatareclosetogetherare
clusteredasyouzoomout.
9.2.2 MapWidget
ThelocationsshownbythemapwidgetcomefromtheremotesandcannotbeeditedinProxmox
DatacenterManager. Configurethemontheremoteside:
• OnProxmoxVE,setacluster-widedefaultinthedatacenteroptions,andoptionallyoverride
itpernodeinthenodeoptions.
• OnProxmoxBackupServer,setthelocationunderthe”Configuration”menu,inthe”Other”
tab’s”Location”section.
The map background is drawn from public-domain vector data by Natural Earth, shipped in the
proxmox-geojson-datapackage.
9.3 Access Control
Youcangrantpermissionsonspecificviews. Withsuchapermissiontheusercanoperateonthe
viewandallitsselectedresources.
9.3. AccessControl 34

CHAPTER
TEN
SUBSCRIPTION REGISTRY
ThesubscriptionregistrymaintainsacentralpoolofProxmoxVEandProxmoxBackupServersub-
scriptionkeysandletsanadministratorassignthemtoremotenodesfromasingleplace,without
havingtoselectandconfigureakeyforallremotenodesindividually.
10.1 Key Pool
ThepoolacceptsProxmoxVEandProxmoxBackupServerkeys;otherkeyprefixesarerejectedso
thatanewproducttypeisnoticedinsteadofsilentlyparkingunusableentries. Eachentryrecords
itsoriginandtheoptionalremotenodeithasbeenassignedto.
Keys can be added in bulk from the web interface or with the proxmox-datacenter-client
subscriptions add-keyscommand. TheAdddialogtakesmultiplekeys,separatedbynewlines
orcommas,andvalidatesthewholebatchatomically.
10.2 Node Subscription Status
TheNodeSubscriptionStatuspanelshowsthelivesubscriptionstateofeverynodebehindaconfig-
uredremotealongsideanypendingplanfromthepool. Nodesthatalreadyholdakeytheregistry
assignedappearwiththelivelevel;nodeswithapendingpoolassignmentshowaclockiconuntil
thechangeispushedtotheremote. Thefilterbuttonnarrowsthelistbysubscriptionstatus,orby
afree-textremoteornodenamesearch.
35

ProxmoxDatacenterManagerDocumentation,Release1.1.9
From this view an operator can revert a pending change on the selected node (an unpushed as-
signment or a queued Clear Key) or queue a new Clear Key. Clear Key frees the live subscription
keyfromanodesoitcanbereassignedelsewhere. Theactionisqueueduntilitiscommittedvia
ApplyPendingorrevertedonaper-nodebasis.
10.3 Assignment and Clearing
Akeycanbepinnedtoasinglenodemanually.
The Auto-Assign action proposes a plan that fills unsubscribed nodes from free pool keys. For
ProxmoxVE,thesmallestcoveringkeybysocketcountischosen,soa4-socketkeyisnotusedon
a2-sockethostwhilealargerhoststaysunsubscribed.
The Clear Key action queues the live subscription on the selected node for removal. The action
requires the (remote, node) to already be tracked by the pool. Apply Pending later issues the re-
movalontheremoteandreleasesthepoolbindingsothekeybecomesavailableforreassignment.
DiscardPendingdropsthequeuedclearwithouttouchingtheremote;thebindingstaysintactand
theoperatorcanretry.
The Adopt Key action imports the live subscription on a remote node into the pool as a bound
entry,withouttouchingtheremote. Useittobringapre-existingsubscription--oneinstalledona
nodebeforePDMtookoveritspoolmanagement--undertheregistrysothatpoolactionssuchas
ClearKeyandAuto-Assigncanactonit. Nodesthatareeligibleforadoptionarehighlightedwitha
downloadhinticonintheNodeSubscriptionStatustree;thepoolgridcarriesahidden-by-default
Sourcecolumndistinguishingmanually-addedfromadoptedentries,whichcanbeenabledviathe
columnpickerifthedistinctionmatters.
TheAdoptAllactionrunsthesameimportacrosseveryremotetheoperatorcanauditinonetrans-
action. UseitafterfirstconnectinganexistingfleetofnodestoPDMsothepoolcatchesupwith
thelivesubscriptionsalreadydeployed,withouthavingtoclickthroughAdoptKeyforeachnode.
Candidatestheoperatorhasnomodifyprivilegeon,whosekeyisalreadyboundelsewhereinthe
pool, whose(remote, node)targetisalreadyboundbyanotherpoolentry, orwhosekeyornode
namefailsschemavalidationareskippedsilently.
The proposed plan can be reviewed and adjusted before it is applied: untick a row to skip that
node,orpickadifferentfreekeyforarowfromitskeydropdown. ApplyPendingwalksthequeue
inorderandattemptseveryentry;anythatfailarereportedandstaypending,sooneunreachable
10.3. AssignmentandClearing 36

ProxmoxDatacenterManagerDocumentation,Release1.1.9
nodedoesnotstrandtherestandalaterApplyPendingretriesonlythefailures. DiscardPending
dropstheplanwithouttouchinganyremote.
TheCheckSubscriptionactiontriggersafreshshop-sideverificationofthelivesubscriptiononthe
selectednode,equivalenttotheper-product”Check”buttononPVE/PBS.Usefulforpromotinga
staleInvalidorExpiredverdicttoActiveoncetheunderlyingissueisfixedattheshop,without
having to wait for the next periodic check. The Status column tooltip surfaces the last-checked
timestampandthenext-due-dateasreportedbytheremote,whereavailable.
10.4 Permissions
Listingthepoolandthenodestatusviewfollowstheregularauditprivilegesoneachaffectedre-
mote. Poolentriespinnedtoaremotetheoperatorhasnoauditprivilegeonarehiddenfromthe
listing;unboundentriesstayvisibletoanyonewiththesystem-scopeauditprivilege.
Adding or removing pool entries requires the system-scope MODIFY privilege. Any action that
drives a change on a remote, such as assigning or clearing a key, adopting a live subscription, or
applying the pending plan, additionally requires the matching resource privilege on that remote,
so an operator with global system access alone cannot drive changes against remotes they have
no other authority on. Auto-Assign skips remotes the caller cannot modify, so a previewed plan
neversilentlycommitsanassignmentonaremotetheoperatoronlyhadauditon.
10.4. Permissions 37

CHAPTER
ELEVEN
AUTHENTICATION & ACCESS CONTROL
11.1 User Configuration
ProxmoxDatacenterManagersupportsseveralauthenticationrealms,andyouneedtochoosethe
realmwhenyouaddanewuser. Possiblerealmsare:
pam
LinuxPAMstandardauthentication. UsethisifyouwanttoauthenticateasaLinux
systemuser. Theusersneedstoalreadyexistonthehostsystem.
pdm
ProxmoxDatacenterManagerrealm. Thistypestoreshashedpasswordsin/etc/
proxmox-datacenter-manager/access/shadow.json.
openid
OpenID Connect server. Users can authenticate against an external OpenID Con-
nectserver.
ldap
LDAPserver. UserscanauthenticateagainstexternalLDAPservers.
ad
Active Directory server. Users can authenticate against external Active Directory
servers.
Theroot@pamsuperuserhasfulladministrationrightsoneverything,soit’srecommendedtoadd
otheruserswithlessprivileges.
11.2 API Tokens
Any authenticated user can generate API tokens, which can in turn be used to configure various
clients,insteadofdirectlyprovidingtheusernameandpassword.
APItokensservetwopurposes:
1. Easyrevocationincaseclientgetscompromised
2. Limitpermissionsforeachclient/tokenwithintheusers’permission
An API token consists of two parts: an identifier consisting of the user name, the realm and a
tokenname(user@realm!tokenname),andasecretvalue. Bothneedtobeprovidedtotheclient
inplaceoftheuserID(user@realm)andtheuserpassword,respectively.
TheAPItokenispassedfromtheclienttotheserverbysettingtheAuthorizationHTTPheader
withmethodPDMAPITokentothevalueTOKENID:TOKENSECRET.
38

ProxmoxDatacenterManagerDocumentation,Release1.1.9
11.3 Access Control
By default, new users and API tokens do not have any permissions. Instead you need to specify
whatisallowedandwhatisnot.
Proxmox Datacenter Manager uses a role- and path-based permission management system. An
entryinthepermissionstableallowsauser,grouportokentotakeonaspecificrolewhenaccessing
an ’object’ or ’path’. This means that such an access rule can be represented as a triple of ’(path,
user, role)’, ’(path, group, role)’ or ’(path, token, role)’, with the role containing a set of allowed
actions,andthepathrepresentingthetargetoftheseactions.
11.3.1 Privileges
Privileges are the building blocks of access roles. They are internally used to enforce the actual
permissionchecksintheAPI.
System.Audit
Allowsknowingaboutthesystemanditsstatus.
System.Modify
Allowsmodifyingsystem-levelconfiguration.
Sys.Console
Allowsaccesstothesystem’sconsole
Sys.PowerManagement
Allowspoweringofforrebootingthesystem.
Resource.Audit
Allowsauditingguests,storagesandotherresources.
Resource.Manage
Allowsmanagingresources,likestartingorstoppingguests.
Resource.Modify
Allowsmodifyingresources,likemakingconfigurationchanges.
Resource.Create
Allowscreatingaguest.
Resource.Delete
Allowsdeletingaguest.
Resource.Migrate
Allowsremotemigrationofaguest.
Access.Audit
Allowsauditingpermissionsandusers.
Access.Modify
Allowsmodifyingpermissionsandusers.
Realm.Allocate
Allowsviewing,creating,modifyinganddeletingrealms
11.3.2 AccessRoles
Anaccessrolecombinesoneormoreprivilegesintosomethingthatcanbeassignedtoauseror
APItokenonanobjectpath.
Currently,thereareonlybuilt-inroles,meaningyoucannotcreateyourown,customrole.
Thefollowingrolesexist:
NoAccess
DisableAccess-nothingisallowed.
11.3. AccessControl 39

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Administrator
Candoanything,ontheobjectpathassigned.
Auditor
Canviewthestatusandconfigurationofthings,butisnotallowedtochangesettings.
11.3.3 ObjectsandPaths
Access permissions are assigned to objects, such as a datastore, namespace or some system re-
sources.
We use filesystem-like paths to address these objects. These paths form a natural tree, and per-
missionsofhigherlevels(shorterpaths)canoptionallybepropagateddownwithinthishierarchy.
Pathscanbetemplated,meaningtheycanrefertotheactualidofaconfigurationentry. Whenan
APIcallrequirespermissionsonatemplatedpath,thepathmaycontainreferencestoparameters
oftheAPIcall. Thesereferencesarespecifiedincurlybrackets.
Someexamplesare:
/resource Access to all resources managed by a Proxmox Datacenter
Manager.
/resource/{id} Accesstoresourcesonaspecificremote.
/resource/{id}/guest Accesstoallvirtualguestresourcesonaspecificremote.
/resource/{id}/guest/ Accesstoaspecificvirtualguestonaspecificremote.
{vmid}
/resource/{id}/node Accesstoallnodesresourcesonaspecificremote.
/resource/{id}/node/ Accesstoaspecificnodeonaspecificremote.
{name}
/views/ Accesstoviews.
/views/{id} Accesstoaspecificview.
/system/network Accesstoconfigurethehostnetwork.
/access/users Useradministration.
/access/domains Administrativeaccesstorealms.
Inheritance
As mentioned earlier, object paths form a file system like tree, and permissions can be inherited
byobjectsdownthattreethroughthepropagateflag,whichissetbydefault. Weusethefollowing
inheritancerules:
• PermissionsforAPItokensarealwayslimitedtothoseoftheuser.
• Permissionsondeeper,morespecificlevelsreplacethoseinheritedfromanupperlevel.
11.3.4 Configuration&Management
Access permission information is stored in /etc/proxmox-datacenter-manager/access/
acl.cfg. The file contains 5 fields, separated using a colon (’:’) as a delimiter. A typical entry
takestheform:
acl:1:/datastore:john@pdm:Administrator
Thedatarepresentedineachfieldisasfollows:
1. aclidentifier
2. A1or0,representingwhetherpropagationisenabledordisabled,respectively
3. Theobjectonwhichthepermissionisset. Thiscanbeaspecificobject(likeasingleview)or
atoplevelobject,whichwithpropagationenabled,representsallchildrenoftheobjectalso.
11.3. AccessControl 40

ProxmoxDatacenterManagerDocumentation,Release1.1.9
4. Theuser(s)/token(s)forwhichthepermissionisset
5. Therolebeingset
YoucanmanagepermissionsviaConfiguration->AccessControl->Permissionsinthewebin-
terface.
11.3.5 APITokenPermissions
APItokenpermissionsarecalculatedbasedonACLscontainingtheirID,independentlyofthoseof
theircorrespondinguser. Theresultingpermissionsetonagivenpathisthenintersectedwiththat
ofthecorrespondinguser.
Inpracticethismeans:
1. APItokensrequiretheirownACLentries
2. APItokenscanneverdomorethantheircorrespondinguser
11.4 Two‐Factor Authentication
11.4.1 Introduction
Withsimpleauthentication,onlyapassword(singlefactor)isrequiredtosuccessfullyclaimaniden-
tity(authenticate),forexample,tobeabletologinasroot@pamonaspecificinstanceofProxmox
DatacenterManager. Inthiscase,ifthepasswordgetsleakedorstolen,anybodycanuseittolog
in-eveniftheyshouldnotbeallowedtodoso.
Withtwo-factorauthentication(TFA),auserisaskedforanadditionalfactortoverifytheirauthen-
ticity. Ratherthanrelyingonsomethingonlytheuserknows(apassword),thisextrafactorrequires
somethingonlytheuserhas,forexample,apieceofhardware(securitykey)orasecretsavedon
the user’s smartphone. This prevents a remote user from gaining unauthorized access to an ac-
count,aseveniftheyhavethepassword,theywillnothaveaccesstothephysicalobject(second
factor).
11.4.2 AvailableSecondFactors
You can set up multiple second factors, in order to avoid a situation in which losing your smart-
phoneorsecuritykeylocksyououtofyouraccountpermanently.
ProxmoxDatacenterManagersupportsthreedifferenttwo-factorauthenticationmethods:
• TOTP(Time-basedOne-TimePassword). Ashortcodederivedfromasharedsecretandthe
currenttime,itchangesevery30seconds.
• WebAuthn (Web Authentication). A general standard for authentication. It is implemented
by various security devices, like hardware keys or trusted platform modules (TPM) from a
computerorsmartphone.
• Single use Recovery Keys. A list of keys which should either be printed out and locked in a
secureplaceorsaveddigitallyinanelectronicvault. Eachkeycanbeusedonlyonce. These
areperfectforensuringthatyouarenotlockedout, evenifallofyourothersecondfactors
arelostorcorrupt.
11.4. Two‐FactorAuthentication 41

CHAPTER
TWELVE
HOST SYSTEM ADMINISTRATION
ProxmoxDatacenterManagerisbasedonthefamousDebianLinuxdistribution. Thismeansthat
you have access to the entire range of Debian packages, and that the base system is well docu-
mented. TheDebianAdministrator’sHandbookisavailableonline,andprovidesacomprehensive
introductiontotheDebianoperatingsystem.
A standard Proxmox Datacenter Manager installation uses the default repositories from Debian,
soyougetbugfixesandsecurityupdatesthroughthatchannel. Inaddition, weprovideourown
packagerepositorytorolloutallProxmoxrelatedpackages. ThisincludesupdatestosomeDebian
packageswhennecessary.
WealsodeliveraspeciallyoptimizedLinuxkernel,basedontheUbuntukernel. Thiskernelincludes
driversforZFS.
ThefollowingsectionswillexplainthingswhicharedifferentonProxmoxDatacenterManager,or
tasks which are commonly used on Proxmox Datacenter Manager. For other topics, please refer
tothestandardDebiandocumentation.
12.1 ZFS on Linux
ZFSisacombinedfilesystemandlogicalvolumemanager,designedbySunMicrosystems. There
isnoneedtomanuallycompileZFSmodules-allpackagesareincluded.
ByusingZFS,it’spossibletoachievemaximumenterprisefeatureswithlowbudgethardware,and
also high performance systems by leveraging SSD caching or even SSD only setups. ZFS can re-
place expensive hardware raid cards with moderate CPU and memory load, combined with easy
management.
GeneraladvantagesofZFS:
• EasyconfigurationandmanagementwithGUIandCLI.
• Reliable
• Protectionagainstdatacorruption
• Datacompressiononfilesystemlevel
• Snapshots
• Copy-on-writeclone
• Variousraidlevels: RAID0,RAID1,RAID10,RAIDZ-1,RAIDZ-2andRAIDZ-3
• CanuseSSDforcache
• Selfhealing
• Continuousintegritychecking
• Designedforhighstoragecapacities
• Asynchronousreplicationovernetwork
42

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• OpenSource
• Encryption
12.1.1 Hardware
ZFS depends heavily on memory, so it’s recommended to have at least 8GB to start. In practice,
useasmuchyoucangetforyourhardware/budget. Topreventdatacorruption, werecommend
theuseofhighqualityECCRAM.
Ifyouuseadedicatedcacheand/orlogdisk,youshoulduseanenterpriseclassSSD(forexample,
IntelSSDDCS3700Series). Thiscanincreasetheoverallperformancesignificantly.
(cid:489) Important
Do not use ZFS on top of a hardware controller which has its own cache management. ZFS
needstodirectlycommunicatewithdisks. AnHBAadapterorsomethinglikeanLSIcontroller
flashedinITmodeisrecommended.
12.1.2 ZFSAdministration
This section gives you some usage examples for common tasks. ZFS itself is really powerful and
providesmanyoptions. ThemaincommandstomanageZFSarezfsandzpool. Bothcommands
comewithextensivemanualpages,whichcanbereadwith:
# man zpool
# man zfs
Createanewzpool
Tocreateanewpool,atleastonediskisneeded. Theashiftshouldhavethesamesector-size(2
powerof ashift)orlargerastheunderlyingdisk.
# zpool create -f -o ashift=12 <pool> <device>
CreateanewpoolwithRAID‐0
Minimum1disk
# zpool create -f -o ashift=12 <pool> <device1> <device2>
CreateanewpoolwithRAID‐1
Minimum2disks
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2>
CreateanewpoolwithRAID‐10
Minimum4disks
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2> mirror <device3> <device4>
CreateanewpoolwithRAIDZ‐1
Minimum3disks
12.1. ZFSonLinux 43

ProxmoxDatacenterManagerDocumentation,Release1.1.9
# zpool create -f -o ashift=12 <pool> raidz1 <device1> <device2> <device3>
CreateanewpoolwithRAIDZ‐2
Minimum4disks
# zpool create -f -o ashift=12 <pool> raidz2 <device1> <device2> <device3> <device4>
Createanewpoolwithcache(L2ARC)
Itispossibletouseadedicatedcachedrivepartitiontoincreasethereadperformance(useSSDs).
For<device>,youcanusemultipledevices,asisshownin”CreateanewpoolwithRAID*”.
| # zpool | create -f -o ashift=12 |     | <pool> <device> | cache <cache_device> |
| ------- | ---------------------- | --- | --------------- | -------------------- |
Createanewpoolwithlog(ZIL)
Itispossibletouseadedicatedcachedrivepartitiontoincreasethewriteperformance(useSSDs).
For<device>,youcanusemultipledevices,asisshownin”CreateanewpoolwithRAID*”.
| # zpool | create -f -o ashift=12 |     | <pool> <device> | log <log_device> |
| ------- | ---------------------- | --- | --------------- | ---------------- |
Addcacheandlogtoanexistingpool
Youcanaddcacheandlogdevicestoapoolafteritscreation. Inthisexample,wewilluseasingle
driveforbothcacheandlog. First,youneedtocreate2partitionsontheSSDwithpartedorgdisk
| (cid:489) | Important |     |     |     |
| --------- | --------- | --- | --- | --- |
AlwaysuseGPTpartitiontables.
The maximum size of a log device should be about half the size of physical memory, so this is
| usuallyquitesmall. | TherestoftheSSDcanbeusedascache. |                    |     |                      |
| ------------------ | -------------------------------- | ------------------ | --- | -------------------- |
| # zpool            | add -f <pool>                    | log <device-part1> |     | cache <device-part2> |
Changingafaileddevice
| # zpool | replace -f <pool> | <old | device> <new | device> |
| ------- | ----------------- | ---- | ------------ | ------- |
Changingafailedbootabledevice
Depending on how Proxmox Datacenter Manager was installed, it is either using grub or
systemd-bootasabootloader.
Ineithercase,thefirststepsofcopyingthepartitiontable,reissuingGUIDsandreplacingtheZFS
partitionarethesame. Tomakethesystembootablefromthenewdisk,differentstepsareneeded
whichdependonthebootloaderinuse.
| # sgdisk | <healthy bootable | device> | -R <new        | device>             |
| -------- | ----------------- | ------- | -------------- | ------------------- |
| # sgdisk | -G <new device>   |         |                |                     |
| # zpool  | replace -f <pool> | <old    | zfs partition> | <new zfs partition> |
12.1. ZFSonLinux 44

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:174) Note
Usethezpoolstatus-vcommandtomonitorhowfartheresilveringprocessofthenewdiskhas
progressed.
Withsystemd-boot:
# proxmox-boot-tool format <new ESP> # proxmox-boot-tool init <new ESP>
(cid:174) Note
ESP stands for EFI System Partition, which is setup as partition #2 on bootable disks by the
ProxmoxDatacenterManagerinstaller. Fordetails,seeSettingupanewpartitionforuseassynced
ESP.
Withgrub:
Usuallygrub.cfgislocatedin/boot/grub/grub.cfg
# grub-install <new disk> # grub-mkconfig -o /path/to/grub.cfg
Activatee‐mailnotification
ZFScomeswithaneventdaemon,ZED,whichmonitorseventsgeneratedbytheZFSkernelmodule.
The daemon can also send emails upon ZFS events, such as pool errors. Newer ZFS packages
shipthedaemoninaseparatepackagezfs-zed, whichshouldalreadybeinstalledbydefaultin
ProxmoxDatacenterManager.
Youcanconfigurethedaemonviathefile/etc/zfs/zed.d/zed.rc,usingyourpreferrededitor.
TherequiredsettingforemailnotificationisZED_EMAIL_ADDR,whichissettorootbydefault.
ZED_EMAIL_ADDR="root"
PleasenotethatProxmoxDatacenterManagerforwardsmailstoroottotheemailaddressconfig-
uredfortherootuser.
LimitZFSmemoryusage
Itisgoodtouseatmost50percent(whichisthedefault)ofthesystemmemoryforZFSARC,topre-
ventperformancedegradationofthehost. Useyourpreferrededitortochangetheconfiguration
in/etc/modprobe.d/zfs.confandinsert:
options zfs zfs_arc_max=8589934592
Theaboveexamplelimitstheusageto8GiB(’8*2^30^’).
(cid:489) Important
Incaseyourdesiredzfs_arc_maxvalueislowerthanorequaltozfs_arc_min(whichdefaults
to1/32ofthesystemmemory),zfs_arc_maxwillbeignored. Thus,forittoworkinthiscase,
you must set zfs_arc_min to at most zfs_arc_max - 1. This would require updating the
configurationin/etc/modprobe.d/zfs.conf,with:
options zfs zfs_arc_min=8589934591
options zfs zfs_arc_max=8589934592
12.1. ZFSonLinux 45

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Thisexamplesettinglimitstheusageto8GiB(’8*2^30^’)onsystemswithmorethan256GiBof
totalmemory,wheresimplysettingzfs_arc_maxalonewouldnotwork.
(cid:489)
Important
IfyourrootfilesystemisZFS,youmustupdateyourinitramfseverytimethisvaluechanges.
| # update-initramfs | -u  |     |
| ------------------ | --- | --- |
SwaponZFS
Swap-spacecreatedonazvolmaycausesomeissues,suchasblockingtheserverorgeneratinga
highIOload.
Westronglyrecommendusingenoughmemory,sothatyounormallydonotrunintolowmemory
situations. Shouldyouneedorwanttoaddswap,itispreferredtocreateapartitiononaphysical
diskanduseitasaswapdevice. Youcanleavesomespacefreeforthispurposeintheadvanced
optionsoftheinstaller. Additionally,youcanlowertheswappinessvalue. Agoodvalueforservers
is10:
| # sysctl | -w vm.swappiness=10 |     |
| -------- | ------------------- | --- |
To make the swappiness persistent, create a new file /etc/sysctl.d/99-swappiness.conf
withaneditorofyourchoiceandaddthefollowingline:
| vm.swappiness | = 10 |     |
| ------------- | ---- | --- |
Table1: Linuxkernelswappinessparametervalues
| Value |     | Strategy |
| ----- | --- | -------- |
vm.swappiness=0 Thekernelwillswaponlytoavoidan’outofmemory’condition
vm.swappiness=1 Minimumamountofswappingwithoutdisablingitentirely.
vm.swappiness=10 Sometimes recommended to improve performance when sufficient
memoryexistsinasystem.
| vm.swappiness=60  |     | Thedefaultvalue.               |
| ----------------- | --- | ------------------------------ |
| vm.swappiness=100 |     | Thekernelwillswapaggressively. |
ZFScompression
Toactivatecompression:
| # zpool | set compression=lz4 | <pool> |
| ------- | ------------------- | ------ |
Werecommendusingthelz4algorithm,sinceitaddsverylittleCPUoverhead. Otheralgorithms
such as lzjb, zstd and gzip-N (where N is an integer from 1-9 representing the compression
ratio,where1isfastestand9isbestcompression)arealsoavailable. Dependingonthealgorithm
andhowcompressiblethedatais,havingcompressionenabledcanevenincreaseI/Operformance.
Youcandisablecompressionatanytimewith:
| # zfs set | compression=off | <dataset> |
| --------- | --------------- | --------- |
Onlynewblockswillbeaffectedbythischange.
12.1. ZFSonLinux 46

ProxmoxDatacenterManagerDocumentation,Release1.1.9
ZFSspecialdevice
Sinceversion0.8.0,ZFSsupportsspecialdevices. Aspecialdeviceinapoolisusedtostoremetadata,
deduplicationtables,andoptionallysmallfileblocks.
A special device can improve the speed of a pool consisting of slow spinning hard disks with a
lot of metadata changes. For example, workloads that involve creating, updating or deleting a
large number of files will benefit from the presence of a special device. ZFS datasets can also be
configured to store small files on the special device, which can further improve the performance.
UsefastSSDsforthespecialdevice.
(cid:489) Important
Theredundancyofthespecialdeviceshouldmatchtheoneofthepool,sincethespecialdevice
isapointoffailurefortheentirepool.
(cid:193) Warning
Addingaspecialdevicetoapoolcannotbeundone!
TocreateapoolwithspecialdeviceandRAID-1:
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2> special mirror <device3>
,→<device4>
AddingaspecialdevicetoanexistingpoolwithRAID-1:
# zpool add <pool> special mirror <device1> <device2>
ZFS datasets expose the special_small_blocks=<size> property. size can be 0 to disable
storing small file blocks on the special device, or a power of two in the range between 512B to
128K. After setting this property, new file blocks smaller than size will be allocated on the special
device.
(cid:489) Important
Ifthevalueforspecial_small_blocksisgreaterthanorequaltotherecordsize(default
128K)ofthedataset,alldatawillbewrittentothespecialdevice,sobecareful!
Settingthespecial_small_blockspropertyonapoolwillchangethedefaultvalueofthatprop-
ertyforallchildZFSdatasets(forexample,allcontainersinthepoolwilloptinforsmallfileblocks).
Optinforallfilessmallerthan4K-blockspool-wide:
# zfs set special_small_blocks=4K <pool>
Optinforsmallfileblocksforasingledataset:
# zfs set special_small_blocks=4K <pool>/<filesystem>
Optoutfromsmallfileblocksforasingledataset:
# zfs set special_small_blocks=0 <pool>/<filesystem>
12.1. ZFSonLinux 47

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Troubleshooting
Corruptcachefile
zfs-import-cache.serviceimportsZFSpoolsusingtheZFScachefile. Ifthisfilebecomescorrupted,
theservicewon’tbeabletoimportthepoolsthatit’sunabletoreadfromit.
Asaresult,incaseofacorruptedZFScachefile,somevolumesmaynotbemountedduringboot
andmustbemountedmanuallylater.
Foreachpool,run:
# zpool set cachefile=/etc/zfs/zpool.cache POOLNAME
then,updatetheinitramfsbyrunning:
# update-initramfs -u -k all
andfinally,rebootthenode.
Anotherworkaroundtothisproblemisenablingthezfs-import-scan.service,whichsearches
andimportspoolsviadevicescanning(usuallyslower).
12.2 Host Bootloader
ProxmoxDatacenterManagercurrentlyusesoneoftwobootloaders,dependingonthedisksetup
selectedintheinstaller.
ForEFISystemsinstalledwithZFSastherootfilesystemsystemd-bootisused,unlessSecureBoot
is enabled. All other deployments use the standard grub bootloader (this usually also applies to
systemswhichareinstalledontopofDebian).
12.2.1 PartitioningSchemeUsedbytheInstaller
TheProxmoxDatacenterManagerinstallercreates3partitionsonalldisksselectedforinstallation.
Thecreatedpartitionsare:
• A1MBBIOSBootPartition(gdisktypeEF02)
• A1GBEFISystemPartition(ESP,gdisktypeEF00)
• Athirdpartitionspanningtheconfiguredhdsizeparameterortheremainingspaceavailable
forthechosenstoragetype
Systems using ZFS as a root filesystem are booted with a kernel and initrd image stored on the
1 GB EFI System Partition. For legacy BIOS systems, and EFI systems with Secure Boot enabled,
grubisused,forEFIsystemswithoutSecureBoot,systemd-bootisused. Bothareinstalledand
configuredtopointtotheESPs.
grubinBIOSmode(--target i386-pc)isinstalledontotheBIOSBootPartitionofallselected
disksonallsystemsbootedwithgrub(thatis,allinstallswithrootonext4orxfs,andinstallswith
rootonZFSonnon-EFIsystems).
12.2.2 SynchronizingtheContentoftheESPwithproxmox-boot-tool
proxmox-boot-tool is a utility used to keep the contents of the EFI System Partitions properly
configured and synchronized. It copies certain kernel versions to all ESPs and configures the re-
spectivebootloadertobootfromthevfatformattedESPs. InthecontextofZFSasrootfilesystem,
thismeansthatyoucanusealltheoptionalfeaturesonyourrootpool,insteadofthesubsetwhich
isalsopresentintheZFSimplementationingruborhavingtocreateasmall,separateboot-pool
(see: BootingZFSonrootwithgrub).
12.2. HostBootloader 48

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Insetupswithredundancy,alldisksarepartitionedwithanESPbytheinstaller. Thisensuresthe
systemboots,evenifthefirstbootdevicefailsoriftheBIOScanonlybootfromaparticulardisk.
TheESPsarenotkeptmountedduringregularoperation. Thishelpstopreventfilesystemcorrup-
tioninthevfatformattedESPsincaseofasystemcrash,andremovestheneedtomanuallyadapt
/etc/fstabincasetheprimarybootdevicefails.
proxmox-boot-toolhandlesthefollowingtasks:
• Formattingandsettingupanewpartition
• CopyingandconfiguringnewkernelimagesandinitrdimagestoalllistedESPs
• Synchronizingtheconfigurationonkernelupgradesandothermaintenancetasks
• Managingthelistofkernelversionswhicharesynchronized
• Configuringtheboot-loadertobootaparticularkernelversion(pinning)
YoucanviewthecurrentlyconfiguredESPsandtheirstatebyrunning:
# proxmox-boot-tool status
SettingupaNewPartitionforuseasSyncedESP
To format and initialize a partition as synced ESP, for example, after replacing a failed vdev in an
rpool,proxmox-boot-toolfromproxmox-kernel-helpercanbeused.
(cid:193) Warning
the format command will format the <partition>. Make sure to pass in the right de-
vice/partition!
Forexample,toformatanemptypartition/dev/sda2asESP,runthefollowing:
# proxmox-boot-tool format /dev/sda2
Tosetupanexisting,unmountedESPlocatedon/dev/sda2forinclusioninProxmoxDatacenter
Manager’skernelupdatesynchronizationmechanism,usethefollowing:
# proxmox-boot-tool init /dev/sda2
or
# proxmox-boot-tool init /dev/sda2 grub
toforceinitializationwithGrubinsteadofsystemd-boot,forexampleforSecureBootsupport.
Followingthis,/etc/kernel/proxmox-boot-uuids‘ shouldcontainanewlinewiththeUUIDofthenewly
addedpartition. TheinitcommandwillalsoautomaticallytriggerarefreshofallconfiguredESPs.
UpdatingtheConfigurationonallESPs
To copy and configure all bootable kernels and keep all ESPs listed in /etc/kernel/
proxmox-boot-uuidsinsync,youjustneedtorun:
# proxmox-boot-tool refresh
(Equivalenttorunningupdate-grubonsystemswithext4orxfsonroot).
Thisisnecessaryaftermakingchangestothekernelcommandline,orifyouwanttosyncallkernels
andinitrds.
12.2. HostBootloader 49

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:174) Note
Bothupdate-initramfsandapt(whennecessary)willautomaticallytriggerarefresh.
KernelVersionsConsideredbyproxmox-boot-tool
Thefollowingkernelversionsareconfiguredbydefault:
• Thecurrentlyrunningkernel
• Theversionbeingnewlyinstalledonpackageupdates
• Thetwolatest,alreadyinstalledkernels
• Thelatestversionofthesecond-to-lastkernelseries(e.g. 5.0,5.3),ifapplicable
• Anymanuallyselectedkernels
ManuallyKeepingaKernelBootable
Should you wish to add a certain kernel and initrd image to the list of bootable kernels, use
proxmox-boot-tool kernel add.
For example, run the following to add the kernel with ABI version 6.14.1-1-pve to the list of
kernelstokeepinstalledandsyncedtoallESPs:
# proxmox-boot-tool kernel add 6.14.1-1-pve
proxmox-boot-tool kernel listwilllistallkernelversionscurrentlyselectedforbooting:
# proxmox-boot-tool kernel list
Manually selected kernels:
6.14.1-1-pve
Automatically selected kernels:
6.17.2-2-pve
Runproxmox-boot-tool kernel removetoremoveakernelfromthelistofmanuallyselected
kernels,forexample:
# proxmox-boot-tool kernel remove 6.14.1-1-pve
(cid:174) Note
It’s required to run proxmox-boot-tool refresh to update all EFI System Partitions (ESPs)
afteramanualkerneladditionorremovalfromabove.
12.2.3 DeterminewhichBootloaderisUsed
The simplest and most reliable way to determine which bootloader is used, is to watch the boot
processoftheProxmoxDatacenterManagernode.
Youwilleitherseetheblueboxof gruborthesimpleblackonwhitesystemd-boot.
Determiningthebootloaderfromarunningsystemmightnotbe100%accurate. Themostreliable
wayistorunthefollowingcommand:
# efibootmgr -v
IfitreturnsamessagethatEFIvariablesarenotsupported,grubisusedinBIOS/Legacymode.
Iftheoutputcontainsalinethatlookssimilartothefollowing,grubisusedinUEFImode.
12.2. HostBootloader 50

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Boot0005* proxmox [...] File(\EFI\proxmox\grubx64.efi)
Iftheoutputcontainsalinesimilartothefollowing,systemd-bootisused.
Boot0006* Linux Boot Manager [...] File(\EFI\systemd\systemd-bootx64.efi)
Byrunningthefollowingcommand,youcanfindoutif proxmox-boot-toolisconfigured,which
isagoodindicationofhowthesystemisbooted:
# proxmox-boot-tool status
12.2.4 Grub
grub has been the de facto standard for booting Linux systems for many years and is quite well
documented(seetheGrubManual).
Configuration
Changestothegrubconfigurationaredoneviathedefaultsfile/etc/default/gruborviaconfig
snippets in /etc/default/grub.d. To regenerate the configuration file after a change to the
configuration,run:
# update-grub
(cid:174) Note
Systems using proxmox-boot-tool will call proxmox-boot-tool refresh upon
update-grub
12.2.5 Systemd‐boot
systemd-bootisalightweightEFIbootloader. Itreadsthekernelandinitrdimagesdirectlyfrom
the EFI Service Partition (ESP) where it is installed. The main advantage of directly loading the
kernelfromtheESPisthatitdoesnotneedtoreimplementthedriversforaccessingthestorage.
InProxmoxDatacenterManager,proxmox-boot-toolisusedtokeeptheconfigurationontheESPs
synchronized.
Configuration
systemd-bootisconfiguredviathefileloader/loader.confintherootdirectoryofanEFISys-
temPartition(ESP).Seetheloader.conf(5)manpagefordetails.
Eachbootloaderentryisplacedinafileofitsown,inthedirectoryloader/entries/
Anexampleentry.conflookslikethis(/referstotherootoftheESP):
title Proxmox
version 5.0.15-1-pve
options root=ZFS=rpool/ROOT/pve-1 boot=zfs
linux /EFI/proxmox/5.0.15-1-pve/vmlinuz-5.0.15-1-pve
initrd /EFI/proxmox/5.0.15-1-pve/initrd.img-5.0.15-1-pve
12.2.6 EditingtheKernelCommandline
Youcanmodifythekernelcommandlineinthefollowingplaces,dependingonthebootloaderused:
12.2. HostBootloader 51

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Grub
The kernel commandline needs to be placed in the variable GRUB_CMDLINE_LINUX_DEFAULT in
thefile/etc/default/grub. Runningupdate-grubappendsitscontenttoalllinuxentriesin
/boot/grub/grub.cfg.
systemd‐boot
Thekernelcommandlineneedstobeplacedasonelinein/etc/kernel/cmdline. Toapplyyour
changes,runproxmox-boot-tool refresh,whichsetsitastheoptionlineforallconfigfilesin
loader/entries/proxmox-*.conf.
12.2.7 OverridetheKernel‐VersionfornextBoot
Toselectakernelthatisnotcurrentlythedefaultkernel,youcaneither:
• Usethebootloadermenuthatisdisplayedatthebeginningofthebootprocess
• Use the proxmox-boot-tool to pin the system to a kernel version either once or perma-
nently(untilpinisreset).
Thisshouldhelpyouworkaroundincompatibilitiesbetweenanewerkernelversionandthehard-
ware.
(cid:174) Note
Suchapinshouldberemovedassoonaspossible,sothatallrecentsecuritypatchesfromthe
latestkernelarealsoappliedtothesystem.
Forexample,topermanentlyselecttheversion5.15.30-1-pveforbooting,youwouldrun:
# proxmox-boot-tool kernel pin 5.15.30-1-pve
(cid:98) Tip
The pinning functionality works for all Proxmox Datacenter Manager systems, not only those
usingproxmox-boot-tooltosynchronizethecontentsoftheESPs,ifyoursystemdoesnotuse
proxmox-boot-toolforsynchronizing,youcanalsoskiptheproxmox-boot-tool refresh
callintheend.
You can also set a kernel version to be booted on the next system boot only. This is useful, for
example,totestifanupdatedkernelhasresolvedanissue,whichcausedyoutopinaversionin
thefirstplace:
# proxmox-boot-tool kernel pin 5.15.30-1-pve --next-boot
Toremoveanypinnedversionconfiguration,usetheunpinsubcommand:
# proxmox-boot-tool kernel unpin
While unpin has a --next-boot option as well, it is used to clear a pinned version set with
--next-boot. Asthathappensalreadyautomaticallyonboot,invokingitmanuallyisoflittleuse.
Aftersettingorclearingpinnedversions,youalsoneedtosynchronizethecontentandconfigura-
tionontheESPsbyrunningtherefreshsubcommand.
12.2. HostBootloader 52

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:98) Tip
Youwillbepromptedtoautomaticallydoforproxmox-boot-toolmanagedsystemsifyoucall
thetoolinteractively.
# proxmox-boot-tool refresh
12.2.8 SecureBoot
ProxmoxDatacenterManagersupportsSecureBootoutoftheboxviasignedpackagesandinte-
grationinproxmox-boot-tool.
ThefollowingpackagesneedtobeinstalledforSecureBoottobeenabled:
• shim-signed(shimbootloadersignedbyMicrosoft)
• shim-helpers-amd64-signed(fallbackbootloaderandMOKManager,signedbyProxmox)
• grub-efi-amd64-signed(GrubEFIbootloader,signedbyProxmox)
• proxmox-kernel-6.X.Y-Z-pve-signed(Kernelimage,signedbyProxmox)
Only Grub as bootloader is supported out of the box, since there are no other pre-signed boot-
loaderpackagesavailable. AnynewinstallationofProxmoxDatacenterManagerwillautomatically
havealloftheabovepackagesincluded.
MoredetailsabouthowSecureBootworks, andhowtocustomizethesetup, areavailableinour
wiki.
SwitchinganExistingInstallationtoSecureBoot
(cid:193) Warning
Thiscanleadtoanunbootableinstallationinsomecasesifnotdonecorrectly. Reinstallingthe
hostwillsetupSecureBootautomaticallyifavailable,withoutanyextrainteractions. Makesure
youhaveaworkingandwell-testedbackupofyourProxmoxDatacenterManagerhost!
AnexistingUEFIinstallationcanbeswitchedovertoSecureBootifdesired,withouthavingtorein-
stallProxmoxDatacenterManagerfromscratch.
First,ensureallyoursystemisup-to-date. Next,installalltherequiredpre-signedpackagesaslisted
above. GrubautomaticallycreatestheneededEFIbootentryforbootingviathedefaultshim.
systemd‐boot
Ifsystemd-bootisusedasabootloader(seeDeterminewhichBootloaderisused),someadditional
setupisneeded. ThisisonlythecaseifProxmoxDatacenterManagerwasinstalledwithZFS-on-
root.
Tocheckthelatter,run:
# findmnt /
IfthehostisindeedusingZFSasrootfilesystem,theFSTYPEcolumnshouldcontainzfs:
TARGET SOURCE FSTYPE OPTIONS
/ rpool/ROOT/pdm-1 zfs rw,relatime,xattr,noacl
Next, a suitable potential ESP (EFI system partition) must be found. This can be done using the
lsblkcommandasfollowing:
12.2. HostBootloader 53

ProxmoxDatacenterManagerDocumentation,Release1.1.9
| # lsblk -o | +FSTYPE |     |     |
| ---------- | ------- | --- | --- |
Theoutputshouldlooksomethinglikethis:
| NAME MAJ:MIN | RM SIZE | RO TYPE MOUNTPOINTS | FSTYPE     |
| ------------ | ------- | ------------------- | ---------- |
| sda 8:0      | 0 32G   | 0 disk              |            |
| ├─sda1 8:1   | 0 1007K | 0 part              |            |
| ├─sda2 8:2   | 0 1G    | 0 part              | vfat       |
| └─sda3 8:3   | 0 31G   | 0 part              | zfs_member |
| sdb 8:16     | 0 32G   | 0 disk              |            |
| ├─sdb1 8:17  | 0 1007K | 0 part              |            |
| ├─sdb2 8:18  | 0 1G    | 0 part              | vfat       |
| └─sdb3 8:19  | 0 31G   | 0 part              | zfs_member |
Inthiscase,thepartitionssda2andsdb2arethetargets. Theycanbeidentifiedbythetheirsize
of1GandtheirFSTYPEbeingvfat,inthiscaseonaZFSRAID-1installation.
These partitions must be properly set up for booting through Grub using proxmox-boot-tool.
Thiscommand(usingsda2asanexample)mustberunseparatelyforeachindividualESP:
| # proxmox-boot-tool | init | /dev/sda2 grub |     |
| ------------------- | ---- | -------------- | --- |
Afterwards,youcansanity-checkthesetupbyrunningthefollowingcommand:
| # efibootmgr | -v  |     |     |
| ------------ | --- | --- | --- |
Thislistshouldcontainanentrylookingsimilartothis:
[..]
Boot0009* proxmox HD(2,GPT,..,0x800,0x100000)/File(\EFI\proxmox\shimx64.efi)
[..]
(cid:174) Note
Theoldsystemd-bootbootloaderwillbekept,butGrubwillbepreferred. Thisway,ifbooting
usingGrubinSecureBootmodedoesnotworkforanyreason,thesystemcanstillbebooted
usingsystemd-bootwithSecureBootturnedoff.
NowthehostcanberebootedandSecureBootenabledintheUEFIfirmwaresetuputility.
On reboot, a new entry named proxmox should be selectable in the UEFI firmware boot menu,
whichbootsusingthepre-signedEFIshim.
If, for any reason, no proxmox entry can be found in the UEFI boot menu, you can try adding it
manually (if supported by the firmware), by adding the file \EFI\proxmox\shimx64.efi as a
custombootentry.
(cid:174)
Note
SomeUEFIfirmwaresareknowntodroptheproxmoxbootoptiononreboot. Thiscanhappen
iftheproxmoxbootentryispointingtoaGrubinstallationonadisk,wherethediskitselfisnot
abootoption. Ifpossible,tryaddingthediskasabootoptionintheUEFIfirmwaresetuputility
andrunproxmox-boot-toolagain.
(cid:98) Tip
Toenrollcustomkeys,seetheaccompanyingSecureBootwikipage.
12.2. HostBootloader 54

ProxmoxDatacenterManagerDocumentation,Release1.1.9
UsingDKMS/ThirdPartyModulesWithSecureBoot
OnsystemswithSecureBootenabled,thekernelwillrefusetoloadmoduleswhicharenotsigned
by a trusted key. The default set of modules shipped with the kernel packages is signed with an
ephemeralkeyembeddedinthekernelimagewhichistrustedbythatspecificversionofthekernel
image.
Inordertoloadothermodules,suchasthosebuiltwithDKMSormanually,theyneedtobesigned
with a key trusted by the Secure Boot stack. The easiest way to achieve this is to enroll them as
MachineOwnerKey(MOK)withmokutil.
The dkms tool will automatically generate a keypair and certificate in /var/lib/dkms/mok.key
and/var/lib/dkms/mok.pubanduseitforsigningthekernelmodulesitbuildsandinstalls.
Youcanviewthecertificatecontentswith
# openssl x509 -in /var/lib/dkms/mok.pub -noout -text
andenrollitonyoursystemusingthefollowingcommand:
# mokutil --import /var/lib/dkms/mok.pub
input password:
input password again:
Themokutilcommandwillaskfora(temporary)passwordtwice,thispasswordneedstobeen-
teredonemoretimeinthenextstepoftheprocess! Rebootingthesystemshouldautomatically
bootintotheMOKManagerEFIbinary,whichallowsyoutoverifythekey/certificateandconfirmthe
enrollmentusingthepasswordselectedwhenstartingtheenrollmentusingmokutil. Afterwards,
thekernelshouldallowloadingmodulesbuiltwithDKMS(whicharesignedwiththeenrolledMOK).
TheMOKcanalsobeusedtosigncustomEFIbinariesandkernelimagesifdesired.
The same procedure can also be used for custom/third-party modules not managed with DKMS,
butthekey/certificategenerationandsigningstepsneedtobedonemanuallyinthatcase.
12.3 Certificate Management
Access to the API and thus the web-based administration interface is always encrypted through
https. EachProxmoxDatacenterManagerhostcreatesbydefaultitsown(self-signed)certificate.
This certificate is used for encrypted communication with the host’s proxmox-datacenter-api
service,foranyAPIcallbetweenauserorbackup-clientandtheweb-interface.
Certificate verification when sending backups to a Proxmox Datacenter Manager is either done
basedonpinningthecertificatefingerprintsinthestorage/remoteconfiguration,orbyusingcer-
tificates,signedbyatrustedcertificateauthority.
12.3.1 CertificatesfortheAPIandSMTP
ProxmoxDatacenterManagerstoresitscertificateandkeyin:
• /etc/proxmox-datacenter-manager/auth/api.pem
• /etc/proxmox-datacenter-manager/auth/api.key
Youhavethefollowingoptionsforthecertificate:
1. Keep using the default self-signed certificate in /etc/proxmox-datacenter-manager/
auth/api.pem.
2. Use an externally provided certificate (for example, signed by a commercial Certificate Au-
thority(CA)).
3. Use an ACME provider like Let’s Encrypt to get a trusted certificate with automatic renewal;
thisisalsointegratedintheProxmoxDatacenterManagerAPIandwebinterface.
CertificatesaremanagedthroughtheProxmoxDatacenterManagerweb-interfaceorAPI.
12.3. CertificateManagement 55

ProxmoxDatacenterManagerDocumentation,Release1.1.9
12.3.2 UploadCustomCertificate
If you already have a certificate which you want to use for a Proxmox Datacenter Manager host,
youcansimplyuploadthatcertificateoverthewebinterface.
Notethatanycertificatekeyfilesmustnotbepasswordprotected.
12.3.3 TrustedcertificatesviaLet’sEncrypt(ACME)
Proxmox Datacenter Manager includes an implementation of the Automatic Certificate
ManagementEnvironment(ACME)protocol,allowingProxmoxDatacenterManageradminstouse
anACMEproviderlikeLet’sEncryptforeasysetupofTLScertificates,whichareacceptedandtrusted
bymodernoperatingsystemsandwebbrowsersoutofthebox.
Currently,thetwoACMEendpointsimplementedaretheLet’sEncrypt(LE)productionandstaging
environments. Our ACME client supports validation of http-01 challenges using a built-in web
serverandvalidationofdns-01challengesusingaDNSpluginsupportingalltheDNSAPIendpoints
acme.shdoes.
ACMEAccount
YouneedtoregisteranACMEaccountpercluster, withtheendpointyouwanttouse. Theemail
addressusedforthataccountwillserveasthecontactpointforrenewal-dueorsimilarnotifications
fromtheACMEendpoint.
You can register or deactivate ACME accounts over the web interface Certificates -> ACME
Accounts.
(cid:98) Tip
Becauseofrate-limitsyoushoulduseLEstagingforexperimentsorifyouuseACMEforthe
veryfirsttimeuntilallisworkingthere,andonlythenswitchovertotheproductiondirectory.
ACMEPlugins
The ACME plugin’s role is to provide automatic verification that you, and thus the Proxmox Dat-
acenter Manager Server under your operation, are the real owner of a domain. This is the basic
buildingblockofautomaticcertificatemanagement.
TheACMEprotocolspecifiesdifferenttypesofchallenges,forexamplethehttp-01,whereaweb
serverprovidesafilewithaspecifictokentoprovethatitcontrolsadomain. Sometimesthisisn’t
possible,eitherbecauseoftechnicallimitationsoriftheaddressofarecordisnotreachablefrom
thepublicinternet. Thedns-01challengecanbeusedinsuchcases. Thischallengeisfulfilledby
creatingacertainDNSrecordinthedomain’szone.
ProxmoxDatacenterManagersupportsbothofthosechallengetypesoutofthebox,youcancon-
figurepluginseitheroverthewebinterfaceunderCertificates -> ACME Challenges.
ACME Plugin configurations are stored in /etc/proxmox-datacenter-manager/acme/
plugins.cfg.
Domains
YoucanaddnewormanageexistingdomainentriesunderCertificates.
Afterconfiguringthedesireddomain(s)foranodeandensuringthatthedesiredACMEaccountis
selected,youcanorderyournewcertificateovertheweb-interface. Onsuccess,theinterfacewill
reloadafterroughly10seconds.
Renewalwillhappenautomatically
12.3. CertificateManagement 56

ProxmoxDatacenterManagerDocumentation,Release1.1.9
12.3.4 ACMEHTTPChallengePlugin
Thereisalwaysanimplicitlyconfiguredstandalonepluginforvalidatinghttp-01challengesvia
thebuilt-inwebserverspawnedonport80.
(cid:174) Note
Thename standalone meansthat it can providethe validation on its own, without any third
partyservice.
ThereareafewprerequisitestousethisforcertificatemanagementwithLet’sEncryptsACME.
• YouhavetoaccepttheToSofLet’sEncrypttoregisteranaccount.
• Port80ofthenodeneedstobereachablefromtheinternet.
• Theremustbenootherlisteneronport80.
• Therequested(sub)domainneedstoresolvetoapublicIPoftheProxmoxDatacenterMan-
agerhost.
12.3.5 ACMEDNSAPIChallengePlugin
Onsystemswhereexternalaccessforvalidationviathehttp-01methodisnotpossibleordesired,
itispossibletousethedns-01validationmethod. ThisvalidationmethodrequiresaDNSserver
thatallowsprovisioningof TXTrecordsviaanAPI.
ConfiguringACMEDNSAPIsforvalidation
ProxmoxDatacenterManagerreusestheDNSpluginsdevelopedfortheacme.sh1project. Please
refertoitsdocumentationfordetailsonconfigurationofspecificAPIs.
The easiest way to configure a new plugin with the DNS API is using the web interface
(Certificates -> ACME Accounts/Challenges).
HereyoucanaddanewchallengepluginbyselectingyourAPIproviderandenteringthecredential
datatoaccessyouraccountovertheirAPI.
(cid:98) Tip
Seetheacme.shHowtouseDNSAPIwikiformoredetailedinformationaboutgettingAPIcre-
dentialsforyourprovider. Configurationvaluesdonotneedtobequotedwithsingleordouble
quotes;forsomepluginsthatisevenanerror.
AstherearemanyDNSprovidersandAPIendpoints,ProxmoxDatacenterManagerautomatically
generatestheformforthecredentials,butnotallprovidersareannotatedyet. Forthoseyouwill
seeabiggertextarea,intowhichyousimplyneedtocopyallthecredential’sKEY=VALUEpairs.
DNSValidationthroughCNAMEAlias
A special alias mode can be used to handle validation on a different domain/DNS server, in
case your primary/real DNS does not support provisioning via an API. Manually set up a perma-
nent CNAME record for _acme-challenge.domain1.example pointing to _acme-challenge.
domain2.example,andsetthealiaspropertyintheProxmoxDatacenterManagernodeconfigu-
rationfile/etc/proxmox-datacenter-manager/acme/domains.cfgtodomain2.exampleto
allowtheDNSserverof domain2.exampletovalidateallchallengesfordomain1.example.
1acme.shhttps://github.com/acmesh-official/acme.sh
12.3. CertificateManagement 57

ProxmoxDatacenterManagerDocumentation,Release1.1.9
WildcardCertificates
WildcardDNSnamesstartwitha*.prefixandareconsideredvalidforall(one-level)subdomain
names of the verified domain. So a certificate for *.domain.example is valid for foo.domain.
exampleandbar.domain.example,butnotforbaz.foo.domain.example.
Currently,youcanonlycreatewildcardcertificateswiththeDNSchallengetype.
CombinationofPlugins
Combininghttp-01anddns-01validationispossibleincaseyournodeisreachableviamultiple
domainswithdifferentrequirements/DNSprovisioningcapabilities. MixingDNSAPIsfrommulti-
pleprovidersorinstancesisalsopossiblebyspecifyingdifferentplugininstancesperdomain.
(cid:98) Tip
Accessingthesameserviceovermultipledomainsincreasescomplexityandshouldbeavoided
ifpossible.
12.3.6 AutomaticrenewalofACMEcertificates
IfanodehasbeensuccessfullyconfiguredwithanACME-providedcertificate,thecertificatewillbe
renewed automatically by the proxmox-datacenter-manager-daily-update.service. Cur-
rently,renewalistriggeredifthecertificateeitherhasalreadyexpiredorifitwillexpireinthenext
30days.
12.3.7 ManuallyChangeCertificateovertheCommandLine
Ifyouwanttogetridofcertificateverificationwarnings,youhavetogenerateavalidcertificatefor
yourserver.
LogintoyourProxmoxDatacenterManagerviasshorusetheconsole:
| openssl | req -newkey rsa:2048 | -nodes -keyout | key.pem -out | req.pem |
| ------- | -------------------- | -------------- | ------------ | ------- |
Followtheinstructionsonthescreen,forexample:
| Country  | Name (2 letter  | code) [AU]: AT                  |     |     |
| -------- | --------------- | ------------------------------- | --- | --- |
| State or | Province Name   | (full name) [Some-State]:Vienna |     |     |
| Locality | Name (eg, city) | []:Vienna                       |     |     |
Organization Name (eg, company) [Internet Widgets Pty Ltd]: Proxmox GmbH
| Organizational | Unit Name                 | (eg, section) []:Proxmox             | Datacenter | Manager |
| -------------- | ------------------------- | ------------------------------------ | ---------- | ------- |
| Common Name    | (eg, YOUR                 | name) []: yourproxmox.yourdomain.com |            |         |
| Email Address  | []:support@yourdomain.com |                                      |            |         |
Please enter the following 'extra' attributes to be sent with your certificate request
| A challenge | password     | []: not necessary |     |     |
| ----------- | ------------ | ----------------- | --- | --- |
| An optional | company name | []: not necessary |     |     |
After you have finished the certificate request, you have to send the file req.pem to your Certifi-
cationAuthority(CA).TheCAwillissuethecertificate(BASE64encoded),basedonyourrequest–
savethisfileascert.pemtoyourProxmoxDatacenterManager.
Toactivatethenewcertificate,dothefollowingonyourProxmoxDatacenterManager
| cp key.pem  | /etc/proxmox-datacenter-manager/auth/api.key |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| cp cert.pem | /etc/proxmox-datacenter-manager/auth/api.pem |     |     |     |
ThenrestarttheAPIservers:
| systemctl | restart proxmox-datacenter-api.service |     |     |     |
| --------- | -------------------------------------- | --- | --- | --- |
Testyournewcertificate,usingyourbrowser.
12.3. CertificateManagement 58

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:174) Note
TotransferfilestoandfromyourProxmoxDatacenterManager,youcanusesecurecopy: Ifyour
desktoprunsLinux,youcanusethescpcommand-linetool. IfyourdesktopPCrunswindows,
pleaseuseanscpclientlikeWinSCP(seehttps://winscp.net/).
12.4 Service Daemons
12.4.1 proxmox-datacenter-api
ThisdaemonexposesthewholeProxmoxDatacenterManagerAPIonTCPport8443usingHTTPS.It
runsasuserwww-dataandhasverylimitedpermissions. Operationsrequiringmorepermissions
areforwardedtothelocalproxmox-datacenter-privileged-apiservice.
12.4.2 proxmox-datacenter-privileged-api
This daemon exposes the Proxmox Datacenter Manager management API through a restricted
UNIX socket at /run/proxmox-datacenter-manager/priv.sock. The daemon runs as root
andhaspermissiontodoallprivilegedoperations.
NOTE:ThedaemonlistenstoalocalUNIXsocketaddressonly,soyoucannotaccessitfromoutside.
Theproxmox-datacenter-apidaemonexposestheAPItotheoutsideworld.
12.5 Command‐line Tools
12.5.1 proxmox-datacenter-manager-client
Thistoolimplementsadatacentermanagerclient, i.e. itcanconnecttoanydatacentermanager
withthesamemajorversionandissuemanagementcommands,querystatusandcontrolremotes
andtheirresources.
12.5.2 proxmox-datacenter-manager-admin
ThistoolexposessomeofthedatacentermanagersadministrativeAPIonthecommandline.
12.4. ServiceDaemons 59

CHAPTER
THIRTEEN
FAQ
13.1 What distribution is Proxmox Datacenter Manager (PDM) based
on?
ProxmoxDatacenterManagerisbasedonDebianGNU/Linux.
13.2 Will Proxmox Datacenter Manager run on a 32‐bit processor?
ProxmoxDatacenterManageronlysupports64-bitCPUs(AMDorIntel). Therearenofutureplans
tosupport32-bitprocessors.
13.3 How long will my Proxmox Datacenter Manager version be sup‐
ported?
Proxmox Datacenter Man‐ DebianVersion First Re‐ Debian Proxmox Data‐
ager lease EOL centerManager
EOL
Proxmox Datacenter Man- Debian13(Trixie) 2025-12 TBA TBA
ager1
13.4 HowcanIupgradeProxmoxDatacenterManagertothenextpoint
release?
Minorversionupgrades,forexampleupgradingfromProxmoxDatacenterManagerinversion1.0
to1.1or1.3,canbedonejustlikeanynormalupdate.
But,youshouldstillcheckthereleasenotesforanyrelevantnotable,orbreakingchange.
FortheupdateitselfuseeithertheWebUIAdministration->UpdatespanelorthroughtheCLIwith:
apt update
apt full-upgrade
(cid:193) Warning
AsProxmoxDatacenterManagerusesarollingreleasemodelontopofDebian,performingan
aptupgrademayresultinapartiallyupgradedorbrokenpackagestate. Thisisbecauseaptfull-
upgradecanalsoremoveexistingpackagestosatisfydependenciesifneeded,whileaptupgrade
cannot.
60

ProxmoxDatacenterManagerDocumentation,Release1.1.9
(cid:174) Note
Always ensure you correctly setup the package repositories and only continue with the actual
upgradeifaptupdatedidnothitanyerror.
13.5 IsthereadedicatedsubscriptionfortheProxmoxDatacenterMan‐
ager?
No,thereisnot. However,yourexistingBasicorhighersubscriptionforProxmoxVEandProxmox
BackupServerremotesincludesaccesstotheProxmoxDatacenterManagerEnterpriseRepository
andsupportatnoextracost.
13.6 How can I get Enterprise Support for the Proxmox Datacenter
Manager?
Existing customers with active Basic or higher subscriptions for their Proxmox remotes also gain
accesstotheProxmoxDatacenterManagerenterpriserepositoryandsupport.
13.7 How can I get access to the Proxmox Datacenter Manager Enter‐
prise Repository?
TheProxmoxDatacenterManagercanusetheenterpriserepositoryifatleast80%oftheconfig-
uredremotenodeshaveavalidBasicorhighersubscription.
13.5. IsthereadedicatedsubscriptionfortheProxmoxDatacenterManager? 61

APPENDIX
A
COMMAND SYNTAX
A.1 proxmox-datacenter-manager-admin
proxmox-datacenter-manager-admin acme account deactivate <name> [OPTIONS]
DeactivateanACMEaccount.
<name>
[<string>]ACMEaccountname.
Optionalparameters:
--force<boolean> (default=true)
Deleteaccountdataeveniftheserverrefusestodeactivatetheaccount.
proxmox-datacenter-manager-admin acme account info <name> [OPTIONS]
ShowACMEaccountinformation.
<name>
[<string>]ACMEaccountname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin acme account list [OPTIONS]
ListACMEaccounts.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin acme account register <name> <contact>
[OPTIONS]
RegisteranACMEaccount.
<name>
[<string>]ACMEaccountname.
<contact>
[<string>]Listofemailaddresses.
Optionalparameters:
62

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--directory<string>
TheACMEDirectory.
proxmox-datacenter-manager-admin acme account update <name> [<contact>]
UpdateanACMEAccount.
<name>
[<string>]ACMEaccountname.
<contact>
[<string>]Listofemailaddresses.
proxmox-datacenter-manager-admin acme certificate order [OPTIONS]
OrderanewACMEcertificate.
Optionalparameters:
--force<boolean> (default=false)
Forcerenewalevenifthecertificatedoesnotexpiresoon.
proxmox-datacenter-manager-admin acme certificate revoke
RevokeACMEcertificate.
proxmox-datacenter-manager-admin acme plugin add <type> <id> --api <string>
--data <string> [OPTIONS]
AddACMEpluginconfiguration.
<type>
[<string>]TheACMEchallengeplugintype.
<id>
[<string>]ACMEChallengePluginID.
--api<string>
DNSAPIPluginId.
--data<string>
Filecontainingtheplugindata.
Optionalparameters:
--disable<boolean> (default=false)
Flagtodisabletheconfig.
--validation-delay<integer> (0 - 172800) (default=30)
Extradelayinsecondstowaitbeforerequestingvalidation.
AllowstocopewithlongTTLofDNSrecords.
proxmox-datacenter-manager-admin acme plugin config <id> [OPTIONS]
ShowACMEplugininformation.
<id>
[<string>]PluginID
Optionalparameters:
A.1. proxmox-datacenter-manager-admin 63

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin acme plugin list [OPTIONS]
ListACMEplugins.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin acme plugin remove <id>
DeleteanACMEpluginconfiguration.
<id>
[<string>]ACMEChallengePluginID.
proxmox-datacenter-manager-admin acme plugin set <id> [OPTIONS]
UpdateanACMEpluginconfiguration.
<id>
[<string>]ACMEChallengePluginID.
Optionalparameters:
--api<string>
DNSAPIPluginId.
--data<string>
DNSplugindata(base64encodedwithpadding).
--deletedisable|validation-delay
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean> (default=false)
Flagtodisabletheconfig.
--validation-delay<integer> (0 - 172800) (default=30)
Extradelayinsecondstowaitbeforerequestingvalidation.
AllowstocopewithlongTTLofDNSrecords.
proxmox-datacenter-manager-admin cert info
Displaynodecertificateinformation.
proxmox-datacenter-manager-admin cert update [OPTIONS]
Updatenodecertificatesandgenerateallneededfiles/directories. IfnoauthenticationkeyorCSRF
secretkeyexists,thiswillalsogeneratenewones. Thesetwokeyswillgointoeffectthenexttime
theproxmox-datacenter-api.serviceisstarted.
Optionalparameters:
A.1. proxmox-datacenter-manager-admin 64

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--force<boolean>
ForcegenerationofnewSSLcertificate.
proxmox-datacenter-manager-admin help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-datacenter-manager-admin remote add --authid <string> --id <string>
--nodes <string> --token <string> --type pve|pbs [OPTIONS]
Addanewremote.
--authid<string>
AuthenticationID
--id<string>
RemoteID.
--nodes<string>
Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
--token<string>
Theaccesstoken’ssecret.
--typepve|pbs (default=pve)
Thetypeofaremoteentry.
Optionalparameters:
--web-url<string>
ConfigurationfortheWebUIURLlinkgeneration.
proxmox-datacenter-manager-admin remote list [OPTIONS]
Listalltheremotesthisinstanceismanaging.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin remote remove <id> [OPTIONS]
Removearemote.
<id>
[<string>]RemoteID.
Optionalparameters:
--delete-token<boolean> (default=true)
Ifsettofalse,tokendeletionontheremoteisskipped.
A.1. proxmox-datacenter-manager-admin 65

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-admin remote subscriptions [OPTIONS]
Getthestatusofalltheremotesthisinstanceismanaging.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-datacenter-manager-admin remote update <id> [OPTIONS]
Updatearemote.
<id>
[<string>]RemoteID.
Optionalparameters:
--authid<string>
AuthenticationID
--nodes<string>
Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
--token<string>
Theaccesstoken’ssecret.
--web-url<string>
ConfigurationfortheWebUIURLlinkgeneration.
proxmox-datacenter-manager-admin remote version <id>
Addanewremote.
<id>
[<string>]RemoteID.
proxmox-datacenter-manager-admin report
Generatethesystemreport.
proxmox-datacenter-manager-admin support-status get
Getthesupportstatusinformation.
proxmox-datacenter-manager-admin support-status update
Updatethesupportstatusinformation.
proxmox-datacenter-manager-admin versions [OPTIONS]
ListpackageversionsforimportantProxmoxDatacenterManagerpackages.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
--verbose<boolean> (default=false)
Outputverbosepackageinformation. Itisignoredifoutput-formatisspecified.
A.1. proxmox-datacenter-manager-admin 66

ProxmoxDatacenterManagerDocumentation,Release1.1.9
A.2 proxmox-datacenter-manager-client
Optionsavailableforcommandgroupproxmox-datacenter-manager-client:
--colorno|always|auto (default=auto)
Controlterminalcoloroutput.
--output-formattext|json|json-pretty
Outputformat.
--fingerprint<string>
Certificatefingerprinttoexpect.
--host<string>
Servertoconnectto,oruser@realm@hosttriple.
--password-command<string>
Commandtoruntogetthepassword.
--password-file<string>
Filetoreadthepasswordfrom.
--port<integer> (0 - 65535) (default=8443)
Porttoconnect.
--user<string>
UserID
proxmox-datacenter-manager-client acl delete <path> <role> --auth-id
<string> [OPTIONS]
DeleteanACLentry.
<path>
[<string>]Accesscontrolpath.
<role>
[<role>]Enumrepresentingrolesviatheir[PRIVILEGES]combination.
Sinceprivilegesareimplementedasbitflags,eachuniquecombinationofprivilegesmapsto
asingle,uniqueu64valuethatisusedinthisenumdefinition.
--auth-id<string>
AuthenticationID
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 67

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client acl list [OPTIONS]
Listallusersorshowasingleuser’sinformation.
Optionalparameters:
--exact<boolean> (default=false)
Ifset,returnsonlyACLfortheexactpath.
--path<string>
Accesscontrolpath.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client acl update <path> <role> --auth-id
<string> [OPTIONS]
AddorupdateanACLentry.
<path>
[<string>]Accesscontrolpath.
<role>
[<role>]Enumrepresentingrolesviatheir[PRIVILEGES]combination.
Sinceprivilegesareimplementedasbitflags,eachuniquecombinationofprivilegesmapsto
asingle,uniqueu64valuethatisusedinthisenumdefinition.
--auth-id<string>
AuthenticationID
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--propagate<boolean> (default=true)
Allowtopropagate(inherit)permissions.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
A.2. proxmox-datacenter-manager-client 68

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--user
proxmox-datacenter-manager-client help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client login
Logintoaserver.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client metric-collection status
Showmetriccollectionstatus.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
A.2. proxmox-datacenter-manager-client 69

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--password-file
--port
--user
proxmox-datacenter-manager-client metric-collection trigger [OPTIONS]
Triggermetriccollection. Ifaremoteispassed,onlythisremotewillbecollected,otherwiseall.
Optionalparameters:
--remote<string>
RemoteID.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs datastore list <remote>
Listalltheremotesthisinstanceismanaging.
<remote>
[<string>]RemoteID.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs datastore rrddata <remote>
<datastore> <mode> <timeframe>
ReturnaPBSdatastore’smetricdata.
<remote>
[<string>]RemoteID.
<datastore>
[<string>]Datastorename.
A.2. proxmox-datacenter-manager-client 70

ProxmoxDatacenterManagerDocumentation,Release1.1.9
<mode>
[MAX|AVERAGE]RRDconsolidationmode
<timeframe>
[hour|day|week|month|year|decade]RRDtimeframe
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs node rrddata <remote> <mode>
<timeframe>
ReturnaPBSnode’smetricdata.
<remote>
[<string>]RemoteID.
<mode>
[MAX|AVERAGE]RRDconsolidationmode
<timeframe>
[hour|day|week|month|year|decade]RRDtimeframe
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs snapshot list <remote> <datastore>
[OPTIONS]
Listalltheremotesthisinstanceismanaging.
<remote>
[<string>]RemoteID.
<datastore>
[<string>]Datastorename.
Optionalparameters:
A.2. proxmox-datacenter-manager-client 71

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--ns<string>
Namespace.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs task list <remote>
Listthetasksofacluster.
<remote>
[<string>]RemoteID.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pbs task status <remote> <upid>
Querythestatusofatask.
<remote>
[<string>]RemoteID.
<upid>
[<string>]ThetaskUPID,optionallywiththeremotenameprefix
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
A.2. proxmox-datacenter-manager-client 72

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--user
proxmox-datacenter-manager-client pve lxc config <remote> <vmid> [OPTIONS]
Querytheconfigurationofacontainer.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
--snapshot<string>
Thenameofthesnapshot
--statepending|active (default=pending)
Guestconfigurationaccess.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc list {<remote>} [OPTIONS]
ListtheLXCcontainersofacluster.
<remote>
[<string>]Listofremotestoquery. Canbespecifiedmorethanonce.
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 73

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client pve lxc migrate <remote> <vmid> <target>
[OPTIONS]
Migrateacontainertoadifferentnodeinthesamecluster.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<target>
[<string>]RemoteID.
Optionalparameters:
--bwlimit<integer> (0 - N)
OverrideI/Obandwidthlimit(inKiB/s).
--map-storageFROM:TO,...
Mappingofsourcestoragestoonesonthetargetcluster. Canbespecifiedmorethanonce.
--node<string>
Nodename(or’localhost’)
--online<boolean>
Performanonlinemigrationifthevmisrunning.
--restart<boolean> (default=false)
Performarestart-migration.
--timeout<integer> (0 - N)
Addashutdowntimeoutfortherestart-migration.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc remote-migrate <remote> <vmid>
<target> --map-bridge FROM:TO,... --map-storage FROM:TO,... [OPTIONS]
Migrateacontainertoadifferentcluster.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<target>
[<string>]RemoteID.
A.2. proxmox-datacenter-manager-client 74

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--map-bridgeFROM:TO,...
Mappingofsourcenetworkbridgestoonesonthetargetcluster. Canbespecifiedmorethan
once.
--map-storageFROM:TO,...
Mappingofsourcestoragestoonesonthetargetcluster. Canbespecifiedmorethanonce.
Optionalparameters:
--bwlimit<integer> (0 - N)
OverrideI/Obandwidthlimit(inKiB/s).
--delete<boolean>
DeletetheoriginalVMandrelateddataaftersuccessfulmigration.
--node<string>
Nodename(or’localhost’)
--online<boolean>
Performanonlinemigrationifthevmisrunning.
--restart<boolean> (default=false)
Performarestart-migration.
--target-vmid<integer> (1 - N)
AguestID
--timeout<integer> (0 - N)
Addashutdowntimeoutfortherestart-migration.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc rrddata <remote> <vmid> <mode>
<timeframe>
ReturnaCT’smetricdata.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<mode>
[MAX|AVERAGE]RRDconsolidationmode
<timeframe>
[hour|day|week|month|year|decade]RRDtimeframe
Inheritedgroupparameters:
--color
--fingerprint
A.2. proxmox-datacenter-manager-client 75

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc shutdown <remote> <vmid>
[OPTIONS]
Shutdownacontainer.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc snapshot create <remote> <vmid>
<snapname> [OPTIONS]
CreateasnapshotofanLXCguest.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--description<string>
Atextualdescriptionorcomment.
--node<string>
Nodename(or’localhost’)
A.2. proxmox-datacenter-manager-client 76

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc snapshot delete <remote> <vmid>
<snapname> [OPTIONS]
DeleteasnapshotofanLXCguest.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc snapshot list <remote> <vmid>
[OPTIONS]
ListthesnapshotsofanLXCguest.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
A.2. proxmox-datacenter-manager-client 77

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc snapshot rollback <remote> <vmid>
<snapname> [OPTIONS]
RollbackanLXCguesttoasnapshot(destructive: revertsdiskandconfigtoit).
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--node<string>
Nodename(or’localhost’)
--start<boolean>
Startthecontainerafterasuccessfulrollback.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc snapshot update-description
<remote> <vmid> <snapname> [OPTIONS]
UpdateanLXCsnapshot’sdescription.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
A.2. proxmox-datacenter-manager-client 78

ProxmoxDatacenterManagerDocumentation,Release1.1.9
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--description<string>
Thenewdescription;passanemptystringtoclear.
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc start <remote> <vmid> [OPTIONS]
Startacontainer.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve lxc stop <remote> <vmid> [OPTIONS]
Stopacontainerabruptly.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
A.2. proxmox-datacenter-manager-client 79

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve node list <remote>
Listallthenodesofapvecluster.
<remote>
[<string>]RemoteID.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve node rrddata <remote> <node> <mode>
<timeframe>
ReturnaPVEnode’smetricdata.
<remote>
[<string>]RemoteID.
<node>
[<string>]Nodename(or’localhost’)
<mode>
[MAX|AVERAGE]RRDconsolidationmode
<timeframe>
[hour|day|week|month|year|decade]RRDtimeframe
Inheritedgroupparameters:
--color
--fingerprint
A.2. proxmox-datacenter-manager-client 80

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu config <remote> <vmid> [OPTIONS]
QuerytheconfigurationofaVM.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
--snapshot<string>
Thenameofthesnapshot
--statepending|active (default=pending)
Guestconfigurationaccess.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu list {<remote>} [OPTIONS]
ListtheQEMUVMsofacluster.
<remote>
[<string>]Listofremotestoquery. Canbespecifiedmorethanonce.
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
A.2. proxmox-datacenter-manager-client 81

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu migrate <remote> <vmid> <target>
[OPTIONS]
MigrateaVMtoadifferentnodeofthesamecluster.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<target>
[<string>]RemoteID.
Optionalparameters:
--bwlimit<integer> (0 - N)
OverrideI/Obandwidthlimit(inKiB/s).
--force<boolean>
Performanonlinemigrationifthevmisrunning.
--map-storageFROM:TO,...
Mappingofsourcestoragestoonesonthetargetcluster. Canbespecifiedmorethanonce.
--migration-network<string>
CIDRofthe(sub)networkthatisusedformigration.
--migration-typesecure|insecure
MigrationtrafficisencryptedusinganSSHtunnelbydefault. Onsecure,completelyprivate
networksthiscanbedisabledtoincreaseperformance.
--node<string>
Nodename(or’localhost’)
--online<boolean>
Performanonlinemigrationifthevmisrunning.
--with-local-disks<boolean>
Enablelivestoragemigrationforlocaldisks.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 82

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client pve qemu remote-migrate <remote> <vmid>
<target> --map-bridge FROM:TO,... --map-storage FROM:TO,... [OPTIONS]
MigrateaVMtoadifferentcluster.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<target>
[<string>]RemoteID.
--map-bridgeFROM:TO,...
Mappingofsourcenetworkbridgestoonesonthetargetcluster. Canbespecifiedmorethan
once.
--map-storageFROM:TO,...
Mappingofsourcestoragestoonesonthetargetcluster. Canbespecifiedmorethanonce.
Optionalparameters:
--bwlimit<integer> (0 - N)
OverrideI/Obandwidthlimit(inKiB/s).
--delete<boolean>
DeletetheoriginalVMandrelateddataaftersuccessfulmigration.
--node<string>
Nodename(or’localhost’)
--online<boolean>
Performanonlinemigrationifthevmisrunning.
--target-vmid<integer> (1 - N)
AguestID
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu rrddata <remote> <vmid> <mode>
<timeframe>
ReturnaVM’smetricdata.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<mode>
[MAX|AVERAGE]RRDconsolidationmode
A.2. proxmox-datacenter-manager-client 83

ProxmoxDatacenterManagerDocumentation,Release1.1.9
<timeframe>
[hour|day|week|month|year|decade]RRDtimeframe
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu shutdown <remote> <vmid>
[OPTIONS]
ShutdownaVM.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu snapshot create <remote> <vmid>
<snapname> [OPTIONS]
CreateasnapshotofaQEMUguest.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
A.2. proxmox-datacenter-manager-client 84

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--description<string>
Atextualdescriptionorcomment.
--node<string>
Nodename(or’localhost’)
--vmstate<boolean>
IncludetheVM’sRAMstate.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu snapshot delete <remote> <vmid>
<snapname> [OPTIONS]
DeleteasnapshotofaQEMUguest.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu snapshot list <remote> <vmid>
[OPTIONS]
ListthesnapshotsofaQEMUguest.
A.2. proxmox-datacenter-manager-client 85

ProxmoxDatacenterManagerDocumentation,Release1.1.9
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu snapshot rollback <remote>
<vmid> <snapname> [OPTIONS]
RollbackaQEMUguesttoasnapshot(destructive: revertsdiskandconfigtoit).
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--node<string>
Nodename(or’localhost’)
--start<boolean>
Starttheguestafterasuccessfulrollback.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 86

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client pve qemu snapshot update-description
<remote> <vmid> <snapname> [OPTIONS]
UpdateaQEMUsnapshot’sdescription.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
<snapname>
[<string>]Thenameofthesnapshot
Optionalparameters:
--description<string>
Thenewdescription;passanemptystringtoclear.
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve qemu start <remote> <vmid> [OPTIONS]
StartaVM.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 87

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client pve qemu stop <remote> <vmid> [OPTIONS]
StopaVMabruptly.
<remote>
[<string>]RemoteID.
<vmid>
[<integer> (1 - N)]AguestID
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve resources <remote> [<kind>]
Querytheclusterresources.
<remote>
[<string>]RemoteID.
<kind>
[vm|storage|node|sdn]Resourcetype.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve task list <remote> [OPTIONS]
Listthetasksofacluster.
<remote>
[<string>]RemoteID.
A.2. proxmox-datacenter-manager-client 88

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Optionalparameters:
--node<string>
Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client pve task status <remote> <upid>
Querythestatusofatask.
<remote>
[<string>]RemoteID.
<upid>
[<string>]ThetaskUPID,optionallywiththeremotenameprefix
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client remote add <type> <id> --authid <string>
--nodes <string> --token <string> [OPTIONS]
Addanewremote.
<type>
[pve|pbs (default=pve)]Thetypeofaremoteentry.
<id>
[<string>]RemoteID.
--authid<string>
AuthenticationID
--nodes<string>
Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
--token<string>
Theaccesstoken’ssecret.
A.2. proxmox-datacenter-manager-client 89

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Optionalparameters:
--create-token<string>
Ifgiven,createthistokenontheremoteanduseit.
--web-url<string>
ConfigurationfortheWebUIURLlinkgeneration.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client remote delete <id> [OPTIONS]
Deletearemote.
<id>
[<string>]RemoteID.
Optionalparameters:
--delete-token<boolean> (default=true)
Ifsettofalse,tokendeletionontheremoteisskipped.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client remote list
Listalltheremotesthisinstanceismanaging.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
A.2. proxmox-datacenter-manager-client 90

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--password-file
--port
--user
proxmox-datacenter-manager-client remote probe-certificate <id> <node>
Re-probeaconfigurednode’sTLScertificate,ignoringthepinnedfingerprint.
Useful to detect a rotated certificate. Apply the new fingerprint with remote set-fingerprint <id>
<node><fingerprint>,orclearthepinbyomittingit.
<id>
[<string>]RemoteID.
<node>
[<string>]Hostnameoftheconfigurednodetoprobe.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client remote set-fingerprint <id> <node>
[OPTIONS]
Setorclearanode’sstoredTLScertificatefingerprint.
Omitthefingerprinttoclearthepinandrelyonthesystemtruststore. Runremoteprobe-certificate
firsttoreadthefingerprintthenodecurrentlypresents.
<id>
[<string>]RemoteID.
<node>
[<string>]Hostnameoftheconfigurednodewhosefingerprinttoset.
Optionalparameters:
--fingerprint<string>
X509certificatefingerprint(sha256).
Inheritedgroupparameters:
--color
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 91

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client remote update <id> [OPTIONS]
Updatearemote.
<id>
[<string>]RemoteID.
Optionalparameters:
--authid<string>
AuthenticationID
--delete<string>
Listofpropertiestoclear,e.g. ’group’or’web-url’. Canbespecifiedmorethanonce.
--nodes<string>
Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
--token<string>
Theaccesstoken’ssecret.
--web-url<string>
ConfigurationfortheWebUIURLlinkgeneration.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client remote version <id>
Showaremote’sversion.
<id>
[<string>]RemoteID.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client resources [OPTIONS]
A.2. proxmox-datacenter-manager-client 92

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Listalltheremotesthisinstanceismanaging.
Optionalparameters:
--max-age<integer> (0 - N)
Maximumageofcachedremoteresources.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions add-keys {<keys>} [OPTIONS]
Addoneormoresubscriptionkeystothepool.
<keys>
[<string>]Subscriptionkeystoaddtothepool. Canbespecifiedmorethanonce.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions adopt-all [OPTIONS]
Adopteveryforeignlivesubscriptionintothepoolinonetransaction.
Walks all remotes the caller can audit, imports any (remote, node) with a live current key and no
pool binding. Candidates the caller has no modify privilege on, or whose key is already bound
elsewhereinthepool,aresilentlyskipped.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
A.2. proxmox-datacenter-manager-client 93

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions adopt-key <remote> <node>
[OPTIONS]
Adoptthelivesubscriptiononaremotenodeintothepool.
BringsaforeignsubscriptionunderPDMmanagementwithouttouchingtheremote: thelivecur-
rent key on remote/node is imported as a pool entry bound to that node. Refuses if the (remote,
node)targetalreadyhasapool-managedbinding.
<remote>
[<string>]RemoteID.
<node>
[<string>]Nodename(or’localhost’)
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions apply-pending [OPTIONS]
Pushallpendingkeyassignmentstoremotesasaworkertask.
Blocksuntiltheworkerfinishessotheoperatorseestheexitstatusoftheactualpushrun,notjust
aUPIDtheywouldhavetochasedownbyhand.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
A.2. proxmox-datacenter-manager-client 94

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions assign-key <key> --node
<string> --remote <string> [OPTIONS]
Assignakeyfromthepooltoaremotenode.
<key>
[<string>]Subscriptionkey.
--node<string>
Nodename(or’localhost’)
--remote<string>
RemoteID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions auto-assign [OPTIONS]
Propose(andoptionallyapply)automatickey-to-nodeassignments.
Optionalparameters:
--apply<boolean> (default=false)
Committheproposalimmediatelyviabulk-assign. Withoutthis,onlyapreviewisprinted.
Inheritedgroupparameters:
--color
--fingerprint
A.2. proxmox-datacenter-manager-client 95

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions check <remote> <node>
Triggerafreshshop-sidesubscriptioncheckonaremotenode.
Equivalent to the per-product ”Check” button: re-verifies the live subscription status against the
shop. Useful for promoting a stale Invalid/Expired verdict to Active once the underlying issue is
fixedattheshop,withoutwaitingforthenextperiodiccheck.
<remote>
[<string>]RemoteID.
<node>
[<string>]Nodename(or’localhost’)
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions clear-assignment <key>
[OPTIONS]
Cleartheassignmentofakey(unassignfromitsremotenode).
<key>
[<string>]Subscriptionkey.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
A.2. proxmox-datacenter-manager-client 96

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--port
--user
proxmox-datacenter-manager-client subscriptions clear-key <remote> <node>
[OPTIONS]
QueueaClearKeyonaremotenodesoitssubscriptioncanberemovedatnextApplyPending.
Refuses if no pool entry is bound to (remote, node): foreign live subscriptions must first be im-
portedviatheexplicitAdoptKeyaction,neverasasideeffectofqueueingaclear.
<remote>
[<string>]RemoteID.
<node>
[<string>]Nodename(or’localhost’)
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions clear-pending [OPTIONS]
Cleareverypendingassignmentinonebulktransaction.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 97

ProxmoxDatacenterManagerDocumentation,Release1.1.9
proxmox-datacenter-manager-client subscriptions list-keys
Listallsubscriptionkeysinthepool.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions remove-key <key>
Removeakeyfromthepoolentirely.
<key>
[<string>]Subscriptionkey.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions revert-clear <remote>
<node> [OPTIONS]
DropaqueuedClearKeyonaremotenodewhilekeepingthepoolbinding.
<remote>
[<string>]RemoteID.
<node>
[<string>]Nodename(or’localhost’)
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
Inheritedgroupparameters:
--color
--fingerprint
--host
A.2. proxmox-datacenter-manager-client 98

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client subscriptions status [OPTIONS]
Showthesubscriptionstatusofallremotes.
Optionalparameters:
--max-age<integer> (0 - N) (default=86400)
Maximumage(inseconds)ofcachedremotesubscriptionstate.
--verbose<boolean> (default=false)
Iftrue,includessubscriptioninformationpernode(withenoughprivileges)
--view<string>
Viewname.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user create <userid> [OPTIONS]
Listallusersorshowasingleuser’sinformation.
<userid>
[<string>]UserID
Optionalparameters:
--comment<string>
Comment.
--email<string>
E-MailAddress.
--enable<boolean> (default=true)
Enabletheaccount(default). Youcansetthisto’0’todisabletheaccount.
--expire<integer> (0 - N) (default=0)
Accountexpirationdate(secondssinceepoch). ’0’meansnoexpirationdate.
--firstname<string>
Firstname.
--lastname<string>
Lastname.
A.2. proxmox-datacenter-manager-client 99

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--password<string>
Password.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user delete <userid>
Listallusersorshowasingleuser’sinformation.
<userid>
[<string>]UserID
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user list
Listallusersorshowasingleuser’sinformation.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user passwd <userid> [OPTIONS]
Changeauser’spassword. Ifnopasswordisprovided,itwillbepromptedforinteractively.
A.2. proxmox-datacenter-manager-client 100

ProxmoxDatacenterManagerDocumentation,Release1.1.9
<userid>
[<string>]UserID
Optionalparameters:
--password<string>
Password.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user tfa add <type> <description>
[OPTIONS]
AddaTFAmethodtoauser(currentlyonlyrecoverykeys).
<type>
[totp|u2f|webauthn|recovery|yubico]ATFAentrytype.
<description>
[<string>]adescriptionforthetfaentry
Optionalparameters:
--userid<string>
userid
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user tfa delete <id> [OPTIONS]
DeleteaTFAentrybyid.
<id>
[<string>]thetfaidtoremove
Optionalparameters:
--userid<string>
userid
A.2. proxmox-datacenter-manager-client 101

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user tfa list [OPTIONS]
Listalltheremotesthisinstanceismanaging.
Optionalparameters:
--userid<string>
UserID
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
proxmox-datacenter-manager-client user update <userid> [OPTIONS]
Changeuserinformation.
<userid>
[<string>]UserID
Optionalparameters:
--comment<string>
Comment.
--deletecomment|enable|expire|firstname|lastname|email
Clear/resetuserproperties. Canbespecifiedmorethanonce.
--email<string>
E-MailAddress.
--enable<boolean> (default=true)
Enabletheaccount(default). Youcansetthisto’0’todisabletheaccount.
--expire<integer> (0 - N) (default=0)
Accountexpirationdate(secondssinceepoch). ’0’meansnoexpirationdate.
--firstname<string>
Firstname.
A.2. proxmox-datacenter-manager-client 102

ProxmoxDatacenterManagerDocumentation,Release1.1.9
--lastname<string>
Lastname.
Inheritedgroupparameters:
--color
--fingerprint
--host
--output-format
--password-command
--password-file
--port
--user
A.2. proxmox-datacenter-manager-client 103

APPENDIX
B
CONFIGURATION FILES
The Proxmox Datacenter Manager configuration files are stored at /etc/
proxmox-datacenter-manager/directory.
B.1 remotes.cfg
B.1.1 Options
Sectiontype’pbs’: Theinformationrequiredtoconnecttoaremoteinstance.
Requiredproperties:
authid
[<string>]AuthenticationID
nodes
[<string>]Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
token
[<string>]Theaccesstoken’ssecret.
type
[pve|pbs (default=pve)]Thetypeofaremoteentry.
Optionalproperties:
web-url
[<string>]ConfigurationfortheWebUIURLlinkgeneration.
Sectiontype’pve’: Theinformationrequiredtoconnecttoaremoteinstance.
Requiredproperties:
authid
[<string>]AuthenticationID
nodes
[<string>]Alistofclusternodeaddresses. Canbespecifiedmorethanonce.
token
[<string>]Theaccesstoken’ssecret.
type
[pve|pbs (default=pve)]Thetypeofaremoteentry.
Optionalproperties:
web-url
[<string>]ConfigurationfortheWebUIURLlinkgeneration.
104

ProxmoxDatacenterManagerDocumentation,Release1.1.9
B.2 views.cfg
B.2.1 Options
Optionalproperties:
exclude
[[exact:]resource-type=<storage|qemu|lxc|sdn-zone|datastore|node>|[exact:]resource-pool=<pool-name>|[exact:]tag=<tag-name>|[exact:]remote=<remote-name>|[exact:]resource=id:<resource-id>]
Listoffilterrules. Canbespecifiedmorethanonce.
include
[[exact:]resource-type=<storage|qemu|lxc|sdn-zone|datastore|node>|[exact:]resource-pool=<pool-name>|[exact:]tag=<tag-name>|[exact:]remote=<remote-name>|[exact:]resource=id:<resource-id>]
Listoffilterrules. Canbespecifiedmorethanonce.
include-all
[<boolean>]Includeallresourcesbydefault.
layout
[<string>]Theconfiguredlayout,encodedasjson
B.2. views.cfg 105

APPENDIX
C
ROADMAP
Forcompleteditems,seethereleasenotesforpreviousversionsbelow.
The items below describe development directions and priorities. Not all are planned for imme-
diate delivery. Some are long-term efforts spanning multiple major releases, and items may be
reprioritized based on engineering capacity, enterprise customer requirements, and community
feedback.
• Resourceorganizationandaccesscontrol:
– Folders as a first-class hierarchical entity: each remote has a single home folder, and
accesscanbedelegatedperfolder.
– Tagsasaflatlabelingscheme,independentofthefolderhierarchy,wherearesourcecan
carryseveraltags.
– A finer-grained ACL schema: Resource* roles that separate managing a resource from
modifyingitsdefinition,foldersactingasACLanchors,andclosingtheremainingcross-
clusterdelegationgaps.
• Guestandresourcemanagement:
– Bulk actions on virtual guests across the selection in the central guest list, building on
the cluster-wide bulk-action endpoints that the underlying Proxmox products provide
anddegradinggracefullywheretheyaremissing;thesameoperationsalsothroughthe
adminCLI,withaggregatedprogressandper-itemresults.
– Moreinformationinresourceoverviewsanddetailpanels,andmoreoptionsinthemi-
grationdialog,suchasabandwidthlimitandanonline/offlinepreference.
– Managementoffurthercoreconfigurationsofremoteresources: abackup-joboverview
withlast-executionstatus,andbasicguestconfigurationbeyondsnapshots,lifecycleand
migration. ProxmoxDatacenterManagerkeepslinkingouttotheremote’sfullinterface
foranythingcomplex.
– Aconsoleforremoteresources(nodesandguests).
• Remotesandonboarding:
– Simplifyaddingremotesthroughcopy-and-pasteQuick-Addinformation, mirroringthe
ProxmoxVEcluster-joinflowbutindependentofclustercommunicationandworkingon
singlenodestoo.
– Handlemulti-factorauthenticationfortheinitialProbeRemoteconnection.
• Networking:
– First-classSDNintegration,furtherphases: stretchEVPNVNetsacrossclusters,support
multipleVRFsacrossclusters,andautomateroute-targetimportandexport.
– Firewallmanagement,likelylandingtogetherwiththeSDNwork.
• Notifications:
106

ProxmoxDatacenterManagerDocumentation,Release1.1.9
– Standard system, update and task notifications for the Proxmox Datacenter Manager
nodeitself.
– Evaluate whether Proxmox Datacenter Manager can act as a notification target for re-
motes.
• Searchandusability:
– Moreexpressivesearchandfiltersyntax: wildcardsforviewfiltervalues,richerexpres-
sionsintheresourcesearchbar,andadditionalcategorykeywords.
– Polisherrormessagesandhandlingacrossthewebinterface, theCLIandtheAPI,with
richer presentation of API errors and more actionable guidance on common failure
modes.
• Furtherintegrationsandresilience:
– IntegrationoffurtherProxmoxprojects: ProxmoxMailGatewayasaremote,anddeeper
ProxmoxBackupServerintegrationincludingjobstatus,datastorecontentbrowsingand
pruneretention.
– Off-site replication copies of virtual guests for manual recovery on a datacenter failure
(notHA).
– Evaluateanactive-standbyarchitectureforProxmoxDatacenterManageritself,toavoid
asinglepointoffailure; twoinstancesside-by-sidealreadycoverthisinpractice, atthe
costofdoubledmetriccollection.
C.1 Release History
C.1.1 ProxmoxDatacenterManager1.1
Released28. May2026
• BasedonDebianTrixie(13.5)
• Latest7.0Kernelasstabledefault
• ZFS2.4.2
Features(Highlights)
• Integrationofautomatedinstallationfunctionality.
ProxmoxDatacenterManagercannowmanageanswerfileconfigurationsandserve
themtoremotes,allowingforcentralizedmanagementofinstallationparameters.
InstallationprogresscanbetrackedfromwithinProxmoxDatacenterManager’sweb
interface.
Atokensystemprotectstheinstallationprocess,enhancingoverallsecurity.
PreparedanswerscancarryanoptionalProxmoxsubscriptionkey, soanewnode
registersitssubscriptionautomaticallywithoutanextraoperatorstep.
• SubscriptionscannowbecentrallymanagedthroughasubscriptionregistryinProxmoxDat-
acenterManager.
Administratorscanconfigureacentralpoolofsubscriptionkeysandassignthemto
specificremotes.
Subscriptionscanbeassignedtoorclearedfromremotes.
Assignments can also be suggested automatically to ease handling large numbers
ofremotes.
• Cephclustersonconnectedhyper-convergedProxmoxVEremotescannowbemonitored.
C.1. ReleaseHistory 107

ProxmoxDatacenterManagerDocumentation,Release1.1.9
ThestatusofmultipleCephclusterscanbeseenataglancefromasinglepanel.
Thehealthstatus,capacityandperformance,aswellasthestatusofmonitors,man-
agers,OSDsandflags,canbeinspected.
• MetricsarenowcollectedfortheProxmoxDatacenterManagerhostitself.
AdministratorscantellataglancehowutilizedtheirProxmoxDatacenterManager
hostis.
• Newwidgetsvisualizethelocationofremotesonamapandusegaugestoshowtheutilization
ofresources.
LocationsshouldbesetviathenodeordatacenteroptionsonProxmoxVEremotes.
ForProxmoxBackupServerremotes,thelocationcanbesetunderConfiguration￿
Other￿Location.
• Firststeptowardcentralguestmanagementacrossconnectedremotes.
Anewcross-remoteviewlistsallQEMUandLXCguestsasaflatsortabletableorasa
treegroupedbyremote,withtextfilteringandthemostcommonper-guestactions
readilyavailable.
SnapshotmanagementiscentrallyavailableforQEMUandLXCguests: listaguest’s
snapshots in a parent/child tree and create, roll back, delete or edit a snapshot’s
description,eitherfromthecentralguestlistorfromtheper-guestdetailpanel.
AnexplicitResumeactionisofferedforpausedorsuspendedQEMUguests, com-
plementingtheexistingstart,stopandshutdownactions.
Thisistheinitialiterationofcentralguestmanagement; expectfurtherday-to-day
taskstobeintegratedinupcomingreleases.
ChangelogOverview
EnhancementsintheWebInterface(GUI)
• AddRRDgraphsfortheProxmoxDatacenterManagerhosttothenodestatuspanel.
• Add gauge chart widgets for CPU, memory and storage utilization for views and the default
dashboard.
• Anewwidgetallowsvisualizingremotesonamap.
• Add a cross-remote guest list showing all QEMU and LXC guests across connected Proxmox
VEremotes, eitherasaflatsortabletableorasatreegroupedbyremote, withtextfiltering
andthecommonper-guestactions.
• Add central snapshot management for QEMU and LXC guests, accessible from the central
guestlistorasaSnapshotstabintheper-guestdetailpanels(issue7207).
• OfferanexplicitResumeactionforpausedorsuspendedQEMUguests,complementingthe
existingstart,stopandshutdownactions.
• Addacertificatecheckandre-pindialogforremotes: afteraTLScertificaterotation,thedialog
re-probestheconfigurednodes,letstheoperatoracceptthenewfingerprintpernodeorclear
the stored pin, and applies the changes as one batch. It is reachable from the remotes list
andoffereddirectlyonaProxmoxVEorProxmoxBackupServerremotewhoseconnectionis
currentlyfailing.
• ThenotesfieldnowsupportsasubsetofMathMLtoallowpresentingcalculationsinproper
mathematicalnotation.
• DeriveIDsforheadingsinthenotesfieldautomaticallytoenableintra-documentlinks.
• Addabuttontodownloadthesystemreportonthenodestatuspage.
C.1. ReleaseHistory 108

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Fixanissuewhereasharedstorageinaclusterwascountedmultipletimestowardthestorage
capacitycalculations(issue7135).
• Allowrefreshingremotetasksinthetaskviewer.
• UsetheIECstandardforshowingdrivespace.
• ImproveaddingpermissionsbylistingACLpathsforspecificresourcesandviewsaswell.
• Fixanissuethatwouldprematurelylogoutusersrightafterafreshlogin.
• Fixanissuethatwouldclearfiltervaluefieldswheneditinganexistingview.
• Allowshowingviewseveniftheycontainunknownwidgets,whichcanhappenduringupdates.
• Forcearefreshafteraviewwaseditedtoloadpotentiallymissingdataimmediately.
• Add a message to the top entities widget when it is empty, explaining why nothing can be
displayed.
• Showanexplanatorymessagewhenaviewisempty.
• NamesofviewsarenowvalidatedintheUI.
• Improvethesubscriptionkeypoolexperience: validatekeyswhenaddingthem,allowper-row
keyoverridesandrowdeselectionintheAuto-Assignproposal,surfaceerrorswhenremoving
akeyfails,andfilterthenodestatustreebystatus.
• Whenmigratingaguesttoanewcluster,querytheremoteclusterforitsnextfreeVMIDand
useittopre-fillthemigrationdialog.
• Properly handle the OpenID redirection authorization, improving compatibility with certain
OpenIDproviders,forexampleGoogle(issue7290).
• AllowtheUItorendertheadd-userdialogproperlydependingontherealm.
• Avoidanissuethatpreventedusersfrombeingeditedwhenthe”expire”fieldwasset.
• UseapasswordfieldfortheOpenIDclientkeyfield.
• AllowchanginganLDAPrealmtouseanonymoussearch.
• Allowarealmsyncdialogtobesubmittedevenifthedefaultvalueswerenotchanged.
• ImproveandextendUIroutingtoincludetabsinaProxmoxVEremotepanelandavoidun-
necessaryhistoryentries.
• Improvetheexperiencewhenrefreshingremoteupdateandsubscriptionstatusbydisabling
buttonsandshowingaloadingbar.
• Disable the datastore content view and show an appropriate message if the datastore is in
the’offline’maintenancemode.
• Fixaflawwhereanattackercouldmanipulateapanicdisplaytorunarbitrarycodeinauser’s
browsercontext.
• HardentheMarkdownviewer’sHTMLsanitizerbyalsoencodingthe’base’tagandfixingtag-
namecomparisonsthatpreviouslydidnotmatchuppercasevariants.
• AddproperdescriptionsfortasksnativetoProxmoxDatacenterManager.
• Preventthebrowserfromreloadingthepagewhenaddingaremotethroughthewizard.
• FixanissuethatdisplayedthewrongtimezoneforKyiv(issue7141).
• ImproveaddingProxmoxBackupServerremotesbynormalizingthehostnameintheremote
additionwizard.
• Properlydisplay theendpoint URLwhen showingthe automated installerpreparationcom-
mand.
• Fixanissuewherelongercombo-boxescouldbeoverlappedbytheirpicker.
C.1. ReleaseHistory 109

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Use”SystemLog”insteadof”Syslog”inthewebinterface.
• Improvedandupdatedtranslationsformanylanguages,including:
– Arabic
– BrazilianPortuguese
– Croatian
– Czech
– French
– German
– Hungarian
– Italian
– Japanese
– Korean
– Polish
– Russian
– SimplifiedChinese
– Spanish
– Swedish
– TraditionalChinese
– Turkish
– Ukrainian
ResourceManagement
• AllowProxmoxDatacenterManagertoserveanswerfilesforautomatedinstallations.
InstallationscanbetrackedthroughProxmoxDatacenterManager.
Optionsfortheautomatedinstallationcanbemanagedthroughthewebinterface.
AnadditionaltokensystemletsnewinstallationsauthenticateagainstProxmoxDat-
acenterManager,improvingsecurity.
PreparedanswerscanoptionallycarryaProxmoxsubscriptionkey,soanewnode
registersitssubscriptionautomaticallyonfirstboot.
• Whenmigratingaresourcewithoutaspecifictargetendpointacrossclusters,ProxmoxData-
centerManagernowprefershoststhatareknowntobereachable.
Previouslythefirstconfiguredhostofthetargetclusterwaschosen.
• AddatabpanelfortasksintheProxmoxBackupServerremotepanel.
• Take the first step toward central guest management: list and operate on QEMU and LXC
guestsacrossconnectedremotesfromasinglepanel,managetheirsnapshotscentrally,and
resumepausedorsuspendedQEMUguests. Seethehighlightssectionfordetails.
RemotesManagement
• ProxmoxDatacenterManagercannowmanagesubscriptionsforconnectedremotes.
C.1. ReleaseHistory 110

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Thisallowsadministratorstoconfigureacentrallymanagedpoolofsubscriptions.
Subscriptionscanbeappliedtoandclearedfromaremoteviathewebinterface.
Subsequent fixes ensure that key removal tolerates a corrupt shadow file and fin-
ishestheauthoritativepoolconfigremovalfirst.
• AllowmonitoringCephclustersonconnectedhyper-convergedProxmoxVEremotes.
AnewpaneltellsthestatusofmultipleCephclustersataglance.
Further details such as the current health status, capacity, performance, and the
statusofmonitors,managers,OSDsorflagscanbeinspected.
• Re-probe and re-pin a remote’s TLS certificate from the UI or CLI after a certificate rotation,
insteadofhavingtoremoveandre-addtheremote.
Anewdialogre-probestheconfigurednodes,letstheoperatoracceptthenewfin-
gerprintpernodeorclearthestoredpin,andappliesthechangesasasinglebatch.
Thisisastop-gapuntilallProxmoxproductssupportstagedcertificaterotation.
• AddpropersupportfordifferentrealmtypeswhenaddingProxmoxBackupServerremotes.
• AllowremovingthetokengeneratedforProxmoxDatacenterManagerwhenremovingare-
mote(issue6914).
• Properlydropremotesfromthecacheiftheyhavevanished(issue7120).
This fixes an issue where a node could be removed fromthe cluster but still show
upinProxmoxDatacenterManager.
• Whenqueryingthesnapshotsofadatastorefails,moreappropriateerrormessagesarenow
passedthrough.
BackendImprovements
• AllowqueryingProxmoxDatacenterManagerhostmetrics.
• ReturnglobalCPU,memoryandstoragestatisticswhenqueryingthestatusofaresource.
• AddanAPIendpointforrefreshingthetaskcacheforasingleremoteorallremotes.
• AddsupportforOpenIDaudiences(issue5076).
ThisisrequiredtosupportcertainOpenIDproviderslikeZitadel.
• FixabugthatpreventedusersfromanOpenIDrealmfrombeingaddedmanually(issue7182).
• Ensurethatfreshlyfetchedsubscriptiondataisreturnedwhenthemax_ageparameterisset
to0.
• Add better ACME support for servers returning status code 204 when requesting a nonce
(issue6939).
• Reworktheresource,subscriptionandremote-updatecachesontoashared,persistentkey-
value store, making the cached data self-healing and more consistent across these subsys-
tems.
• MovetheviewsAPIhandlersintotheproxyprocessandtightentheirschemaanderrormes-
sages,includingaclearererrorforviewlayoutsthatcontainunknownwidgets.
• Relax the privilege required to list certificate information from Modify to Audit, allowing
read-onlyaccesstocertificatestatewithoutgrantingmodificationrights.
• Thebackendpackagenowrecommendsifupdown2.
• Queryingthehost’scertificateinformationisnowpermittedforanylogged-inuser.
C.1. ReleaseHistory 111

ProxmoxDatacenterManagerDocumentation,Release1.1.9
CommandLineInterfaceEnhancements
• AllowmanagingguestsnapshotsviatheCLI.
• Addasub-commandtoquerythesupportstatusofaProxmoxDatacenterManagerhostand
includeitinthesystemreport.
• AllowmanagingACMEsettingsthroughtheproxmox-datacenter-manager-adminCLI(is-
sue7179).
• AllowspecifyingthetargetIDwhenmigratingaVMorcontainerbetweenProxmoxVEremotes
viatheCLI.
• ImproveCLIcompletioninbash.
• Allow(re-)probingandmanagingthefingerprintofremotesviatheCLI.
• Fixanissuethatpreventedzshcompletionsfrombeinggeneratedproperly.
• ImproveFIDOauthenticatorsupportwhenmultipledevicesareconnectedviatheCLIclient.
KnownIssues&BreakingChanges
• Removedthe/nodes/localhost/rrdataAPIhandler. Theimpactshouldbeminimal,asit
alwaysfailedpreviously.
C.1.2 ProxmoxDatacenterManager1.0
Released04. December2025
• BasedonDebianTrixie(13.2)
• Latest6.17.2-2Kernelasstabledefault
• ZFS2.3.4
Features(Highlights)
• Firststablerelease.
• AddSupportforProxmoxBackupServer.
AllowsmanagingProxmoxBackupServerremotessimilarlytoProxmoxVEremotes.
AnoverviewshowsthecontentsofdifferentdatastoresalongsideRRDgraphs.
The dashboard now includes metrics from Proxmox Backup Server remotes in its
widgets.
• CustomViewsallowcreatingcustomoverviewsofallremotes.
Viewsallowprovidinganoverviewsimilartothedashboardbutwithcustomlayouts
andfilters.
Thedataaviewhasaccesstocanbefilteredbyremotes,resources,resourcetype,
ortags.
Userscanbegrantedaccesstospecificviewswithoutgrantingthemaccesstothe
underlyingremotesorresourcesdirectly.
• Addsupportforaccessingaremote’sshell.
WiththereleaseofProxmoxVE9.1andProxmoxBackupServer4.1,APItokenscan
nowrequestshellaccess.
Proxmox Datacenter Manager leverages this capability to allow accessing shells of
supportedremotesthroughoneunifiedcontrolplane.
• Globalpackagerepositoryandpendingupdatesstatus.
C.1. ReleaseHistory 112

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Anewpaneloffersanoverviewofthestatusofallpackagerepositoriesandavailable
updatesfromremotes.
UpdatescanbeappliedfromwithinProxmoxDatacenterManagerbyleveragingthe
newremoteshellfeatures.
• Improvedauthenticationfunctionalityallowseasierusermanagement.
Proxmox Datacenter Manager now supports LDAP, Active Directory and OpenID
Connectrealmsforauthentication.
Tokens allow granting more fine-grained access to other applications that want to
usetheAPI.
ChangelogOverview
EnhancementsintheWebInterface(GUI)
• Viewsallowforcustomoverviewsofalloraspecificsetofremotesandresources.
Adraganddropeditorallowseasyadjustmentofanywidget.
Thedatathataviewdisplayscanbeeasilytweakedviafilters.
Thedefaultdashboardisprovidedasaninitialview.
• Addapanelforaddingandmanagingnewrealms.
LDAP,ActiveDirectory,andOpenIDconnectrealmscanbeaddedtoalloweasyau-
thenticationmanagement.
LDAPandActiveDirectoryrealmscanalsobesyncedusingthispanel.
Theserealmscanbeconfiguredasdefaultrealms. Defaultrealmsareusedbythe
loginmaskbydefaultinsteadofthePAMrealm.
• AddapanelthatallowsmanagingtokensandallowconfiguringACLentriesfortokens.
• Enablethedocumentationbuttoninthetopnavigationbar.
• LinktoproperbuiltindocumentationinsteadofBetadocumentation.
• A new tab under the “Administration” menu shows the status of the Proxmox Datacenter
Managerhostandallowsshuttingitdownorrebootingit(issue6300).
• Addpresentationofsubscriptionstatusofremotes:
– Theremotesubscriptionstatuscannowberefreshedmanually.
– Remotesubscriptionscannowbeinspectedbyclickingonthesubscriptionstatuspanel
inthedashboard(issue6797).
– Adda“Details”buttoninthesubscriptionpaneltoshowthesubscriptionstatusdialog.
• TagsofProxmoxVEguestsarenowshownintheresourcetree.
• AddapaneldisplayingthenotesofProxmoxVEnodesanddatacenters.
• AlignavailablefunctionalityforProxmoxVEguestswiththeversionoftheremote.
• AllowtheUItorendercomponentsbasedontheuser’sprivileges.
• Removeaduplicateentryfromthepermissionpathselector.
• ImproveProxmoxBackupServerdatastorepanelbymakingthelabelstranslatable.
• ProxmoxBackupServerremotetasksarehandledcorrectlynow.
• Theremotesetupwizardnowvalidatestheremote’sID.
• AddatitletotheProxmoxVEremotetreetoolbar.
• Removeunnecessary“enabled”statuslineforProxmoxVEstorages.
C.1. ReleaseHistory 113

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• DonotshowstorageentriesintheProxmoxVEresourcetreeunconditionally.
• Add a button to allow navigating to a Proxmox VE guest directly in their respective details
views.
• TabsforProxmoxVEandProxmoxBackupServerremotesnowproperlysupporthistorynav-
igation.
• Addawindowtodisplayandcopythesystemreport.
• AnewpanelshowstheProxmoxDatacenterManager’ssubscriptioninformation.
• When adding a remote via the setup wizard, the token name will now include the Proxmox
DatacenterManagerhost. ThisensuresmultipleinstancesofProxmoxDatacenterManager
canbeconnectedtothesameremote.
• Maskremoteshellsiftheremoteversionistoooldtosupportthefeature.
• Fixanissuethatpreventedrealmsfrombeingdeleted(issue6885).
• Fixanissuewhereupdatingastorage’sstatusdidnottriggercorrectly.
• FixanissuethatpreventedusersinthePAMrealmfrombeingaddedasProxmoxDatacenter
Managerusers(issue6787).
• TheUInowproperlyrespectsthetextdirectionforArabic,Persian(Farsi)andHebrew.
• Fixanissuewheretheresourcetreeforasearchwasnotloadedcorrectly.
• Makenavigatingtonetworkresourcesworkproperlyagain.
• Updatedtranslations,amongothers:
– Czech
– French
– Georgian
– German
– Italian
– Japanese
– Korean
– Polish
– Spanish
– Swedish
– TraditionalChinese
– Ukrainian
ResourceManagement
• Remote shells for Proxmox VE and Proxmox Datacenter Manager can be accessed directly
fromtheUI.
ProxmoxVEremotesmakethisshellavailablethroughanewtabinanode’sdetails
panel.
For Proxmox Backup Server remotes, a button was added in the top bar of the
overviewtoopenanewwindowwiththeshell.
• AnewpanelshowshardwareandoptionsconfigurationforProxmoxVEremote’sguests.
• Makesearchtermscase-insensitive.
• Allowsearchingforresourcesbyremotetype.
C.1. ReleaseHistory 114

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Extendmatchingtopropertiesofresources.
• Viewscannowbesearchedfor.
Resourcescanspecifyalistofpropertiesthatcanthenbesearchedfor.
• AddsupportfornewProxmoxVEnetworkresourcetype.
• Allowsearchingforresourcesbynetworktype.
• FixanissuethatneedlesslykeptpollingtheAPIwhenuserswereloggedout.
This could trigger a bug where users were instantly logged out again after a fresh
login.
• ShowVMsandCTsoverviewsinatabpanelforProxmoxVEremotes.
RemotesManagement
• ProxmoxBackupServerremotescannowbeaddedsimilarlytoProxmoxVEremotes.
AwizardcanbeusedtoaddnewProxmoxBackupServerremotes.
ThisincludestheabilitytoinspecttheTLScertificateoftheremotefromwithinthe
wizard,enablingtrust-on-first-use.
Anoverviewpanelshowsthestatusofadatastore,suchasusageandI/Oinforma-
tion,anditscontentsasatreeofbackupsnapshots.
The content of datastores can be inspected, including namespaces and backup
snapshotstheycontain.
The dashboard has also been improved to include new functionality for Proxmox
BackupServerremotes:
– ProxmoxBackupServerremotescanbeaddeddirectlyfromthedashboard.
– ThestatusofallProxmoxBackupServerremotescanbeinspectedfromaded-
icatedpanel.
– Anewpanelshowsdatastoresandtheirstatistics.
• Implementaviewthatdisplaysaglobaloverviewofallavailableupdatesforallremotes.
Thisincludesversioninformationaswellasrepositorystatusinformation.
• AddanupdatepanelforProxmoxBackupServerremotes.
• The subscription status endpoint now marks clusters with nodes that all have an unknown
subscriptionstatusas”unknown”insteadof”mixed”subscriptionstatus.
• TopentitiesnowincludeProxmoxBackupServerremotes.
• ShowmorestatusinformationonProxmoxVEnodesinthenodeoverviewpanel.
FirewallandSoftwareDefinedNetwork
• AddbasicsupporttogatherinformationonaProxmoxVEremote’sfirewallsetup.
An overview panel shows which remote nodes and remote guests have an active
firewallandhowmanyrulesareenabled.
Detailedrulescanbeinspectedbyselectinganentityfromtheoverviewpanel.
• TheIP-VRFandMAC-VRFofaEVPNVNetcannowbequeried.
• ShowthestatusofanIP-VRFandMAC-VRFinnewpanelsintheEVPNpanel.
• Showunknownzonesifthereareany.
• ShowfabricsonProxmoxVEremotesinadditiontozones.
C.1. ReleaseHistory 115

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• ShowSDNzoneswithpendingchangesasstatus“pending”insteadof“unknown”.
BackendImprovements
• AllowfilteringAPIresponsesbasedonaviewparameter.
AviewcanfiltertheresultsofanAPIendpointbasedonresourceID,resourcepool,
resourcetype,remote,andtags.
Bygrantingauserpermissionstoaview,userscanqueryanAPIendpointbasedon
theview’sfilterregardlessoftheirownpermissions.
Currently,viewscanbeusedwhenlistingresources,queryingtopentities,statusof
resources,subscriptionstatusofremotes,andremotetasks.
• Addendpointsthatallowproxyingaremote’sshellviaawebsocket.
• BackendsupportforProxmoxBackupServerremotes:
– AddTLSprobingforProxmoxBackupServerremotes.
– AllowscanningProxmoxBackupServerremotesanalogoustoProxmoxVEremotes.
– Assign an ACL with admin role on “/” for newly created Proxmox Backup Server tokens
whenaddingthemasaremote.
– AllowqueryingaProxmoxBackupServer’sremotestatus.
– AddanewAPIendpointthatreturnsthenamespacesofaremotedatastore.
– AddAPIendpointstoqueryProxmoxBackupServertasks.
– ImproveinformationcollectiononProxmoxBackupServerdatastoresbyincludingcon-
figurationpropertiesandmorestatustypes.
– SupportProxmoxBackupServerremoteupdateinformationcollection.
– RequestlatestmetricsforProxmoxBackupServerwhenusinghourlytimeframe.
– Fix an issue where some Proxmox Backup Server remotes wrongly signaled HttpOnly
cookiesupport,leadingtoanissuewhenqueryingthem.
• Add an endpoint for listing Proxmox VE and Proxmox Backup Server remotes under /pve/
remotesand/pbs/remotesrespectively.
• AddanAPIendpointforretrievingandrefreshingtheremoteupdatesummary.
• Cacheresultsforremoteupdateavailability.
• Polltheremoteupdatestatusviaaperiodictask.
• ImplementLDAPandActiveDirectoryrealmsupport.
• AddsupportforOpenIDConnectrealms.
• Whencollectingtheremotestatus,keeptrackofallremotesthatcollectionhasfailedfor.
• Allownon-rootuserstoaccessseveralendpoints,suchas:
– Queryingtopentities(issue6794).
– ProxmoxBackupServerRRDendpointsandoverview(issue6901).
– ListingSDNcontrollers,VNetsandzonesforallconfiguredProxmoxVEhosts(issue6901).
• Improvepermissionsontheremotetasksendpoint.
• Thenodeupdatesummarynowincludesinformationforpackageversionandrepositorysta-
tus.
• AddanendpointthatallowsqueryingremoteAPTrepositorystatus.
• RemoveentriesofauserintheACLtreewhentheuserisremoved.
C.1. ReleaseHistory 116

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• LogswillnowincludetheAPIpathwhenanAPIcallfails. Unknownerrorswillbeloggedtoo.
• Add endpoints for querying the Proxmox Datacenter Manager host’s status and shutting it
downorrebootingit.
• Fixanissuewhereonlyactivetaskswereincludedintheremotetasklistinsteadofallother
tasks.
• Fixanissuethatbrokemigrationofremoteguests.
• ImprovedocumentationofAPIendpointsandtheirreturntype.
• Task,auth,andaccesslogswillnowberotated.
• Splitremoteconfigurationandtokenstorageintoseparatefiles.
• AddendpointsforqueryingthesubscriptionstatusofProxmoxDatacenterManagerandcon-
nectedProxmoxVEandProxmoxBackupServerremotes.
• NewendpointsallowsqueryingtheconfigurationofaProxmoxVEnodeandclusteroptions.
• AddanAPIendpointtogetthecachedversioninformationofaremote.
CommandLineInterfaceEnhancements
• TheCLIclientcannowlistthestatusandtasklistforProxmoxBackupServerremotes.
• ThetypeofremoteUPIDcanbeinferredbytheclientinsteadofhavingtobeexplicitlyspeci-
fied.
• Add a command for getting all remote subscriptions to
proxmox-datacenter-manager-admin.
• Anewsub-commandtoshowthesubscriptionstatusofallremoteswasadded.
• Fix a bug that prevented the proxmox-datacenter-manager-admin to function as in-
tended.
DocumentationandSupportforTroubleshooting
• AddinitialProxmoxDatacenterManagerdocumentation.
• AddasystemreporttomakesupportingProxmoxDatacenterManagersetupseasier.
• IncludeanAPIviewer.
KnownIssues&BreakingChanges
• TheAPIwasrestructured:
– Endpointsunder/remotes/{id}weremovedto/remotes/remote/{id}.
– API Endpoints for remote-tasks, remote-update, and metrics-collection were
movedunder/remotes.
• Some API endpoints will now correctly return 403 Forbidden error codes when a user has
insufficientpermissionsinsteadof401Unauthorized.
API users relying on the previous erroneous return code may break. Affected are
thefollowingendpoints:
– POST /api2/json/pve/remotes/remote/{remote}/lxc/{vmid}/
remote-migrate
– GET /api2/json/pve/remotes/remote/{remote}/resources
– GET /api2/json/pve/remotes/remote/{remote}/lxc
– GET /api2/json/pve/remotes/remote/{remote}/qemu
C.1. ReleaseHistory 117

ProxmoxDatacenterManagerDocumentation,Release1.1.9
– POST /api2/json/pve/remotes/remote/{remote}/qemu/{vmid}/
remote-migrate
– GET /api2/json/resources/list
– GET /api2/json/resources/status
• SomeAlphareleasesdidnotshipwiththenewHttpOnlyauthenticationflow,APIusersthat
reliedonitmayneedtoadapt.
IdeallynewAPIuserswouldbeswitchedtousetokenswhereverpossible.
• Aminimumpasswordlengthofeightcharactersisnowenforcedonusersofthe“pdm”realm.
• Move the file storing the LDAP password from /etc/proxmox-datacenter-manager/
ldap_passwords.json to /etc/proxmox-datacenter-manager/access/
ldap-passwords.json
ProxmoxDatacenterManager0.9BETA
Released11. September2025
• BasedonDebianTrixie(13)
• Latest6.14.11-1Kernelasstabledefault
• ZFS2.3.4
Features(Highlights)
• NewreleasebasedonthegreatDebianTrixie.
• SeamlessupgradefromProxmoxDatacenterManagerAlpha,seeProxmoxDatacenterMan-
agerUpgradefromAlphatoBeta.
• EVPNconfigurationforSoftware-DefinedNetworkingbetweenclusters.
AnewpanelprovidesanoverviewofthestateofallEVPNzonesacrossallremotes.
CreateEVPNZonesandVNetsacrossmultipleremotesfromasingleinterface.
AmoredetailedexplanationofProxmoxDatacenterManager’sSDNcapabilitiescan
befoundinthedocumentation.
• Improvedsearchfunctionalitytofindresourcesquicker.
Allows filtering by resource type (remote, virtual machine, container…), status
(stopped,running…)andmuchmore.
ThequerysyntaxisinspiredbyElasticsearchandGitHub’squerylanguage.
Pleaserefertothedocumentationforamorethoroughexplanationofthesyntax.
• Moreefficientmetriccollectionlogic.
Metricsarenowcollectedconcurrently.
• IntegrateprivilegemanagementintheaccesscontrolUI.
AllowmanagingthepermissionsofProxmoxDatacenterManagerusers.
ChangelogOverview
EnhancementsintheWebInterface(GUI)
• AddatimeframeselectorforRRDgraphstoallowuserstoselectthedisplayedtimeframe.
• DisplaynewmetricssuchasPressureStallInformation(PSI)forProxmoxVE9hosts.
C.1. ReleaseHistory 118

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Improve the remote URL list of a remote by adding a placeholder, clear trigger and clearer
columnheaders.
• EnhancementstotheProxmoxVEremotesetupwizard.
Probehostsforfingerprintsettings,toverifyaprovidedfingerprintortoenabletrust
onfirstuse(TOFU).
Try matching the provided host against the host list that was queried from the re-
motetoavoidduplicates.
Resetlaterpageswhenpreviouspageshavebeenchanged,astheyneedtobere-
visited.
• Makethe“remoteloading”iconnicer.
• Correctlyshowa“cube”iconforcontainerguests.
• Addapanelthatallowsaddingandeditingpermissions.
• Movethenodeoverviewtoatabandaddatabthatdisplaysavailableupdates.
• Addabuttonlinkingtheusertoaremote’supgradepage.
• AdddescriptionsforSoftwareDefinedNetworkingtasks.
• ProvideanEVPNoverviewpanelfordisplayingEVPNZonesandVnets.
• AddaviewforshowingEVPNVRFinstancesacrossallremotes.
• AllowcreatingEVPNVNets.
• Open the search panel when clicking different panels in the dashboard and pre-fill it with
appropriatefilters.
• Addacleartriggertothesearchbar.
• Provideasearchiconintheguestpanelforbetterdiscoverabilityofthesearchfunction.
• Includeasummaryofalltasksinthedashboard.
• Renderstatusiconswithashadowinsteadofasolidbackgroundforacleanerlook.
• Enhancethereloadinglogicforthedashboard.
• Showtasksfromthelast48hoursinthedashboard’stasksummary.
• Closethesearchboxifausernavigatedtoanentry.
• DisplayalistofstoragesandtheirstatusintheresourcetreeofaProxmoxVEremote.
• Changethewarningandcriticalthresholdsto90%and97.5%respectively.
• Don’tshowastartorshutdownbuttonfortemplates(issue6782).
• ThedashboardnowincludesapanelshowingtheSDNstatusreport.
• ShowanoverviewofallSDNzonesandtheirstatusasatree.
TheEVPNsectionisnowmovedbelowtheSDNmenutomimicProxmoxVE’smenu
structure.
• Routetocorrectpanelswhennavigatingbetweencomponents.
• Allowfilteringtasksinthetasklistbyremote.
• Showthe remotetasks when selecting the rootnode of the resourcetreefor aProxmoxVE
remote.
• AllownavigatingtoanSDNzoneandSDNpanelofaremotefromthezonetreeoverview.
• Showfailedtasksonlyintasksummary.
• Addsupportforinitialtranslations:
C.1. ReleaseHistory 119

ProxmoxDatacenterManagerDocumentation,Release1.1.9
– Arabic
– Bulgarian
– Catalan
– Chinese(Simplified)
– Chinese(Traditional)
– Croatian
– Czech
– Danish
– Dutch
– Euskera(Basque)
– French
– Georgian
– German
– Hebrew
– Italian
– Japanese
– Korean
– Norwegian(Bokmal)
– Norwegian(Nynorsk)
– Persian(Farsi)
– Polish
– Portuguese(Brazil)
– Russian
– Slovenian
– Spanish
– Swedish
– Turkish
– Ukrainian
RemotesManagement
• EnableProxmoxBackupServerIntegration,CLIonlyfornow.
• EnableconnectiontrackingwhenlivemigratingVMsonremotes.
Whetherconnectiontrackingactuallypersistsaftermigrationalsodependsonthe
environmentandespeciallyonwhetherthirdpartyfirewallsareused.
• Enabletrustonfirstuse(TOFU)promptswhenaddingremotes.
• Includetemplatesinstatuscounts.
• AddanAPIendpointthatallowsqueryingupdatesandchangelogsfromremotes.
• AddtheAPIinfrastructurefortheinitialSoftwareDefinedNetworkingintegration.
BackendImprovements
• Improverobustnessofincomingconnectionhandling.
C.1. ReleaseHistory 120

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Improvesizerequirementsandperformanceforremotetaskscache.
• Moreintelligentlyqueryremotetasks.
• FixanissuewheretheACMEconfigurationwouldnotbeconstructedproperlyforthedefault
account.
• Collectmetricsfromremotesconcurrentlytoimproveperformance.
• Persistmetriccollectionstateafteraruntoallowreusingitafteradaemonrestart.
Thisshouldallowmoreefficientmetriccollectionrunsafterrestarts.
• Metrics that should have been collected already, but were not due to collection timing
changes,willnowbecollected.
• Keep track of the time it took to collect metrics from each single remote and all remotes
together.
Thisprovidesbetterinsightsintotheperformanceofmetriccollectionruns.
• AddanAPIendpointtotriggermetriccollection.
• Triggerimmediatemetriccollectionwhenaremoteisadded.
• Whenametriccollectiontaskisdelayedskipitinsteadoftriggeringitquicker.
• AddamorecomplexfilterandsearchsyntaxinspiredbyElasticsearchandGitHubquerylan-
guage.
• Whenqueryingtheremotetasklisttreatalimitof“0”asunboundedandreturntheentirelist.
• Allowfilteringremotetasksbyremote.
• AddanAPIendpointthatallowsqueryingremotetaskstatistics.
• AddAPIendpointsforqueryingProxmoxVEstorage’sRRDdataandstatus.
• Addaresource-typeparametertotheresourcesAPIendpoints.
This allows more efficient filtering when querying the API for tasks and resource
statuses.
• Don’tmatchtemplateswhensearchingbyremote.
• Improvesearchwhensearchingbyremotes.
Forexample,searchingforallVMsofaspecificremoteisnowpossible.
• Whenencounteringanerror,returntherootcausenotthetoplevelerrorwhenfetchingre-
motes.
Thismakesthereportederrormessagesmorespecific.
CommandLineInterfaceEnhancements
• Allow query the status and RRD data from remotes via
proxmox-datacenter-manager-client.
• Addanupgradecheckingscript(pdmAtoB)tomakeupgradesmoreseamless.
• The utility proxmox-datacenter-manager-admin can now display the currently running
version.
MiscellaneousImprovements
• Loganerrorwhenatasktoqueryremotetasksfailsinsteadofcancellingalltasks.
• Fixtheorderfiltersareappliedwhenrequestingafilteredtasklist.
• Usethenewdeb822formatforpackagerepositories.
• Add a CLI command to allow querying the metric collection status and triggering a metric
collectionrun.
C.1. ReleaseHistory 121

ProxmoxDatacenterManagerDocumentation,Release1.1.9
• Handleamissingjournalfileerrormoregracefullywhenqueryingthetasklist.
KnownIssues&BreakingChanges
• TheAPIendpointforlistingrealmswaschangedfromaPOSTtoaGETrequest.
ProxmoxDatacenterManager0.1ALPHA
Released19. December2024
• BasedonDebianBookworm(12.8)
• Latest6.8.12-5Kernelasstabledefault
• Newer6.11Kernelasopt-in
• ZFS:2.2.6(withcompatibilitypatchesforKernel6.11)
Features(Highlights)
• Connecttoandviewanynumberofindependentnodesorclusters(”Datacenters”)
• Viewthebasicresourceusageofallnodesandtheirguests.
Savesandcachesthelistofresources(mainlyguestsandstorage)andtheirusage
metrics to provide a quick overview of all resources and the last-seen state for of-
fline/unresponsiveones.
• Basicmanagementoftheresources: shutdown,reboot,start,…
Formorecomplexmanagementtasks,itprovidesadirectlinktothefullwebinter-
faceofProxmoxVE/ProxmoxBackupServer/…
• Remotemigrationofvirtualguestsbetweendifferentdatacenters.
• SupportforthestandardProxmoxfeaturesetincludingcomplexMulti-FactorAuthentication
orACME/Let’sEncryptfromthebeginning.
ChangelogOverview
Notapplicableforthefirstalpharelease.
KnownIssues&BreakingChanges
Thisisanalpharelease,theremightbelotsofstuffthatisbroken,getsreworkedandfixedsome-
whatfrequently.
C.1. ReleaseHistory 122

APPENDIX
D
MARKDOWN PRIMER
”Markdownisatext-to-HTMLconversiontoolforwebwriters. Markdownallowsyouto
writeusinganeasy-to-read,easy-to-writeplaintextformat,thenconvertittostructurally
validXHTML(orHTML).”
—JohnGruber,https://daringfireball.net/projects/markdown/
The”Notes”paneloftheProxmoxDatacenterManagerweb-interfacesupportsrenderingMarkdown
text.
ProxmoxBackupServersupportsCommonMarkwithmostextensionsofGFM(GitHubFlavoured
Markdown),liketablesortask-lists.
D.1 Markdown Basics
Notethatweonlydescribethebasicshere. Pleasesearchthewebformoreextensiveresources,
forexampleonhttps://www.markdownguide.org/
D.1.1 Headings
# This is a Heading h1
## This is a Heading h2
##### This is a Heading h5
D.1.2 Emphasis
Use*text*or_text_foremphasis.
Use**text**or__text__forbold,heavy-weighttext.
Combinationsarealsopossible,forexample:
_You **can** combine them_
D.1.3 Links
You can use automatic detection of links. For example, https://forum.proxmox.com/ would
transformitintoaclickablelink.
Youcanalsocontrolthelinktext,forexample:
Now, [the part in brackets will be the link text](https://forum.proxmox.com/).
123

ProxmoxDatacenterManagerDocumentation,Release1.1.9
D.1.4 Lists
UnorderedLists
Use*or-forunorderedlists,forexample:
* Item 1
* Item 2
* Item 2a
* Item 2b
Youcancreatenestedlistsbyaddingindentation.
OrderedLists
1. Item 1
1. Item 2
1. Item 3
| 1. Item | 3a  |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
| 1. Item | 3b  |     |     |     |     |
NOTE:Theintegeroforderedlistsdoesnotneedtobecorrect,theywillbenumberedautomatically.
TaskLists
Tasklistsuseaemptybox[ ]forunfinishedtasksandaboxwithanX forfinishedtasks.
Forexample:
| - [X] First  | task already | done! |     |     |     |
| ------------ | ------------ | ----- | --- | --- | --- |
| - [X] Second | one too      |       |     |     |     |
| - [ ] This   | one is still | to-do |     |     |     |
| - [ ] So     | is this one  |       |     |     |     |
D.1.5 Tables
Tablesusethepipesymbol|toseparatecolumns,and-toseparatethetableheaderfromthetable
body. Inthatseparation,youcanalsosetthetextalignment,makingonecolumnleft-,center-,or
right-aligned.
| Left columns | Right columns | Some | More | Cols.| Centering Works Too
| ------------- |--------------:|--------|------|------|:------------------:|
| | left | foo | right | foo | | First | Row | Here  | | >center< | |   |
| ------ | ----------- | ----- | ------------------- | ---------- | --- |
| | left | bar | right | bar | | Second | Row | Here | | 12345    | |   |
| | left | baz | right | baz | | Third | Row | Here  | | Test     | |   |
| | left | zab | right | zab | | Fourth | Row | Here | | ☁☁☁      | |   |
| | left | rab | right | rab | | And | Last | Here   | | The End  | |   |
Note that you do not need to align the columns nicely with white space, but that makes editing
tableseasier.
D.1.6 BlockQuotes
Youcanenterblockquotesbyprefixingalinewith>,similarasinplain-textemails.
> Markdown is a lightweight markup language with plain-text-formatting syntax,
| > created | in 2004 by | John Gruber with | Aaron Swartz. |     |     |
| --------- | ---------- | ---------------- | ------------- | --- | --- |
>
>> Markdown is often used to format readme files, for writing messages in online discussion␣
,→forums,
| >> and | to create rich | text using a | plain text editor. |     |     |
| ------ | -------------- | ------------ | ------------------ | --- | --- |
D.1.7 CodeandSnippets
Youcanusebacktickstoavoidprocessingagroupofwordsorparagraphs. Thisisusefulforpre-
ventingacodeorconfigurationhunkfrombeingmistakenlyinterpretedasmarkdown.
D.1. MarkdownBasics 124

ProxmoxDatacenterManagerDocumentation,Release1.1.9
InlineCode
Surroundingpartofalinewithsinglebackticksallowsyoutowritecodeinline,forexamples:
| This hosts | IP address | is `10.0.0.1`. |     |
| ---------- | ---------- | -------------- | --- |
EntireBlocksofCode
Forcodeblocksspanningseverallines,youcanusetriple-backtickstostartandendsuchablock,
forexample:
```
| # This | is the network | config I want to remember | here |
| ------ | -------------- | ------------------------- | ---- |
auto vmbr2
| iface vmbr2 | inet static         |        |     |
| ----------- | ------------------- | ------ | --- |
|             | address 10.0.0.1/24 |        |     |
|             | bridge-ports        | ens20  |     |
|             | bridge-stp          | off    |     |
|             | bridge-fd           | 0      |     |
|             | bridge-vlan-aware   | yes    |     |
|             | bridge-vids         | 2-4094 |     |
```
D.1. MarkdownBasics 125

APPENDIX
E
GNU FREE DOCUMENTATION LICENSE
Version1.3,3November2008
Copyright(C)2000,2001,2002,2007,2008FreeSoftwareFoundation,Inc. <https://fsf.org/>
Everyoneispermittedtocopyanddistributeverbatimcopiesofthis
licensedocument,butchangingitisnotallowed.
0. PREAMBLE
ThepurposeofthisLicenseistomakeamanual,textbook,orotherfunctionalandusefuldocument
”free”inthesenseoffreedom: toassureeveryonetheeffectivefreedomtocopyandredistribute
it,withorwithoutmodifyingit,eithercommerciallyornoncommercially. Secondarily,thisLicense
preservesfortheauthorandpublisherawaytogetcreditfortheirwork,whilenotbeingconsidered
responsibleformodificationsmadebyothers.
ThisLicenseisakindof”copyleft”,whichmeansthatderivativeworksofthedocumentmustthem-
selvesbefreeinthesamesense. ItcomplementstheGNUGeneralPublicLicense,whichisacopy-
leftlicensedesignedforfreesoftware.
WehavedesignedthisLicenseinordertouseitformanualsforfreesoftware,becausefreesoft-
ware needs free documentation: a free program should come with manuals providing the same
freedomsthatthesoftwaredoes. ButthisLicenseisnotlimitedtosoftwaremanuals;itcanbeused
foranytextualwork,regardlessofsubjectmatterorwhetheritispublishedasaprintedbook. We
recommendthisLicenseprincipallyforworkswhosepurposeisinstructionorreference.
1. APPLICABILITYANDDEFINITIONS
This License applies to any manual or other work, in any medium, that contains a notice placed
bythecopyrightholdersayingitcanbedistributedunderthetermsofthisLicense. Suchanotice
grantsaworld-wide,royalty-freelicense,unlimitedinduration,tousethatworkunderthecondi-
tions stated herein. The ”Document”, below, refers to any such manual or work. Any member of
the public is a licensee, and is addressed as ”you”. You accept the license if you copy, modify or
distributetheworkinawayrequiringpermissionundercopyrightlaw.
A”ModifiedVersion”oftheDocumentmeansanyworkcontainingtheDocumentoraportionofit,
eithercopiedverbatim,orwithmodificationsand/ortranslatedintoanotherlanguage.
A”SecondarySection”isanamedappendixorafront-mattersectionoftheDocumentthatdeals
exclusivelywiththerelationshipofthepublishersorauthorsoftheDocumenttotheDocument’s
overallsubject(ortorelatedmatters)andcontainsnothingthatcouldfalldirectlywithinthatoverall
subject. (Thus,iftheDocumentisinpartatextbookofmathematics,aSecondarySectionmaynot
explain any mathematics.) The relationship could be a matter of historical connection with the
subjectorwithrelatedmatters,oroflegal,commercial,philosophical,ethicalorpoliticalposition
regardingthem.
The”InvariantSections”arecertainSecondarySectionswhosetitlesaredesignated,asbeingthose
of Invariant Sections, in the notice that says that the Document is released under this License. If
asectiondoesnotfittheabovedefinitionofSecondarythenitisnotallowedtobedesignatedas
Invariant. TheDocumentmaycontainzeroInvariantSections. IftheDocumentdoesnotidentify
anyInvariantSectionsthentherearenone.
126

ProxmoxDatacenterManagerDocumentation,Release1.1.9
The ”Cover Texts” are certain short passages of text that are listed, as Front-Cover Texts or Back-
CoverTexts,inthenoticethatsaysthattheDocumentisreleasedunderthisLicense. AFront-Cover
Textmaybeatmost5words,andaBack-CoverTextmaybeatmost25words.
A ”Transparent” copy of the Document means a machine-readable copy, represented in a format
whose specification is available to the general public, that is suitable for revising the document
straightforwardly with generic text editors or (for images composed of pixels) generic paint pro-
gramsor(fordrawings)somewidelyavailabledrawingeditor,andthatissuitableforinputtotext
formattersorforautomatictranslationtoavarietyofformatssuitableforinputtotextformatters.
A copy made in an otherwise Transparent file format whose markup, or absence of markup, has
been arranged to thwart or discourage subsequent modification by readers is not Transparent.
AnimageformatisnotTransparentifusedforanysubstantialamountoftext. Acopythatisnot
”Transparent”iscalled”Opaque”.
Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo
input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-
conformingsimpleHTML,PostScriptorPDFdesignedforhumanmodification. Examplesoftrans-
parentimageformatsincludePNG,XCFandJPG.Opaqueformatsincludeproprietaryformatsthat
canbereadandeditedonlybyproprietarywordprocessors,SGMLorXMLforwhichtheDTDand/or
processingtoolsarenotgenerallyavailable,andthemachine-generatedHTML,PostScriptorPDF
producedbysomewordprocessorsforoutputpurposesonly.
The ”Title Page” means, for a printed book, the title page itself, plus such following pages as are
needed to hold, legibly, the material this License requires to appear in the title page. For works
in formats which do not have any title page as such, ”Title Page” means the text near the most
prominentappearanceofthework’stitle,precedingthebeginningofthebodyofthetext.
The”publisher”meansanypersonorentitythatdistributescopiesoftheDocumenttothepublic.
A section ”Entitled XYZ” means a named subunit of the Document whose title either is precisely
XYZ or contains XYZ in parentheses following text that translates XYZ in another language. (Here
XYZ stands for a specific section name mentioned below, such as ”Acknowledgements”, ”Dedica-
tions”,”Endorsements”,or”History”.) To”PreservetheTitle”ofsuchasectionwhenyoumodifythe
Documentmeansthatitremainsasection”EntitledXYZ”accordingtothisdefinition.
TheDocumentmayincludeWarrantyDisclaimersnexttothenoticewhichstatesthatthisLicense
appliestotheDocument. TheseWarrantyDisclaimersareconsideredtobeincludedbyreferencein
thisLicense,butonlyasregardsdisclaimingwarranties: anyotherimplicationthattheseWarranty
DisclaimersmayhaveisvoidandhasnoeffectonthemeaningofthisLicense.
2. VERBATIMCOPYING
You may copy and distribute the Document in any medium, either commercially or noncommer-
cially, provided that this License, the copyright notices, and the license notice saying this License
appliestotheDocumentarereproducedinallcopies,andthatyouaddnootherconditionswhat-
soever to those of this License. You may not use technical measures to obstruct or control the
reading or further copying of the copies you make or distribute. However, you may accept com-
pensationinexchangeforcopies. Ifyoudistributealargeenoughnumberofcopiesyoumustalso
followtheconditionsinsection3.
Youmayalsolendcopies,underthesameconditionsstatedabove,andyoumaypubliclydisplay
copies.
3. COPYINGINQUANTITY
Ifyoupublishprintedcopies(orcopiesinmediathatcommonlyhaveprintedcovers)oftheDoc-
ument, numbering more than 100, and the Document’s license notice requires Cover Texts, you
mustenclosethecopiesincoversthatcarry,clearlyandlegibly,alltheseCoverTexts: Front-Cover
Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly
andlegiblyidentifyyouasthepublisherofthesecopies. Thefrontcovermustpresentthefulltitle
withallwordsofthetitleequallyprominentandvisible. Youmayaddothermaterialonthecovers
in addition. Copying with changes limited to the covers, as long as they preserve the title of the
Documentandsatisfytheseconditions,canbetreatedasverbatimcopyinginotherrespects.
127

ProxmoxDatacenterManagerDocumentation,Release1.1.9
Iftherequiredtextsforeithercoveraretoovoluminoustofitlegibly,youshouldputthefirstones
listed(asmanyasfitreasonably)ontheactualcover,andcontinuetherestontoadjacentpages.
IfyoupublishordistributeOpaquecopiesoftheDocumentnumberingmorethan100,youmust
either include a machine-readable Transparent copy along with each Opaque copy, or state in or
witheachOpaquecopyacomputer-networklocationfromwhichthegeneralnetwork-usingpub-
lichasaccesstodownloadusingpublic-standardnetworkprotocolsacompleteTransparentcopy
of the Document, free of added material. If you use the latter option, you must take reasonably
prudentsteps,whenyoubegindistributionofOpaquecopiesinquantity,toensurethatthisTrans-
parentcopywillremainthusaccessibleatthestatedlocationuntilatleastoneyearafterthelast
timeyoudistributeanOpaquecopy(directlyorthroughyouragentsorretailers)ofthateditionto
thepublic.
Itisrequested,butnotrequired,thatyoucontacttheauthorsoftheDocumentwellbeforeredis-
tributinganylargenumberofcopies,togivethemachancetoprovideyouwithanupdatedversion
oftheDocument.
4. MODIFICATIONS
YoumaycopyanddistributeaModifiedVersionoftheDocumentundertheconditionsofsections
2 and 3 above, provided that you release the Modified Version under precisely this License, with
theModifiedVersionfillingtheroleoftheDocument,thuslicensingdistributionandmodification
oftheModifiedVersiontowhoeverpossessesacopyofit. Inaddition,youmustdothesethingsin
theModifiedVersion:
A. Use in the Title Page (and on the covers, if any) a title distinct from that of the Document,
andfromthoseofpreviousversions(whichshould,iftherewereany,belistedintheHistory
section of the Document). You may use the same title as a previous version if the original
publisherofthatversiongivespermission.
B. ListontheTitlePage,asauthors,oneormorepersonsorentitiesresponsibleforauthorship
ofthemodificationsintheModifiedVersion,togetherwithatleastfiveoftheprincipalauthors
oftheDocument(allofitsprincipalauthors,ifithasfewerthanfive),unlesstheyreleaseyou
fromthisrequirement.
C. StateontheTitlepagethenameofthepublisheroftheModifiedVersion,asthepublisher.
D. PreserveallthecopyrightnoticesoftheDocument.
E. Add an appropriate copyright notice for your modifications adjacent to the other copyright
notices.
F. Include, immediately after the copyright notices, a license notice giving the public permis-
sion to use the Modified Version under the terms of this License, in the form shown in the
Addendumbelow.
G. PreserveinthatlicensenoticethefulllistsofInvariantSectionsandrequiredCoverTextsgiven
intheDocument’slicensenotice.
H. IncludeanunalteredcopyofthisLicense.
I. PreservethesectionEntitled”History”,PreserveitsTitle,andaddtoitanitemstatingatleast
thetitle,year,newauthors,andpublisheroftheModifiedVersionasgivenontheTitlePage.
If there is no section Entitled ”History” in the Document, create one stating the title, year,
authors,andpublisheroftheDocumentasgivenonitsTitlePage,thenaddanitemdescribing
theModifiedVersionasstatedintheprevioussentence.
J. Preservethenetworklocation,ifany,givenintheDocumentforpublicaccesstoaTransparent
copyoftheDocument,andlikewisethenetworklocationsgivenintheDocumentforprevious
versions it was based on. These may be placed in the ”History” section. You may omit a
networklocationforaworkthatwaspublishedatleastfouryearsbeforetheDocumentitself,
oriftheoriginalpublisheroftheversionitreferstogivespermission.
K. ForanysectionEntitled”Acknowledgements”or”Dedications”, PreservetheTitleofthesec-
tion, and preserve in the section all the substance and tone of each of the contributor ac-
knowledgementsand/ordedicationsgiventherein.
128

ProxmoxDatacenterManagerDocumentation,Release1.1.9
L. PreservealltheInvariantSectionsoftheDocument,unalteredintheirtextandintheirtitles.
Sectionnumbersortheequivalentarenotconsideredpartofthesectiontitles.
M. DeleteanysectionEntitled”Endorsements”. SuchasectionmaynotbeincludedintheMod-
ifiedVersion.
N. DonotretitleanyexistingsectiontobeEntitled”Endorsements”ortoconflictintitlewithany
InvariantSection.
O. PreserveanyWarrantyDisclaimers.
IftheModifiedVersionincludesnewfront-mattersectionsorappendicesthatqualifyasSecondary
Sections and contain no material copied from the Document, you may at your option designate
someorallofthesesectionsasinvariant. Todothis,addtheirtitlestothelistofInvariantSections
intheModifiedVersion’slicensenotice. Thesetitlesmustbedistinctfromanyothersectiontitles.
YoumayaddasectionEntitled”Endorsements”,provideditcontainsnothingbutendorsementsof
yourModifiedVersionbyvariousparties--forexample,statementsofpeerrevieworthatthetext
hasbeenapprovedbyanorganizationastheauthoritativedefinitionofastandard.
YoumayaddapassageofuptofivewordsasaFront-CoverText,andapassageofupto25words
asaBack-CoverText,totheendofthelistofCoverTextsintheModifiedVersion. Onlyonepassage
ofFront-CoverTextandoneofBack-CoverTextmaybeaddedby(orthrougharrangementsmade
by) any one entity. If the Document already includes a cover text for the same cover, previously
addedbyyouorbyarrangementmadebythesameentityyouareactingonbehalfof,youmaynot
addanother;butyoumayreplacetheoldone,onexplicitpermissionfromthepreviouspublisher
thataddedtheoldone.
Theauthor(s)andpublisher(s)oftheDocumentdonotbythisLicensegivepermissiontousetheir
namesforpublicityforortoassertorimplyendorsementofanyModifiedVersion.
5. COMBININGDOCUMENTS
You may combine the Document with other documents released under this License, under the
terms defined in section 4 above for modified versions, provided that you include in the combi-
nation all of the Invariant Sections of all of the original documents, unmodified, and list them all
as Invariant Sections of your combined work in its license notice, and that you preserve all their
WarrantyDisclaimers.
The combined work need only contain one copy of this License, and multiple identical Invariant
Sectionsmaybereplacedwithasinglecopy. IftherearemultipleInvariantSectionswiththesame
name but different contents, make the title of each such section unique by adding at the end of
it, inparentheses,thenameoftheoriginalauthororpublisherofthatsectionifknown, orelsea
uniquenumber. MakethesameadjustmenttothesectiontitlesinthelistofInvariantSectionsin
thelicensenoticeofthecombinedwork.
Inthecombination, youmustcombineanysectionsEntitled”History”inthevariousoriginaldoc-
uments, forming one section Entitled ”History”; likewise combine any sections Entitled ”Acknowl-
edgements”, and any sections Entitled ”Dedications”. You must delete all sections Entitled ”En-
dorsements”.
6. COLLECTIONSOFDOCUMENTS
YoumaymakeacollectionconsistingoftheDocumentandotherdocumentsreleasedunderthis
License, and replace the individual copies of this License in the various documents with a single
copythatisincludedinthecollection,providedthatyoufollowtherulesofthisLicenseforverbatim
copyingofeachofthedocumentsinallotherrespects.
Youmayextractasingledocumentfromsuchacollection,anddistributeitindividuallyunderthis
License, provided you insert a copy of this License into the extracted document, and follow this
Licenseinallotherrespectsregardingverbatimcopyingofthatdocument.
7. AGGREGATIONWITHINDEPENDENTWORKS
AcompilationoftheDocumentoritsderivativeswithotherseparateandindependentdocuments
or works, in or on a volume of a storage or distribution medium, is called an ”aggregate” if the
129

ProxmoxDatacenterManagerDocumentation,Release1.1.9
copyright resulting from the compilation is not used to limit the legal rights of the compilation’s
usersbeyondwhattheindividualworkspermit. WhentheDocumentisincludedinanaggregate,
thisLicensedoesnotapplytotheotherworksintheaggregatewhicharenotthemselvesderivative
worksoftheDocument.
IftheCoverTextrequirementofsection3isapplicabletothesecopiesoftheDocument,thenifthe
Documentislessthanonehalfoftheentireaggregate,theDocument’sCoverTextsmaybeplaced
oncoversthatbrackettheDocumentwithintheaggregate, ortheelectronicequivalentofcovers
iftheDocumentisinelectronicform. Otherwisetheymustappearonprintedcoversthatbracket
thewholeaggregate.
8. TRANSLATION
Translation is considered a kind of modification, so you may distribute translations of the Docu-
mentunderthetermsofsection4. ReplacingInvariantSectionswithtranslationsrequiresspecial
permissionfromtheircopyrightholders,butyoumayincludetranslationsofsomeorallInvariant
SectionsinadditiontotheoriginalversionsoftheseInvariantSections. Youmayincludeatrans-
lationofthisLicense, andallthelicensenoticesintheDocument, andanyWarrantyDisclaimers,
providedthatyoualsoincludetheoriginalEnglishversionofthisLicenseandtheoriginalversions
ofthosenoticesanddisclaimers. Incaseofadisagreementbetweenthetranslationandtheorigi-
nalversionofthisLicenseoranoticeordisclaimer,theoriginalversionwillprevail.
If a section in the Document is Entitled ”Acknowledgements”, ”Dedications”, or ”History”, the re-
quirement(section4)toPreserveitsTitle(section1)willtypicallyrequirechangingtheactualtitle.
9. TERMINATION
You may not copy, modify, sublicense, or distribute the Document except as expressly provided
underthisLicense. Anyattemptotherwisetocopy,modify,sublicense,ordistributeitisvoid,and
willautomaticallyterminateyourrightsunderthisLicense.
However, if you cease all violation of this License, then your license from a particular copyright
holderisreinstated(a)provisionally,unlessanduntilthecopyrightholderexplicitlyandfinallyter-
minatesyourlicense,and(b)permanently,ifthecopyrightholderfailstonotifyyouoftheviolation
bysomereasonablemeanspriorto60daysafterthecessation.
Moreover, your license from a particular copyright holder is reinstated permanently if the copy-
rightholdernotifiesyouoftheviolationbysomereasonablemeans,thisisthefirsttimeyouhave
receivednoticeofviolationofthisLicense(foranywork)fromthatcopyrightholder,andyoucure
theviolationpriorto30daysafteryourreceiptofthenotice.
Terminationofyourrightsunderthissectiondoesnotterminatethelicensesofpartieswhohave
receivedcopiesorrightsfromyouunderthisLicense. Ifyourrightshavebeenterminatedandnot
permanentlyreinstated,receiptofacopyofsomeorallofthesamematerialdoesnotgiveyouany
rightstouseit.
10. FUTUREREVISIONSOFTHISLICENSE
TheFreeSoftwareFoundationmaypublishnew,revisedversionsoftheGNUFreeDocumentation
License from time to time. Such new versions will be similar in spirit to the present version, but
maydifferindetailtoaddressnewproblemsorconcerns. Seehttps://www.gnu.org/licenses/.
Each version of the License is given a distinguishing version number. If the Document specifies
thataparticularnumberedversionofthisLicense”oranylaterversion”appliestoit,youhavethe
optionoffollowingthetermsandconditionseitherofthatspecifiedversionorofanylaterversion
that has been published (not as a draft) by the Free Software Foundation. If the Document does
notspecifyaversionnumberofthisLicense, youmaychooseanyversioneverpublished(notas
adraft)bytheFreeSoftwareFoundation. IftheDocumentspecifiesthataproxycandecidewhich
futureversionsofthisLicensecanbeused,thatproxy’spublicstatementofacceptanceofaversion
permanentlyauthorizesyoutochoosethatversionfortheDocument.
11. RELICENSING
”Massive Multiauthor Collaboration Site” (or ”MMC Site”) means any World Wide Web server that
publishes copyrightable works and also provides prominent facilities for anybody to edit those
130

ProxmoxDatacenterManagerDocumentation,Release1.1.9
works. A public wiki that anybody can edit is an example of such a server. A ”Massive Multiau-
thor Collaboration” (or ”MMC”) contained in the site means any set of copyrightable works thus
publishedontheMMCsite.
”CC-BY-SA”meanstheCreativeCommonsAttribution-ShareAlike3.0licensepublishedbyCreative
CommonsCorporation,anot-for-profitcorporationwithaprincipalplaceofbusinessinSanFran-
cisco,California,aswellasfuturecopyleftversionsofthatlicensepublishedbythatsameorgani-
zation.
”Incorporate” means to publish or republish a Document, in whole or in part, as part of another
Document.
AnMMCis”eligibleforrelicensing”ifitislicensedunderthisLicense,andifallworksthatwerefirst
published under this License somewhere other than this MMC, and subsequently incorporated
in whole or in part into the MMC, (1) had no cover texts or invariant sections, and (2) were thus
incorporatedpriortoNovember1,2008.
TheoperatorofanMMCSitemayrepublishanMMCcontainedinthesiteunderCC-BY-SAonthe
samesiteatanytimebeforeAugust1,2009,providedtheMMCiseligibleforrelicensing.
131