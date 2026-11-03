Migration Toolkit for Virtualization 2.12
Planning your migration to Red Hat OpenShift
Virtualization
Planning your migration of virtual machines from VMware vSphere, Red Hat
Virtualization or OpenStack platforms, or other platforms to Red Hat OpenShift
Virtualization by using the Migration Toolkit for Virtualization
Last Updated: 2026-09-15

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat
OpenShift Virtualization
Planning your migration of virtual machines from VMware vSphere, Red Hat Virtualization or
OpenStack platforms, or other platforms to Red Hat OpenShift Virtualization by using the Migration
Toolkit for Virtualization
Red Hat Modernization and Migration Documentation Team
ccs-mms-docs@redhat.com

Legal Notice
Copyright © Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by
Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you
distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert,
Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of
Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux ® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its
subsidiaries in the United States and other countries.
The OpenStack ® Word Mark and OpenStack logo are trademarks or registered trademarks of the
Linux Foundation, used under license.
All other trademarks are the property of their respective owners.
Abstract
Install the Migration Toolkit for Virtualization (MTV) Operator and configure MTV to plan a cold or
warm migration of virtual machines to Red Hat OpenShift Virtualization on an OpenShift platform.
Map the source and destination infrastructure for your migration, including storage and networking,
and create validation rules.

Table of Contents
Table of Contents
.C . H. .A . P. .T .E . R. . 1.. .P . L. .A . N. .N . I. N. .G . .A . .M . .I G. .R . A. .T . I.O . .N . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1. TYPES OF MIGRATION 6
.C . H. .A . P. .T .E . R. . 2. .. C. .O . .L . D. . A. .N . D. . W. . A. .R . M. . .M . I. G. .R . A. .T . I.O . N. . I. N. . M. . T. V. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1. ABOUT COLD AND WARM MIGRATION 7
2.2. COLD MIGRATION 7
2.3. WARM MIGRATION 7
2.3.1. Additional resources 8
2.3.2. Precopy stage 8
2.3.2.1. Additional resources 8
2.3.3. Cutover stage 8
2.4. MIGRATION SPEED COMPARISON 8
2.5. CHOOSING A MIGRATION TYPE 9
.C . H. .A . P. .T .E . R. . 3. .. L. .I V. .E . .M . .I G. .R . A. .T . I.O . .N . .I N. . M. . T. .V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1. 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1. ADDITIONAL RESOURCES 12
3.2. BENEFITS OF LIVE MIGRATION 12
3.3. LIVE MIGRATION, MTV, AND OPENSHIFT VIRTUALIZATION 12
3.4. LIMITATIONS OF LIVE MIGRATION 13
3.5. LIVE MIGRATION WORKFLOW 13
.C . H. .A . P. .T .E . R. . 4. .. .S .O . .F . T. W. . A. .R . E. . R. .E .Q . .U . I.R . E. .M . .E .N . .T .S . .F . O. .R . .M . .I G. .R . A. .T . I.O . N. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1. 5. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1. ADDITIONAL RESOURCES 15
4.2. STORAGE SUPPORT AND DEFAULT MODES 15
4.3. NETWORK PREREQUISITES 16
4.4. PORTS 17
4.5. SOURCE VM PREREQUISITES 18
4.6. SOURCE VM MIGRATION CONSIDERATIONS 18
4.7. MTV ENCRYPTION SUPPORT 19
.C . H. .A . P. .T .E . R. . 5. .. P. .R . O. . V. .I D. .E . R. .- .S .P . E. .C . I.F . I.C . .R . E. .Q . U. .I R. .E . M. . E. .N . T. S. . F. .O . R. . M. . I.G . .R .A . T. .I O. . N. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2 . 0. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1. RED HAT VIRTUALIZATION PREREQUISITES 20
5.2. OPENSTACK PREREQUISITES 20
5.2.1. Using token authentication with an OpenStack source provider 21
5.2.2. Using application credential authentication with an OpenStack source provider 22
5.3. VMWARE PREREQUISITES 24
5.3.1. VMware privileges 25
5.3.1.1. Privileges required for all migrations 25
5.3.1.2. Provisioning privileges 26
5.3.1.3. Warm migration and deep inspection privileges 27
5.3.1.4. Privileges for encrypted VMs 27
5.3.2. Creating a VMware role to grant MTV privileges 28
5.3.3. Creating a VDDK image 28
5.3.4. Increasing the NFC service memory of an ESXi host 29
5.3.5. VDDK validator containers need requests and limits 30
5.4. OPEN VIRTUAL APPLIANCE (OVA) PREREQUISITES 31
5.5. MICROSOFT HYPER-V PREREQUISITES 32
5.5.1. Prerequisites 33
5.5.2. Network requirements 33
5.5.3. WinRM configuration 33
5.5.4. SMB share requirements 34
5.5.5. Credential requirements 34
1

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
5.6. OPENSHIFT VIRTUALIZATION PREREQUISITES 34
5.6.1. OpenShift Virtualization live migration prerequisites 35
5.7. AWS EC2 PREREQUISITES 35
5.8. SOFTWARE COMPATIBILITY GUIDELINES 36
5.8.1. OpenShift Operator Life Cycles 36
.C . H. .A . P. .T .E . R. . 6. .. .I N. .S . T. A. .L . L. .I N. .G . . A. .N . D. . C. .O . N. . F. I. G. .U . R. .I N. .G . . T. .H . E. .M . .T . V. . O. .P . E. .R . A. .T .O . .R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3 . 7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1. INSTALLING THE MTV OPERATOR BY USING THE RED HAT OPENSHIFT WEB CONSOLE 37
6.2. INSTALLING THE MTV OPERATOR BY USING THE COMMAND-LINE INTERFACE 37
6.3. CONFIGURING THE MTV OPERATOR 39
6.4. MTV OPERATOR PARAMETERS 39
6.5. CONFIGURING THE CONTROLLER_MAX_VM_INFLIGHT PARAMETER 42
.C . H. .A . P. .T .E . R. . 7. .. R. .E . D. . H. .A . T. . O. .P . E. .N . S. .H . I.F . T. . L. I. G. .H . T. .S . P. .E .E . D. . I.N . .T .E . G. .R . A. .T . I.O . .N . .W . .I T. .H . .M . .T .V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4 .3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1. PREREQUISITES 43
7.2. ABOUT LIGHTSPEED AND MTV 43
7.2.1. Lightspeed use cases 43
7.2.2. Data access and analysis 44
7.2.3. Privacy and data handling 44
7.2.4. How the integration works 44
7.3. ENABLING THE RED HAT OPENSHIFT LIGHTSPEED INTEGRATION 45
7.4. ADDITIONAL RESOURCES 46
.C . H. .A . P. .T .E . R. . 8. .. .M . I. G. .R . A. .T .I .N . G. . V. .I R. .T . U. .A . L. . M. . A. .C . H. .I N. .E . S. . B. .Y . .U . S. I.N . .G . .T . H. .E . .R . E. D. . H. . A. .T . O. . P. .E .N . .S .H . .I F. T. . W. . E. .B . .C . O. .N . .S .O . .L .E . . . . . . .4 . 7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.1. ADDITIONAL RESOURCES 47
8.2. NAVIGATING MTV PAGES 47
8.3. THE MTV USER INTERFACE 48
8.3.1. The Tips and tricks panel 48
8.4. THE MTV OVERVIEW PAGE 48
8.4.1. Overview tab 49
8.4.2. YAML tab 49
8.4.3. Health tab 50
8.4.4. History tab 50
8.4.5. Settings tab 50
8.4.6. Choosing a different controller transfer network 52
8.5. PREPARING VMS FOR MIGRATION 53
8.5.1. Renaming virtual machines 53
8.5.2. Configuring the target power state of VMs 54
.C . H. .A . P. .T .E . R. . 9. .. .M . I. G. .R . A. .T . I.N . G. . V. .I .R .T . U. .A . L. . M. . A. .C . H. .I N. .E . S. . B. .Y . .U . S. I.N . .G . .T . H. .E . .C . O. .M . .M . .A . N. .D . -. L. .I N. .E . .I N. .T . E. .R . F. A. .C . .E . . . . . . . . . . . . . . .5 . 6. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.1. ADDITIONAL RESOURCES 56
9.2. PERMISSIONS NEEDED BY NON-ADMINISTRATORS TO WORK WITH MIGRATION PLAN COMPONENTS
56
.C . H. .A . P. .T .E . R. . 1.0 . .. M. . A. .P . P. .I N. .G . . N. .E . T. W. . O. . R. .K .S . .A . N. .D . . S . T. .O . R. .A . G. . E. .I .N . .M . .I G. .R . A. .T . I.O . N. . .P .L . A. .N . S. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5 . 8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.1. ABOUT NETWORK MAPS IN MIGRATION PLANS 58
10.2. ABOUT STORAGE MAPS IN MIGRATION PLANS 58
10.3. CREATING OWNERLESS STORAGE MAPS IN THE MTV UI 59
.C . H. .A . P. .T .E . R. . 1.1 .. .P . L. A. .N . .N . I.N . G. . .A . .M . I. G. .R . A. .T .I .O . N. . O. . F. . V . I. R. .T .U . A. .L . .M . .A . C. .H . I.N . E. .S . .F .R . O. . M. . .V . M. .W . .A . R. .E . .V . S. .P .H . .E .R . E. . . . . . . . . . . . . . . . .6 .0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 60
11.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 60
11.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 62
11.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 63
11.5. MIGRATING VMWARE VIRTUAL MACHINES BY USING STORAGE COPY OFFLOAD 64
2

Table of Contents
11.5.1. How storage copy offload works 65
11.5.2. Supported storage providers 66
11.5.3. Planning and running storage copy offload migrations 66
11.5.4. Cloning methods used by storage copy offload 66
11.5.5. Advantages of the SSH cloning method 67
11.5.6. Setting up storage copy offload using the VIB 67
11.5.7. Setting up storage copy offload by using an SSH key 68
11.5.8. Security requirements and recommendations for the SSH cloning method 69
11.5.9. Setting up storage copy offload by using automatically generated SSH keys 69
11.5.10. Setting up storage copy offload by using manually generated SSH keys 71
11.5.11. Migrating VMware vSphere VMs in the UI by using storage copy offload 72
11.6. ADDING A VMWARE VSPHERE SOURCE PROVIDER 79
11.7. SELECTING A MIGRATION NETWORK FOR A VMWARE SOURCE PROVIDER 81
11.8. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 83
11.9. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 84
11.10. CREATING A VMWARE VSPHERE MIGRATION PLAN BY USING THE MTV WIZARD 85
11.11. CONFIGURING VMWARE MIGRATION PLAN SETTINGS 89
11.11.1. PVC name template variables 94
11.11.1.1. Available variables 95
11.11.1.2. Template functions 95
11.11.1.3. Examples 95
11.11.2. Network name template variables 96
11.11.2.1. Available variables 96
11.11.2.2. Examples 96
11.11.3. Volume name template variables 96
11.11.3.1. Available variables 97
11.11.3.2. Examples 97
11.12. ABOUT DEEP INSPECTION 97
11.12.1. Inspection methods 98
11.12.2. How Deep Inspection works 98
11.12.3. When to use Deep Inspection 98
11.13. UNDERSTANDING DEEP INSPECTION VALIDATION RESULTS 99
11.13.1. Validation concerns 99
11.13.2. Migration preparation considerations 99
11.14. MIGRATION OF LUKS-ENCRYPTED DISKS 99
11.15. ENABLING NETWORK-BOUND DISK ENCRYPTION WITH CLEVIS 100
11.16. ABOUT SCHEDULING IMPORTER PODS 101
.C . H. .A . P. .T .E . R. . 1.2 . .. P. .L .A . N. . N. .I N. .G . . A. . M. .I .G . R. .A . T. .I O. .N . .O . .F . V. .I .R .T . U. .A . L. . M. . A. .C . H. .I N. .E . S. . F. R. .O . .M . . R. E. .D . .H . A. .T . .V . I.R . T. .U . A. .L . I.Z .A . T. .I O. . N. . . . . . . .1 .0 . 3. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 103
12.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 103
12.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 105
12.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 105
12.5. ADDING A RED HAT VIRTUALIZATION SOURCE PROVIDER 107
12.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 108
12.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 109
12.8. CREATING A RED HAT VIRTUALIZATION MIGRATION PLAN BY USING THE MTV WIZARD 110
.C . H. .A . P. .T .E . R. . 1.3 . .. P. .L .A . N. . N. .I N. .G . . A. . M. .I .G . R. .A . T. .I O. .N . . O . .F . .V . I.R . T. U. .A . L. . M. . A. .C . H. .I N. .E . S. . F. .R .O . .M . . O. .P . E. .N . S. .T .A . C. . K. . . . . . . . . . . . . . . . . . . . . . .1 1. 6. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 116
13.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 116
13.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 118
13.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 118
3

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
13.5. ADDING AN OPENSTACK SOURCE PROVIDER 120
13.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 122
13.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 123
13.8. CREATING AN OPENSTACK MIGRATION PLAN BY USING THE MTV WIZARD 124
.C . H. .A . P. .T .E . R. . 1.4 . .. P. .L . A. .N . N. .I N. . G. . A. . M. . I.G . R. .A . T. .I O. .N . . O. .F . .V . I.R . T. .U . A. .L . M. . A. .C . H. .I N. . E. S. . F. .R . O. .M . . O. .V . A. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 . 9. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 129
14.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 129
14.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 131
14.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 131
14.5. ADDING AN OPEN VIRTUAL APPLIANCE (OVA) SOURCE PROVIDER 133
14.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 133
14.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 134
14.8. CREATING AN OPEN VIRTUALIZATION APPLIANCE (OVA) MIGRATION PLAN BY USING THE MTV
WIZARD 136
14.9. CONFIGURING OVA FILE UPLOAD BY WEB BROWSER 140
.C . H. .A . P. .T .E . R. . 1.5 . .. P. .L .A . N. . N. .I N. .G . . A. . M. .I .G . R. .A . T. .I O. .N . .O . .F . .V . I.R . T. U. .A . L. . M. . A. .C . H. .I N. .E . S. . (. V. .M . S. .) . F. .R .O . .M . . M. .I .C . R. .O . S. .O . F. .T . .H . Y. .P . E. R. .- .V . . . . .1 .4 . 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 142
15.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 143
15.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 144
15.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 145
15.5. ADDING A MICROSOFT HYPER-V SOURCE PROVIDER 146
15.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 147
15.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 148
15.8. RETRIEVING MICROSOFT HYPER-V NETWORK AND STORAGE IDENTIFIERS 149
15.9. CREATING A MICROSOFT HYPER-V MIGRATION PLAN BY USING THE MTV WIZARD 151
15.10. ADDITIONAL RESOURCES 155
.C . H. .A . P. .T .E . R. . 1.6 . .. P. .L . A. .N . N. .I N. .G . . A. . M. . I.G . R. .A . T. .I O. .N . . O. .F . .V . I.R . T. U. . A. .L . M. . A. .C . H. .I N. . E. S. . F. .R . O. .M . . A. .W . .S . E. .C . 2. . . . . . . . . . . . . . . . . . . . . . . . . .1 .5 .6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16.1. CREATING OWNERLESS NETWORK MAPS FROM THE FORM PAGE IN THE MTV UI 156
16.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 157
16.3. CREATING OWNERLESS STORAGE MAPS FROM THE FORM PAGE IN THE MTV UI 158
16.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 159
16.5. ADDING AN AWS EC2 SOURCE PROVIDER 160
16.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 162
16.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 163
16.8. CREATING AN AWS EC2 MIGRATION PLAN BY USING THE MTV WIZARD 164
.C . H. .A . P. .T .E . R. . 1.7 . .. P. .L .A . N. . N. .I N. .G . . A. . M. .I .G . R. .A . T. .I O. .N . .O . .F . .V .I .R . T. U. .A . L. . M. . A. .C . H. .I N. .E . S. . F. .R .O . .M . . O. .P . E. .N . S. .H . I.F . T. .V . I. R. T. .U . A. .L . I.Z . A. .T .I .O . N. . . . .1 .6 . 9. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM PAGE OF THE MTV UI 169
17.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 169
17.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM PAGE OF THE MTV UI 171
17.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR JSON DEFINITIONS IN THE MTV UI 171
17.5. ADDING A RED HAT OPENSHIFT VIRTUALIZATION SOURCE PROVIDER 173
17.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION PROVIDER 174
17.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT VIRTUALIZATION PROVIDER 175
17.8. CREATING AN OPENSHIFT VIRTUALIZATION MIGRATION PLAN BY USING THE MTV WIZARD 176
17.8.1. PVC name template variables for OpenShift Virtualization-to-OpenShift Virtualization migrations 180
17.8.1.1. Available variables 181
17.8.1.2. Template functions 181
17.8.1.3. Default behavior 181
17.8.1.4. Examples 181
17.8.2. Creating a migration plan for a live migration by using the MTV wizard 182
4

Table of Contents
5

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 1. PLANNING A MIGRATION
You can use the Migration Toolkit for Virtualization (MTV) to plan your migration of virtual machines
(VMs) from specific source providers to OpenShift Virtualization destination providers.
The supported source providers are:
VMware vSphere
Red Hat Virtualization
OpenStack
Open Virtual Appliances (OVAs) that were created by VMware vSphere
Remote OpenShift Virtualization clusters
NOTE
OVA migration is validated for migrating supported guest operating systems exported
from VMware vSphere. For third-party networking or security appliances, check with the
vendor for native QCOW2 or Kernel-based Virtual Machine (KVM) images.
1.1. TYPES OF MIGRATION
MTV supports three types of migration: cold, warm, and live.
Cold migration is available for all of the preceding source providers. This type of migration
migrates VMs that are powered off and does not require shared storage.
Warm migration is available only for VMware vSphere and Red Hat Virtualization. This type of
migration migrates VMs that are powered on and requires shared storage.
Live migration is available only for migrations between OpenShift Virtualization clusters or
between namespaces on the same OpenShift Virtualization cluster. It requires MTV version 2.10
or later and OpenShift Virtualization version 4.20 or later.
Additional resources
About cold and warm migration
Live migration in MTV
6

CHAPTER 2. COLD AND WARM MIGRATION IN MTV
CHAPTER 2. COLD AND WARM MIGRATION IN MTV
MTV supports cold migration for VMs that are shut down and warm migration for running VMs with
minimal downtime.
2.1. ABOUT COLD AND WARM MIGRATION
Cold migration is for shut-down VMs and works with VMware vSphere, Red Hat Virtualization,
OpenStack, Open Virtual Appliances (OVAs), Microsoft Hyper-V, and remote OpenShift Virtualization
clusters. Warm migration is for running VMs from VMware vSphere and Red Hat Virtualization.
NOTE
OVA migration is validated for migrating supported guest operating systems exported
from VMware vSphere. For third-party networking or security appliances, check with the
vendor for native QCOW2 or Kernel-based Virtual Machine (KVM) images.
2.2. COLD MIGRATION
Cold migration is the default migration type. The source virtual machines are shut down while the data is
copied.
Cold migration converts each VM to be compatible with OpenShift before transferring it. If a VM cannot
be converted, the migration fails immediately (fail fast). All disk blocks are copied once in a sequential
process.
NOTE
VMware only: In cold migrations, in situations in which a package manager cannot be used
during the migration, MTV does not install the qemu-guest-agent daemon on the
migrated VMs. This has some impact on the functionality of the migrated VMs, but basic
VM operations remain supported.
To enable MTV to automatically install qemu-guest-agent on the migrated VMs, ensure
that your package manager can install the daemon during the first boot of the VM after
migration.
If that is not possible, use your preferred automated or manual procedure to install
qemu-guest-agent manually.
2.3. WARM MIGRATION
Warm migration copies most of the data while the source virtual machines (VMs) remain running,
minimizing downtime.
The migration process has two stages:
Precopy stage: Most data is copied while VMs continue running. VM disks are copied
incrementally using changed block tracking (CBT) snapshots. For more information about CBT
snapshots, see the "Additional resources" section.
Cutover stage: VMs are shut down and the remaining data is migrated. Data stored in RAM is
not migrated.
7

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Warm migration transfers snapshots to OpenShift first, then converts the VM during the cutover stage.
This means disk blocks may be copied multiple times if the VM has high utilization, but VMs remain
available during most of the migration process. You must enable CBT for each source VM and each VM
disk before starting a warm migration.
2.3.1. Additional resources
Changed Block Tracking (CBT) on virtual machines
2.3.2. Precopy stage
The VMs are not shut down during the precopy stage.
The VM disks are copied incrementally by using changed block tracking (CBT) snapshots. The snapshots
are created at one-hour intervals by default. You can change the snapshot interval by updating the
forklift-controller deployment. For more information about CBT snapshots, see the "Additional
resources" section.
A VM can support up to 28 CBT snapshots. If the source VM has too many CBT snapshots and the
Migration Controller service is not able to create a new snapshot, warm migration might fail. The
Migration Controller service deletes each snapshot when the snapshot is no longer required.
The precopy stage runs until the cutover stage is started manually or is scheduled to start.
2.3.2.1. Additional resources
Changed block tracking (CBT) on virtual machines
2.3.3. Cutover stage
The VMs are shut down during the cutover stage and the remaining data is migrated. Data stored in RAM
is not migrated.
You can start the cutover stage manually by using the MTV console or you can schedule a cutover time
in the Migration custom resource (CR).
The duration of the cutover stage depends on how much data has changed since the last snapshot was
created during the precopy stage.
2.4. MIGRATION SPEED COMPARISON
Compare cold and warm migration speeds to choose the best type for your workload. Both have similar
transfer speeds, but warm migration runs in background with hourly snapshots while cold migration
requires VMs to be shut down.
The observed speeds for the warm migration single disk transfer and disk conversion are
approximately the same as for cold migration.
The benefit of warm migration is that the transfer of the snapshot happens in the background
while the VM is running.
The default snapshot time is taken every 60 minutes. If VMs change substantially, more data
needs to be transferred than in cold migration when the VM is shut down.
The cutover stage, meaning the final VM shutdown and last snapshot transfer, depends on how
8

CHAPTER 2. COLD AND WARM MIGRATION IN MTV
The cutover stage, meaning the final VM shutdown and last snapshot transfer, depends on how
much the VM has changed since the last snapshot.
NOTE
Live migration reduces downtime even further than warm migration, but live migration is
available only for migration between OpenShift Virtualization clusters or between
namespaces on the same OpenShift Virtualization cluster. Therefore it is not included in
the comparison above.
2.5. CHOOSING A MIGRATION TYPE
Choose the migration type that best fits your requirements for downtime, migration speed, and source
VM compatibility.
Cold migration
A cold migration moves a shutdown VM between hosts. It is the default migration type in MTV.
Use cold migration when:
Downtime is acceptable: You can afford to shut down VMs during migration. The VM remains
shut down for the entire duration of the data transfer.
The VM is not a critical production workload: For VMs used for development, testing, or other
non-essential tasks, the downtime is unlikely to have a major business impact.
You are migrating VMs with large amounts of data on a single disk: Since the VM is offline,
there are no live changes to track, making the data copy a one-time, full-disk transfer.
You are migrating from OpenStack or OVA sources: Warm migration is not supported for
these source types.
Changed block tracking (CBT) cannot be enabled on the source VMs: Warm migration
requires CBT to track changes incrementally.
You need to ensure a clean state: Because the VM is fully shut down, there is no risk of data
changes or I/O operations during the migration.
You want the fastest migration for individual VMs with minimal complexity: Cold migration is
the simplest and most straightforward method.
Cold migration shuts down the source VMs and copies all data in a single operation. Each VM is
converted to be compatible with OpenShift before transfer, which means migrations fail immediately if
conversion is not possible (fail fast).
Warm migration
A warm migration moves an active VM between hosts with minimal downtime. This is not live migration.
IMPORTANT
9

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
IMPORTANT
You must enable changed block tracking (CBT) for each source VM and each VM disk
before starting a warm migration. CBT allows the migration to copy only the data that has
changed since the last copy, which enables incremental data transfer while the VM runs.
Warm migration is only supported when migrating from VMware vSphere or Red Hat
Virtualization.
Use warm migration when:
You must minimize downtime for a critical workload: The process is designed to reduce the
service interruption to a few minutes, or even just seconds, during the final cutover phase.
The VM is a production server or a business-critical application: For applications that need
continuous availability, warm migration is the preferred choice to ensure business continuity.
You are migrating VMs with large amounts of data spread across multiple disks: Parallel disk
transfers reduce overall migration time.
You need to stage the migration over a period of time: Warm migration copies the majority of
the VM data (the precopy stage) while the VM is still running. This allows you to perform the bulk
of the data transfer during business hours without impacting users.
You have a pre-planned maintenance window for the final cutover: Even with warm
migration, there is a brief period of downtime when the VM is shut down to perform the final
data synchronization. You can schedule this cutover for a time with the least impact.
Decision guide
Use the following guide to select the appropriate migration type:
Table 2.1. Migration type decision guide
Your priority Recommended migration type Key consideration
Minimize downtime Warm migration Requires CBT enabled on source VMs and
disks. Most data transfers while VMs run.
Fastest migration Cold migration VMs are shut down during entire
for single-disk VMs migration. Each disk block copied once.
Migrating from Cold migration Warm migration is not supported for
OpenStack or these source types.
OVA
Cannot enable Cold migration Warm migration requires CBT to track
CBT changes incrementally.
Multi-disk VMs Warm migration Parallel disk transfers reduce overall
with even data migration time despite longer total
distribution duration.
10

CHAPTER 2. COLD AND WARM MIGRATION IN MTV
| Your priority | Recommended migration type | Key consideration |
| ------------- | -------------------------- | ----------------- |
Fail-fast validation Cold migration Conversion happens first, so incompatible
VMs fail immediately without data
transfer.
Clean state Cold migration VM is fully shut down with no risk of data
| required |     | changes during migration. |
| -------- | --- | ------------------------- |
Production Warm migration Service interruption reduced to seconds
| workload requiring |     | or minutes during cutover. |
| ------------------ | --- | -------------------------- |
continuous
availability
Pre-planned Warm migration Bulk data transfer during business hours,
| maintenance |     | final cutover during maintenance window. |
| ----------- | --- | ---------------------------------------- |
window
NOTE
OpenStack and OVA sources do not support warm migration. Remote OpenShift
Virtualization clusters support only cold migration.
11

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 3. LIVE MIGRATION IN MTV
Use live migration to migrate VMs between OpenShift Virtualization clusters or namespaces on the
same OpenShift Virtualization cluster with minimal downtime. Live migration simplifies Day 2 tasks such
as maintenance and workload balancing.
Live migration is supported by Migration Toolkit for Virtualization (MTV) version 2.10.0 and later. It
requires OpenShift Virtualization 4.20 or later on both your source and target clusters.
IMPORTANT
Migration between namespaces on the same OpenShift Virtualization cluster fails
because of MAC address collisions. For more information about this known issue, see the
"Additional resources" section.
3.1. ADDITIONAL RESOURCES
(MTV-2446)
3.2. BENEFITS OF LIVE MIGRATION
Use live migration to perform Day 2 operations like maintenance and workload balancing with minimal
service disruption. You can migrate VMs between OpenShift Virtualization clusters and namespaces
while they run, avoiding the need for scheduled downtime.
Live migration has the following benefits:
Additional migration functionality: Live migration supports migrating virtual machines (VMs)
between OpenShift Virtualization clusters and between namespaces on the same OpenShift
Virtualization clusters, making Day 2 operations easier and safer to perform.
Improved service continuity: Live migration lets you quickly migrate VMs from one cluster to
another, allowing you to eliminate the need for scheduled downtime during cluster maintenance
or upgrades. This allows you to provide more consistent and reliable services.
Greater operational flexibility: Live migration allows your IT team to manage your
infrastructure dynamically without harming business operations. Your team can respond to
changing demands or perform necessary maintenance without complex, disruptive procedures.
Enhanced performance and scalability: Live migration gives you the ability to balance
workloads across clusters. This helps ensure that applications have the resources they need,
leading to better overall system performance and scalability.
3.3. LIVE MIGRATION, MTV, AND OPENSHIFT VIRTUALIZATION
Live migration is a joint operation between Migration Toolkit for Virtualization (MTV) and OpenShift
Virtualization that leverages the strengths of MTV when you migrate VMs from one OpenShift
Virtualization cluster to another.
Tasks and responsibilities are divided between MTV and OpenShift Virtualization:
MTV manages the high-level orchestration that is needed to perform a live migration of
OpenShift Virtualization Kubevirt VMs from one cluster to another.
OpenShift Virtualization is responsible for the low-level migration mechanics, such as the actual
12

CHAPTER 3. LIVE MIGRATION IN MTV
OpenShift Virtualization is responsible for the low-level migration mechanics, such as the actual
state and storage transfer between the clusters.
Orchestration is done by the ForkliftController component of MTV, rather than by OpenShift
Virtualization, because ForkliftController is already designed to manage the migration pipeline, which
includes the following responsibilities:
Build an inventory of source resources and map them to the destination cluster.
Create and run the migration plan.
Ensure that all necessary shared resources, such as instance types, SSH keys, secrets, and
config maps, are available and accessible on the destination cluster.
3.4. LIMITATIONS OF LIVE MIGRATION
You can perform live migration to migrate VMs between OpenShift Virtualization clusters or between
namespaces on the same OpenShift Virtualization cluster with minimal downtime.
Limitations
Live migration is available only for migrations between OpenShift Virtualization clusters or
between namespaces on the same OpenShift Virtualization cluster. It is not available for any
other source provider, whether the provider is supported by Migration Toolkit for
Virtualization (MTV) or not.
Live migration does not establish connectivity between OpenShift Virtualization clusters.
Establishing such connectivity is the responsibility of the cluster administrator.
Live migration does not migrate resources unrelated to VMs, such as services, routes, or
other application components, that may be necessary for application availability after a
migration.
Live migration is not supported with host OpenShift Virtualization providers that you create
in custom namespaces (providers that you configure without a URL or token). These
providers operate with restricted permissions that prevent MTV from accessing the
resources needed for live migration, such as verifying feature gates or synchronizing
certificates between namespaces. As a workaround, use the host OpenShift Virtualization
provider that is installed in the openshift-mtv namespace or create an OpenShift
Virtualization provider with a URL and service account token that has cluster-level
permissions.
3.5. LIVE MIGRATION WORKFLOW
Live migration follows a unique workflow. Understanding how Migration Toolkit for Virtualization (MTV)
orchestrates with OpenShift Virtualization helps you troubleshoot migration issues.
1. Start: When you click Start plan, MTV initiates the migration plan.
2. PreHook: If you added a pre-migration hook, MTV runs it now.
3. Create empty DataVolumes: MTV creates empty target DataVolumes in the target OpenShift
Virtualization cluster. OpenShift Virtualization uses KubeVirt to handle the actual storage
migration.
13

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
4. Ensure resources: MTV copies all secrets or config maps that are mounted by a source VM to
the target namespace.
5. Create target VMs: MTV creates target VMs in a running state and creates a
VirtualMachineInstanceMigration resource on each cluster. The VMs have a special KubeVirt
annotation indicating to start them in migration target mode.
6. Wait for state transfer: MTV waits for KubeVirt to handle the state transfer and for the
destination VMs to report as ready. KubeVirt also handles the shutdown of the source VMs
after the state transfer.
7. PostHook: If you added a post-migration hook, MTV runs it now.
8. Completed: MTV indicates that the migration is finished.
14

CHAPTER 4. SOFTWARE REQUIREMENTS FOR MIGRATION
CHAPTER 4. SOFTWARE REQUIREMENTS FOR MIGRATION
Review the following software requirements to ensure that your environment is prepared for migration.
Migration Toolkit for Virtualization (MTV) has software requirements for all providers as well as specific
software requirements per provider.
You must install compatible versions of Red Hat OpenShift and OpenShift Virtualization. For more
information about requirements, see the "Additional resources" section.
4.1. ADDITIONAL RESOURCES
Provider-specific requirements for migration
4.2. STORAGE SUPPORT AND DEFAULT MODES
Migration Toolkit for Virtualization (MTV) uses the following default volume and access modes for
supported storage.
Table 4.1. Default volume and access modes
| Provisioner              | Volume mode | Access mode   |
| ------------------------ | ----------- | ------------- |
| kubernetes.io/aws-ebs    | Block       | ReadWriteOnce |
| kubernetes.io/azure-disk | Block       | ReadWriteOnce |
| kubernetes.io/azure-file | Filesystem  | ReadWriteMany |
| kubernetes.io/cinder     | Block       | ReadWriteOnce |
| kubernetes.io/gce-pd     | Block       | ReadWriteOnce |
| kubernetes.io/hostpath-  | Filesystem  | ReadWriteOnce |
provisioner
| manila.csi.openstack.org | Filesystem | ReadWriteMany |
| ------------------------ | ---------- | ------------- |
| openshift-               | Filesystem | ReadWriteMany |
storage.cephfs.csi.ceph.com
| openshift- | Block | ReadWriteOnce |
| ---------- | ----- | ------------- |
storage.rbd.csi.ceph.com
| kubernetes.io/rbd            | Block | ReadWriteOnce |
| ---------------------------- | ----- | ------------- |
| kubernetes.io/vsphere-volume | Block | ReadWriteOnce |
NOTE
15

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
If the OpenShift Virtualization storage does not support dynamic provisioning, you must
apply the following settings:
Filesystem volume mode
Filesystem volume mode is slower than Block volume mode.
ReadWriteOnce access mode
ReadWriteOnce access mode does not support live virtual machine migration.
See Enabling a statically-provisioned storage class for details on editing the storage
profile.
NOTE
If your migration uses block storage and persistent volumes created with an EXT4 file
system, increase the file system overhead in the Containerized Data Importer (CDI) to be
more than 10%. The default overhead that is assumed by CDI does not completely
include the reserved place for the root partition. If you do not increase the file system
overhead in CDI by this amount, your migration might fail.
NOTE
When you migrate from OpenStack, or when you run a cold migration from Red Hat
Virtualization to the Red Hat OpenShift cluster that MTV is deployed on, the migration
allocates persistent volumes without CDI. In these cases, you might need to adjust the file
system overhead.
If the configured file system overhead, which has a default value of 10%, is too low, the
disk transfer will fail due to lack of space. In such a case, you would want to increase the
file system overhead.
In some cases, however, you might want to decrease the file system overhead to reduce
storage consumption.
You can change the file system overhead by changing the value of the
controller_filesystem_overhead in the spec portion of the forklift-controller CR, as
described in Configuring the MTV Operator.
4.3. NETWORK PREREQUISITES
Network prerequisites apply to all migrations from a source provider to OpenShift Virtualization.
Prerequisites
Do not change IP addresses, VLANs, and other network configuration settings during a
migration. The MAC addresses of the virtual machines (VMs) are preserved during migration.
The network connections between the source environment, the OpenShift Virtualization
cluster, and the replication repository must be reliable and uninterrupted.
If you are mapping more than one source and destination network, you must create a
NetworkAttachmentDefinition (NAD) for each additional destination network.
16

CHAPTER 4. SOFTWARE REQUIREMENTS FOR MIGRATION
4.4. PORTS
The firewalls must enable traffic over the following ports for a successful migration to OpenShift
Virtualization.
Table 4.2. Network ports required for migrating from VMware vSphere
| Port | Protocol | Source    | Destination | Purpose                   |
| ---- | -------- | --------- | ----------- | ------------------------- |
| 443  | TCP      | OpenShift | VMware      | VMware provider inventory |
|      |          | nodes     | vCenter     |                           |
Disk transfer authentication
| 443 | TCP | OpenShift | VMware ESXi | Disk transfer authentication |
| --- | --- | --------- | ----------- | ---------------------------- |
|     |     | nodes     | hosts       |                              |
| 902 | TCP | OpenShift | VMware ESXi | Disk transfer data copy      |
|     |     | nodes     | hosts       |                              |
Table 4.3. Network ports required for migrating from Red Hat Virtualization
| Port | Protocol | Source    | Destination | Purpose                |
| ---- | -------- | --------- | ----------- | ---------------------- |
| 443  | TCP      | OpenShift | RHV Engine  | RHV provider inventory |
nodes
Disk transfer authentication
| 54322 | TCP | OpenShift | RHV hosts | Disk transfer data copy |
| ----- | --- | --------- | --------- | ----------------------- |
nodes
Table 4.4. Network ports required for migrating from OpenStack
| Port | Protocol | Source    | Destination | Purpose            |
| ---- | -------- | --------- | ----------- | ------------------ |
| 8776 | Cinder   | OpenShift | OpenStack   | Block storage API  |
|      |          | nodes     | hosts       |                    |
| 8774 | Nova     | OpenShift | OpenStack   | Virtualization API |
|      |          | nodes     | hosts       |                    |
| 5000 | Keystone | OpenShift | OpenStack   | Authentication API |
|      |          | nodes     | hosts       |                    |
| 9696 | Neutron  | OpenShift | OpenStack   | Network API        |
|      |          | nodes     | hosts       |                    |
| 9292 | Glance   | OpenShift | OpenStack   | Image service API  |
|      |          | nodes     | hosts       |                    |
17

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Table 4.5. Network ports required for migrating from Open Virtual Appliance (OVA) files
| Port | Protocol | Source    | Destination    | Purpose     |
| ---- | -------- | --------- | -------------- | ----------- |
| 2049 | TCP      | OpenShift | Server         | NFS service |
|      |          | nodes     | containing the |             |
OVA files
| 111 | TCP or UDP | OpenShift | Server         | RPC Portmapper, only needed |
| --- | ---------- | --------- | -------------- | --------------------------- |
|     |            | nodes     | containing the | for NFSv4.0                 |
OVA files
Table 4.6. Network ports required for migrating from OpenShift Virtualization
| Port | Protocol | Source    | Destination    | Purpose                       |
| ---- | -------- | --------- | -------------- | ----------------------------- |
| 6443 | API      | OpenShift | OpenShift      | Access API to get information |
|      |          | nodes     | Virtualization | from a VM’s manifest          |
host
| 443 | TCP | OpenShift | OpenShift      | Download VM data using the  |
| --- | --- | --------- | -------------- | --------------------------- |
|     |     | nodes     | Virtualization | virtualMachineExport        |
|     |     |           | host           | resource                    |
4.5. SOURCE VM PREREQUISITES
Source VM prerequisites apply to all migrations from a source provider to OpenShift Virtualization.
Prerequisites
ISO images and CD-ROMs are unmounted.
Each NIC contains an IPv4 address, an IPv6 address, or both.
The OS of each VM is certified and supported as a guest OS for conversions.
NOTE
You can check that the OS is supported by referring to the table in Converting
virtual machines from other hypervisors to KVM with virt-v2v in RHEL 7, RHEL
8, RHEL 9, and RHEL 10. See the column of the table that refers to RHEL 10
hosts.
4.6. SOURCE VM MIGRATION CONSIDERATIONS
Review these considerations when planning your migration of VMs from a source provider to OpenShift
Virtualization.
VM naming
18

CHAPTER 4. SOFTWARE REQUIREMENTS FOR MIGRATION
DNS compliance in OpenShift Virtualization: VM names must be DNS-compliant and
unique in the OpenShift Virtualization environment. Migration Toolkit for Virtualization
(MTV) automatically adjusts noncompliant VM names in the target cluster. Alternatively, you
can rename target VMs in the MTV UI. For information about renaming VMs, see Renaming
virtual machines.
Windows-specific considerations
Windows services for warm migrations: For warm migrations of Microsoft Windows VMs
from VMware, the following Windows services must be enabled (set to Manual or
Automatic) on the source VM:
Volume Shadow Copy Service (VSS): Used to quiesce the file system and applications
during snapshot creation.
VMware Snapshot Provider: Integrated with VMware Tools to trigger VSS during
snapshot operations.
You do not need to manually start the VSS service before migration. When MTV initiates
a snapshot with Quiesce guest file system enabled, VMware Tools automatically
trigger VSS to start. If VSS is disabled or missing, snapshot creation fails with an error
similar to:
An error occurred while taking a snapshot: Failed to restart the virtual machine
Measured Boot limitation: Microsoft Windows VMs that use the Measured Boot feature
cannot be migrated. Measured Boot is a mechanism that prevents device changes by
checking each start-up component, from the firmware to the boot driver. For more
information, see Measured Boot in the Microsoft documentation.
The alternative to migration is to re-create the Windows VM directly on OpenShift
Virtualization.
Secure Boot limitation: VMs with Secure Boot enabled might fail to migrate automatically
because Secure Boot prevents the VMs from booting on the destination provider. Secure
Boot is a security standard developed by members of the PC industry to ensure that a device
boots using only software trusted by the Original Equipment Manufacturer (OEM).
Workaround: Disable Secure Boot on the destination. For more details, see Disabling Secure
Boot in the Microsoft documentation.
(MTV-1548)
Operating system compatibility
Limited support for dual-boot OS VMs: MTV has limited support for the migration of dual-
boot OS VMs. In the case of a dual-boot OS VM, MTV attempts to convert the first boot disk
it finds. Alternatively, you can specify the root device in the MTV UI.
4.7. MTV ENCRYPTION SUPPORT
Migrate encrypted VMs to maintain security during migration to Migration Toolkit for Virtualization
(MTV). You can migrate Linux VMs encrypted with Linux Unified Key Setup (LUKS) and Windows VMs
encrypted with BitLocker.
19

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR
MIGRATION
Review the specific software requirements per source provider.
5.1. RED HAT VIRTUALIZATION PREREQUISITES
The following prerequisites apply to Red Hat Virtualization migrations:
To create a source provider, you must have at least the UserRole and ReadOnlyAdmin roles
assigned to you. These are the minimum required permissions, however, any other administrator
or superuser permissions will also work.
IMPORTANT
You must keep the UserRole and ReadOnlyAdmin roles until the virtual machines of the
source provider have been migrated. Otherwise, the migration will fail.
To migrate virtual machines:
You must have one of the following:
RHV admin permissions. These permissions allow you to migrate any virtual machine in
the system.
DiskCreator and UserVmManager permissions on every virtual machine you want to
migrate.
You must use a compatible version of Red Hat Virtualization.
You must have the Manager CA certificate, unless it was replaced by a third-party
certificate, in which case, specify the Manager Apache CA certificate.
You can obtain the Manager CA certificate by navigating to https://<engine_host>/ovirt-
engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA in a
browser.
If you are migrating a virtual machine with a direct logical unit number (LUN) disk, ensure
that the nodes in the OpenShift Virtualization destination cluster that the VM is expected
to run on can access the backend storage.
NOTE
Unlike disk images that are copied from a source provider to a target provider,
LUNs are detached, but not removed, from virtual machines in the source
provider and then attached to the virtual machines (VMs) that are created in the
target provider.
LUNs are not removed from the source provider during the migration in case
fallback to the source provider is required. However, before re-attaching the
LUNs to VMs in the source provider, ensure that the LUNs are not used by VMs
on the target environment at the same time, which might lead to data corruption.
5.2. OPENSTACK PREREQUISITES
20

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
To migrate from OpenStack to OpenShift Virtualization, verify you have a compatible OpenStack
version and configure authentication. You can use token authentication, application credentials, or
standard username and password credentials with MTV.
You can use these methods to migrate VMs from OpenStack source providers by using the command-
line interface (CLI) the same way you migrate other VMs, except for how you prepare the Secret
manifest.
5.2.1. Using token authentication with an OpenStack source provider
You can use token authentication, instead of username and password authentication, when you create
an OpenStack source provider.
MTV supports both of the following types of token authentication:
Token with user ID
Token with user name
For each type of token authentication, you need to use data from OpenStack to create a Secret
manifest.
Prerequisites
Have an OpenStack account.
Procedure
1. In the dashboard of the OpenStack web console, click Project > API Access.
2. Expand Download OpenStack RC file and click OpenStack RC file.
The file that is downloaded, referred to here as <openstack_rc_file>, includes the following
fields used for token authentication:
OS_AUTH_URL
OS_PROJECT_ID
OS_PROJECT_NAME
OS_DOMAIN_NAME
OS_USERNAME
3. To get the data needed for token authentication, run the following command:
$ openstack token issue
The output, referred to here as <openstack_token_output>, includes the token, userID, and
projectID that you need for authentication using a token with user ID.
4. Create a Secret manifest similar to the following:
For authentication using a token with user ID:
cat << EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
21

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
name: openstack-secret-tokenid
namespace: openshift-mtv
labels:
createdForProviderType: openstack
type: Opaque
stringData:
authType: token
token: <token_from_openstack_token_output>
projectID: <projectID_from_openstack_token_output>
userID: <userID_from_openstack_token_output>
url: <OS_AUTH_URL_from_openstack_rc_file>
EOF
For authentication using a token with user name:
cat << EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
name: openstack-secret-tokenname
namespace: openshift-mtv
labels:
createdForProviderType: openstack
type: Opaque
stringData:
authType: token
token: <token_from_openstack_token_output>
domainName: <OS_DOMAIN_NAME_from_openstack_rc_file>
projectName: <OS_PROJECT_NAME_from_openstack_rc_file>
username: <OS_USERNAME_from_openstack_rc_file>
url: <OS_AUTH_URL_from_openstack_rc_file>
EOF
5.2.2. Using application credential authentication with an OpenStack source
provider
You can use application credential authentication, instead of username and password authentication,
when you create an OpenStack source provider.
MTV supports both of the following types of application credential authentication:
Application credential ID
Application credential name
For each type of application credential authentication, you need to use data from OpenStack to create a
Secret manifest.
Prerequisites
You have an OpenStack account.
Procedure
1. In the dashboard of the OpenStack web console, click Project > API Access.
22

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
2. Expand Download OpenStack RC file and click OpenStack RC file.
The file that is downloaded, referred to here as <openstack_rc_file>, includes the following
fields used for application credential authentication:
OS_AUTH_URL
OS_PROJECT_ID
OS_PROJECT_NAME
OS_DOMAIN_NAME
OS_USERNAME
3. To get the data needed for application credential authentication, run the following command:
$ openstack application credential create --role member --role reader --secret redhat forklift
The output, referred to here as <openstack_credential_output>, includes:
The id and secret that you need for authentication using an application credential ID
The name and secret that you need for authentication using an application credential name
4. Create a Secret manifest similar to the following:
For authentication using the application credential ID:
cat << EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
name: openstack-secret-appid
namespace: openshift-mtv
labels:
createdForProviderType: openstack
type: Opaque
stringData:
authType: applicationcredential
applicationCredentialID: <id_from_openstack_credential_output>
applicationCredentialSecret: <secret_from_openstack_credential_output>
url: <OS_AUTH_URL_from_openstack_rc_file>
EOF
For authentication using the application credential name:
cat << EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
name: openstack-secret-appname
namespace: openshift-mtv
labels:
createdForProviderType: openstack
type: Opaque
stringData:
authType: applicationcredential
applicationCredentialName: <name_from_openstack_credential_output>
applicationCredentialSecret: <secret_from_openstack_credential_output>
23

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
domainName: <OS_DOMAIN_NAME_from_openstack_rc_file>
username: <OS_USERNAME_from_openstack_rc_file>
url: <OS_AUTH_URL_from_openstack_rc_file>
EOF
5.3. VMWARE PREREQUISITES
Verify that your VMware vSphere environment meets the requirements for migrating virtual machines
(VMs) to OpenShift Virtualization. Understanding these prerequisites helps you prepare your source
environment and avoid migration failures.
Create a VDDK image to accelerate migrations. For more information, see Creating a VDDK image.
Limitations
Migration Toolkit for Virtualization (MTV) cannot migrate VMware vSphere 6 and VMware
vSphere 7 VMs to a FIPS-compliant OpenShift Virtualization cluster.
Migration Toolkit for Virtualization (MTV) does not support migrating hibernated VMs.
Prerequisites
You must use a compatible version of VMware vSphere. For more information, see Software
compatibility guidelines.
You must be logged in as a user with at least the minimal set of VMware privileges. For more
information, see VMware privileges.
You must use a VDDK image if the source VMs are backed by VMware vSAN.
The target namespace must have network connectivity to the VMware source environment.
NetworkPolicies that block egress connections from the target namespace cause the
migration to fail.
The VM operating system must be certified and supported for use as a guest operating
system with OpenShift Virtualization and for conversion to KVM with virt-v2v. For more
information, see Certified Guest Operating Systems in OpenShift Virtualization and
Converting virtual machines from other hypervisors to KVM with virt-v2v in RHEL 7, RHEL 8,
RHEL 9, and RHEL 10.
Disable hibernation on the source VMs. When hibernation is disabled, VM data might be lost
if there is a power outage.
VMware Tools must be installed on the source VM to run a warm migration or to access the
VM using a pre-migration hook. For more information, see VMware Tools.
If you are running a warm migration, you must enable changed block tracking (CBT) on the
VMs and on the VM disks. For more information, see Changed Block Tracking (CBT) on
virtual machines.
If you are migrating more than 10 VMs from an ESXi host in the same migration plan, you
must increase the Network File Copy (NFC) service memory of the host.
A default MigController instance must be present. This instance is required for the Storage
Migration option in the Red Hat OpenShift web console in certain OpenShift versions. For
steps to create the default MigController instance, see Storage Migration Option Missing
24

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
for Virtual Machines in OpenShift 4.20 Despite Availability in 4.18.
Considerations
Warm migrations of Microsoft Windows VMs :For warm migrations of Microsoft Windows
virtual machines from VMware, the following Windows services must be enabled (set to
Manual or Automatic) on the source VM:
Volume Shadow Copy Service (VSS): Used to quiesce the file system and applications
during snapshot creation.
VMware Snapshot Provider: Integrated with VMware Tools to trigger VSS during
snapshot operations.
You do not need to manually start the VSS service before migration. When MTV initiates
a snapshot with Quiesce guest file system enabled, VMware Tools automatically
triggers VSS to start. If VSS is disabled or missing, snapshot creation fails with an error
similar to: An error occurred while taking a snapshot: Failed to restart the virtual
machine.
5.3.1. VMware privileges
Configure VMware vSphere user permissions to allow Migration Toolkit for Virtualization (MTV) to
access and migrate VMs. Privileges vary based on migration type and VM encryption status.
The required privileges vary based on migration type (cold or warm) and VM characteristics (encrypted
or unencrypted). All migrations require datastore access and session validation. Warm migrations require
additional snapshot and guest operating system management privileges. Encrypted VMs require
cryptographic privileges.
5.3.1.1. Privileges required for all migrations
The following privileges are required for all VM migrations, regardless of migration type or VM
characteristics.
Table 5.1. Datastore privileges
Privilege Description
Datastore.Browse datastore Allows exploring the contents of a datastore.
Datastore.Low level file operations Allows performing low-level file operations - read,
write, delete, and rename - in a datastore.
Table 5.2. Sessions privileges
Privilege Description
Sessions.Validate session Allows verification of the validity of a session.
Table 5.3. Virtual machine.Interaction privileges
25

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Privilege Description
Virtual machine.Interaction.Power Off Allows powering off a powered-on virtual machine.
This operation powers down the guest operating
system.
Virtual machine.Interaction.Power On Allows powering on a powered-off virtual machine
and resuming a suspended virtual machine.
Virtual machine.Guest operating system Allows managing a virtual machine by the VMware
management by VIX API Virtual Infrastructure eXtension (VIX) API.
5.3.1.2. Provisioning privileges
The following provisioning privileges are required to access VM disks and transfer configuration files.
Table 5.4. Virtual machine.Provisioning privileges (required)
Privilege Description
Virtual machine.Provisioning.Allow disk Allows opening a disk on a virtual machine for
access random read and write access. Used mostly for
remote disk mounting.
Virtual machine.Provisioning.Allow file Allows operations on files associated with a virtual
access machine, including VMX, disks, logs, and NVRAM.
Virtual machine.Provisioning.Allow read-only Allows opening a disk on a virtual machine for
disk access random read access. Used mostly for remote disk
mounting.
Virtual machine.Provisioning.Allow virtual Allows read operations on files associated with a
machine download virtual machine, including VMX, disks, logs, and
NVRAM.
Virtual machine.Provisioning.Allow virtual Allows write operations on files associated with a
machine files upload virtual machine, including VMX, disks, logs, and
NVRAM.
The following provisioning privileges may be required depending on your environment and VM
configuration, such as when migrating templates or VMs that require customization.
Table 5.5. Virtual machine.Provisioning privileges (optional)
Privilege Description
Virtual machine.Provisioning.Clone template Allows cloning of a template.
26

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
Privilege Description
Virtual machine.Provisioning.Clone virtual Allows cloning of an existing virtual machine and
machine allocation of resources.
Virtual machine.Provisioning.Create template Allows creation of a new template from a virtual
from virtual machine machine.
Virtual machine.Provisioning.Customize Allows customization of a virtual machine’s guest
guest operating system without moving the virtual machine.
Virtual machine.Provisioning.Deploy Allows deployment of a virtual machine from a
template template.
Virtual machine.Provisioning.Mark as Allows marking an existing powered-off virtual
template machine as a template.
Virtual machine.Provisioning.Mark as virtual Allows marking an existing template as a virtual
machine machine.
Virtual machine.Provisioning.Modify Allows creation, modification, or deletion of
customization specification customization specifications.
Virtual machine.Provisioning.Promote disks Allows promote operations on a virtual machine’s
disks.
Virtual machine.Provisioning.Read Allows reading a customization specification.
customization specifications
5.3.1.3. Warm migration and deep inspection privileges
The following snapshot management privileges are required for warm migrations and deep inspection.
Table 5.6. Virtual machine.Snapshot management privileges
Privilege Description
Virtual machine.Snapshot Allows creation of a snapshot from the virtual
management.Create snapshot machine’s current state.
Virtual machine.Snapshot Allows removal of a snapshot from the snapshot
management.Remove snapshot history.
5.3.1.4. Privileges for encrypted VMs
The following privileges are required only when migrating encrypted VMs.
27

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Table 5.7. Cryptographic privileges
Privilege Description
Cryptographic.Decrypt Allows decryption of an encrypted virtual machine.
Cryptographic.Direct access Allows access to encrypted resources.
TIP
Create a role in VMware with the permissions described in the preceding tables and then apply this role
to the Inventory section. For more information, see Creating a VMware role to apply MTV permissions .
5.3.2. Creating a VMware role to grant MTV privileges
You can create a role in VMware to grant privileges for Migration Toolkit for Virtualization (MTV) and
then grant those privileges to users with that role.
The procedure that follows explains how to do this in general. For detailed instructions, see VMware
documentation.
Procedure
1. In the vCenter Server UI, create a role that includes the set of privileges described in the tables
in VMware privileges.
2. In the vSphere inventory UI, grant privileges for users with this role to the appropriate vSphere
logical objects at one of the following levels:
a. At the user or group level: Assign privileges to the appropriate logical objects in the data
center and use the Propagate to child objects option.
b. At the object level: Apply the same role individually to all the relevant vSphere logical
objects involved in the migration, for example, hosts, vSphere clusters, data centers, or
networks.
5.3.3. Creating a VDDK image
It is strongly recommended that Migration Toolkit for Virtualization (MTV) should be used with the
VMware Virtual Disk Development Kit (VDDK) SDK when transferring virtual disks from VMware
vSphere.
NOTE
Creating a VDDK image, although optional, is highly recommended. Using MTV without
VDDK is not recommended and could result in significantly lower migration speeds.
To make use of this feature, build a VDDK image and push the VDDK image to your image registry.
The VDDK package contains symbolic links, therefore, the procedure of creating a VDDK image must be
performed on a file system that preserves symbolic links (symlinks).
NOTE
28

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
NOTE
Storing the VDDK image in a public registry might violate the VMware license terms.
Prerequisites
Red Hat OpenShift image registry.
You have podman installed.
You are working on a file system that preserves symbolic links (symlinks).
If you are using an external registry, OpenShift Virtualization must be able to access it.
Procedure
1. Extract the VDDK archive:
$ tar -xzf VMware-vix-disklib-<version>.x86_64.tar.gz
2. Create a Dockerfile:
$ cat > Dockerfile <<EOF
FROM registry.access.redhat.com/ubi8/ubi-minimal
USER 1001
COPY vmware-vix-disklib-distrib /vmware-vix-disklib-distrib
RUN mkdir -p /opt
ENTRYPOINT ["cp", "-r", "/vmware-vix-disklib-distrib", "/opt"]
EOF
3. Build the VDDK image:
$ podman build . -t <registry_route_or_server_path>/vddk:<tag>
4. Push the VDDK image to the registry:
$ podman push <registry_route_or_server_path>/vddk:<tag>
5. Ensure that the image is accessible to your OpenShift Virtualization environment.
5.3.4. Increasing the NFC service memory of an ESXi host
If you are migrating more than 10 VMs from an ESXi host in the same migration plan, you must increase
the Network File copy (NFC) service memory of the host. Otherwise, the migration fails because the
NFC service memory is limited to 10 parallel connections.
Procedure
1. Log in to the ESXi host as root.
2. Change the value of maxMemory to 1000000000 in /etc/vmware/hostd/config.xml:
...
<nfcsvc>
29

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
<path>libnfcsvc.so</path>
<enabled>true</enabled>
<maxMemory>1000000000</maxMemory>
<maxStreamMemory>10485760</maxStreamMemory>
</nfcsvc>
...
3. Restart hostd:
# /etc/init.d/hostd restart
You do not need to reboot the host.
5.3.5. VDDK validator containers need requests and limits
If you have the cluster or project resource quotas set, you must ensure that you have a sufficient quota
for the MTV pods to perform the migration.
You can see the defaults, which you can override in the ForkliftController custom resource (CR), listed
as follows. If necessary, you can adjust these defaults.
These settings are highly dependent on your environment. If there are many migrations happening at
once and the quotas are not set enough for the migrations, then the migrations can fail. This can also be
correlated to the MAX_VM_INFLIGHT setting that determines how many VMs/disks are migrated at
once.
The following defaults can be overridden in the ForkliftController CR:
Defaults that affect both cold and warm migrations:
For cold migration, it is likely to be more resource intensive as it performs the disk copy. For
warm migration, you could potentially reduce the requests.
virt_v2v_container_limits_cpu: 4000m
virt_v2v_container_limits_memory: 8Gi
virt_v2v_container_requests_cpu: 1000m
virt_v2v_container_requests_memory: 1Gi
NOTE
Cold and warm migration using virt-v2v can be resource-intensive. For more
details, see Compute power and RAM.
Defaults that affect any migrations with hooks:
hooks_container_limits_cpu: 1000m
hooks_container_limits_memory: 1Gi
hooks_container_requests_cpu: 100m
hooks_container_requests_memory: 150Mi
30

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
Defaults that affect any OVA migrations:
ova_container_limits_cpu: 1000m
ova_container_limits_memory: 1Gi
ova_container_requests_cpu: 100m
ova_container_requests_memory: 150Mi
5.4. OPEN VIRTUAL APPLIANCE (OVA) PREREQUISITES
OVA migrations to OpenShift Virtualization require VMware vSphere files in NFS-shared directories.
MTV supports both compressed .ova packages and extracted packages.
NOTE
Migration of OVA files that were not created by VMware vSphere but are compatible with
vSphere might succeed. However, migration of such files is not supported by MTV. MTV
supports only OVA files created by VMware vSphere. Moreover, converting a vendor
OVA may invalidate vendor support agreements.
To ensure stability and vendor support, always prioritize importing the vendor’s native
QCOW2 image by using either the OpenShift Virtualization "Upload Image" or the
OpenShift Virtualization "Import from URL" workflow rather than using the Migration
Toolkit for Virtualization (MTV) OVA path.
Prerequisites
The NFS share is writable by the QEMU group (GID 107) if you plan to use the web upload
feature for OVA files.
The OVA files are in one or more folders under an NFS shared directory in one of the
following structures:
In one or more compressed OVF packages that hold all the VM information.
The filename of each compressed package must have the .ova extension. Several
compressed packages can be stored in the same folder.
When this structure is used, MTV scans the root folder and the first-level subfolders for
compressed packages.
For example, if the NFS share is /nfs, then:
The folder /nfs is scanned.
The folder /nfs/subfolder1 is scanned.
However, /nfs/subfolder1/subfolder2 is not scanned.
In extracted OVF packages.
When this structure is used, MTV scans the root folder, first-level subfolders, and
second-level subfolders for extracted OVF packages.
However, there can be only one .ovf file in a folder. Otherwise, the migration will fail.
31

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For example, if the NFS share is /nfs, then:
The OVF file /nfs/vm.ovf is scanned.
The OVF file /nfs/subfolder1/vm.ovf is scanned.
The OVF file /nfs/subfolder1/subfolder2/vm.ovf is scanned.
However, the OVF file /nfs/subfolder1/subfolder2/subfolder3/vm.ovf is not
scanned.
If you plan to upload OVA files using the web browser, ensure that each .ova file has a unique
filename.
NOTE
You can optionally configure OVA file upload by web browser to upload OVA files directly
to the NFS share. For more information, see Configuring OVA file upload by web
browser.
5.5. MICROSOFT HYPER-V PREREQUISITES
To migrate from Microsoft Hyper-V to OpenShift Virtualization, verify that your environment meets the
requirements and configure host connectivity and storage access. For general software requirements,
see Software requirements for migration.
IMPORTANT
Importing VMs from Microsoft Hyper-V is a Technology Preview feature only. Technology
Preview features are not supported with Red Hat production service level agreements
(SLAs) and might not be functionally complete. Red Hat does not recommend using
them in production. These features provide early access to upcoming product features,
enabling customers to test functionality and provide feedback during the development
process.
For more information about the support scope of Red Hat Technology Preview features,
see Technology Preview Features Support Scope.
MTV supports Generation 1 and Generation 2 VMs and automatically detects VHD and VHDX disk
formats by file extension.
Limitations
MTV supports only cold migration from Microsoft Hyper-V. Warm migration is not available.
VMs with checkpoints (snapshots) are flagged and may not migrate successfully.
System Center Virtual Machine Manager (SCVMM) integration is not supported.
Clustered Hyper-V environments are not supported.
Cluster Shared Volumes (CSV) are not explicitly handled. Only disks located on the SMB
share are usable.
32

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
5.5.1. Prerequisites
You must use a compatible version of Windows Server with Hyper-V. For more information, see
Software compatibility guidelines.
You must configure Windows Remote Management (WinRM) on the Hyper-V host for HTTPS
communication.
A Server Message Block (SMB) share must be available and accessible from both the Hyper-V
host and the OpenShift cluster.
VM disk files (VHD or VHDX) must be exposed on the SMB share before migration. MTV does
not export VMs automatically.
The service account must be a member of the Hyper-V Administrators group and have read
access to the SMB share, for example, Local Administrator.
The target namespace must have network connectivity to both the SMB share and the Hyper-V
WinRM endpoint. NetworkPolicies that block egress connections from the target namespace
prevent migration from succeeding.
The VM operating system must be certified and supported for use as a guest operating system
with OpenShift Virtualization and for conversion to KVM with virt-v2v.
A default MigController instance must be present. This instance is required for the Storage
Migration option in the Red Hat OpenShift web console in certain OpenShift versions. For steps
to create the default MigController instance, see Storage Migration Option Missing for Virtual
Machines in OpenShift 4.20 Despite Availability in 4.18.
5.5.2. Network requirements
The following network ports must be accessible for Microsoft Hyper-V migrations:
Table 5.8. Network ports
Port Protocol Description
5986 TCP WinRM HTTPS
445 TCP SMB file sharing
5.5.3. WinRM configuration
MTV connects to the Hyper-V host by using WinRM to discover VM metadata (disks, NICs, and other
properties). You must configure WinRM for HTTPS communication on the Hyper-V host before creating
the provider.
Quick configuration
Run the following command on the Windows host to configure WinRM with HTTPS:
$ winrm quickconfig -transport:https
Manual configuration
33

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Alternatively, configure WinRM manually by running the following PowerShell commands on the
Windows host:
$ Enable-PSRemoting -Force
$ New-SelfSignedCertificate -DnsName "<hostname>" -CertStoreLocation Cert:\LocalMachine\My
$ winrm create winrm/config/Listener?Address=*+Transport=HTTPS '@{Hostname="
<hostname>";CertificateThumbprint="<thumbprint>"}'
$ Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
$ New-NetFirewallRule -Name "WinRM-HTTPS" -DisplayName "WinRM HTTPS" -Protocol TCP -
LocalPort 5986 -Action Allow
Replace <hostname> with your Hyper-V host FQDN and <thumbprint> with the certificate
thumbprint from the New-SelfSignedCertificate command output.
5.5.4. SMB share requirements
The SMB share provides access to VM disk files during migration. MTV reads VM disk files from the SMB
share by using the SMB CSI driver.
The share must be accessible by using the Linux SMB path format (//server/share).
The service account credentials must have read access to the SMB share. Write access is not
required.
VM disk files (VHD or VHDX) must be accessible at the share path before migration begins.
The share must have sufficient storage space to hold the VM disk files.
5.5.5. Credential requirements
The provider credentials are used for both WinRM connectivity and SMB share access by default.
Dedicated SMB credentials can be specified in the CLI if the SMB share uses different authentication.
The service account must be a member of the Hyper-V Administrators group at minimum.
The service account must have read access to the SMB share.
Local Administrator is the simplest option as it provides all necessary permissions.
5.6. OPENSHIFT VIRTUALIZATION PREREQUISITES
To migrate between OpenShift Virtualization clusters, verify both clusters have matching MTV versions
and the source uses OpenShift Virtualization 4.16 or later.
IMPORTANT
It is strongly recommended to migrate only between clusters with the same version of
OpenShift Virtualization, although migration from an earlier version of OpenShift
Virtualization to a later one is supported.
34

CHAPTER 5. PROVIDER-SPECIFIC REQUIREMENTS FOR MIGRATION
5.6.1. OpenShift Virtualization live migration prerequisites
In addition to the regular OpenShift Virtualization prerequisites, live migration has the following
additional prerequisites:
Migration Toolkit for Virtualization (MTV) 2.10.0 or later installed. MTV treats all OpenShift
Virtualization migrations run on MTV 2.9 or earlier as cold migrations, even if they are configured
as live migrations.
OpenShift Virtualization 4.20.0 or later installed on both source and target clusters.
In the KubeVirt resource of both clusters in the featureGates of the
YAML,DecentralizedLiveMigration is listed. You must have cluster-admin privileges to set this
field.
Connectivity between the clusters must be established, including connectivity for state transfer.
Technologies such as Submariner can be used for this purpose.
The target cluster has VirtualMachineInstanceTypes and VirtualMachinePreferences that
match those used by the VMs on the source cluster.
5.7. AWS EC2 PREREQUISITES
Before migrating EC2 instances to OpenShift Virtualization, verify your environment meets the cluster,
region, availability zone, and credential requirements. Cold migration uses AWS Elastic Block Store
(EBS) snapshots and the EBS Container Storage Interface (CSI) driver.
The following prerequisites apply to AWS EC2 migrations:
Red Hat OpenShift Service on AWS (ROSA) or OpenShift Dedicated (OSD) on AWS cluster
EBS CSI driver must be installed and configured on the target cluster with storage classes
available for mapping
MTV Operator must be installed
EC2 instances must be in the same AWS region as the ROSA or OSD cluster. MTV does not
support cross-region migration.
EC2 instances must be stopped before migration. MTV supports cold migration only.
EC2 instances must use EBS volumes only. MTV does not support instances with instance store
volumes.
AWS IAM credentials with the following permissions for same-account migrations:
ec2:Describe* (includes DescribeInstances, DescribeSnapshots, DescribeVolumes)
ec2:CreateSnapshot
ec2:DeleteSnapshot
ec2:StopInstances
ec2:CreateVolume
ec2:DeleteVolume
35

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For cross-account migrations, you must also include the following permission:
ec2:ModifySnapshotAttribute
5.8. SOFTWARE COMPATIBILITY GUIDELINES
You must install compatible software versions. The table that follows lists the relevant software versions
for this version of Migration Toolkit for Virtualization (MTV).
Table 5.9. Compatible software versions
Migration Red Hat OpenShift VMware Red Hat OpenStack Microsoft
Toolkit for OpenShift Virtualizatio vSphere Virtualizati Hyper-V
Virtualizati n on
on
2.12 4.22, 4.21, 4.22, 4.21, 6.5 or later 4.4 SP1 or 16.1 or later Windows
4.20 4.20 later Server 2019
or later
NOTE
Migration from Red Hat Virtualization 4.3
MTV was tested only with Red Hat Virtualization 4.4 SP1. Migration from Red Hat
Virtualization (RHV) 4.3 has not been tested with MTV 2.12. While not supported, basic
migrations from RHV 4.3 are expected to work.
Generally it is advised to upgrade Red Hat Virtualization Manager to the previously
mentioned supported version before the migration to OpenShift Virtualization.
Therefore, it is recommended to upgrade RHV to the supported version above before
the migration to OpenShift Virtualization.
However, migrations from RHV 4.3.11 were tested with MTV 2.3, and might work in
practice in many environments by using MTV 2.12. In this case, it is recommended to
upgrade Red Hat Virtualization Manager to the previously mentioned supported version
before the migration to OpenShift Virtualization.
5.8.1. OpenShift Operator Life Cycles
Red Hat Operators have specific software maintenance life cycles. You can read about the life cycle of
the MTV Operator in the "Platform Agnostic Operators" section of OpenShift Operator Life Cycles.
36

CHAPTER 6. INSTALLING AND CONFIGURING THE MTV OPERATOR
CHAPTER 6. INSTALLING AND CONFIGURING THE MTV
OPERATOR
You can install the MTV Operator by using the Red Hat OpenShift web console or CLI. Migration Toolkit
for Virtualization (MTV) version 2.4 and later includes the MTV plugin for the web console.
6.1. INSTALLING THE MTV OPERATOR BY USING THE RED HAT
OPENSHIFT WEB CONSOLE
You can install the MTV Operator by using the Red Hat OpenShift web console.
Prerequisites
Red Hat OpenShift 4.22, 4.21, 4.20 installed.
OpenShift Virtualization Operator installed on an OpenShift migration target cluster.
You must be logged in as a user with cluster-admin permissions.
Procedure
1. In the Red Hat OpenShift web console, click Operators → OperatorHub.
2. Use the Filter by keyword field to search for mtv-operator.
3. Click Migration Toolkit for Virtualization Operator and then click Install.
4. Click Create ForkliftController when the button becomes active.
5. Click Create.
Your ForkliftController appears in the list that is displayed.
6. Click Workloads → Pods to verify that the MTV pods are running.
7. Click Operators → Installed Operators to verify that Migration Toolkit for Virtualization
Operator appears in the openshift-mtv project with the status Succeeded.
When the plugin is ready you will be prompted to reload the page. The Migration menu item is
automatically added to the navigation bar, displayed on the left of the Red Hat OpenShift web
console.
6.2. INSTALLING THE MTV OPERATOR BY USING THE COMMAND-
LINE INTERFACE
You can install the MTV Operator by using the command-line interface (CLI).
Prerequisites
Red Hat OpenShift 4.22, 4.21, 4.20 installed.
OpenShift Virtualization Operator installed on an OpenShift migration target cluster.
You must be logged in as a user with cluster-admin permissions.
Procedure
37

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Procedure
1. Create the openshift-mtv project:
$ cat << EOF | oc apply -f -
apiVersion: project.openshift.io/v1
kind: Project
metadata:
name: openshift-mtv
EOF
2. Create an OperatorGroup CR called migration:
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
name: migration
namespace: openshift-mtv
spec:
targetNamespaces:
- openshift-mtv
EOF
3. Create a Subscription CR for the Operator:
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
name: mtv-operator
namespace: openshift-mtv
spec:
channel: release-v2.12
installPlanApproval: Automatic
name: mtv-operator
source: redhat-operators
sourceNamespace: openshift-marketplace
startingCSV: "mtv-operator.v2.12.8"
EOF
4. Create a ForkliftController CR:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: ForkliftController
metadata:
name: forklift-controller
namespace: openshift-mtv
spec:
olm_managed: true
EOF
5. Verify that the MTV pods are running:
38

CHAPTER 6. INSTALLING AND CONFIGURING THE MTV OPERATOR
$ oc get pods -n openshift-mtv
The following is example output:
Example:
NAME READY STATUS RESTARTS AGE
forklift-api-bb45b8db4-cpzlg 1/1 Running 0 6m34s
forklift-controller-7649db6845-zd25p 2/2 Running 0 6m38s
forklift-must-gather-api-78fb4bcdf6-h2r4m 1/1 Running 0 6m28s
forklift-operator-59c87cfbdc-pmkfc 1/1 Running 0 28m
forklift-ui-plugin-5c5564f6d6-zpd85 1/1 Running 0 6m24s
forklift-validation-7d84c74c6f-fj9xg 1/1 Running 0 6m30s
forklift-volume-populator-controller-85d5cb64b6-mrlmc 1/1 Running 0 6m36s
6.3. CONFIGURING THE MTV OPERATOR
Configure the MTV Operator through the Settings section of the Overview page or by modifying the
ForkliftController custom resource (CR). Some configurations are available only in the CR.
NOTE
You can only use the string values "true" and "false" for feature gates, such as plugins and
some services, in the ForkliftController CR. The ForkliftController API does not accept
boolean values for these settings.
For information about the Settings section of the Overview page, see Settings tab.
Procedure
Change a parameter’s value in the spec section of the ForkliftController CR by adding the
parameter and value as follows:
spec:
<parameter: value>
Replace <parameter: value> with one of the parameters from the MTV Operator
parameters table. For more information, see MTV Operator parameters.
6.4. MTV OPERATOR PARAMETERS
The MTV Operator parameters table contains a description of each MTV Operator parameter and its
default value.
Table 6.1. MTV Operator parameters
Parameter Description Default value
39

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
| Parameter                  | Description                    | Default value |
| -------------------------- | ------------------------------ | ------------- |
| controller_max_vm_inflight | The maximum number of disks or | 20            |
VMs that can transfer or migrate
simultaneously. Varies with
provider. For more information,
see Configuring the
controller_max_vm_inflight
parameter.
| must_gather_api_cleanup_m |     | -1 (disabled) |
| ------------------------- | --- | ------------- |
The duration in hours for retaining
| ax_age | must gather reports before they |     |
| ------ | ------------------------------- | --- |
are automatically deleted.
| controller_container_limits_c |     | 500m |
| ----------------------------- | --- | ---- |
The CPU limit allocated to the
| pu  | main controller container. |     |
| --- | -------------------------- | --- |
controller_container_limits_ The memory limit allocated to the 800Mi
| memory | main controller container. |     |
| ------ | -------------------------- | --- |
controller_precopy_interval The interval in minutes at which a 60
new snapshot is requested before
initiating a warm migration.
| controller_snapshot_status_ | The frequency in seconds with | 10  |
| --------------------------- | ----------------------------- | --- |
| check_rate_seconds          | which the system checks the   |     |
status of snapshot creation or
removal during a warm migration.
| controller_filesystem_overhe |     | 10  |
| ---------------------------- | --- | --- |
Percentage of space in persistent
| ad  | volumes allocated as file system |     |
| --- | -------------------------------- | --- |
overhead when the
storageclass is filesystem.
ForkliftController CR only.
| controller_block_overhead | Fixed amount of additional space | 0   |
| ------------------------- | -------------------------------- | --- |
allocated in persistent block
volumes. This setting is applicable
for any storageclass that is
block-based. It can be used when
data, such as encryption headers,
is written to the persistent
volumes in addition to the content
of the virtual disk.
ForkliftController CR only.
40

CHAPTER 6. INSTALLING AND CONFIGURING THE MTV OPERATOR
Parameter Description Default value
vsphere_osmap_configmap_ Config map for vSphere source forklift-vsphere-osmap
name providers. This config map maps
the operating system of the
incoming VM to an OpenShift
Virtualization preference name.
This config map needs to be in the
namespace where the MTV
Operator is deployed.
To see the list of preferences in
your OpenShift Virtualization
environment, open the OpenShift
web console and click
Virtualization > Preferences.
Add values to the config map
when this parameter has the
default value, forklift-vsphere-
osmap. To override or delete
values, specify a config map that
is different from forklift-
vsphere-osmap.
ForkliftController CR only.
ovirt_osmap_configmap_na Config map for RHV source forklift-ovirt-osmap
me providers. This config map maps
the operating system of the
incoming VM to an OpenShift
Virtualization preference name.
This config map needs to be in the
namespace where the MTV
Operator is deployed.
To see the list of preferences in
your OpenShift Virtualization
environment, open the OpenShift
web console and click
Virtualization → Preferences.
You can add values to the config
map when this parameter has the
default value, forklift-ovirt-
osmap. To override or delete
values, specify a config map that
is different from forklift-ovirt-
osmap.
ForkliftController CR only.
41

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Parameter Description Default value
controller_retain_precopy_i Whether to retain importer pods false
mporter_pods so that the Containerized Data
Importer (CDI) does not delete
them during migration.
ForkliftController CR only.
controller_transfer_network The Default transfer network
NetworkAttachmentDefinitio
n used for data transmission.
6.5. CONFIGURING THE CONTROLLER_MAX_VM_INFLIGHT
PARAMETER
The value of controller_max_vm_inflight parameter, which is shown in the UI as Max concurrent
virtual machine migrations, varies by the source provider of the migration
For all migrations except Open Virtual Appliance (OVA) or VMware migrations, the parameter
specifies the maximum number of disks that Migration Toolkit for Virtualization (MTV) can
transfer simultaneously. In these migrations, MTV migrates the disks in parallel. This means that
if the combined number of disks that you want to migrate is greater than the value of the
setting, additional disks must wait until the queue is free, without regard for whether a VM has
finished migrating.
For example, if the value of the parameter is 15, and VM A has 5 disks, VM B has 5 disks, and VM
C has 6 disks, all the disks except for the 16th disk start migrating at the same time. Once any of
them has migrated, the 16th disk can be migrated, even though not all the disks on VM A and the
disks on VM B have finished migrating.
For OVA migrations, the parameter specifies the maximum number of VMs that MTV can
migrate simultaneously, meaning that all additional disks must wait until at least one VM has
been completely migrated.
For example, if the value of the parameter is 2, and VM A has 5 disks, VM B has 5 disks, and VM
C has 6 disks, all the disks on VM C must wait to migrate until either all the disks on VM A or on
VM B finish migrating.
For VMware migrations, the parameter has the following meanings:
Cold migration:
To local OpenShift Virtualization: VMs for each ESXi host that can migrate
simultaneously.
To remote OpenShift Virtualization: Disks for each ESXi host that can migrate
simultaneously.
Warm migration: Disks for each ESXi host that can migrate simultaneously.
42

CHAPTER 7. RED HAT OPENSHIFT LIGHTSPEED INTEGRATION WITH MTV
CHAPTER 7. RED HAT OPENSHIFT LIGHTSPEED
INTEGRATION WITH MTV
Get AI-powered troubleshooting assistance for your virtual machine migrations with Red Hat OpenShift
Lightspeed, which provides plain-language explanations of errors and recommended solutions.
7.1. PREREQUISITES
Red Hat OpenShift 4.15 or later
MTV 2.12 or later
Red Hat OpenShift Lightspeed Operator installed and configured on your cluster
7.2. ABOUT LIGHTSPEED AND MTV
Use Red Hat OpenShift Lightspeed to quickly diagnose migration issues and get step-by-step guidance
without manually parsing logs or searching documentation.
Red Hat OpenShift Lightspeed is integrated into the Red Hat OpenShift web console. It provides
intelligent assistance through a natural-language interface where you can ask questions, receive
troubleshooting guidance, and get step-by-step instructions.
NOTE
Red Hat OpenShift Lightspeed integration with MTV is available as a Technology Preview
feature. Technology Preview features are not supported with Red Hat production service
level agreements (SLAs) and might not be functionally complete. Red Hat does not
recommend using them in production. These features provide early access to upcoming
product features, enabling customers to test functionality and provide feedback during
the development process.
7.2.1. Lightspeed use cases
You can ask Lightspeed questions in natural language throughout the migration lifecycle:
Planning and assessment
Ask questions about migration prerequisites, recommended settings, best practices, and
configuration requirements for your specific environment and source platform.
For example:
"What are the prerequisites for warm migration from VMware?"
"What network requirements do I need for migrating VMs?"
"How do I check network mapping for a failed migration?"
Real-time troubleshooting
Get plain-language explanations of migration failures, error messages, and stalled migrations
without manually parsing logs.
For example:
"Why did the migration for VM ProdDB-01 fail?"
43

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
"Why is my warm migration stalled?"
"What does the error import retry limit exceeded mean?"
"How do I resolve Changed Block Tracking (CBT) snapshot issues?"
Post-migration guidance
Receive recommendations for validating migrated virtual machines, optimizing resource
configurations, and troubleshooting post-migration issues.
For example:
"Why are my VMs not working after migration?"
"How do I verify my migrated VMs are running correctly?"
"What should I check after migration is complete?"
7.2.2. Data access and analysis
When you ask Lightspeed a question about MTV, Lightspeed:
1. Accesses real-time data from your cluster, including migration plan status, custom resources,
and logs
2. Analyzes the data based on your user credentials and role-based access control (RBAC)
permissions
3. Provides a conversational response with specific, actionable information
7.2.3. Privacy and data handling
Lightspeed uses your own user credentials and can only access resources that you have permission to
view. Lightspeed accesses cluster metadata, migration resource status, and log data to provide
contextual assistance. All data access respects your existing RBAC permissions, and Lightspeed cannot
access resources beyond your authorization level.
IMPORTANT
When you use Lightspeed with an external AI service provider, cluster information, logs,
and resource details may be transmitted to that provider. Evaluate whether external AI
services align with the security and compliance requirements of your organization.
7.2.4. How the integration works
After you enable the feature_mcp_server feature flag in the ForkliftController custom resource, the
MTV Operator configures the integration with Red Hat OpenShift Lightspeed by:
Deploying the MTV MCP (Model Context Protocol) server
Registering the MCP server with Red Hat OpenShift Lightspeed
Configuring the necessary endpoints
This integration enables Lightspeed to access MTV resources and provide context-aware assistance for
44

CHAPTER 7. RED HAT OPENSHIFT LIGHTSPEED INTEGRATION WITH MTV
This integration enables Lightspeed to access MTV resources and provide context-aware assistance for
your migrations.
Additional resources
Enabling the Red Hat OpenShift Lightspeed integration
Technology Preview Features Support Scope
7.3. ENABLING THE RED HAT OPENSHIFT LIGHTSPEED INTEGRATION
Enable Red Hat OpenShift Lightspeed integration to access AI-powered migration assistance and
troubleshooting directly from the Red Hat OpenShift web console.
Prerequisites
You are logged in to the Red Hat OpenShift web console as a user with cluster administrator
privileges.
Red Hat OpenShift Lightspeed is installed and configured on the cluster.
For information about installing and configuring Red Hat OpenShift Lightspeed, see the Red
Hat OpenShift Lightspeed documentation.
The MTV Operator is installed.
Procedure
1. In the Red Hat OpenShift web console, click Operators → Installed Operators in the left
navigation menu.
2. Ensure you are in the correct project. For example, openshift-mtv.
3. Click the MTV Operator from the list of installed operators.
4. Click the ForkliftController tab.
5. Click your controller instance to view its details.
6. Click the YAML tab to edit the resource configuration.
7. In the spec: section, locate or add the feature_mcp_server parameter and set its value to
'true':
spec:
feature_mcp_server: 'true'
NOTE
To disable the feature later, you can change this value to 'false'.
8. Click Save.
The Red Hat OpenShift Lightspeed pods restart to load the new Model Context Protocol
(MCP) configuration for MTV.
45

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
9. Optional: Monitor the pod restart progress by running the following command:
$ oc get pods -n openshift-lightspeed -w
Verification
1. In the Red Hat OpenShift web console, open the Red Hat OpenShift Lightspeed chat assistant:
Click the Red Hat OpenShift Lightspeed icon in the top global header of the web console,
or
Click the floating Red Hat OpenShift Lightspeed icon at the bottom right of the screen.
2. Type a query related to your MTV environment into the chat prompt.
For example:
Can you list my MTV providers from all namespaces?
3. Press Enter or click the send icon.
Lightspeed uses its mtv_read capabilities to fetch and display your providers directly in the
chat window.
7.4. ADDITIONAL RESOURCES
Red Hat OpenShift Lightspeed documentation
46

CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE RED HAT OPENSHIFT WEB CONSOLE
CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE
RED HAT OPENSHIFT WEB CONSOLE
Use the MTV user interface to migrate virtual machines (VMs) from VMware vSphere, Red Hat
Virtualization (RHV), OpenStack, Open Virtual Appliances (OVAs) that were created by VMware
vSphere, or OpenShift Virtualization clusters.
For all migrations, you specify the source provider, the destination provider, and the migration plan. The
specific procedures vary per provider.
IMPORTANT
You must ensure that all prerequisites are met.
VMware only: You must have the minimal set of VMware privileges.
VMware only: Creating a VMware Virtual Disk Development Kit (VDDK) image will
increase migration speed.
For more information about the requirements, see the "Additional resources" section.
8.1. ADDITIONAL RESOURCES
Software requirements for migration
VMware privileges
Creating a VDDK image
8.2. NAVIGATING MTV PAGES
The Migration Toolkit for Virtualization (MTV) user interface provides several main pages to help you
manage your VM migrations.
You can access MTV in the OpenShift web console by clicking Migration for Virtualization in the left
navigation menu under the Virtualization section.
The main pages include:
Providers
View and manage your source and target virtualization providers. Add new providers, test
connections, and monitor provider health.
Migration plans
Create, view, and manage migration plans. Monitor the status of running migrations and view
migration history. Access the plan details page to configure settings, select VMs, and customize
migration parameters.
Mappings for virtualization
Create and manage network and storage mappings that define how source resources map to target
resources in the destination environment.
Overview (administrators only)
View system-wide migration statistics, health information, and configure MTV settings. This page
provides charts showing migration history, VM status, and plan status across all migrations.
47

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Each page provides filtering, sorting, and search capabilities to help you manage your resources
efficiently.
8.3. THE MTV USER INTERFACE
The Migration Toolkit for Virtualization (MTV) user interface is integrated into the OpenShift web
console.
In the left panel, you can choose a page related to a component of the migration progress, for example,
Providers. Or, if you are an administrator, you can choose Overview, which contains information about
migrations and lets you configure MTV settings.
In pages related to components, you can click on the Projects list, which is in the upper-left portion of
the page, and see which projects (namespaces) you are allowed to work with.
8.3.1. The Tips and tricks panel
The Tips and tricks panel provides contextual guidance and best practices to help you plan and execute
your migrations successfully.
You can access the panel by clicking the Tips and tricks link in the upper-right corner of all MTV pages
in the web console.
The panel includes a dropdown menu where you can select from the following topics:
Creating a provider
Migrating your virtual machines
Choosing the right migration type
Creating a network mapping
Creating a storage mapping
Optimizing migration speed
Troubleshooting
Each topic includes explanations of key terminology and considerations, with links to MTV
documentation, MTV performance recommendations, Red Hat Customer Support, and Red Hat
OpenShift Virtualization Administration training.
8.4. THE MTV OVERVIEW PAGE
The Migration Toolkit for Virtualization (MTV) Overview page displays system-wide information about
migrations and a list of Settings you can change.
If you have Administrator privileges, you can access the Overview page by clicking Migration for
Virtualization > Overview in the Red Hat OpenShift web console.
The Overview page has 3 tabs:
Overview
YAML
48

CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE RED HAT OPENSHIFT WEB CONSOLE
Health
History
Settings
8.4.1. Overview tab
The Overview tab is to help you quickly create providers and find information about the whole system:
In the upper pane, is the Welcome section, which includes buttons that let you open the Create
provider UI for each vendor (VMware, Open Virtual Appliance, OpenStack, Red Hat
Virtualization, and OpenShift Virtualization). You can close this section by clicking the Options
menu in the upper-right corner and selecting Hide from view. You can reopen it by clicking
Show the welcome card in the upper-right corner.
In the center-left pane is a "donut" chart named Virtual machines. This chart shows the number
of running, failed, and successful virtual machine migrations that MTV ran for the time interval
that you select. You can choose a different interval by clicking the list in the upper-right corner
of the pane. You can select a different interval by clicking the list. The options are: Last 24 hours,
Last 10 days, Last 31 days, and All. By clicking on each division of the chart, you can navigate to
the History tab for information about the migrations.
NOTE
Data for this chart includes only the most recent run of a migration plan that was
modified due to a failure. For example, if a plan with 3 VMs fails 4 times, then this
chart shows that 3 VMs failed, not 12.
In the center-right pane is an area chart named Migration history. This chart shows the number
of migrations that succeeded, failed, or were running during the interval shown in the title of the
chart. You can choose a different interval by clicking the Options menu in the upper-right
corner of the pane. The options are: Last 24 hours, Last 10 days, and Last 31 days. By clicking on
each division of the chart, you can navigate to the History tab for information about the
migrations.
In the lower-left pane is a "donut" chart named Migration plans. This chart shows the current
number of migration plans grouped by their status. This includes plans that were not started,
cannot be started, are incomplete, archived, paused, or have an unknown status. By clicking the
Show all plans link, you can quickly navigate to the Migration plans page.
NOTE
Since a single migration might involve many virtual machines, the number of
migrations performed using MTV might vary significantly from the number of
migrated virtual machines.
In the lower-right pane is a table named MTV health. This table lists all of the MTV pods. The
most important one, forklift-controller, is first. The remaining pods are listed in alphabetical
order. The View all link opens the Health tab. The status and creation time of each pod are
listed. You can also see a link to the logs of each pod.
8.4.2. YAML tab
49

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
The YAML tab displays the ForkliftController custom resource (CR) that defines the operation of the
MTV Operator. You can modify the CR in this tab.
8.4.3. Health tab
The Health tab has two panes:
In the upper pane, there is a table named Health. It lists all the MTV pods. The most important
one, forklift-controller, is first. The remaining pods are listed in alphabetical order. For each
pod, the status, and creation time of the pod are listed, and there is a link to the logs of the pod.
In the lower pane, there is a table named Conditions. It lists the following possible types (states)
of the MTV Operator, the status of the type, the last time the condition was updated, the reason
for the update, and a message about the condition.
8.4.4. History tab
The History tab displays information about migrations.
In the upper-left of the page, there is a filter that you can use to display only migrations of a
certain status, for example, Succeeded.
To the right of the filter is the Group by plan toggle switch, which lets you display either all
migrations or view only the most recent migration run per plan within the specified time range.
8.4.5. Settings tab
The table that follows describes the settings that are visible in the Settings tab, their default values, and
other possible values that can be set or chosen, if needed.
Table 8.1. MTV settings
Setting Description Default value Additional values
Maximum concurrent Varies with provider as 20. Adjustable by either
VM migrations follows: using the + and - keys to
set a different value or
For all by clicking the textbox
migrations
and entering a new
except OVA or
value.
VMware
migrations: The
maximum
number of disks
that MTV can
transfer
simultaneously.
For OVA
migrations: The
maximum
number of VMs
that MTV can
migrate
simultaneously.
For VMware
migrations, the
50

CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE RED HAT OPENSHIFT WEB CONSOLE
setting has the
Setting Descriptifoonllowing Default value Additional values
meanings:
Cold
migration:
To
local
Open
Shift
Virtual
ization
: VMs
for
each
ESXi
host
that
can
migrat
e
simult
aneou
sly.
To
remot
e
Open
Shift
Virtual
ization
: Disks
for
each
ESXi
host
that
can
migrat
e
simult
aneou
sly.
Warm
migration:
Disks for
each ESXi
host that
can
migrate
simultaneo
usly.
Controller main The CPU limit that is 500 m. Adjustable by selecting
container CPU limit allocated to the main another value from the
controller container, in list. Options: 200 m, 500
milliCPUs (m). m, 2000 m, 8000 m.
51

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
| Setting | Description | Default value | Additional values |
| ------- | ----------- | ------------- | ----------------- |
Controller main The memory limit that is 800 Mi. Adjustable by selecting
container memory limit allocated to the main another value from the
|     | controller container in |     | list. Options: 200 Mi, |
| --- | ----------------------- | --- | ---------------------- |
|     | mebibytes (Mi).         |     | 800 Mi, 2000 Mi, 8000  |
Mi.
Controller inventory The memory limit that is 1000 Mi. Adjustable by selecting
container memory limit allocated to the another value from the
|     | inventory controller   |     | list. Options: 400 Mi, |
| --- | ---------------------- | --- | ---------------------- |
|     | container in mebibytes |     | 1000 Mi, 2000 Mi, 8000 |
|     | (Mi).                  |     | Mi.                    |
Precopy internal The interval in minutes 60 minutes. Adjustable by selecting
| (minutes) | at which a new snapshot |     | another value from the    |
| --------- | ----------------------- | --- | ------------------------- |
|           | is requested before     |     | list. Options: 5 minutes, |
|           | initiating a warm       |     | 30 minutes, 60 minutes,   |
|           | migration.              |     | 120 minutes.              |
Snapshot polling interval The interval in seconds 10 seconds. Adjustable by choosing
|     | between which the   |     | another value from the     |
| --- | ------------------- | --- | -------------------------- |
|     | system checks the   |     | list. Options: 1 second, 5 |
|     | status of snapshot  |     | seconds, 10 seconds, 60    |
|     | creation or removal |     | seconds.                   |
during a warm migration.
Controller transfer The  Default transfer network Adjustable by choosing
| network | NetworkAttachment   |     | another value from the |
| ------- | ------------------- | --- | ---------------------- |
|         | Definition used for |     | list.                  |
data transmission.
Additional resources
Configuring the controller_max_vm_inflight parameter
8.4.6. Choosing a different controller transfer network
Some enterprise environments isolate provider APIs, such as the vSphere API or the OpenStack API, on
a dedicated transfer network segment. Choosing a different controller transfer network in these
environments gives you reliable connectivity and migration capability for MTV.
Prerequisites
You have MTV Administrator privileges.
Procedure
1.  In the Red Hat OpenShift web console, click Migration for Virtualization → Overview.
2.  Click Settings and scroll down to  Controller transfer network.
52

CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE RED HAT OPENSHIFT WEB CONSOLE
3. Choose a different controller transfer network from the list and click Save.
4. To verify that your choice was recorded, perform the following actions:
a. Click the YAML tab of the Overview page.
The Forklift Controller YAML opens.
b. Verify that the value of the spec:controller_transfer_network section is correct.
NOTE
The spec:controller_transfer_network section of the YAML does not
appear when the default transfer network is used.
8.5. PREPARING VMS FOR MIGRATION
Before running a migration plan, you can prepare your virtual machines to ensure a successful migration.
The MTV web console provides tools to help you configure VM settings in advance.
Common preparation tasks include:
Renaming VMs: Ensure VM names comply with DNS naming requirements for the target
OpenShift Virtualization environment.
Configuring power states: Set the target power state for VMs after migration to control
whether they start automatically or remain powered off.
You can perform these tasks after creating a migration plan but before running the migration. The
changes you make apply to the target VMs in the destination environment.
8.5.1. Renaming virtual machines
VM names must be DNS-compliant and unique in the OpenShift Virtualization environment. When you
migrate source VMs, Migration Toolkit for Virtualization (MTV) automatically adjusts noncompliant VM
names in the target cluster to compliant names. Alternatively, you can rename target VMs in the MTV UI.
Valid names consist only of lowercase alphanumeric characters (a-z, 0-9) and hyphens (-), with no
leading or trailing hyphens, no consecutive hyphens, and a maximum of 63 characters.
Table 8.2. Examples of VM naming conflicts
Source VM name Naming conflict Target VM name
App_VM_01 Contains uppercase letters and app-vm-01
underscores
-app-server Starts with a hyphen app-server
app--server Contains consecutive hyphens app-server
long-name-for-server- Exceeds the 63-character length limit db-server-prod-01
that-contains-more-than-
sixty-three-characters
53

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Open the Plan details page for your migration plan.
3. Click the Virtual machines tab to view a table of all VMs from the configured source provider.
4. If the Target name column does not already show in the VM table, click Manage columns to
select Target name and display the column.
5. Identify noncompliant names in the list of VMs by checking the alerts in the Concerns column.
6. To rename a VM, click the More icon at the end of the row for the VM, and click Edit target
name.
7. Enter and save a new name for the VM. Ensure that the new name consists only of lowercase
alphanumeric characters (a-z, 0-9) and hyphens (-), with no leading or trailing hyphens, no
consecutive hyphens, and a maximum of 63 characters.
8.5.2. Configuring the target power state of VMs
Configure the post-migration power state of VMs to start up automatically, remain powered off, or
preserve the source VM power state.
You can set the power state of a target VM to off, on, or auto either in the MTV UI or in the spec.vms
section of the Plan Custom Resource (CR). The auto setting preserves the power state of the source
VM.
You can apply different post-migration power states to different VMs in a single migration plan.
Procedure
1. Configure the power state for target VMs in the MTV UI.
a. In the Create migration plan wizard, navigate to Other settings under Additional setup in
the left navigation pane.
b. Scroll down to VM target power state.
c. Select Auto, Powered on, or Powered off from the dropdown menu to apply the setting to
all VMs in your migration plan. You can customize the power state for selected VMs when
your plan is created.
d. Click Next, and verify that the correct power state shows for VM target power state under
Other settings (optional).
e. When you create your migration plan, click Migration plans in the left navigation menu, and
open the Plan details page for your migration plan.
f. Verify that the correct power state shows for the VM target power state field. You can click
the Edit icon to change the power state.
g. Click the Virtual machines tab to view a table of all VMs from the configured source
provider.
h. Click Manage columns to select Target power state and display the column.
i. To change the power state for a specific VM, click the More icon at the end of the row for
54

CHAPTER 8. MIGRATING VIRTUAL MACHINES BY USING THE RED HAT OPENSHIFT WEB CONSOLE
i. To change the power state for a specific VM, click the More icon at the end of the row for
the VM, and click Edit target power state.
j. Select and save a new power state for the VM.
2. Configure the power state for target VMs in the YAML file.
a. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration
plans.
b. Open the Plan details page for your migration plan.
c. Click the YAML tab to open the Plan custom resource (CR) for your migration plan.
d. For each VM under vms in the YAML file, enter the target power state. In this example, you
set a different target power state for each VM:
Example:
vms:
- id: vm-1
targetPowerState: off
- id: vm-2
targetPowerState: on
- id: vm-3
targetPowerState: auto
55

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 9. MIGRATING VIRTUAL MACHINES BY USING THE
COMMAND-LINE INTERFACE
You migrate VMs to OpenShift Virtualization from the command-line by creating MTV custom
resources (CRs). The CRs and the migration procedure vary by source provider.
IMPORTANT
You must specify a name for cluster-scoped CRs.
You must specify both a name and a namespace for namespace-scoped CRs.
To migrate to or from an OpenShift cluster that is different from the one the migration
plan is defined on, you must have an OpenShift Virtualization service account token with
cluster-admin privileges.
IMPORTANT
You must ensure that all prerequisites are met. For more information about prerequisites,
see the "Additional resources" section.
9.1. ADDITIONAL RESOURCES
Software requirements for migration
9.2. PERMISSIONS NEEDED BY NON-ADMINISTRATORS TO WORK
WITH MIGRATION PLAN COMPONENTS
If you are an administrator, you can work with all components of migration plans (for example, providers,
network mappings, and migration plans).
By default, non-administrators have limited ability to work with migration plans and their components.
As an administrator, you can modify their roles to allow them full access to all components, or you can
give them limited permissions.
For example, administrators can assign non-administrators one or more of the following cluster roles for
migration plans:
Table 9.1. Example migration plan roles and their privileges
Role Description
plans.forklift.konveyor.io-v1beta1-view Can view migration plans but not to create, delete or
modify them
plans.forklift.konveyor.io-v1beta1-edit Can create, delete or modify (all parts of edit
permissions) individual migration plans
plans.forklift.konveyor.io-v1beta1-admin All edit privileges and the ability to delete the entire
collection of migration plans
NOTE
56

CHAPTER 9. MIGRATING VIRTUAL MACHINES BY USING THE COMMAND-LINE INTERFACE
NOTE
Predefined cluster roles include a resource (for example, plans), an API group (for
example, forklift.konveyor.io-v1beta1) and an action (for example, view, edit).
As a more comprehensive example, you can grant non-administrators the following set of permissions
per namespace:
Create and modify storage maps, network maps, and migration plans for the namespaces they
have access to
Attach providers created by administrators to storage maps, network maps, and migration plans
Not be able to create providers or to change system settings
Table 9.2. Example permissions required for non-administrators to work with migration plan
components but not create providers
Actions API group Resource
get, list, watch, create, update, forklift.konveyor.io plans
patch, delete
get, list, watch, create, update, forklift.konveyor.io migrations
patch, delete
get, list, watch, create, update, forklift.konveyor.io hooks
patch, delete
get, list, watch forklift.konveyor.io providers
get, list, watch, create, update, forklift.konveyor.io networkmaps
patch, delete
get, list, watch, create, update, forklift.konveyor.io storagemaps
patch, delete
get, list, watch forklift.konveyor.io forkliftcontrollers
create, patch, delete Empty string secrets
NOTE
Non-administrators need to have the create permissions that are part of edit roles for
network maps and for storage maps to create migration plans, even when using a
template for a network map or a storage map.
57

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 10. MAPPING NETWORKS AND STORAGE IN
MIGRATION PLANS
You can create network maps and storage maps in the Migration Toolkit for Virtualization (MTV) to map
source networks and disk storage to OpenShift Virtualization networks and storage classes.
10.1. ABOUT NETWORK MAPS IN MIGRATION PLANS
Create network maps in Migration Toolkit for Virtualization (MTV) to map source networks to OpenShift
Virtualization networks. You can create two types of network map: maps for a specific migration plan and
maps for use by any migration plan.
Plan-specific maps
Plan-specific maps are owned by that plan. You can create this kind of map in the Network maps
step of the Plan creation wizard.
Ownerless maps
Maps created for use by any migration plan are said to be ownerless. You can create this kind of map
in the Network maps page of the Migration for Virtualization section of the OpenShift
Virtualization web console.
You, or anyone working in the same project, can use ownerless maps when creating a migration plan
in the Plan creation wizard. When you choose one of these unowned maps for a migration plan, MTV
creates a copy of the map and defines your migration plan as the owner of that copy. Any changes
you make to the copy do not affect the original map, nor do they apply to any other plan that uses a
copy of the map.
Both types of network map for a project are shown in the Network maps page, but there is an important
difference in the information displayed in the Owner column of that page for each:
Maps created in the Network maps step of the Plan creation wizard are shown as being owned
by the migration plan.
Maps created in the Network maps page of the Migration for Virtualization section of the
OpenShift Virtualization web console are shown as having no owner.
10.2. ABOUT STORAGE MAPS IN MIGRATION PLANS
Create storage maps in Migration Toolkit for Virtualization (MTV) to map source disk storages to
OpenShift Virtualization storage classes. You can create two types of storage map: maps for a specific
migration plan and maps for use by any migration plan.
Plan-specific maps
Plan-specific maps are owned by that plan. You can create these kinds of maps in the Storage maps
step of the Plan creation wizard.
Ownerless maps
Maps created for use by any migration plan are said to be ownerless. You can create this kind of map
in the Storage maps page of the Migration for Virtualization section of the OpenShift
Virtualization web console.
You, or anyone working in the same project, can use ownerless maps when creating a migration plan
in the Plan creation wizard. When you choose one of these unowned maps for a migration plan, MTV
creates a copy of the map and defines your migration plan as the owner of that copy. Any changes
58

CHAPTER 10. MAPPING NETWORKS AND STORAGE IN MIGRATION PLANS
you make to the copy do not affect the original map, nor do they apply to any other plan that uses a
copy of the map.
Both types of storage map for a project are shown in the Storage maps page, but there is an important
difference in the information displayed in the Owner column of that page for each:
Maps created in the Storage maps step of the Plan creation wizard are shown as being owned
by the migration plan.
Maps created in the Storage maps page of the Migration for Virtualization section of the
OpenShift Virtualization web console are shown as having no owner.
10.3. CREATING OWNERLESS STORAGE MAPS IN THE MTV UI
You can create ownerless storage maps by using the MTV UI to map source disk storage to OpenShift
Virtualization storage classes.
You can create this type of map by using one of the following methods:
Create with form, selecting items such as a source provider from lists
Create with YAML, either by entering YAML or JSON definitions or by attaching files
containing the same
59

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM VMWARE VSPHERE
Create a VMware vSphere migration plan by setting up network maps, configuring source and
destination providers with migration networks, and defining the migration plan in the Migration Toolkit
for Virtualization (MTV) UI.
11.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless network maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a VMware source provider and an OpenShift Virtualization destination provider. For more
information, see Adding a VMware vSphere source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
11.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps by using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
60

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a VMware source provider and an OpenShift Virtualization destination provider. For more
information, see Adding a VMware vSphere source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_network_id>
name: <source_network_name>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
id: <source_network_id>
name: <source_network_name>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod, multus, and ignored. Use ignored to avoid attaching VMs to
this network for this migration.
source: You can use either the id or the name parameter to specify the source network.
For id, specify the VMware vSphere network Managed Object Reference (moRef). For
more information about retrieving the moRef, see Retrieving a VMware vSphere moRef in
61

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Migrating your virtual machines to Red Hat OpenShift Virtualization.
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network.
<network_attachment_definition_namespace>: Required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
11.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless storage maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a VMware source provider and an OpenShift Virtualization destination provider. For more
information, see Adding a VMware vSphere source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
4. Optional: If this is a storage map for a migration using storage copy offload, specify the following
offload options:
Offload plugin: Select vSphere XCOPY from the list.
Storage secret: Select from the list.
62

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Storage product: Select from the list.
NOTE
Storage copy offload is a feature that allows you to migrate VMware virtual
machines (VMs) that are in a storage array network (SAN) more efficiently.
This feature makes use of the command vmkfstools on the ESXi host, which
invokes the XCOPY command on the storage array using an Internet Small
Computer Systems Interface (iSCSI) or Fibre Channel (FC) connection.
Storage copy offload lets you copy data inside a SAN more efficiently than
copying the data over a network.
For more information about storage copy offload, see Migrating VMware
virtual machines by using storage copy offload.
5. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
6. Click Create.
Your map appears in the list of storage maps.
11.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a VMware source provider and an OpenShift Virtualization destination provider. For more
information, see Adding a VMware vSphere source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
63

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
id: <source_datastore>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
accessMode: Allowed values are ReadWriteOnce and ReadWriteMany.
id: Specify the VMware vSphere datastore moRef, for example, datastore-11. For more
information about retrieving the moRef, see Retrieving a VMware vSphere moRef in
Migrating your virtual machines to Red Hat OpenShift Virtualization.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
11.5. MIGRATING VMWARE VIRTUAL MACHINES BY USING STORAGE
COPY OFFLOAD
Migrate VMware virtual machines (VMs) that are in a storage array network (SAN) more efficiently by
using the storage copy offload feature of Migration Toolkit for Virtualization (MTV). Use this feature to
accelerate migration speed and to reduce the load on your network.
VMware’s vSphere Storage APIs-Array Integration (VAAI) includes a command named vmkfstools. This
command sends the XCOPY command, which is part of the SCSI protocol. The XCOPY command lets
you copy data inside a SAN more efficiently than copying the data over a network. The command is
executed by a populator named vsphere-xcopy-volume-populator.
Migration Toolkit for Virtualization (MTV) uses this command as the basis for storage copy offload,
which clones your VMs' data to the storage hardware instead of transmitting it between MTV and
OpenShift Virtualization.
You enable storage copy offload by configuring the storage map in your migration plan to point to your
storage array instead of the network that you usually use for migration. When you start the migration
plan, MTV migrates your VMs by copying them to the storage array that you choose. MTV then uses
XCOPY to copy them directly to OpenShift Virtualization, instead of transmitting the contents of your
VMs.
The storage copy offload feature has unique configuration prerequisites. You can review these
requirements in "Planning and running storage copy offload migrations". A link to this topic is available in
the "Additional resources" section at the end of this module. After you configure your system, you can
migrate plans by using storage copy offload from either the MTV UI or the CLI. The procedures for
migrating VMware VMs include instructions for storage copy offload.
You must ensure that your migration plans do not mix VDDK mappings with copy-offload mappings.
64

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
You must ensure that your migration plans do not mix VDDK mappings with copy-offload mappings.
Because the migration controller copies disks either through CDI volumes (VDDK) or through Volume
Populators (copy-offload), all storage pairs in the plan must either include copy-offload details (a
Secret + product) or exclude them entirely. Otherwise, the plan fails.
For storage copy offload migrations, especially performance-sensitive migrations, it is strongly
recommended to delete any preexisting snapshots before you start the migration.
IMPORTANT
Preexisting snapshots cause MTV to create snapshot delta chains. These chains prevent
the array from performing block-level hardware acceleration for the hardware clone
because the vmkfstools clone path used for offload cannot use hardware-accelerated
XCOPY.
As a result, the operation falls back to a software clone (host-based copy). Although such
a fallback migration is faster than a standard migration, it increases migration time and
ESXi workload compared to an XCOPY migration.
Snapshots created by a warm migration do not affect storage copy offload migrations.
Only preexisting snapshots cause this issue.
11.5.1. How storage copy offload works
Use storage copy offload to copy a virtual disk directly from a source to the target volume without
needing to transmit data over a network.
Without storage copy offload, MTV migrates a virtual disk as follows:
1. MTV reads the disk from the source storage.
2. MTV sends the data over a network to OpenShift Virtualization.
3. OpenShift Virtualization writes the data to its storage.
This method can be slow and consume significant network and host resources.
With storage copy offload, the process is streamlined:
1. MTV initiates a disk transfer request.
2. Instead of sending the data, MTV instructs the storage array in which the vSphere Virtual
Machine File System (VMFS) datastore holds the source VMs to perform a direct copy from the
source storage to the target volume, on the same array, in the correct storage class.
The storage array handles the cloning of the VM disk internally, often at a much higher speed
than a network-based transfer.
The Forklift project, a key component of MTV, includes a specialized volume populator named vsphere-
xcopy-volume-populator that directly interacts with VMware’s VAAI. This allows MTV to trigger the
high-speed, array-level data copy operation for supported storage systems.
IMPORTANT
65

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
IMPORTANT
The storage arrays must be supported storage providers. Otherwise, XCOPY performs a
fallback network disk copy on the ESXi. Although a fallback network disk copy on the ESXi
is usually considerably faster than a standard migration using a VDDK image over the
network, it is not as quick as a properly configured storage copy offload migration.
11.5.2. Supported storage providers
Use any of these storage providers with storage copy offload:
Hitachi Vantara
NetApp ONTAP
Pure Storage FlashArray
Dell PowerMax
Dell PowerFlex
Dell PowerStore
HPE 3PAR
HPE Primera
Infinidat InfiniBox
IBM Flashsystem
11.5.3. Planning and running storage copy offload migrations
You need to perform the following steps when you plan and run storage copy offload migrations:
Procedure
1. Before your first migration, choose and implement a cloning method. This step is discussed in
Cloning methods used by storage copy offload and in the sections that follow it.
2. For each migration, follow the procedure in either Migrating VMware vSphere VMs in the UI by
using storage copy offload or Migrating VMware vSphere VMs in the CLI by using storage copy
offload.
3. If you encounter problems that are specific to storage copy offload, consult Troubleshooting
storage copy offload.
11.5.4. Cloning methods used by storage copy offload
You can use either of the following two cloning (copying) methods to run storage copy offload
migrations: vSphere Installation on Bundle (VIB) or SSH. Both use the volume populator named
vsphere-xcopy-volume-populator to perform vmkfstools clone operations on ESXi hosts.
vSphere Installation on Bundle (VIB) is the default method. This method uses a custom VIB installed on
ESXi hosts to expose vmkfstools operations via the vSphere API.
66

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
SSH is the recommended method. This method uses SSH to directly run vmkfstools commands on
ESXi hosts. This method is useful when VIB installation is not possible and for the advantages that
follow.
11.5.5. Advantages of the SSH cloning method
The SSH cloning method offers you the following advantages:
No VIB installation: Does not require custom VIB deployment on ESXi hosts
Standard SSH: Uses the standard ESXi SSH service with no custom components
Security: Uses secure key-based authentication with command restrictions
Compatibility: Works with any ESXi version that supports SSH
Flexibility: Easier to troubleshoot and monitor SSH connections
11.5.6. Setting up storage copy offload using the VIB
You can set up storage copy offload using the vSphere Installation on Bundle (VIB). This is the default
method for running storage copy offload migrations.
IMPORTANT
If you use this method, you must install the VIB on every ESXi host that you use for copy-
offload operations.
Prerequisites
Podman or Docker installed on your local machine.
Root user SSH access to ESXi hosts.
SSH private key for ESXi authentication. This can be the same key used for the SSH clone
method, if you use both.
Optional: vSphere credentials. These allow you to auto-discovery ESXi hosts.
Procedure
1. Configure the VIB clone method in your Provider CR by setting settings:esxiCloneMethod to
"vib".
Example Provider CR
apiVersion: forklift.konveyor.io/v1beta1
kind: Provider
metadata:
name: my-vsphere-provider
namespace: openshift-mtv
spec:
type: vsphere
url: https://vcenter.example.com
secret:
67

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
name: vsphere-credentials
namespace: openshift-mtv
settings:
esxiCloneMethod: "vib"
2. Install the VIB by using the vib-installer utility included in the container image by running one of
the following methods:
a. Auto-discover ESXi hosts from vSphere and install the VIB by running the following
commands:
$ podman run -it --rm \
--entrypoint /bin/vib-installer \
-v $HOME/.ssh/id_rsa:/tmp/esxi_key:Z \
-e GOVMOMI_USERNAME=administrator@vsphere.local \
-e GOVMOMI_PASSWORD=your-password \
-e GOVMOMI_HOSTNAME=vcenter.example.com \
-e GOVMOMI_INSECURE=true \
$(oc get deployment forklift-volume-populator-controller -n openshift-mtv -o
jsonpath={.spec.template.spec.containers[0].env[?(@.name ==
"VSPHERE_XCOPY_VOLUME_POPULATOR_IMAGE")].value}) \
--ssh-key-file /tmp/esxi_key \
--datacenter MyDatacenter
b. Or specify ESXi hosts manually and install the VIB by running the following commands:
$ podman run -it --rm \
--entrypoint /bin/vib-installer \
-v $HOME/.ssh/id_rsa:/tmp/esxi_key:Z \
$(oc get deployment forklift-volume-populator-controller -n openshift-mtv -o
jsonpath={.spec.template.spec.containers[0].env[?(@.name ==
"VSPHERE_XCOPY_VOLUME_POPULATOR_IMAGE")].value}) \
--ssh-key-file /tmp/esxi_key \
--esxi-hosts esxi1.example.com,esxi2.example.com,esxi3.example.com
NOTE
Run vib-installer --help for a list of all available flags. Flags match the main
populator naming conventions and support environment variables such as
SSH_KEY_FILE, ESXI_HOSTS, and GOVMOMI_USERNAME.
NOTE
For alternative VIB installation methods using Ansible, see Esxcli plugin that
wraps vmkfstools.
11.5.7. Setting up storage copy offload by using an SSH key
You can use either an automatically generated SSH key or a manually generated SSH key for your
storage copy offload migrations.
Although SSH keys are automatically generated when you choose to use the SSH method, you have the
option to generate manual SSH keys.
68

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Procedures for both options are given in the sections that follow.
11.5.8. Security requirements and recommendations for the SSH cloning method
Follow these security requirements and recommendations when you use the SSH cloning method:
Security requirements
All public keys must include command restrictions for security.
The command path in the restrictions must match the secure script path:
/vmfs/volumes/{datastore-name}/secure-vmkfstools-wrapper.py.
You must install the SSH key in each ESXi host in your migration environment.
SSH service must be enabled on all target ESXi hosts.
To support ESXi access control, commands are restricted to vmkfstools operations.
Security recommendations
Use separate key pairs for different environments.
Rotate keys periodically.
Consider using shorter-lived keys for enhanced security.
11.5.9. Setting up storage copy offload by using automatically generated SSH keys
By default, when you use the SSH method for setting up storage copy migrations, SSH keys are
automatically generated when you create or update a relevant vSphere provider.
These keys have the following characteristics:
2048-bit RSA keys
Stored in separate Kubernetes Secrets in the provider’s namespace
Automatically injected into migration pods as needed
SSH keys are stored in secrets with predictable names based on the name of your vSphere provider:
Table 11.1. Patterns of SSH secret names
Secret type Naming pattern Contains
Private key offload-ssh-keys-{provider- private-key: RSA private key in
name}-private PEM format
Public key offload-ssh-keys-{provider- `public-key: SSH public key in
name}-public authorized_keys format
Example: For a provider with the name vcenter-example, the secrets would be offload-ssh-keys-
69

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Example: For a provider with the name vcenter-example, the secrets would be offload-ssh-keys-
vcenter-example-private and offload-ssh-keys-vcenter-example-public.
Prerequisites
Ensure that SSH traffic is permitted from the OpenShift Virtualization network to the ESXis.
Procedure
1. Configure the SSH clone method in your Provider CR by setting settings:esxiCloneMethod to
"ssh".
Example Provider CR
apiVersion: forklift.konveyor.io/v1beta1
kind: Provider
metadata:
name: my-vsphere-provider
namespace: openshift-mtv
spec:
type: vsphere
url: https://vcenter.example.com
secret:
name: vsphere-credentials
namespace: openshift-mtv
settings:
esxiCloneMethod: "ssh"
2. Find the SSH secrets for your vSphere Provider by running one of the following commands:
a. List all SSH key secrets in the provider’s namespace by running the following command:
$ oc get secrets -l app.kubernetes.io/component=ssh-keys -n openshift-mtv
b. View a specific private or public key secret by running the following command:
$ oc get secret <name_of_private_or_public_key> -o yaml -n openshift-mtv
3. Optional: If needed, you can replace an auto-generated key pair by running the following
command:
$ ssh-keygen -t rsa -b 4096 -f custom_esxi_key -N ""
This is a simpler procedure than manually generating the key pair, as described in Setting up
storage copy offload by using manually generated SSH keys.
4. Optional: If needed, you can replace either a private key secret or a public key secret by running
one of the following commands:
a. Replace a private key secret by running the following command:
$ oc create secret generic <name_of_private_key> \
--from-file=private-key=custom_esxi_key \
--dry-run=client -o yaml | oc replace -f - -n openshift-mtv
70

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
b. Replace a public key secret by running the following command:
$ oc create secret generic <name of public key> \
--from-file=public-key=custom_esxi_key.pub \
--dry-run=client -o yaml | oc replace -f - -n openshift-mtv
5. Optional: Configure the SSH timeout by adding it to your provider secret, which is the main
storage credentials secret, by running the following command:
$ oc patch secret <provider_credentials> -p {"data":{"SSH_TIMEOUT_SECONDS":"$(echo -
n "60" | base64)"}} -n <provider_namespace>
11.5.10. Setting up storage copy offload by using manually generated SSH keys
You can manually generate restricted SSH keys to use for storage copy offload migrations. After you
generate the keys, you can then add the public key to your ESXi hosts.
Prerequisites
Ensure that SSH traffic is permitted from the OpenShift Virtualization network to the ESXis.
Ensure you have network access from your local machine to the ESXi host.
Procedure
1. Configure the SSH clone method in your Provider CR by setting settings:esxiCloneMethod to
"ssh".
Example Provider CR
apiVersion: forklift.konveyor.io/v1beta1
kind: Provider
metadata:
name: my-vsphere-provider
namespace: openshift-mtv
spec:
type: vsphere
url: https://vcenter.example.com
secret:
name: vsphere-credentials
namespace: openshift-mtv
settings:
esxiCloneMethod: "ssh"
2. Get the public key from the auto-generated secret by performing the following steps:
$ oc get secrets -l app.kubernetes.io/component=ssh-keys -n <namespace_with_key>
a. Extract the public key you want by running the following command:
$ oc get secret <your_public_key> \
-o jsonpath='{.data.public-key}' -n <namespace_with_key> | base64 -d >
esxi_public_key.pub
71

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
b. View the public key by running the following command:
$ cat esxi_public_key.pub
3. Prepare the restricted key entry by performing the following steps:
a. Prefix the public key with command restrictions by running the following command:
$ echo 'command="python /vmfs/volumes/<datastore_name>/secure-vmkfstools-
wrapper.sh",no-port-forwarding,no-agent-forwarding,no-X11-forwarding '$(cat
esxi_public_key.pub) > restricted_key.pub
The command runs a script that adds the prefix.
b. View the final restricted key by running the following command:
$ cat restricted_key.pub
4. Install the restricted key on the ESXI host directly by running the following command:
$ cat restricted_key.pub | ssh root@<your_ESXi_host_IP> \
'cat >> /etc/ssh/keys-root/authorized_keys'
5. Verify the installation by performing the following steps:
a. Extract the private key from the Secret by running the following command:
$ oc get secret <your_private_key> \
-o jsonpath='{.data.private-key}' -n <namespace_with_key> | base64 -d >
esxi_private_key
b. Set the permissions of your private key by running the following command:
$ chmod 600 esxi_private_key
c. Test the connection by running the following command:
$ ssh -i esxi_private_key root@<your_ESXi_host_IP>
If the installation was successful, you are connected to the ESXi host with restricted
commands.
d. Run a test command that is restricted to the secure script to verify the connection.
6. Clean up the local key files by running the following command:
$ rm -f esxi_public_key.pub restricted_key.pub esxi_private_key
11.5.11. Migrating VMware vSphere VMs in the UI by using storage copy offload
You can use the storage copy offload feature of Migration Toolkit for Virtualization (MTV) to migrate
VMware vSphere virtual machines (VMs) faster than by other methods.
72

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Prerequisites
In addition to the regular VMware prerequisites, storage copy offload has the following additional
prerequisites:
One of the following storage systems, configured:
Hitachi Vantara
NetApp ONTAP
Pure Storage FlashArray
Dell PowerMax
Dell PowerFlex
Dell PowerStore
HPE 3PAR or HPE Primera
Infinidat InfiniBox
IBM Flashsystem
A working Container Storage Interface (CSI) driver connected to the above and to OpenShift
Virtualization
A configured VMware vSphere provider
vSphere users must have a role that includes the following privileges (suggested name:
StorageOffloader):
Global
Settings
Datastore
Browse datastore
Low level file operations
Host Configuration
Advanced settings
Query patch
Storage partition configuration
It is strongly recommended to delete any preexisting snapshots before you start a storage copy
offload migration, especially performance-sensitive migrations. Pre-existing snapshots prevent
use of XCOPY and force vmkfstools to use a slower software-based cloning method.
IMPORTANT
73

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
IMPORTANT
Snapshots created by a warm migration do not affect storage copy offload migrations.
Only preexisting snapshots cause this issue.
Procedure
1.  In the MTV Operator, set the value of feature_copy_offload to true in forklift-controller by
running the following command:
$ oc patch forkliftcontrollers.forklift.konveyor.io forklift-controller --type merge -p {"spec":
{"feature_copy_offload": "true"}} -n openshift-mtv
2.  Create a Secret in the namespace in which the migration provider is set up, usually  openshift-
mtv. Include the credentials from the appropriate vendor in your  Secret.
Table 11.2. Credentials for a Hitachi Vantara storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
| GOVMOMI_HOS | The hostname or URL of the vSphere API   | Yes |     |
| ----------- | ---------------------------------------- | --- | --- |
| TNAME       | (string)                                 |     |     |
| GOVMOMI_USE | The username of the vSphere API (string) | Yes |     |
RNAME
| GOVMOMI_PAS | The password of the vSphere API (string) | Yes |     |
| ----------- | ---------------------------------------- | --- | --- |
SWORD
STORAGE_HOS
|             | The hostname or URL of the storage vendor | Yes |     |
| ----------- | ----------------------------------------- | --- | --- |
| TNAME       | API (string)                              |     |     |
| STORAGE_USE | The username of the storage vendor API    | Yes |     |
| RNAME       | (string)                                  |     |     |
| STORAGE_PAS | The password of the storage vendor API    | Yes |     |
| SWORD       | (string)                                  |     |     |
STORAGE_POR The port of the storage vendor API (string) Yes
T
| STORAGE_ID | The storage array serial number (string) | Yes |     |
| ---------- | ---------------------------------------- | --- | --- |
HOSTGROUP_I A list of I/O ports and host group IDs, for Yes
| D_LIST | example, CL1-A,1:CL2-B,2:CL4-A,1:CL6- |     |     |
| ------ | ------------------------------------- | --- | --- |
A,1
Table 11.3. Credentials for a NetApp ONTAP storage copy offload Secret
74

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
STORAGE_HOS
|       | The IP or URL of the host (string). Either enter | Yes |     |
| ----- | ------------------------------------------------ | --- | --- |
| TNAME | the management IP for the entire cluster or      |     |     |
enter a dedicated storage virtual machine
management logical interface (SVM LIF).
| STORAGE_USE | The username (string) | Yes |     |
| ----------- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed No false
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
| ONTAP_SVM | The storage virtual machine (SVM) to be used | Yes |     |
| --------- | -------------------------------------------- | --- | --- |
in all client interactions. It can be taken from
the
trident.netapp.io/v1/TridentBackend.co
nfig.ontap_config.svm resource field.
Table 11.4. Credentials for a Pure Storage FlashArray storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
| STORAGE_HOS | The IP or URL of the host (string) | Yes |     |
| ----------- | ---------------------------------- | --- | --- |
TNAME
| STORAGE_USE | The username (string) | Yes |     |
| ----------- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed false
No
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
75

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
PURE_CLUSTE
|          | The cluster prefix is set in the        | Yes |     |
| -------- | --------------------------------------- | --- | --- |
| R_PREFIX | StorageCluster resource. Retrieve it by |     |     |
running printf "px_%.8s" $(oc get
storagecluster -A -
o=jsonpath='{.items[?
(@.spec.cloudStorage.provider=="pure
")].status.clusterUid}') in the CLI.
Table 11.5. Credentials for a Dell PowerMax storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
STORAGE_HOS
|     | The IP or URL of the host (string) | Yes |     |
| --- | ---------------------------------- | --- | --- |
TNAME
| STORAGE_USE | The username (string) | Yes |     |
| ----------- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed No false
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
POWERMAX_SY The Symmetrix ID of the storage array. It can Yes
| MMETRIX_ID | be taken from the config map under the  |     |     |
| ---------- | --------------------------------------- | --- | --- |
powermax namespace, which the CSI driver
uses.
| POWERMAX_P  | The port group to use for masking view | Yes |     |
| ----------- | -------------------------------------- | --- | --- |
| ORT_GROUP_N | creation                               |     |     |
AME
Table 11.6. Credentials for a Dell PowerFlex storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
STORAGE_HOS
|     | The IP or URL of the host (string) | Yes |     |
| --- | ---------------------------------- | --- | --- |
TNAME
76

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
STORAGE_USE
|     | The username (string) | Yes |     |
| --- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed false
No
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
POWERFLEX_S The system ID of the storage array. It can be Yes
taken from vxflexos-config from the
YSTEM_ID
vxflexos namespace or from the openshift-
operators namespace.
Table 11.7. Credentials for a Dell PowerStore storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
| STORAGE_HOS | The IP or URL of the host (string) | Yes |     |
| ----------- | ---------------------------------- | --- | --- |
TNAME
| STORAGE_USE | The username (string) | Yes |     |
| ----------- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed false
No
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
Table 11.8. Credentials for an HPE 3PAR or HPE Primera storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
77

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
STORAGE_HOS
|       | Must include the full URL with protocol. For | Yes |     |
| ----- | -------------------------------------------- | --- | --- |
| TNAME | HPE 3PAR, must also include Web Services     |     |     |
API (WSAPI) port. Use the HPE 3PAR
command cli% showwsapi to determine the
correct WSAPI port. HPE 3PAR systems
default to port 8080 for both HTTP and
HTTPS connections. HPE Primera defaults to
port 443 (SSL/HTTPS). Depending on
configured certificates, you might need to skip
SSL verification. Example:
https://192.168.1.1:8080.
STORAGE_USE
|     | The username (string) | Yes |     |
| --- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed No false
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
Table 11.9. Credentials for an Infinidat InfiBox storage copy offload Secret
| Key | Description | Mandatory | Default |
| --- | ----------- | --------- | ------- |
?
| STORAGE_HOS | The IP or URL of the host (string) | Yes |     |
| ----------- | ---------------------------------- | --- | --- |
TNAME
STORAGE_USE
|     | The username (string) | Yes |     |
| --- | --------------------- | --- | --- |
RNAME
| STORAGE_PAS | The user password (string) | Yes |     |
| ----------- | -------------------------- | --- | --- |
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed No false
| _SSL_VERIFICA | (true, false). |     |     |
| ------------- | -------------- | --- | --- |
TION
Table 11.10. Credentials for an IBM FlashSystem storage copy offload Secret
78

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Key Description Mandatory Default
?
STORAGE_HOS The IP or URL of the host (string) Yes
TNAME
STORAGE_USE The username (string) Yes
RNAME
STORAGE_PAS The user password (string) Yes
SWORD
STORAGE_SKIP If set to true, SSL verification is not performed No false
_SSL_VERIFICA (true, false).
TION
3. In the UI complete the following steps:
a. Create an ownerless storage map by using the procedure in Creating ownerless storage
maps using the form page of the MTV UI. Use the Offload plugin named vSphere XCOPY.
b. Create a migration plan by using the procedure in Creating a VMware vSphere migration
plan by using the MTV wizard.
11.6. ADDING A VMWARE VSPHERE SOURCE PROVIDER
You can migrate VMware vSphere virtual machines (VMs) from VMware vCenter or from a VMware
ESX/ESXi server without going through vCenter.
Considerations
MTV disables EMS enforcement for VMware vSphere source provider migrations, enabling
migrations from supported vSphere versions that do not comply with 2023 FIPS
requirements. Therefore, you should consider whether migrations from vSphere source
providers risk your compliance with FIPS. See Software compatibility guidelines for
supported versions of vSphere.
Remove anti-virus software from source VMs before migration to prevent migration failures.
MTV does not support migrating VMware Non-Volatile Memory Express (NVMe) disks.
If you specify a non-default maximum transmission unit (MTU) value for your migration
network, you must use the same MTU value in the OpenShift transfer network. For more
information about the OpenShift transfer network, see Creating a VMware vSphere
migration plan using the MTV wizard.
Prerequisites
Create a VMware Virtual Disk Development Kit (VDDK) image in a secure registry accessible to
all clusters. VDDK is required for warm migrations and VMs backed by VMware vSAN. For cold
migrations, VDDK is optional but accelerates the migration process. For more information, see
79

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Creating a VDDK image.
NOTE
You can configure the provider without VDDK if you are only performing cold
migrations of VMs that are not backed by vSAN, but VDDK is strongly
recommended to improve migration performance and reliability.
Procedure
1. Access the Create provider page for VMware by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click VMware.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click VMware in the Welcome pane, and
select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider.
Endpoint type: Select vCenter or ESXi.
You can migrate VMs from:
vCenter
An ESX/ESXi server not managed by vCenter
An ESX/ESXi server managed by vCenter (bypassing vCenter)
URL: URL of the SDK endpoint. Ensure that the URL includes the sdk path, usually /sdk. For
vCenter, use https://vCenter-host-example.com/sdk. For ESXi, use https://esxi-host-
example.com/sdk. If you specify a certificate for FQDN, the value of this field must match
the FQDN in the certificate.
3. Configure the VDDK init image field by doing one of the following:
Enter an existing image path: In the VDDK init image field, enter the image path in the
format <registry_route_or_server_path>/vddk:<tag>.
Upload a VDDK archive: Click Browse next to VDDK init image archive, select the archive
file, click Select, and then click Upload. The VDDK init image archive text box displays the
URL of the uploaded archive.
80

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Skip VDDK: Select Skip VMware Virtual Disk Development Kit (VDDK) SDK acceleration
(not recommended). Only skip VDDK if you are performing cold migrations of VMs that are
not backed by vSAN.
For more information about creating a VDDK image, see Creating a VDDK image.
4. Enter the provider credentials:
Username: vCenter user or ESXi user, for example, user@vsphere.local
Password: vCenter user password or ESXi user password
5. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
6. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
It might take a few minutes for the provider to move to the Ready status.
7. Optional: Add access to the UI of the provider:
a. On the Providers page, click the provider.
The Provider details page opens.
b. Click the Edit icon under External UI web link.
c. Enter the link and click Save.
NOTE
If you do not enter a link, MTV attempts to calculate the correct link.
If MTV succeeds, the hyperlink of the field points to the calculated link.
If MTV does not succeed, the field remains empty.
11.7. SELECTING A MIGRATION NETWORK FOR A VMWARE SOURCE
PROVIDER
You can select a migration network in the Red Hat OpenShift web console for a source provider to
reduce risk to the source environment and to improve performance.
81

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Using the default network for migration can result in poor performance because the network might not
have sufficient bandwidth. This situation can have a negative effect on the source platform because the
disk transfer operation might saturate the network.
You can also control the network from which disks are transferred from a host by using the Network File
Copy (NFC) service in vSphere.
NOTE
If you input any value of maximum transmission unit (MTU) besides the default value in
your migration network, you must also input the same value in the OpenShift transfer
network that you use. For more information about the OpenShift transfer network, see
Creating a migration plan.
Prerequisites
The migration network must have enough throughput, minimum speed of 10 Gbps, for disk
transfer.
The migration network must be accessible to the OpenShift Virtualization nodes through the
default gateway.
The source virtual disks are copied by a pod that is connected to the pod network of the target
namespace.
The target namespace must have network connectivity to the VMware source environment.
Migration pods run in the target namespace and require outbound access to the VMware API
and ESXi hosts. If you use NetworkPolicies to restrict egress connections from the target
namespace, you must configure policies that allow connections to VMware. This requirement
applies whether you use the pod network, user-defined networks (UDNs), or cluster user-
defined networks (CUDNs) in the target namespace.
The migration network should have jumbo frames enabled.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the host number in the Hosts column beside a provider to view a list of hosts.
3. Select one or more hosts and click Select migration network.
4. Specify the following fields:
Network: Network name
ESXi host admin username: For example, root
ESXi host admin password: Password
5. Click Save.
6. Verify that the status of each host is Ready.
If a host status is not Ready, the host might be unreachable on the migration network or the
credentials might be incorrect. You can modify the host configuration and save the changes.
11.8. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
82

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
11.8. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
83

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
11.9. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
84

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
11.10. CREATING A VMWARE VSPHERE MIGRATION PLAN BY USING
THE MTV WIZARD
You can migrate VMware vSphere virtual machines (VMs) from VMware vCenter or from a VMware ESX
or ESXi server by using the Migration Toolkit for Virtualization plan creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.
Limitations
Do not include virtual machines with guest-initiated storage connections, such as Internet
Small Computer Systems Interface (iSCSI) connections or Network File System (NFS)
mounts. These require either additional planning before migration or reconfiguration after
migration. This prevents concurrent disk access to the storage the guest points to.
A plan cannot contain more than 500 VMs or 500 disks.

WARNING
Migration Toolkit for Virtualization (MTV) cannot migrate VMware vSphere 6 and
VMware vSphere 7 VMs to a FIPS-compliant OpenShift Virtualization cluster.
Prerequisites
Have a VMware source provider and an OpenShift Virtualization destination provider. For more
information, see Adding a VMware vSphere source provider or Adding an OpenShift
Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
If you are using a user-defined network (UDN), note the name of its namespace as defined in
OpenShift Virtualization.
Procedure
1. On the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
85

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create project.
4. Click Next.
5. On the Virtual machines page, select the virtual machines you want to migrate and click Next.
6. If you are using a UDN, verify that the IP address of the provider is outside the subnet of the
UDN. If the IP address is within the subnet of the UDN, the migration fails.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
86

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Migration type page, choose one of the following:
Cold migration (default)
Warm migration
12. Click Next.
87

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
13. On the Other settings (optional) page, specify any of the following settings that are
appropriate for your plan. All are optional.
Disk decryption passphrases: For disks encrypted using Linux Unified Key Setup (LUKS).
Enter a decryption passphrase for a LUKS-encrypted device.
To add another passphrase, click Add passphrase and add a passphrase.
Repeat as needed.
You do not need to enter the passphrases in a specific order. For each LUKS-encrypted
device, MTV tries each passphrase until one unlocks the device.
Transfer Network: The network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
must also change the MTU of the VMware migration network. For more information,
see Selecting a migration network for a VMware source provider .
Preserve static IPs: By default, virtual network interface controllers (vNICs) change during
the migration process. As a result, vNICs that are configured with a static IP linked to the
interface name in the guest VM lose their IP during migration.
To preserve static IPs, select the Preserve the static IPs checkbox.
MTV then issues a warning message about any VMs whose vNIC properties are missing.
To retrieve any missing vNIC properties, run those VMs in vSphere. This causes the
vNIC properties to be reported to MTV.
Root device: Applies to multi-boot VM migrations only. By default, MTV uses the first
bootable device detected as the root device.
To specify a different root device, enter it in the text box.
MTV uses the following format for disk location: /dev/sd<disk_identifier>
<disk_partition>. For example, if the second disk is the root device and the operating
system is on the disk’s second partition, the format would be: /dev/sdb2. After you
enter the boot device, click Save.
If the conversion fails because the boot device provided is incorrect, it is possible to get
the correct information by checking the conversion pod logs.
Shared disks: Applies to cold migrations only. Shared disks are disks that are attached to
multiple VMs and that use the multi-writer option. These characteristics make shared disks
difficult to migrate. By default, MTV migrates shared disks.
NOTE
Migrating shared disks might slow down the migration process.
88

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
To migrate shared disks in the migration plan, verify that Shared disks is selected in the
checkbox.
To avoid migrating shared disks, clear the Shared disks checkbox.
14. Click Next.
15. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
16. To add a hook, select the appropriate Enable hook checkbox.
17. Enter the Hook runner image.
18. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
19. Click Next.
20. On the Review and create page, review the information displayed.
21. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
22. When you finish reviewing the details of the plan, click Create plan.
MTV validates your plan. When your plan is validated, the Plan details page for your plan opens.
If everything is OK, the Plan details page for your plan opens. This page contains important
settings that do not appear in the wizard.
Next steps
Configure plan settings on the Plan details page. For more information, see Configuring
VMware migration plan settings.
11.11. CONFIGURING VMWARE MIGRATION PLAN SETTINGS
After you create a migration plan by using the Migration Toolkit for Virtualization wizard, configure
advanced migration plan settings on the Plan details page. These settings do not appear in the wizard
but can affect your migration.
Prerequisites
You have created a migration plan by using the Migration Toolkit for Virtualization wizard. For
more information, see Creating a VMware vSphere migration plan by using the MTV wizard .
89

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Procedure
1. On the Plan details page for your plan, review the Plan settings section.
The Plan settings section includes settings that you specified in the Other settings (optional)
page of the wizard and some additional optional settings. The steps below refer to the
additional optional settings, but all of the settings can be edited by clicking the Options menu
, making the change, and then clicking Save.
2. Check the following items in the Plan settings section of the page:
a. Volume name template: Specifies a template for the volume interface name for the VMs in
your plan.
For a list of available variables and examples, see Volume name template variables.
To specify a volume name template for all the VMs in your plan, do the following:
Click the Edit icon.
Click Enter custom naming template.
Enter the template according to the instructions. Be sure that your template
generates volume names that are DNS-compliant.
Click Save.
To specify a volume name template only for specific VMs, do the following:
Click the Virtual Machines tab.
Select the desired VMs.
Click the Options menu of the VM.
Select Edit Volume name template.
Enter the template according to the instructions. Be sure that your template
generates volume names that are DNS-compliant.
Click Save.
b. PVC name template: Specifies a template for the name of the persistent volume claim
(PVC) for the VMs in your plan.
For a list of available variables, template functions, and examples, see PVC name template
variables.
To specify a PVC name template for all the VMs in your plan, do the following:
Click the Edit icon.
Click Enter custom naming template.
Enter the template according to the instructions. Be sure that your template
generates PVC names that are DNS-compliant.
Click Save.
To specify a PVC name template only for specific VMs, do the following:
Click the Virtual Machines tab.
90

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
Click the Virtual Machines tab.
Select the desired VMs.
Click the Options menu of the VM.
Select Edit PVC name template.
Enter the template according to the instructions. Be sure that your template
generates PVC names that are DNS-compliant.
Click Save.
c. Network name template: Specifies a template for the network interface name for the VMs
in your plan.
For a list of available variables and examples, see Network name template variables.
To specify a network name template for all the VMs in your plan, do the following:
Click the Edit icon.
Click Enter custom naming template.
Enter the template according to the instructions. Be sure that your template
generates network interface names that are DNS-compliant.
Click Save.
To specify a network name template only for specific VMs, do the following:
Click the Virtual Machines tab.
Select the desired VMs.
Click the Options menu of the VM.
Select Edit Network name template.
Enter the template according to the instructions. Be sure that your template
generates network interface names that are DNS-compliant.
Click Save.
IMPORTANT
Changes you make on the Virtual Machines tab override any
changes on the Plan details page.
IMPORTANT
91

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
IMPORTANT
You must ensure that the templates you enter on the Plan details
page generate DNS-compliant names. If the template syntax is
invalid or if the resulting names are not DNS-compliant, MTV adds an
error to the plan conditions and prevents the migration from running.
To help ensure valid names, you might want to run a Go script that
uses the sprig methods that MTV supports. For tables documenting
the methods that MTV supports, see MTV template utility for
VMware.
d. Raw copy mode: By default, during migration, virtual machines (VMs) are converted using a
tool named virt-v2v that makes them compatible with OpenShift Virtualization. For more
information about the virt-v2v conversion process, see How MTV uses the virt-v2v tool.
Raw copy mode copies VMs without converting them. This allows for faster conversions,
migrating VMs running a wider range of operating systems, and supporting migrating disks
encrypted using Linux Unified Key Setup (LUKS) without needing keys. However, VMs
migrated using raw copy mode might not function properly on OpenShift Virtualization.
To use raw copy mode for your migration plan, do the following:
Click the Edit icon.
Toggle the Raw copy mode switch to enable it.
Optional: Configure the Use compatibility mode setting:
When you enable Use compatibility mode (default), MTV uses compatibility
devices (SATA bus, E1000E NICs, USB) to ensure the VM can boot on OpenShift
Virtualization.
When you disable Use compatibility mode, MTV uses pre-installed VirtIO devices
on the source VM for better performance.
IMPORTANT
Only disable Use compatibility mode if VirtIO drivers are already
installed in the source VM. VMs without pre-installed VirtIO drivers
do not boot on OpenShift Virtualization if you disable compatibility
mode.
Click Save.
e. VM target node selector, VM target labels, and VM target affinity rules are options that
support VM target scheduling, a feature that lets you direct MTV to migrate virtual
machines (VMs) to specific nodes or workloads (pods) of OpenShift Virtualization as well as
to schedule when to power on the VMs.
For more information on the feature in general, see Target VM scheduling options.
For more details on using the feature with the UI, see Scheduling target VMs from the user
interface.
VM target node selector allows you to create mandatory exact match key-value label
pairs that the target node must possess. If no node on the cluster has all the labels
specified, the VM is not scheduled and it remains in a Pending state until there is space
on a node that fits these key-value label pairs.
92

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
To use the VM target node selector for your migration plan, do the following:
Click the Edit icon.
Enter a key-value label pair. For example, to require that all VMs in the plan be
migrated to your east data center, enter dataCenter as your key and east as
your label.
To add another key-value label pair, click + and enter another key-value pair.
Click Save.
VM target labels allows you to apply organizational or operational labels to migrated
VMs for identification and management. One use for these labels is to use them to
specify a different scheduler for your migrated VMs, by creating a specific target VM
label for it.
To use the VM target node selector for your migration plan, do the following:
Click the Edit icon.
Enter one or more VM target labels.
Click Save.
VM target affinity rules: Target affinity rules let you use conditions to either require or
prefer scheduling on specific nodes or workloads (pods).
Target anti-affinity rules let you prevent VMs from being scheduled to run on selected
workloads (pods) or prefer that they are not scheduled. These kind of rules offer more
flexible placement control than rigid Node Selector rules, because they support
conditionals such as In, or NotIn.
For example, you could require that a VM be powered on "only if it is migrated to node A
or if it is migrated to an SSD disk, but it cannot be migrated to a node for which license-
tier=silver is true."
Additionally, both target affinity and target anti-affinity rules allow you to include both
hard and soft conditions in the same rule. A hard condition is a requirement, and a soft
condition is a preference. The previous example used only hard conditions. A rule that
states that "a VM can be powered on if it is migrated to node A or if it is migrated to an
SSD disk, but it is preferred not to migrate it to a node for which license-tier=silver is
true" is an example of a rule that uses soft conditions.
MTV supports target affinity rules at both the node level and the workload (pod) level.
It supports anti-affinity rules at the workload (pod) level only.
To use VM target affinity rules for your migration plan, do the following:
Click the Edit icon.
Click Add affinity rule.
Select the Type of affinity rule from the list. Valid options: Node Affinity,
Workload (pod) Affinity, Workload (pod) Anti-Affinity.
Select the Condition from the list. Valid options: Preferred during scheduling
(soft condition), Required during scheduling (hard condition).
93

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Soft condition only: Enter a numerical Weight. The higher the weight, the
stronger the preference. Valid options: whole numbers from 1-100.
Enter a Typology key, the key for the node label that the system uses to
denote the domain.
Optional: Select the Workload labels that you want to set by doing the
following:
Enter a Key.
Select an Operator from the list. Valid options: Exists, DoesNotExist, In,
and NotIn.
Enter a Value.
To add another label, click Add expression and add another key-value pair with
an operator.
Click Save affinity rule.
To add another affinity rule, click Add affinity rule. Rules with a preferred
condition will stack with an AND relation between them. Rules with a required
condition will stack with an OR relation between them.
MTV validates any changes you made on this page.
3. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
4. When you have fixed all conditions listed, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 11.11. Tabs of the Plan details page
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
11.11.1. PVC name template variables
When creating a migration plan, you can use template variables to customize the names of persistent
94

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
When creating a migration plan, you can use template variables to customize the names of persistent
volume claims (PVCs) for migrated virtual machine disks. The template follows Go template syntax.
You must ensure that PVC names are DNS-compliant: they must consist of lowercase alphanumeric
characters or hyphens (-), start with an alphanumeric character, and not exceed 63 characters. If the
template syntax is invalid or if the resulting PVC names are not DNS-compliant, MTV adds an error to
the plan conditions and prevents the migration from running.
11.11.1.1. Available variables
The pvcNameTemplate field has access to the following variables:
.VmName: Name of the VM in the source cluster.
.TargetVmName: Final VM name in the target cluster. May equal .VmName if no rename or
normalization occurs.
.PlanName: Name of the migration plan.
.DiskIndex: Sequential index of the disk (0-based).
.RootDiskIndex: Index value that identifies the root disk.
.Shared: Indicates whether the volume is shared. Options: true for a shared volume, false for a
non-shared volume.
.WinDriveLetter: Windows drive letter in lowercase (for example, c, d). Only applicable to
Windows guests.
This variable requires the QEMU Guest Agent (or VMware Tools) to be active and reachable on
the source VM. It also requires a disk key mapping between the guest operating system and the
hardware disk. This mapping may be missing for some disk configurations, particularly IDE disks.
When the mapping is missing (for example, on Linux VMs or when the Windows drive letter is not
explicitly set), the variable resolves to an empty string. If this results in an invalid PVC name,
MTV adds an error to the plan conditions and prevents the migration from running.
.FileName: Name of the virtual disk file (for example, vm-disk1.vmdk), not the full datastore
path. VMware only.
11.11.1.2. Template functions
You can use Go template functions to transform variable values into valid PVC names. Common
functions include:
trimSuffix: Removes a suffix from a string. For example, ++{{++.FileName | trimSuffix
".vmdk"}} removes the .vmdk extension.
replace: Replaces all occurrences of a substring. For example, ++{{++.FileName | replace "_" "-
"}} replaces underscores with hyphens.
lower: Converts a string to lowercase. For example, ++{{++.FileName | lower}}.
Functions can be chained together using the pipe (|) operator. Regular expression functions such as
mustRegexReplaceAll are also available for advanced transformations.
11.11.1.3. Examples
95

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
"{{.VmName}}-disk-{{.DiskIndex}}" – Basic template with VM name and disk index
"{{if eq .DiskIndex .RootDiskIndex}}root{{else}}data{{end}}-{{.DiskIndex}}" – Conditional
naming for root disk
"{{if .Shared}}shared-{{end}}{{.VmName}}-{{.DiskIndex}}" – Mark shared volumes
"pvc-{{.VmName}}-drive-{{.WinDriveLetter}}" – Include Windows drive letter (results in pvc-
myvm-drive-c)
"{{.FileName | trimSuffix ".vmdk" | replace "_" "-" | replace "." "-" | lower}}-disk-
{{.DiskIndex}}" – Transform filename to valid PVC name (transforms VM_Disk.1.vmdk to vm-
disk-1-disk-0)
11.11.2. Network name template variables
When creating a migration plan, you can use template variables to customize the names of network
interfaces for migrated virtual machines. The template follows Go template syntax.
You must ensure that network interface names are DNS-compliant: they must consist of lowercase
alphanumeric characters or hyphens (-), start with an alphanumeric character, and not exceed 63
characters. If the template syntax is invalid or if the resulting network interface names are not DNS-
compliant, MTV adds an error to the plan conditions and prevents the migration from running.
11.11.2.1. Available variables
The networkNameTemplate field has access to the following variables:
.NetworkName: Name of the Multus Network Attachment Definition if the target network is
multus. Empty otherwise.
.NetworkNamespace: Namespace where the Multus Network Attachment Definition is located
if the target network is multus. Empty otherwise.
.NetworkType: Specifies the network type. Options: multus or pod.
.NetworkIndex: Sequential index of the network interface (0-based).
11.11.2.2. Examples
"net-{{.NetworkIndex}}"
"{{if eq .NetworkType \"pod\"}}pod{{else}}multus-{{.NetworkIndex}}{{end}}"
11.11.3. Volume name template variables
When creating a migration plan, you can use template variables to customize the names of volume
interfaces for migrated virtual machines. The template follows Go template syntax.
You must ensure that volume names are DNS-compliant: they must consist of lowercase alphanumeric
characters or hyphens (-), start with an alphanumeric character, and not exceed 63 characters. If the
template syntax is invalid or if the resulting volume names are not DNS-compliant, MTV adds an error to
the plan conditions and prevents the migration from running.
96

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
11.11.3.1. Available variables
The volumeNameTemplate field has access to the following variables:
.PVCName: Name of the PVC mounted to the VM using this volume.
.VolumeIndex: Sequential index of the volume interface (0-based).
11.11.3.2. Examples
"disk-{{.VolumeIndex}}"
"pvc-{{.PVCName}}"
11.12. ABOUT DEEP INSPECTION
You can use Deep Inspection to analyze virtual machine (VM) disk images before migration. Deep
Inspection finds compatibility issues that standard inspection might miss and helps you plan remediation
before starting the migration.
IMPORTANT
Deep Inspection is a Technology Preview feature only. Technology Preview features are
not supported with Red Hat production service level agreements (SLAs) and might not
be functionally complete. Red Hat does not recommend using them in production. These
features provide early access to upcoming product features, enabling customers to test
functionality and provide feedback during the development process.
Prerequisites
VMware vSphere source provider configured in MTV.
VMware Virtual Disk Development Kit (VDDK) configured for the source provider. Deep
Inspection uses VDDK to access VM disk images.
Changed Block Tracking (CBT) must be enabled.
Cluster resources available to run inspection pods. Each pod needs CPU, memory, and
storage to mount and analyze VM disks.
Limitations
Deep Inspection is available only for VMware vSphere providers.
MTV limits concurrent inspections to 10 by default. Additional inspections are queued until
resources become available.
Considerations
Deep Inspection takes longer than standard inspection. It creates a VM snapshot and
inspects the base disks, then performs detailed analysis.
Inspection time depends on VM disk size and cluster resources.
97

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
11.12.1. Inspection methods
MTV supports two methods for inspecting VMs before migration:
Standard inspection: Queries the source provider’s API to collect VM metadata. This includes
operating system information, disk configuration, and hardware settings. This method is fast
and does not require extra resources, but it relies on metadata from the provider.
Deep Inspection: Launches a temporary worker pod in the OpenShift cluster. The pod mounts
and analyzes the VM’s disk images directly. This method provides greater confidence in
migration success by finding guest-level issues that standard inspection might miss.
11.12.2. How Deep Inspection works
Deep Inspection launches a temporary pod in your OpenShift cluster that uses VDDK to mount the
VM’s disk images. MTV creates a snapshot to analyze the guest operating system without affecting the
VM’s power state, whether it is running or stopped. After analysis, MTV cleans up the pod and stores the
results.
Deep Inspection provides detailed information about the VM to help you assess migration readiness:
Category Information analyzed
Operating system and
Operating system name, version, and architecture
hardware
Kernel version
Storage and file systems
File system types (for example, ext4, xfs, ntfs)
Partition layouts and mount points
Root device path (critical for dual-boot or multi-disk VMs)
11.12.3. When to use Deep Inspection
Use Deep Inspection for:
Critical or production VMs where you need high confidence in successful migration.
Legacy VMs where driver and operating system support is uncertain.
Dual-boot or multi-disk VMs that need the correct root device identified.
VMs with standard inspection warnings that need more detailed information.
Additional resources
Inspecting VMs in the MTV UI
Inspecting VMs by using the command line interface
Red Hat Technology Preview Features Support Scope
98

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
11.13. UNDERSTANDING DEEP INSPECTION VALIDATION RESULTS
Deep Inspection validation results provide categorized findings that help you assess migration
feasibility. The severity levels and concern categories indicate which issues require resolution before
migration.
11.13.1. Validation concerns
Deep Inspection can identify concerns that are organized by category and severity:
Changed Block Tracking (CBT) not enabled
CBT is not enabled on the source VM. This does not prevent migration. However, it can affect
performance during warm migrations.
Unsupported operating system
The guest operating system is not supported for migration to OpenShift Virtualization. For
information about supported operating systems, see the MTV compatibility matrix.
File system issues
The VM has file system configurations that might cause conversion failures.
Multi-boot configuration
The VM has multiple bootable operating systems. You must specify the correct root device path in
the migration plan settings.
11.13.2. Migration preparation considerations
Deep Inspection results help determine the necessary preparation steps before migrating virtual
machines (VMs):
Critical concerns
Resolving errors and verifying operating system support before beginning the migration prevents
failures.
Multi-boot configurations
When Deep Inspection detects a multi-boot configuration, the Root device setting in the migration
plan should match the root device path from the inspection results.
File system compatibility
OpenShift Virtualization and the target operating system version must support all file systems on the
source VM.
Resource allocation
The disk and partition information provides the baseline data required for planning storage
allocations in the destination environment.
Additional resources
Creating a VMware vSphere migration plan by using the MTV wizard
11.14. MIGRATION OF LUKS-ENCRYPTED DISKS
Migrate VMware VMs with Linux Unified Key Setup (LUKS) encrypted disks to OpenShift Virtualization
by enabling Network-Bound Disk Encryption (NBDE) with Clevis or by manually adding passwords in
your migration plan.
99

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
If you enable NBDE, passwords are retrieved from the Clevis server. When you manually add LUKS
passwords to your migration plan, you provide the list of passwords, and you cannot use NBDE to
retrieve them. The two methods for migrating LUKS-encrypted disks are incompatible. You must use
either NBDE or manual LUKS passwords to migrate LUKS-encrypted disks.
MTV transfers the data of VMs with LUKS-encrypted disks from the source environment to the target
OpenShift Virtualization cluster. MTV reads only the blocks that are required for guest conversion,
decrypting the required blocks and re-encrypting them locally with the same key.
Clevis is a client-side framework that automates the decryption of LUKS volumes by binding a LUKS key
slot to a policy. During the migration of VMs with LUKS-encrypted disks, MTV authenticates with the
configured network service by requesting the key to unlock the LUKS-encrypted disk from the Tang
server. The automatic retrieval of the key allows the VM to boot without a manual passphrase entry from
an administrator.
Benefits of NBDE
Automation: Eliminates the need to enter keys manually during migration.
Enhanced security: Maintains the security of VMs throughout their migration lifecycle by
preserving LUKS encryption from the source to the destination.
Seamless operation: Ensures that VMs with encrypted disks can be brought online in the
new OpenShift Virtualization environment with minimal interruption.
11.15. ENABLING NETWORK-BOUND DISK ENCRYPTION WITH CLEVIS
When you enable NBDE with Clevis, the Tang server manages Linux Unified Key Setup (LUKS)-
encrypted disk keys during migration. You can alternatively use manual LUKS passwords.
You can enable NBDE with Clevis either in the MTV UI or in the YAML file for your migration plan:
In the MTV UI, you must select either NBDE with Clevis or LUKS passphrases. You can have only
one encryption type, and you apply the setting to all VMs in your migration plan.
In the YAML file for your migration plan, you can combine encryption types and apply the
setting to selected VMs in the YAML file.
Prerequisites
The Tang server is accessible from your OpenShift cluster and from the migration network.
You have a LUKS key slot bound to the Tang server policy.
NOTE
For MTV to access the keys from the Tang server, the keys must be on a
different subnet range than a user-defined network (UDN).
Procedure
1. Enable NBDE with Clevis in the MTV UI.
a. In the Create migration plan wizard, navigate to Other settings under Additional setup in
the left navigation pane.
100

CHAPTER 11. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM VMWARE VSPHERE
b. Select Use NBDE/Clevis.
If you are not using NBDE with Clevis, you add passphrases for LUKS-encrypted devices so
that the Tang servers can decrypt the disks during a migration.
c. Click Next, and verify that Use NBDE/Clevis shows as Enabled under Other settings
(optional).
d. When you create your migration plan, click Migration plans in the left navigation menu, and
open the Plan details page for your migration plan.
e. Click the Edit icon for Disk decryption under Plan settings.
f. Verify that Use network-bound disk encryption (NBDE/Clevis) is selected.
If you are not using NBDE with Clevis, verify that the passphrases for LUKS-encrypted
devices are added.
2. Enable NBDE with Clevis in the YAML file.
a. Click Migration plans in the left navigation menu and open the Plan details page for your
migration plan.
b. Click the YAML tab to open the Plan custom resource (CR) for your migration plan.
c. For each VM under vms in the YAML file, enter the encryption type. In this example, you set
nbdeClevis as the encryption type for vm-1, LUKS passphrase as the encryption type for
vm-2, and no encryption type for vm-3:
Example:
vms:
- id: vm-1
name: vm-1-esx8.0-rhel8.10-raid1
targetPowerState: on
nbdeClevis: true
- id: vm-2
name: vm-2-esx8.0-rhel8.10-raid1
luks: { name: 'test-secret-1' }
- id: vm-3
name: vm-3-esx8.0-rhel8.10-raid1
Troubleshooting
For information about LUKS or Clevis configuration on the source VM, see Configuring
automated unlocking of encrypted volumes by using policy-based decryption in the RHEL
Security hardening guide.
11.16. ABOUT SCHEDULING IMPORTER PODS
Migration Toolkit for Virtualization uses virt-v2v convertor pods, or importer pods, to transfer data from
VMware source virtual machines (VMs) to target VMs.
By default, OpenShift Virtualization assigns the nodes to which these importer pods transfer data.
However, for cold migrations from VMware VMs, you can schedule the destination nodes for the
importer pods.
IMPORTANT
101

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
IMPORTANT
Scheduling importer pods is supported only for cold migrations from VMware VMs. It is
not supported for warm migrations from VMware or for migrations from other vendors.
In MTV 2.11, scheduling importer pods is available only for migrations from the command-line interface.
You schedule the importer pods in the Plan CR, as described in step 8 of Running a VMware vSphere
migration from the command-line.
102

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM RED HAT VIRTUALIZATION
Create a Red Hat Virtualization migration plan by setting up network maps, configuring source and
destination providers with migration networks, and defining the migration plan in the Migration Toolkit
for Virtualization (MTV) UI.
12.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless network maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Red Hat Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding a Red Hat Virtualization source provider or Adding
an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
12.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps by using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
103

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Red Hat Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding a Red Hat Virtualization source provider or Adding
an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_network_id>
name: <source_network_name>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
id: <source_network_id>
name: <source_network_name>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod and multus.
source: You can use either the id or the name parameter to specify the source network.
For id, specify the RHV network Universal Unique ID (UUID).
<network_attachment_definition>: Specify a network attachment definition for each
104

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network.
<network_attachment_definition_namespace>: Required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
12.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless storage maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Red Hat Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding a Red Hat Virtualization source provider or Adding
an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
4. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
5. Click Create.
Your map appears in the list of storage maps.
12.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
105

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Red Hat Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding a Red Hat Virtualization source provider or Adding
an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
id: <source_storage_domain>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
accessMode: Allowed values are ReadWriteOnce and ReadWriteMany.
id: Specify the RHV storage domain UUID, for example, f2737930-b567-451a-9ceb-
2887f6207009.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
106

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
12.5. ADDING A RED HAT VIRTUALIZATION SOURCE PROVIDER
You can add a Red Hat Virtualization source provider by using the Red Hat OpenShift web console.
Prerequisites
Manager CA certificate. If the certificate was replaced by a third-party certificate, use the
Manager Apache CA certificate instead.
Procedure
1. Access the Create provider page for Red Hat Virtualization by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click Red Hat Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click Red Hat Virtualization in the Welcome
pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider.
URL: URL of the API endpoint of the Red Hat Virtualization Manager (RHVM) on which the
source VM is mounted. Ensure that the URL includes the path leading to the RHVM API
server, usually /ovirt-engine/api. For example, https://rhv-host-example.com/ovirt-
engine/api.
3. Enter the provider credentials:
Username: Username
Password: Password
4. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
107

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
5. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
It might take a few minutes for the provider to move to the Ready status.
6. Optional: Add access to the UI of the provider:
a. On the Providers page, click the provider.
The Provider details page opens.
b. Click the Edit icon under External UI web link.
c. Enter the link and click Save.
NOTE
If you do not enter a link, MTV attempts to calculate the correct link.
If MTV succeeds, the hyperlink of the field points to the calculated link.
If MTV does not succeed, the field remains empty.
12.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
108

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
12.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
109

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
12.8. CREATING A RED HAT VIRTUALIZATION MIGRATION PLAN BY
USING THE MTV WIZARD
You can migrate Red Hat Virtualization virtual machines (VMs) by using the Migration Toolkit for
Virtualization plan creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.
110

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION

WARNING
Do not include virtual machines with guest-initiated storage connections, such as
Internet Small Computer Systems Interface (iSCSI) connections or Network File
System (NFS) mounts. These require either additional planning before migration or
reconfiguration after migration.
This prevents concurrent disk access to the storage the guest points to.
IMPORTANT
A plan cannot contain more than 500 VMs or 500 disks.
IMPORTANT
When you click Create plan on the Review and create page of the wizard, Migration
Toolkit for Virtualization (MTV) validates your plan. If everything is OK, the Plan details
page for your plan opens. This page contains settings that do not appear in the wizard,
but are important. Be sure to read and follow the instructions for this page carefully, even
though it is outside the plan creation wizard. The page can be opened later, any time
before you run the plan, so you can come back to it if needed.
Prerequisites
Have a Red Hat Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding a Red Hat Virtualization source provider or Adding
an OpenShift Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
If you are using a user-defined network (UDN), note the name of the namespace as defined in
OpenShift Virtualization.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
111

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create Project.
4. Click Next.
5. On the Virtual machines page, select the virtual machines you want to migrate and click Next.
6. If you are using a UDN, verify that the IP address of the provider is outside the subnet of the
UDN. If the IP address is within the subnet of the UDN, the migration fails.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
112

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Migration type page, choose one of the following:
Cold migration (default)
Warm migration
12. Click Next.
13. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
113

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
must also change the MTU of the VMware migration network. For more information, see
Selecting a migration network for a VMware source provider .
14. Click Next.
15. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
16. To add a hook, select the appropriate Enable hook checkbox.
17. Enter the Hook runner image.
18. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
19. Click Next.
20. On the Review and create page, review the information displayed.
21. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
22. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
The Plan settings section of the page includes settings that you specified in the Other settings
(optional) page and some additional optional settings. The steps below refer to the additional
optional steps, but all of the settings can be edited by clicking the Options menu , making
the change, and then clicking Save.
23. Check the following item on the Plan settings section of the page:
Preserve CPU mode: Generally, the CPU model (type) for Red Hat Virtualization VMs is set
at the cluster level. However, the CPU model can be set at the VM level, which is called a
custom CPU model.
By default, MTV sets the CPU model on the destination cluster as follows: MTV preserves
custom CPU settings for VMs that have them. For VMs without custom CPU settings, MTV
does not set the CPU model. Instead, the CPU model is later set by OpenShift
Virtualization.
To preserve the cluster-level CPU model of your Red Hat Virtualization VMs, do the
following:
114

CHAPTER 12. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM RED HAT VIRTUALIZATION
| a.  Click the Options menu  |  .  |     |     |     |
| --------------------------- | --- | --- | --- | --- |
b.  Toggle the Whether to preserve the CPU mode lswitch.
c.  Click Save.
MTV validates any changes you made on this page.
24.  In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
25.  After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 12.1. Tabs of the Plan details page
| YAML | Virtual Machines | Resources | Mappings | Hooks |
| ---- | ---------------- | --------- | -------- | ----- |
Editable YAML  The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
| based on your  |     | CPUs, and total | the network and | the hooks used   |
| -------------- | --- | --------------- | --------------- | ---------------- |
| plan’s details |     | memory for both | storage maps    | by your plan, if |
|                |     | total VMs and   | used by your    | any              |
including source
| provider, network |     | running VMs | plan |     |
| ----------------- | --- | ----------- | ---- | --- |
and storage
maps, VMs, and
any issues with
your VMs
115

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM OPENSTACK
Create an OpenStack migration plan by setting up network maps, configuring source and destination
providers with migration networks, and defining the migration plan in the Migration Toolkit for
Virtualization (MTV) UI.
13.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless network maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenStack source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an OpenStack source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
13.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps by using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
116

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenStack source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an OpenStack source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_network_id>
name: <source_network_name>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
id: <source_network_id>
name: <source_network_name>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod and multus.
source: You can use either the id or the name parameter to specify the source network.
For id, specify the OpenStack network UUID.
<network_attachment_definition>: Specify a network attachment definition for each
117

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network.
<network_attachment_definition_namespace> is required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
13.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless storage maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenStack source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an OpenStack source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
4. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
5. Click Create.
Your map appears in the list of storage maps.
13.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
118

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenStack source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an OpenStack source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
id: <source_volume_type>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
accessMode: Allowed values are ReadWriteOnce and ReadWriteMany.
id: Specify the OpenStack volume_type UUID, for example, f2737930-b567-451a-9ceb-
2887f6207009.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
119

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
13.5. ADDING AN OPENSTACK SOURCE PROVIDER
You can add an OpenStack source provider by using the Red Hat OpenShift web console.
IMPORTANT
When you migrate an image-based VM from an OpenStack provider, MTV creates a
snapshot of the source VM image and copies it to the target VM. The snapshot is created
at migration time. Therefore, the target VM has the same state as the source VM at that
point.
Procedure
1. Access the Create provider page for OpenStack by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenStack.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenStack in the Welcome pane, and
select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider.
URL: URL of the OpenStack Identity (Keystone) endpoint. For example,
http://controller:5000/v3.
Authentication type: Choose an authentication method and supply the required
information.
For example, if you choose Application credential ID, the system prompts you for the
application credential ID and secret.
Application credential ID
Application credential ID: OpenStack application credential ID
Application credential secret: OpenStack application credential Secret
Application credential name
Application credential name: OpenStack application credential name
Application credential secret: OpenStack application credential Secret
120

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
Username: OpenStack username
Domain: OpenStack domain name
Token with user ID
Token: OpenStack token
User ID: OpenStack user ID
Project ID: OpenStack project ID
Token with user name
Token: OpenStack token
Username: OpenStack username
Project: OpenStack project
Domain name: OpenStack domain name
Password
Username: OpenStack username
Password: OpenStack password
Project: OpenStack project
Domain: OpenStack domain name
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
It might take a few minutes for the provider to move to the Ready status.
5. Optional: Add access to the UI of the provider:
a. On the Providers page, click the provider.
The Provider details page opens.
121

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
b. Click the Edit icon under External UI web link.
c. Enter the link and click Save.
NOTE
If you do not enter a link, MTV attempts to calculate the correct link.
If MTV succeeds, the hyperlink of the field points to the calculated link.
If MTV does not succeed, the field remains empty.
13.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
122

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
13.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
123

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
13.8. CREATING AN OPENSTACK MIGRATION PLAN BY USING THE
MTV WIZARD
You can migrate OpenStack virtual machines (VMs) by using the Migration Toolkit for Virtualization plan
creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.

WARNING
Do not include virtual machines with guest-initiated storage connections, such as
Internet Small Computer Systems Interface (iSCSI) connections or Network File
System (NFS) mounts. These require either additional planning before migration or
reconfiguration after migration.
This prevents concurrent disk access to the storage the guest points to.
IMPORTANT
A plan cannot contain more than 500 VMs or 500 disks.
IMPORTANT
124

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
IMPORTANT
When you click Create plan on the Review and create page of the wizard, Migration
Toolkit for Virtualization (MTV) validates your plan. If everything is OK, the Plan details
page for your plan opens. This page contains settings that do not appear in the wizard,
but are important. Be sure to read and follow the instructions for this page carefully, even
though it is outside the plan creation wizard. The page can be opened later, any time
before you run the plan, so you can come back to it if needed.
Prerequisites
Have an OpenStack source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an OpenStack source provider or Adding an OpenShift
Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
If you are using a user-defined network (UDN), note the name of its namespace as defined in
OpenShift Virtualization.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create project.
4. Click Next.
125

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
5. On the Virtual machines page, select the virtual machines you want to migrate and click Next.
6. If you are using a UDN, verify that the IP address of the provider is outside the subnet of the
UDN. If the IP address is within the subnet of the UDN, the migration fails.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
126

CHAPTER 13. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSTACK
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
must also change the MTU of the VMware migration network. For more information, see
Selecting a migration network for a VMware source provider .
12. Click Next.
13. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
14. To add a hook, select the appropriate Enable hook checkbox.
15. Enter the Hook runner image.
16. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
17. Click Next.
18. On the Review and create page, review the information displayed.
127

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
19. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
20. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
21. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
22. After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 13.1. Tabs of the Plan details page
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
128

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM OVA
Create an OVA migration plan by setting up network maps, configuring source and destination providers
with migration networks, and defining the migration plan in the Migration Toolkit for Virtualization
(MTV) UI.
14.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless network maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an Open Virtual Appliance (OVA) source provider and an OpenShift Virtualization
destination provider. For more information, see Adding an Open Virtual Appliance (OVA)
source provider or Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
14.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps by using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
129

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an Open Virtual Appliance (OVA) source provider and an OpenShift Virtualization
destination provider. For more information, see Adding an Open Virtual Appliance (OVA)
source provider or Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_network_id>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
id: <source_network_id>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod and multus.
source: Specify the OVA network Universal Unique ID (UUID).
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network.
<network_attachment_definition_namespace>: Required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
130

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
14.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless storage maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an Open Virtual Appliance (OVA) source provider and an OpenShift Virtualization
destination provider. For more information, see Adding an Open Virtual Appliance (OVA)
source provider or Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
4. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
5. Click Create.
Your map appears in the list of storage maps.
14.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
131

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an Open Virtual Appliance (OVA) source provider and an OpenShift Virtualization
destination provider. For more information, see Adding an Open Virtual Appliance (OVA)
source provider or Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
name: Dummy storage for source provider <provider_name>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
accessMode: Allowed values are ReadWriteOnce and ReadWriteMany.
name: For OVA, the StorageMap can map only a single storage, which all the disks from the
OVA are associated with, to a storage class at the destination. For this reason, the storage is
referred to in the UI as "Dummy storage for source provider <provider_name>". In the YAML,
write the phrase as it appears above, without the quotation marks and replacing
<provider_name> with the actual name of the provider.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
132

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
14.5. ADDING AN OPEN VIRTUAL APPLIANCE (OVA) SOURCE
PROVIDER
You can add Open Virtual Appliance (OVA) files that were created by VMware vSphere as a source
provider by using the Red Hat OpenShift web console.
Procedure
1. Access the Create provider page for Open Virtual Appliance by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click Open Virtual Appliance.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click Open Virtual Appliance in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider
URL: URL of the Network File System (NFS) file share that serves the OVA
NOTE
After creating the provider, you can optionally configure OVA file upload by
web browser to upload OVA files directly to the NFS share. For more
information, see Configuring OVA file upload by web browser.
3. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
An error message might appear that states that an error has occurred. You can
ignore this message.
14.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
133

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
14.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
134

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
135

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
14.8. CREATING AN OPEN VIRTUALIZATION APPLIANCE (OVA)
MIGRATION PLAN BY USING THE MTV WIZARD
You can migrate Open Virtual Appliance (OVA) files that were created by VMware vSphere by using the
Migration Toolkit for Virtualization plan creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.

WARNING
Do not include virtual machines with guest-initiated storage connections, such as
Internet Small Computer Systems Interface (iSCSI) connections or Network File
System (NFS) mounts. These require either additional planning before migration or
reconfiguration after migration.
This prevents concurrent disk access to the storage the guest points to.
IMPORTANT
A plan cannot contain more than 500 VMs or 500 disks.
IMPORTANT
When you click Create plan on the Review and create page of the wizard, Migration
Toolkit for Virtualization (MTV) validates your plan. If everything is OK, the Plan details
page for your plan opens. This page contains settings that do not appear in the wizard,
but are important. Be sure to read and follow the instructions for this page carefully, even
though it is outside the plan creation wizard. The page can be opened later, any time
before you run the plan, so you can come back to it if needed.
Prerequisites
Have an OVA source provider and an OpenShift Virtualization destination provider. For more
information, see Adding an Open Virtual Appliance (OVA) source provider or Adding an
OpenShift Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
If you are using a user-defined network (UDN), note the name of its namespace as defined in
OpenShift Virtualization.
Procedure
136

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create Project.
4. Click Next.
5. On the Virtual machines page, select the virtual machines you want to migrate and click Next.
6. If you are using a UDN, verify that the IP address of the provider is outside the subnet of the
UDN. If the IP address is within the subnet of the UDN, the migration fails.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
137

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
138

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
must also change the MTU of the VMware migration network. For more information, see
Selecting a migration network for a VMware source provider .
12. Click Next.
13. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
14. To add a hook, select the appropriate Enable hook checkbox.
15. Enter the Hook runner image.
16. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
17. Click Next.
18. On the Review and create page, review the information displayed.
19. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
20. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
21. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
22. After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 14.1. Tabs of the Plan details page
139

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
14.9. CONFIGURING OVA FILE UPLOAD BY WEB BROWSER
Configure Open Virtual Appliance (OVA) file upload to enable web browser uploads directly to an NFS
share. Enable OVA management in the ForkliftController CR and then enable uploads for each provider
in the MTV UI.
Prerequisites
You have an NFS share to point the OVA provider at.
You have enough storage space in your NFS share.
The NFS share is writable by the QEMU group (GID 107).
You have a valid .ova file to upload.
Your .ova file has a unique file name.
Procedure
1. In the Red Hat OpenShift web console, click Operators > Installed Operators.
2. Click Migration Toolkit for Virtualization Operator.
The Operator Details page opens in the Details tab.
3. Click the ForkliftController tab, and open the forklift-controller resource.
4. Click the forklift-controller YAML tab, and add the feature_ova_appliance_management
field to the spec section of the forklift-controller custom resource (CR):
Example:
spec:
...
feature_ova_appliance_management: 'true'
Wait for the operator to redeploy the controller after updating the forklift-controller CR.
5. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
140

CHAPTER 14. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OVA
6. Click the provider to open the Details page. Click the provider’s YAML tab.
For information about creating a provider, see Adding an Open Virtual Appliance (OVA) source
provider.
7. Scroll down the provider’s YAML file, and add the applianceManagement field to the spec
section. Set applianceManagement to 'true':
Example:
spec:
secret:
...
settings:
applianceManagement: 'true'
type: ova
...
A temporary ConnectionTestFailed error message displays while the update is processing.
You can ignore the error message.
8. Click the provider’s Details tab, and scroll down to the Conditions section. Verify that
ApplianceManagementEnabled shows as True in the list of conditions.
9. In the Upload local OVA files section, click Browse to find a valid .ova file.
10. Click Upload.
A success message confirms the file upload. After several seconds, the number of virtual
machines increases under the Provider inventory section.
141

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL
MACHINES (VMS) FROM MICROSOFT HYPER-V
Create a Microsoft Hyper-V migration plan by setting up network maps, configuring source and
destination providers with migration networks, and defining the migration plan in the Migration Toolkit
for Virtualization (MTV) UI.
IMPORTANT
Importing VMs from Microsoft Hyper-V is a Technology Preview feature only. Technology
Preview features are not supported with Red Hat production service level agreements
(SLAs) and might not be functionally complete. Red Hat does not recommend using
them in production. These features provide early access to upcoming product features,
enabling customers to test functionality and provide feedback during the development
process.
15.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
Use the form page to create ownerless network maps in the Migration Toolkit for Virtualization (MTV)
UI. You can select these maps later when creating a migration plan.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Microsoft Hyper-V source provider and an OpenShift Virtualization destination provider.
For more information, see Adding a Microsoft Hyper-V source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, go to Migration for Virtualization > Network maps >
Create network map > Create with form.
2. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
3. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
4. Click Create.
142

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
Your map appears in the list of network maps.
15.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Use YAML or JSON to create ownerless network maps in the Migration Toolkit for Virtualization (MTV)
UI. You can select these maps later when creating a migration plan.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Microsoft Hyper-V source provider and an OpenShift Virtualization destination provider.
For more information, see Adding a Microsoft Hyper-V source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, go to Migration for Virtualization > Network maps >
Create network map > Create with YAML.
2. Enter the YAML or JSON definitions into the editor, or drag and drop a file.
3. If you enter YAML definitions, use the following:
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_network_id>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
id: <source_network_id>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
type: pod or multus.
source: The Hyper-V network adapter (virtual switch) name or ID. The name is the virtual
143

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
source: The Hyper-V network adapter (virtual switch) name or ID. The name is the virtual
switch friendly name. The id is the switch GUID in 8-4-4-4-12 hexadecimal format. To
retrieve these identifiers, see Retrieving Microsoft Hyper-V network and storage identifiers.
<network_attachment_definition>: A network attachment definition for each additional
OpenShift Virtualization network.
<network_attachment_definition_namespace>: The namespace of the OpenShift
Virtualization network attachment definition. Required only when type is multus.
4. Optional: To download your input, click Download.
5. Click Create.
Your map appears in the list of network maps.
15.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
Use the form page to create ownerless storage maps in the Migration Toolkit for Virtualization (MTV)
UI. You can select these maps later when creating a migration plan.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Microsoft Hyper-V source provider and an OpenShift Virtualization destination provider.
For more information, see Adding a Microsoft Hyper-V source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, go to Migration for Virtualization > Storage maps >
Create storage map > Create with form.
2. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
3. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
4. Click Create.
Your map appears in the list of storage maps.
144

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
15.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Use YAML or JSON to create ownerless storage maps in the Migration Toolkit for Virtualization (MTV)
UI. You can select these maps later when creating a migration plan.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have a Microsoft Hyper-V source provider and an OpenShift Virtualization destination provider.
For more information, see Adding a Microsoft Hyper-V source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, go to Migration for Virtualization > Storage maps >
Create storage map > Create with YAML.
2. Enter the YAML or JSON definitions into the editor, or drag and drop a file.
3. If you enter YAML definitions, use the following:
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
id: <source_storage_id>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
accessMode: ReadWriteOnce or ReadWriteMany.
source: The Hyper-V storage identifier (file path, volume GUID path, or storage pool name).
For example, "C:\VHDs\disk.vhdx" or C:\\VHDs\\disk.vhdx to prevent YAML parsing
errors. To retrieve these identifiers, see Retrieving Microsoft Hyper-V network and storage
identifiers.
4. Optional: To download your input, click Download.
5. Click Create.
Your map appears in the list of storage maps.
145

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
15.5. ADDING A MICROSOFT HYPER-V SOURCE PROVIDER
You can add a Microsoft Hyper-V source provider by using the Red Hat OpenShift web console. The
provider connects to the Hyper-V host by using Windows Remote Management (WinRM) and reads VM
disk files from a configured Server Message Block (SMB) share.
IMPORTANT
Importing VMs from Microsoft Hyper-V is a Technology Preview feature only. Technology
Preview features are not supported with Red Hat production service level agreements
(SLAs) and might not be functionally complete. Red Hat does not recommend using
them in production. These features provide early access to upcoming product features,
enabling customers to test functionality and provide feedback during the development
process.
For more information about the support scope of Red Hat Technology Preview features,
see Technology Preview Features Support Scope.
NOTE
MTV supports only cold migration from Microsoft Hyper-V. Warm migration is not
available.
Procedure
1. Access the Create provider page for Microsoft Hyper-V by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click Microsoft Hyper-V.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click Microsoft Hyper-V in the Welcome
pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider
URL: The Hyper-V host address for WinRM connectivity, for example, 192.168.122.115 or
hyperv-host.example.com
SMB share path: Path to the SMB share that contains the VM disk files, for example,
//192.168.122.115/VMShare
The SMB share must be accessible from both the Hyper-V host and the OpenShift cluster.
146

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
3. Enter the provider credentials:
Username: Username for accessing the SMB share, for example, Administrator or
DOMAIN\username
Password: Password for accessing the SMB share
4. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
5. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
It might take a few minutes for the provider to move to the Ready status.
15.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
147

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
15.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
148

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
15.8. RETRIEVING MICROSOFT HYPER-V NETWORK AND STORAGE
IDENTIFIERS
When you create YAML-based network maps or storage maps for Microsoft Hyper-V migrations, you
need to specify the identifiers for Hyper-V networks and storage. You can retrieve these identifiers
from the MTV Inventory service after you add your Hyper-V source provider.
Prerequisites
149

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
You have added a Microsoft Hyper-V source provider and the provider status is Ready. For
more information, see Adding a Microsoft Hyper-V source provider.
Procedure
1. Retrieve the routes for the project:
$ oc get route -n openshift-mtv
2. Retrieve the Inventory service route:
$ oc get route <inventory_service> -n openshift-mtv
3. Retrieve the access token:
$ TOKEN=$(oc whoami -t)
4. Retrieve the list of Hyper-V providers:
$ curl -H "Authorization: Bearer $TOKEN" https://<inventory_service_route>/providers/hyperv
-k
Note the id of your Hyper-V provider from the output.
5. Retrieve the networks of the Hyper-V source provider:
$ curl -H "Authorization: Bearer $TOKEN"
https://<inventory_service_route>/providers/hyperv/<provider_id>/networks/ -k
Example output: In this example, the network ID is the virtual switch GUID in 8-4-4-4-12
hexadecimal format, and the name is the virtual switch friendly name.
[
{
"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
"name": "External Switch",
"path": "/External Switch",
"revision": 1,
"selfLink": "providers/hyperv/01278af6-e1e4-4799-b01b-
d5ccc8dd0201/networks/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
},
{
"id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
"name": "Internal Switch",
"path": "/Internal Switch",
"revision": 1,
"selfLink": "providers/hyperv/01278af6-e1e4-4799-b01b-
d5ccc8dd0201/networks/b2c3d4e5-f6a7-8901-bcde-f12345678901"
}
]
Use the id value (GUID format) or the name value (friendly name) when creating network
maps.
150

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
6. Retrieve the storage of the Hyper-V source provider:
$ curl -H "Authorization: Bearer $TOKEN"
https://<inventory_service_route>/providers/hyperv/<provider_id>/storages/ -k
Example output: In this example, the storage identifiers include file paths to virtual hard
drives, volume GUID paths, or storage pool names.
[
{
"id": "C:\\VHDs\\Production",
"name": "Production VHDs",
"path": "C:\\VHDs\\Production",
"revision": 1,
"selfLink": "providers/hyperv/01278af6-e1e4-4799-b01b-
d5ccc8dd0201/storages/C:\\VHDs\\Production"
},
{
"id": "\\\\?\\Volume{a1b2c3d4-e5f6-7890-abcd-ef1234567890}\\",
"name": "Volume GUID Path",
"path": "\\\\?\\Volume{a1b2c3d4-e5f6-7890-abcd-ef1234567890}\\",
"revision": 1,
"selfLink": "providers/hyperv/01278af6-e1e4-4799-b01b-d5ccc8dd0201/storages/\\\\?
\\Volume{a1b2c3d4-e5f6-7890-abcd-ef1234567890}\\"
}
]
Use the id value when creating storage maps.
Additional resources
Creating ownerless network maps by using YAML or JSON definitions in the MTV UI
Creating ownerless storage maps by using YAML or JSON definitions in the MTV UI
15.9. CREATING A MICROSOFT HYPER-V MIGRATION PLAN BY USING
THE MTV WIZARD
You can migrate virtual machines (VMs) from Microsoft Hyper-V by using the Migration Toolkit for
Virtualization plan creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.
Limitations
MTV supports only cold migration from Microsoft Hyper-V. Warm migration is not available.
Do not include VMs with guest-initiated storage connections, such as Internet Small
Computer Systems Interface (iSCSI) connections or Network File System (NFS) mounts.
These require either additional planning before migration or reconfiguration after migration.
This prevents concurrent disk access to the storage the guest points to.
A plan cannot contain more than 500 VMs or 500 disks.
Prerequisites
151

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Prerequisites
Have a Microsoft Hyper-V source provider and an OpenShift Virtualization destination provider.
For more information, see Adding a Microsoft Hyper-V source provider or Adding an OpenShift
Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
If you are using a user-defined network (UDN), note the name of its namespace as defined in
OpenShift Virtualization.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create Project.
4. Click Next.
5. On the Virtual machines page, select the VMs you want to migrate and click Next.
6. If you are using a UDN, verify that the IP address of the provider is outside the subnet of the
UDN. If the IP address is within the subnet of the UDN, the migration fails.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
152

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create by using this option are not available in the Use an existing network
map option because each is created with an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create by using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select the SMB share from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
153

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
12. Click Next.
13. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
14. To add a hook, select the appropriate Enable hook checkbox.
15. Enter the Hook runner image.
16. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
17. Click Next.
18. On the Review and create page, review the information displayed.
19. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
20. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
21. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
154

CHAPTER 15. PLANNING A MIGRATION OF VIRTUAL MACHINES (VMS) FROM MICROSOFT HYPER-V
Conditions: Any changes that need to be made to the plan so that it can run successfully
22. When you have fixed all conditions listed, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 15.1. Tabs of the Plan details page
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details, memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
15.10. ADDITIONAL RESOURCES
Technology Preview Features Support Scope
155

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM AWS EC2
Create an AWS EC2 migration plan by setting up network and storage maps and configuring source and
destination providers in the Migration Toolkit for Virtualization (MTV) UI.
IMPORTANT
Importing VMs from Amazon EC2 is a Technology Preview feature only. Technology
Preview features are not supported with Red Hat production service level agreements
(SLAs) and might not be functionally complete. Red Hat does not recommend using
them in production. These features provide early access to upcoming product features,
enabling customers to test functionality and provide feedback during the development
process.
AWS EC2 migration supports cold migration only. The target cluster must be Red Hat OpenShift Service
on AWS (ROSA) or OpenShift Dedicated (OSD) on AWS.
16.1. CREATING OWNERLESS NETWORK MAPS FROM THE FORM
PAGE IN THE MTV UI
You can add ownerless network maps from the form page in the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
Network maps define the mapping between AWS subnet IDs and OpenShift networks (pod network or
Multus networks).
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an AWS EC2 source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an AWS EC2 source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select the AWS EC2 source provider from the list.
Target provider: Select the OpenShift Virtualization destination provider from the list.
Source network: Select the AWS subnet ID from the list.
Target network: Select the OpenShift network from the list. This can be the pod network or
156

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
Target network: Select the OpenShift network from the list. This can be the pod network or
a Multus network attachment definition.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
16.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
Network maps define the mapping between AWS subnet IDs and OpenShift networks (pod network or
Multus networks).
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an AWS EC2 source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an AWS EC2 source provider or Adding an OpenShift
Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
id: <source_subnet_id>
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
157

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
id: <source_subnet_id>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod and multus.
source: Specify the AWS subnet ID, for example, subnet-abc123def456.
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network.
<network_attachment_definition_namespace> is required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
16.3. CREATING OWNERLESS STORAGE MAPS FROM THE FORM
PAGE IN THE MTV UI
You can add ownerless storage maps from the form page in the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
Storage maps define the mapping between AWS EBS volume types and OpenShift storage classes that
use the EBS CSI driver.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
IMPORTANT
You must map EBS volumes to storage classes that use the AWS EBS CSI driver.
Prerequisites
Have an AWS EC2 source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an AWS EC2 source provider or Adding an OpenShift
Virtualization destination provider.
EBS CSI driver installed and configured on the target cluster.
Storage classes configured to use the EBS CSI driver.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
158

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select the AWS EC2 source provider from the list.
Target provider: Select the OpenShift Virtualization destination provider from the list.
Source storage: Select the EBS volume type from the list.
Target storage: Select a storage class that uses the EBS CSI driver from the list.
4. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
5. Click Create.
Your map appears in the list of storage maps.
16.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
Storage maps define the mapping between AWS EBS volume types and OpenShift storage classes that
use the EBS CSI driver.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
IMPORTANT
You must map EBS volumes to storage classes that use the AWS EBS CSI driver.
Prerequisites
Have an AWS EC2 source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an AWS EC2 source provider or Adding an OpenShift
Virtualization destination provider.
EBS CSI driver installed and configured on the target cluster.
Storage classes configured to use the EBS CSI driver.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
159

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
source:
id: <source_volume_type>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
storageClass: Specify a OpenShift Virtualization storage class that uses the AWS EBS CSI
driver.
id: Specify the EBS volume type, for example, gp2, gp3, or io1.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
16.5. ADDING AN AWS EC2 SOURCE PROVIDER
You can add an AWS EC2 source provider to migrate EC2 instances to OpenShift Virtualization on Red
Hat OpenShift Service on AWS (ROSA) or OpenShift Dedicated (OSD) on AWS.
IMPORTANT
Importing VMs from Amazon EC2 is a Technology Preview feature only. Technology
Preview features are not supported with Red Hat production service level agreements
(SLAs) and might not be functionally complete. Red Hat does not recommend using
them in production. These features provide early access to upcoming product features,
enabling customers to test functionality and provide feedback during the development
process.
For more information about the support scope of Red Hat Technology Preview features,
see Technology Preview Features Support Scope.
Prerequisites
AWS credentials with required Identity and Access Management (IAM) permissions. For more
160

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
AWS credentials with required Identity and Access Management (IAM) permissions. For more
information, see AWS EC2 prerequisites.
Elastic Block Store (EBS) Container Storage Interface (CSI) driver installed on the target
cluster.
Procedure
1. Access the Create provider page for AWS EC2 by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click Amazon EC2.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click Amazon EC2 in the Welcome pane, and
select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider.
AWS region: The AWS region where your EC2 instances are located, for example, us-east-1.
This must be the same region as your ROSA or OSD cluster.
3. Enter the provider credentials:
Access key ID: AWS access key ID for authenticating to the EC2 API.
Secret access key: AWS secret access key for authenticating to the EC2 API.
4. Configure target settings:
Auto-detect target settings: Select this checkbox to automatically fetch target AWS
credentials from the cluster and detect the target availability zone from worker nodes. This
option is selected by default.
Use cross-account credentials: Select this checkbox if the target AWS account is different
from the source account. When selected, you must provide the following:
Target access key ID: AWS access key ID for the target account.
Target secret access key: AWS secret access key for the target account.
5. Click Create provider to add and save the provider.
The provider appears in the list of providers.
NOTE
161

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
It might take a few minutes for the provider to move to the Ready status.
16.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
162

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
16.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
163

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
16.8. CREATING AN AWS EC2 MIGRATION PLAN BY USING THE MTV
WIZARD
You can migrate AWS EC2 instances to OpenShift Virtualization by using the Migration Toolkit for
Virtualization plan creation wizard to configure source and target providers, network and storage
mappings, and migration settings.
Limitations
MTV supports cold migration only. MTV does not support warm or live migrations from EC2.
EC2 instances must be stopped before migration begins.
MTV supports Red Hat Enterprise Linux (RHEL) guest operating systems only. MTV does
not support migration of instances running Windows, Amazon Linux, or other non-RHEL
operating systems.
MTV supports Red Hat OpenShift Service on AWS (ROSA) and OpenShift Dedicated (OSD)
on AWS clusters as migration targets only. MTV does not support migration to other
OpenShift platforms.
EC2 instances must be in the same AWS region as the target ROSA or OSD cluster. MTV
does not support cross-region migration.
MTV maps Elastic Block Store (EBS) volumes to EBS-backed storage classes only.
A plan cannot contain more than 500 virtual machines (VMs) or 500 disks.
IMPORTANT
When you click Create plan on the Review and create page of the wizard, Migration
Toolkit for Virtualization (MTV) validates your plan. If everything is OK, the Plan details
page for your plan opens. This page contains settings that do not appear in the wizard,
but are important. Be sure to read and follow the instructions for this page carefully, even
though it is outside the plan creation wizard. You can open this page later, any time
before you run the plan, so you can come back to it if needed.
164

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
Prerequisites
Have an AWS EC2 source provider and an OpenShift Virtualization destination provider. For
more information, see Adding an AWS EC2 source provider or Adding an OpenShift
Virtualization destination provider.
To create a Network map or a Storage map for use with multiple migration plans, create it in
the Network maps or Storage maps page of the UI before you create a migration plan.
Stop all EC2 instances you want to migrate.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select the AWS EC2 source provider from the list.
Target provider: Select the OpenShift Virtualization destination provider from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create project.
4. Click Next.
5. On the Virtual machines page, select the EC2 instances you want to migrate and click Next.
Only stopped EC2 instances appear in the list. Running instances cannot be migrated.
6. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These network maps are available for all plans and are ownerless in terms of the system. If
you select this option and choose a map, MTV attaches a copy of that map to your plan, and
your plan becomes the owner of that copy. Any changes you make to your copy do not
affect the original plan or any copies that other users have.
NOTE
165

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. MTV attaches this map to this plan, which then becomes its owner. Maps that
you create using this option are not available in the Use an existing network map option
because each has an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select the AWS subnet ID from the list.
Target network: Select the OpenShift network from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
7. Click Next.
8. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These storage maps are available for all plans and are ownerless in terms of the system. If
you select this option and choose a map, MTV attaches a copy of that map to your plan, and
your plan becomes the owner of that copy. Any changes you make to your copy do not
affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. MTV attaches these maps to this plan, which then becomes their owner.
Maps that you create using this option are not available in the Use an existing storage map
option because each has an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
IMPORTANT
For AWS EC2 migrations, you must map EBS volumes to storage classes that
use the AWS EBS Container Storage Interface (CSI) driver.
166

CHAPTER 16. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM AWS EC2
Source storage: Select the EBS volume type from the list.
Target storage: Select a storage class that uses the EBS CSI driver from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
9. Click Next.
10. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
11. Click Next.
12. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
13. To add a hook, select the appropriate Enable hook checkbox.
14. Enter the Hook runner image.
15. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
16. Click Next.
17. On the Review and create page, review the information displayed.
18. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
19. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
167

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
20. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
21. After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 16.1. Tabs of the Plan details page
Tab Description
YAML Editable YAML Plan manifest based on your plan’s details including source
provider, network and storage maps, VMs, and any issues with your VMs
Virtual Machines The VMs the plan migrates
Resources Calculated resources: VMs, CPUs, and total memory for both total VMs and
running VMs
Mappings Editable specification of the network and storage maps used by your plan
Hooks Updatable specification of the hooks used by your plan, if any
Additional resources
Technology Preview Features Support Scope
168

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL
MACHINES FROM OPENSHIFT VIRTUALIZATION
Create an OpenShift Virtualization migration plan by setting up network maps, configuring source and
destination providers with migration networks, and defining the migration plan in the Migration Toolkit
for Virtualization (MTV) UI.
17.1. CREATING OWNERLESS NETWORK MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless network maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing network map
option in the Network map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenShift Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding an OpenShift Virtualization source provider or
Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with form.
3. Specify the following:
Network map name: Name of the network map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source network: Select from the list.
Target network: Select from the list.
4. Optional: Click Add mapping to create additional network maps, including mapping multiple
network sources to a single target network.
5. Click Create.
Your map appears in the list of network maps.
17.2. CREATING OWNERLESS NETWORK MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
Add ownerless network maps by using YAML or JSON definitions to map source networks to OpenShift
Virtualization networks. Then add these maps to a migration plan using the wizard.
169

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenShift Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding an OpenShift Virtualization source provider or
Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Network maps.
2. Click Create network map > Create with YAML.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
name: <network_map>
namespace: <namespace>
spec:
map:
- destination:
name: <network_name>
type: pod
source:
name: <network_name>
type: pod
- destination:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
source:
name: <network_attachment_definition>
namespace: <network_attachment_definition_namespace>
type: multus
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
type: Allowed values are pod and multus.
<network_attachment_definition>: Specify a network attachment definition for each
additional OpenShift Virtualization network. Specify the namespace either by using the
namespace property or with a name built as follows:
170

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
<network_namespace>/<network_name>.
<network_attachment_definition_namespace>: Required only when type is multus.
Specify the namespace of the OpenShift Virtualization network attachment definition.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of network maps.
17.3. CREATING OWNERLESS STORAGE MAPS BY USING THE FORM
PAGE OF THE MTV UI
You can add ownerless storage maps by using the form page of the Migration Toolkit for Virtualization
(MTV) UI. Later, you can add these maps to a migration plan by using the Use an existing storage map
option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenShift Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding an OpenShift Virtualization source provider or
Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with form.
3. Specify the following:
Map name: Name of the storage map.
Project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Source storage: Select from the list.
Target storage: Select from the list.
4. Optional: Click Add mapping to create additional storage maps, including mapping multiple
storage sources to a single target storage class.
5. Click Create.
Your map appears in the list of storage maps.
17.4. CREATING OWNERLESS STORAGE MAPS BY USING YAML OR
JSON DEFINITIONS IN THE MTV UI
171

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
You can add ownerless storage maps by using YAML or JSON definitions in the YAML page of the
Migration Toolkit for Virtualization (MTV) UI. Later, you can add these maps to a migration plan by using
the Use an existing storage map option in the Storage map page of the MTV wizard.
For more information about network and storage maps in MTV, see Mapping networks and storage in
migration plans.
Prerequisites
Have an OpenShift Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding an OpenShift Virtualization source provider or
Adding an OpenShift Virtualization destination provider.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Storage maps.
2. Click Create storage map > Create with YAML.
The Create StorageMap page opens.
3. Enter the YAML or JSON definitions into the editor, or drag and drop a file into the editor.
4. If you enter YAML definitions, use the following:
$ cat << EOF | oc apply -f -
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
name: <storage_map>
namespace: <namespace>
spec:
map:
- destination:
storageClass: <storage_class>
accessMode: <access_mode>
source:
name: <storage_class>
provider:
source:
name: <source_provider>
namespace: <namespace>
destination:
name: <destination_provider>
namespace: <namespace>
EOF
accessMode: Allowed values are ReadWriteOnce and ReadWriteMany.
5. Optional: To download your input, click Download.
6. Click Create.
Your map appears in the list of storage maps.
17.5. ADDING A RED HAT OPENSHIFT VIRTUALIZATION SOURCE
172

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
17.5. ADDING A RED HAT OPENSHIFT VIRTUALIZATION SOURCE
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate VMs from the local cluster (where MTV is deployed) to a remote cluster, or from a remote
cluster to the local cluster.
NOTE
The Red Hat OpenShift cluster version of the source provider must be 4.16 or later.
Procedure
1. Access the Create provider page for OpenShift Virtualization by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
Provider resource name: Name of the source provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
173

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
5. Optional: Add access to the UI of the provider:
a. On the Providers page, click the provider.
The Provider details page opens.
b. Click the Edit icon under External UI web link.
c. Enter the link and click Save.
NOTE
If you do not enter a link, MTV attempts to calculate the correct link.
If MTV succeeds, the hyperlink of the field points to the calculated link.
If MTV does not succeed, the field remains empty.
17.6. ADDING AN OPENSHIFT VIRTUALIZATION DESTINATION
PROVIDER
You can use a Red Hat OpenShift Virtualization provider as both source and destination provider. You
can migrate virtual machines (VMs) from the local cluster (where MTV is deployed) to a remote cluster,
or from a remote cluster to the local cluster.
Prerequisites
You must have an OpenShift Virtualization service account token with cluster-admin privileges.
Procedure
1. Access the Create OpenShift Virtualization provider page by doing one of the following:
From the Providers page: In the Red Hat OpenShift web console, click Migration for
Virtualization > Providers, click Create Provider, select a Project from the list, and then
click OpenShift Virtualization.
From the Overview page (Administrators only): In the Red Hat OpenShift web console,
click Migration for Virtualization > Overview, click OpenShift Virtualization in the
Welcome pane, and select a Project from the list.
NOTE
If the Welcome pane is not visible, click Show the welcome card in the
upper-right corner of the page.
The default project depends on the active MTV project. If All projects is active, the default
is openshift-mtv. Administrators can view all projects; authorized non-administrators see
only their assigned projects.
2. Enter the provider details:
174

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
Provider resource name: Name of the destination provider
URL: URL of the endpoint of the API server
Service account bearer token: Token for a service account with cluster-admin privileges
If both URL and Service account bearer token are left blank, the local OpenShift cluster is
used.
3. Choose one of the following options for validating CA certificates:
Use a custom CA certificate: Keep Skip certificate validation toggled left and provide the
certificate:
Upload file: Drag the certificate to the text box, or click Browse and click Select.
Fetch from URL: Click Fetch certificate from URL, select I trust the authenticity of
this certificate, and click Confirm.
Use the system CA certificate: Keep Skip certificate validation toggled left and leave the
CA certificate text box empty.
Skip certificate validation: Toggle Skip certificate validation to the right.
4. Click Create provider to add and save the provider.
The provider appears in the list of providers.
17.7. SELECTING A MIGRATION NETWORK FOR AN OPENSHIFT
VIRTUALIZATION PROVIDER
You can select a default migration network for an OpenShift Virtualization provider in the Red Hat
OpenShift web console to improve performance. The default migration network is used to transfer disks
to the namespaces in which it is configured.
After you select a transfer network, associate its network attachment definition (NAD) with the gateway
to be used by this network.
In MTV version 2.9 and earlier, MTV used the pod network as the default network.
In version 2.10.0 and later, MTV detects if you have selected a user-defined network (UDN) as your
default network. Therefore, if you set the UDN to be the migration’s namespace, you do not need to
select a new default network when you create your migration plan.
Considerations
MTV supports using UDNs for migrations from all source providers except when the source
provider is also OpenShift Virtualization (for OpenShift-to-OpenShift migrations).
You can override the default migration network of the provider by selecting a different
network when you create a migration plan.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Providers.
2. Click the OpenShift Virtualization provider whose migration network you want to change.
175

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
When the Provider details page opens:
3. Click the Networks tab.
4. Click Set default transfer network.
5. Select a default transfer network from the list and click Save.
6. Configure a gateway in the network used for MTV migrations by completing the following steps:
a. In the Red Hat OpenShift web console, click Networking >
NetworkAttachmentDefinitions.
b. Select the appropriate default transfer network NAD.
c. Click the YAML tab.
d. Add forklift.konveyor.io/route to the metadata:annotations section of the YAML, as in the
following example:
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
name: localnet-network
namespace: mtv-test
annotations:
forklift.konveyor.io/route: <IP address>
The NetworkAttachmentDefinition parameter is needed to configure an IP address for
the interface, either from the Dynamic Host Configuration Protocol (DHCP) or
statically. Configuring the IP address enables the interface to reach the configured
gateway.
e. Click Save.
17.8. CREATING AN OPENSHIFT VIRTUALIZATION MIGRATION PLAN
BY USING THE MTV WIZARD
You can migrate OpenShift Virtualization virtual machines (VMs) by using the Migration Toolkit for
Virtualization plan creation wizard.
The wizard is designed to lead you step-by-step in creating a migration plan.

WARNING
Do not include virtual machines with guest-initiated storage connections, such as
Internet Small Computer Systems Interface (iSCSI) connections or Network File
System (NFS) mounts. These require either additional planning before migration or
reconfiguration after migration.
This prevents concurrent disk access to the storage the guest points to.
176

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
IMPORTANT
A plan cannot contain more than 500 VMs or 500 disks.
IMPORTANT
When you click Create plan on the Review and create page of the wizard, Migration
Toolkit for Virtualization (MTV) validates your plan. If everything is OK, the Plan details
page for your plan opens. This page contains settings that do not appear in the wizard,
but are important. Be sure to read and follow the instructions for this page carefully, even
though it is outside the plan creation wizard. The page can be opened later, any time
before you run the plan, so you can come back to it if needed.
Prerequisites
Have an OpenShift Virtualization source provider and an OpenShift Virtualization destination
provider. For more information, see Adding an OpenShift Virtualization source provider or
Adding an OpenShift Virtualization destination provider.
If you plan to create a Network map or a Storage map that will be used by more than one
migration plan, create it in the Network maps or Storage maps page of the UI before you
create a migration plan that uses that map.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list.
Target provider: Select from the list.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
iii. Optional: Enter a Description of the project.
iv. Click Create Project.
4. Click Next.
177

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
5. On the Virtual machines page, select the virtual machines you want to migrate and click Next.
6. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
7. Click Next.
8. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
178

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
9. Click Next.
10. On the Other settings (optional) page, you have the option to change the Transfer network
of your migration plan.
The transfer network is the network used to transfer the VMs to OpenShift Virtualization. This is
the default transfer network of the provider.
Verify that the transfer network is in the selected target project.
To choose a different transfer network, select a different transfer network from the list.
Optional: To configure another OpenShift network in the OpenShift web console, click
Networking > NetworkAttachmentDefinitions.
To learn more about the different types of networks OpenShift supports, see Additional
Networks in OpenShift Container Platform.
To adjust the maximum transmission unit (MTU) of the OpenShift transfer network, you
must also change the MTU of the VMware migration network. For more information, see
Selecting a migration network for a VMware source provider .
11. Click Next.
12. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
13. To add a hook, select the appropriate Enable hook checkbox.
14. Enter the Hook runner image.
15. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
16. Click Next.
17. On the Review and create page, review the information displayed.
18. Edit any item by doing the following:
a. Click its Edit step link.
179

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
19. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
20. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
21. After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 17.1. Tabs of the Plan details page
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
NOTE
You can customize the names of persistent volume claims (PVCs) for migrated
VM disks by editing the YAML Plan manifest on the YAML tab and adding a
pvcNameTemplate field. For more information, see PVC name template
variables for OpenShift Virtualization-to-OpenShift Virtualization migrations.
17.8.1. PVC name template variables for OpenShift Virtualization-to-OpenShift
Virtualization migrations
You can use template variables to customize persistent volume claim (PVC) names for migrated VM
disks to satisfy storage policies, backup requirements, or organizational naming standards.
Templates use Go template syntax to define naming patterns for OpenShift Virtualization-to-
OpenShift Virtualization migrations.
You must ensure that PVC names are DNS-compliant: they must consist of lowercase alphanumeric
characters or hyphens (-), start with an alphanumeric character, and not exceed 63 characters. If the
180

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
template syntax is invalid or if the resulting PVC names are not DNS-compliant, MTV adds an error to
the plan conditions and prevents the migration from running.
17.8.1.1. Available variables
The following variables are available in the pvcNameTemplate field for OpenShift Virtualization-to-
OpenShift Virtualization migrations:
.VmName: Name of the VM in the source Red Hat OpenShift cluster.
.TargetVmName: Final VM name in the target cluster. May equal .VmName if no rename or
normalization occurs.
.PlanName: Name of the migration plan.
.DiskIndex: Sequential index of the disk (0-based, where the first disk is 0, the second is 1, and
so on).
.SourcePVCName: Original name of the PVC in the source cluster.
.SourcePVCNamespace: Namespace of the PVC in the source cluster.
17.8.1.2. Template functions
You can use Go template functions to transform variable values into valid PVC names. Common
functions include:
trunc: Truncates a string to a specified length. For example, ++{{++trunc 10 .PlanName}} limits
the plan name to 10 characters.
replace: Replaces all occurrences of a substring. For example, ++{{++.SourcePVCName |
replace "_" "-"}} replaces underscores with hyphens.
lower: Converts a string to lowercase. For example, ++{{++.VmName | lower}}.
You can chain functions together by using the pipe (|) operator. You can also use regular expression
functions such as mustRegexReplaceAll for advanced transformations.
For a complete list of available template functions, see MTV template utility.
17.8.1.3. Default behavior
If you do not specify a pvcNameTemplate, MTV preserves the original PVC name from the source
cluster: ++{{++.SourcePVCName}}.
NOTE
Unlike VMware migrations, OpenShift Virtualization-to-OpenShift Virtualization
migrations always use the template output as the exact PVC name. OpenShift
Virtualization-to-OpenShift Virtualization migrations ignore the
pvcNameTemplateUseGenerateName field.
17.8.1.4. Examples
181

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
The following examples show common PVC naming patterns. Use the trunc function to prevent
template output from exceeding the 63-character limit:
"{{.TargetVmName}}-{{.SourcePVCName}}" – Prefix the source PVC name with the target VM
name (for example, myvm-data-disk for a VM named myvm and PVC named data-disk)
"migrated-{{.SourcePVCName}}-{{.DiskIndex}}" – Add a migration prefix and disk index
(where 0 is the first disk)
"{{.TargetVmName}}-disk-{{.DiskIndex}}" – Use the target VM name with a disk index
"{{trunc 10 .PlanName}}-{{trunc 20 .TargetVmName}}-{{.DiskIndex}}" – Truncate the plan
and target VM names to prevent exceeding the 63-character limit
"{{.TargetVmName}}-{{.SourcePVCNamespace}}-{{.SourcePVCName}}" – Include source
namespace for clarity in multi-namespace migrations
17.8.2. Creating a migration plan for a live migration by using the MTV wizard
You create a migration plan for a live migration of virtual machines (VMs) almost exactly as you create a
migration plan for a cold migration. The only difference is that you specify it is a Live migration in the
Migration type page.
Prerequisites
As described in OpenShift Virtualization live migration prerequisites.
Procedure
1. In the Red Hat OpenShift web console, click Migration for Virtualization > Migration plans.
2. Click Create plan.
The Create migration plan wizard opens.
3. On the General page, specify the following fields:
Plan name: Enter a name.
Plan project: Select from the list.
Source provider: Select from the list. You can use any OpenShift Virtualization provider.
You do not need to create a new one for a live migration.
Target provider: Select from the list. Be sure to select the correct OpenShift Virtualization
target provider.
Target project: Click the list and do one of the following:
a. Select an existing project from the list.
b. Create a new project by clicking Create project and doing the following:
i. Enter the Name of the project. A project name must consist of lowercase
alphanumeric characters or -. A project name must start and end with alphanumeric
characters. For example, my-name or 123-abc.
ii. Optional: Enter a Display name for the project.
182

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
iii. Optional: Enter a Description of the project.
iv. Click Create project.
4. Click Next.
5. On the Virtual machines page, select the virtual machines you want to migrate and ensure they
are powered on. A live migration fails if any of its VMs are powered off.
6. Click Next.
7. On the Network map page, choose one of the following options:
Use an existing network map: Select an existing network map from the list.
These are network maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
If you select an existing map, be sure it has the same source provider and
target provider as the ones you want to use in your plan.
Use a new network map: Allows you to create a new network map by supplying the
following data. This map is attached to this plan, which is then considered to be its owner.
Maps that you create using this option are not available in the Use an existing network map
option because each is created with an owner.
NOTE
You can create an ownerless network map, which you and others can use for
additional migration plans, in the Network maps section of the UI.
Source network: Select from the list.
Target network: Select from the list.
If needed, click Add mapping to add another mapping.
Network map name: Enter a name or let MTV automatically generate a name for the
network map.
8. Click Next.
9. On the Storage map page, choose one of the following options:
Use an existing storage map: Select an existing storage map from the list.
These are storage maps available for all plans, and therefore, they are ownerless in terms of
the system. If you select this option and choose a map, a copy of that map is attached to
your plan, and your plan is the owner of that copy. Any changes you make to your copy do
not affect the original plan or any copies that other users have.
NOTE
183

Migration Toolkit for Virtualization 2.12 Planning your migration to Red Hat OpenShift Virtualization
NOTE
If you choose an existing map, be sure it has the same source provider and
the same target provider as the ones you want to use in your plan.
Use new storage map: Allows you to create one or two new storage maps by supplying the
following data. These maps are attached to this plan, which is then their owner. Maps that
you create using this option are not available in the Use an existing storage map option
because each is created with an owner.
NOTE
You can create an ownerless storage map, which you and others can use for
additional migration plans, in the Storage maps section of the UI.
Source storage: Select from the list.
Target storage: Select from the list.
If needed, click Add mapping to add another mapping.
Storage map name: Enter a name or let MTV automatically generate a name for the
storage map.
10. Click Next.
11. On the Migration type page, choose Live migration.
If Live migration does not appear as an option, return to the General page and verify that both
the source provider and target provider are OpenShift Virtualization clusters.
If they are both OpenShift Virtualization clusters, have someone with cluster-admin privileges
ensure that the prerequisites for live migration are met. For more information, see OpenShift
Virtualization live migration prerequisites.
12. Click Next.
13. On the Other settings (optional) page, click Next without doing anything else.
14. On the Hooks (optional) page, you can add a pre-migration hook, a post-migration hook, or
both types of migration hooks. All are optional.
15. To add a hook, select the appropriate Enable hook checkbox.
16. Enter the Hook runner image.
17. Enter the Ansible playbook of the hook in the window.
NOTE
You cannot include more than one pre-migration hook or more than one post-
migration hook in a migration plan.
18. Click Next.
19. On the Review and create page, review the information displayed.
184

CHAPTER 17. PLANNING A MIGRATION OF VIRTUAL MACHINES FROM OPENSHIFT VIRTUALIZATION
20. Edit any item by doing the following:
a. Click its Edit step link.
The wizard opens to the page where you defined the item.
b. Edit the item.
c. Either click Next to advance to the next page of the wizard, or click Skip to review to return
directly to the Review and create page.
21. When you finish reviewing the details of the plan, click Create plan. MTV validates your plan.
When your plan is validated, the Plan details page for your plan opens in the Details tab.
22. In addition to listing details based on your entries in the wizard, the Plan details tab includes the
following two sections after the details of the plan:
Migration history: Details about successful and unsuccessful attempts to run the plan
Conditions: Any changes that need to be made to the plan so that it can run successfully
23. After you resolve all listed conditions, you can run your plan from the Plans page.
The Plan details page also includes five additional tabs, which are described in the table that
follows:
Table 17.2. Tabs of the Plan details page
YAML Virtual Machines Resources Mappings Hooks
Editable YAML The VMs the plan Calculated Editable Updatable
Plan manifest migrates resources: VMs, specification of specification of
based on your CPUs, and total the network and the hooks used
plan’s details memory for both storage maps by your plan, if
including source total VMs and used by your any
provider, network running VMs plan
and storage
maps, VMs, and
any issues with
your VMs
185