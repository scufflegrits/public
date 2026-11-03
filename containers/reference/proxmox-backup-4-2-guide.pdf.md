| Proxmox | Backup | Documentation |         |         |
| ------- | ------ | ------------- | ------- | ------- |
|         |        |               | Release | 4.2.8‐1 |
|         |        | Proxmox       | Support | Team    |
Friday,02October2026

TABLE OF CONTENTS
1 Introduction 3
1.1 WhatisProxmoxBackupServer? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 MainFeatures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 ReasonsforDataBackup? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 SoftwareStack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6 GettingHelp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.1 EnterpriseSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.2 CommunitySupportForum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.3 MailingLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.4 BugTracker . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.7 License . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.8 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Installation 7
2.1 SystemRequirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 MinimumServerRequirements,forEvaluation . . . . . . . . . . . . . . . . . . 7
2.1.2 RecommendedServerSystemRequirements . . . . . . . . . . . . . . . . . . . 7
2.1.3 SupportedWebBrowsersforAccessingtheWebInterface . . . . . . . . . . . . 8
2.2 InstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.1 PrepareInstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.2 PrepareaUSBFlashDriveasInstallationMedium . . . . . . . . . . . . . . . . . 8
2.2.3 InstructionsforGNU/Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.4 InstructionsformacOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2.5 InstructionsforWindows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2.6 UsetheInstallationMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3 ServerInstallation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3.1 InstallProxmoxBackupServerusingtheInstaller . . . . . . . . . . . . . . . . . 10
2.3.2 InstallProxmoxBackupServerUnattended. . . . . . . . . . . . . . . . . . . . . 18
2.3.3 InstallProxmoxBackupServeronDebian. . . . . . . . . . . . . . . . . . . . . . 19
2.3.4 InstallProxmoxBackupServeronProxmoxVE . . . . . . . . . . . . . . . . . . . 19
2.4 ClientInstallation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.4.1 InstallProxmoxBackupClientonDebian . . . . . . . . . . . . . . . . . . . . . . 20
2.4.2 InstallStaticallyLinkedProxmoxBackupClient. . . . . . . . . . . . . . . . . . . 20
2.5 DebianPackageRepositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.5.1 RepositoryFormats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.5.2 DebianBaseRepositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.5.3 ProxmoxBackupEnterpriseRepository . . . . . . . . . . . . . . . . . . . . . . . 21
2.5.4 ProxmoxBackupNo-SubscriptionRepository . . . . . . . . . . . . . . . . . . . 22
2.5.5 ProxmoxBackupTestRepository . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.5.6 ProxmoxBackupDebugSymbolRepository . . . . . . . . . . . . . . . . . . . . 22
2.5.7 ProxmoxBackupClient-onlyRepository . . . . . . . . . . . . . . . . . . . . . . . 23
2.5.8 SecureApt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.5.9 RepositoryAccessBehindHTTPProxy . . . . . . . . . . . . . . . . . . . . . . . . 24
i

3 Terminology 25
3.1 BackupContent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.1.1 ImageArchives: <name>.img . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.1.2 FileArchives: <name>.pxar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.1.3 BinaryData(BLOBs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.1.4 CatalogFile: catalog.pcat1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.1.5 TheManifest: index.json . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.2 BackupNamespace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.3 BackupType . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.4 BackupID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.5 BackupTime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.6 BackupGroup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.7 BackupSnapshot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4 GraphicalUserInterface 27
4.1 Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2 Login . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.1 ConsentBanner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.3 GUIOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4 Sidebar. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.1 Dashboard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.2 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.3 Administration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.4 TapeBackup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.4.5 Datastore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5 BackupStorage 33
5.1 DiskManagement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5.2 Datastore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.2.1 DatastoreConfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
5.2.2 BackupNamespaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.2.3 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.3 RansomwareProtection&Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.3.1 Built-inProtection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.3.2 The3-2-1RulewithProxmoxBackupServer . . . . . . . . . . . . . . . . . . . . 45
5.3.3 RestrictiveUser&AccessManagement . . . . . . . . . . . . . . . . . . . . . . . 45
5.3.4 RansomwareDetection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.3.5 GeneralPreventionMethodsandBestPractices . . . . . . . . . . . . . . . . . . 46
6 UserManagement 47
6.1 UserConfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.2 APITokens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6.3 AccessControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.3.1 Privileges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.3.2 AccessRoles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.3.3 ObjectsandPaths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.3.4 Configuration&Management. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.3.5 APITokenPermissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.3.6 EffectivePermissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.4 Two-FactorAuthentication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.4.2 AvailableSecondFactors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6.4.3 Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6.4.4 TFAandAutomatedAccess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
6.4.5 LimitsandLockoutofTwo-FactorAuthentication . . . . . . . . . . . . . . . . . 56
6.5 AuthenticationRealms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.5.1 LinuxPAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.5.2 ProxmoxBackupauthenticationserver . . . . . . . . . . . . . . . . . . . . . . . 57
6.5.3 LDAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
ii

6.5.4 ActiveDirectory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7 BackupClientUsage 59
7.1 BackupRepositoryLocations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
7.2 StaticallyLinkedBackupClient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
7.3 EnvironmentVariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
7.4 SystemandServiceCredentials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
7.5 OutputFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
7.6 CreatingBackups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
7.6.1 ExcludingFiles/DirectoriesfromaBackup. . . . . . . . . . . . . . . . . . . . . . 64
7.6.2 ChangeDetectionMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.7 Encryption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.7.1 UsingaMasterKeytoStoreandRecoverEncryptionKeys . . . . . . . . . . . . 66
7.8 RestoringData . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
7.8.1 InteractiveRestores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.8.2 MountingofArchivesviaFUSE . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.9 LoginandLogout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.10 ChangingtheOwnerofaBackupGroup . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.11 PruningandRemovingBackups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
7.12 GarbageCollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
7.13 Benchmarking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8 ProxmoxVEIntegration 75
8.1 UsingtheProxmoxVEWeb-Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.2 UsingtheProxmoxVECommandLine . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
9 pxarCommand-lineTool 77
9.1 CreatinganArchive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
9.2 ExtractinganArchive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
9.3 ListtheContentsofanArchive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
9.4 MountinganArchive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
10 TapeBackup 79
10.1 TapeTechnologyPrimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
10.2 SupportedHardware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
10.2.1 DrivePerformance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
10.2.2 LTO-9+considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
10.3 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
10.4 TapeQuickStart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
10.5 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
10.5.1 Tapechangers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
10.5.2 Tapedrives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
10.5.3 MediaPools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
10.5.4 TapeBackupJobs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.6 Administration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
10.6.1 LabelTapes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
10.6.2 RunTapeBackups. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.6.3 RestorefromTape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.6.4 UpdateInventory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.6.5 RestoreCatalog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.6.6 EncryptionKeyManagement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
10.6.7 TapeCleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.7 WORMTapes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.8 ExampleSetups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.8.1 SingleContinuedMediaSet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.8.2 WeekdayScheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.8.3 MultiplePoolswithDifferentPolicies . . . . . . . . . . . . . . . . . . . . . . . . 97
10.9 DisasterRecovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.9.1 SettingUpaDatastore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
iii

10.9.2 SettingUptheTapeDrive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.9.3 RestoringDataFromtheTape. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
11 ManagingRemotes&Sync 101
11.1 Remote . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
11.2 SyncJobs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
11.2.1 NamespaceSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.2.2 BandwidthLimit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.2.3 SyncDirectionPush . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.2.4 ServerSideEncryption/DecryptionDuringSync . . . . . . . . . . . . . . . . . . 106
12 MaintenanceTasks 107
12.1 Pruning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
12.1.1 PruneSimulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
12.1.2 PruneJobs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
12.1.3 ManualPruning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
12.1.4 RetentionSettingsExample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
12.2 GarbageCollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
12.2.1 GCBackground . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
12.2.2 ManuallyStartingGC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.2.3 ScheduledGC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.3 Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
12.4 Notifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
12.5 MaintenanceMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
13 HostSystemAdministration 115
13.1 ZFSonLinux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
13.1.1 Hardware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
13.1.2 ZFSAdministration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
13.2 HostBootloader . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
13.2.1 PartitioningSchemeUsedbytheInstaller . . . . . . . . . . . . . . . . . . . . . . 121
13.2.2 SynchronizingtheContentoftheESPwithproxmox-boot-tool . . . . . . . 121
13.2.3 DeterminewhichBootloaderisUsed . . . . . . . . . . . . . . . . . . . . . . . . 124
13.2.4 Grub . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.2.5 Systemd-boot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.2.6 EditingtheKernelCommandline . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.2.7 OverridetheKernel-VersionfornextBoot . . . . . . . . . . . . . . . . . . . . . 126
13.2.8 SecureBoot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
13.3 CertificateManagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
13.3.1 CertificatesfortheAPIandSMTP . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
13.3.2 UploadCustomCertificate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
13.3.3 TrustedcertificatesviaLet’sEncrypt(ACME) . . . . . . . . . . . . . . . . . . . . 130
13.3.4 ACMEHTTPChallengePlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
13.3.5 ACMEDNSAPIChallengePlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
13.3.6 AutomaticrenewalofACMEcertificates . . . . . . . . . . . . . . . . . . . . . . . 133
13.3.7 ManuallyChangeCertificateovertheCommandLine . . . . . . . . . . . . . . . 133
13.4 ExternalMetricServer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
13.4.1 InfluxDB(HTTP)pluginconfiguration . . . . . . . . . . . . . . . . . . . . . . . . 134
13.4.2 InfluxDB(UDP)pluginconfiguration . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.5 ServiceDaemons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.5.1 proxmox-backup-proxy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.5.2 proxmox-backup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6 Command-lineTools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6.1 proxmox-backup-client . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6.2 proxmox-backup-manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6.3 proxmox-tape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6.4 pmt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
13.6.5 pmtx . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
13.6.6 pxar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
iv

13.6.7 proxmox-file-restore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
13.6.8 proxmox-backup-debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
14 NetworkManagement 139
14.1 TrafficControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
14.2 Overridingnetworkdevicenames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
15 Notifications 145
15.1 Overview. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
15.2 NotificationTargets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
15.2.1 Sendmail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
15.2.2 SMTP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
15.2.3 Gotify . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
15.2.4 Webhook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
15.3 NotificationMatchers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
15.3.1 CalendarMatchingRules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
15.3.2 FieldMatchingRules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
15.3.3 SeverityMatchingRules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
15.4 NotificationEvents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
15.5 SystemMailForwarding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
15.6 Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
15.7 NotificationMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
15.7.1 Settingsforlegacy-sendmailnotificationmode . . . . . . . . . . . . . . . . 150
15.8 OverridingNotificationTemplates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
15.9 NotificationThresholdsandResetSchedule(S3DatastoresOnly) . . . . . . . . . . . . 151
16 TechnicalOverview 153
16.1 Datastores. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
16.2 Snapshots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
16.3 Chunks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
16.3.1 Fixed-SizedChunks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
16.3.2 DynamicallySizedChunks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
16.3.3 EncryptedChunks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
16.3.4 ChangeDetectionModeforFile-BasedBackups . . . . . . . . . . . . . . . . . . 155
16.4 CaveatsandLimitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
16.4.1 NotesonHashCollisions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
16.4.2 File-BasedBackup. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
16.4.3 VerificationofEncryptedChunks . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
16.5 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
16.5.1 RestorewithoutaRunningProxmoxBackupServer . . . . . . . . . . . . . . . . 158
17 FAQ 159
17.1 WhatdistributionisProxmoxBackupServer(PBS)basedon? . . . . . . . . . . . . . . 159
17.2 Whichplatformsaresupportedasabackupsource(client)? . . . . . . . . . . . . . . . 159
17.3 WillProxmoxBackupServerrunona32-bitprocessor? . . . . . . . . . . . . . . . . . . 159
17.4 HowlongwillmyProxmoxBackupServerversionbesupported? . . . . . . . . . . . . 159
17.5 HowcanIupgradeProxmoxBackupServertothenextpointrelease? . . . . . . . . . 159
17.6 HowcanIupgradeProxmoxBackupServertothenextmajorrelease? . . . . . . . . . 160
17.7 CanIcopyorsynchronizemydatastoretoanotherlocation? . . . . . . . . . . . . . . . 160
17.8 CanProxmoxBackupSerververifydataintegrityofabackuparchive? . . . . . . . . . 160
17.9 Whenbackinguptoremoteservers,doIhavetotrusttheremoteserver? . . . . . . . 160
17.10Isthebackupincremental/deduplicated/full? . . . . . . . . . . . . . . . . . . . . . . . . 161
A CommandSyntax 163
A.1 proxmox-backup-client . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
A.1.1 CatalogShellCommands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
A.2 proxmox-backup-manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
A.3 proxmox-tape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
A.4 pmt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
v

A.5 pmtx . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
A.6 pxar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
A.7 proxmox-file-restore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
A.8 proxmox-backup-debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
B ConfigurationFiles 263
B.1 acl.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
B.1.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
B.1.2 Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
B.2 datastore.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
B.2.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
B.2.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
B.3 domains.cfg. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
B.3.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
B.3.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
B.4 media-pool.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
B.4.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
B.4.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
B.5 node.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
B.5.1 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
B.6 notifications.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
B.6.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
B.6.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
B.7 notifications-priv.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
B.7.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
B.7.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
B.8 prune.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
B.8.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
B.8.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
B.9 tape.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
B.9.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
B.9.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
B.10 tape-job.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
B.10.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
B.10.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
B.11 user.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
B.11.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
B.11.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
B.12 remote.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
B.12.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
B.12.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
B.13 sync.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
B.13.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
B.13.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
B.14 verification.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
B.14.1 FileFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
B.14.2 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
C FileFormats 283
C.1 ProxmoxFileArchiveFormat(.pxar) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
C.2 ProxmoxFileArchiveFormat-Meta(.mpxar) . . . . . . . . . . . . . . . . . . . . . . . . 283
C.3 ProxmoxFileArchiveFormat-Payload(.ppxar) . . . . . . . . . . . . . . . . . . . . . . 284
C.4 ProxmoxCatalogFileFormat(.pcat1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
C.4.1 CatalogDataTables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
C.4.2 CatalogTableEntries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
C.4.3 EntryTypes: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
C.4.4 VariableLengthEncoding: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
C.5 DataBlobFormat(.blob) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
vi

C.6 FixedIndexFormat(.fidx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
C.7 DynamicIndexFormat(.didx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
D BackupProtocol 289
D.1 BackupProtocolAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
D.1.1 UploadBlobs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
D.1.2 UploadChunks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
D.1.3 UploadFixedIndexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
D.1.4 UploadDynamicIndexes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
D.1.5 FinishBackup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
D.2 Restore/ReaderProtocolAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
D.2.1 DownloadBlobs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
D.2.2 DownloadChunks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
D.2.3 DownloadIndexFiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
E CalendarEvents 293
E.1 IntroductionandFormat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
E.2 Differencestosystemd . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
E.3 NotesonScheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
F MarkdownPrimer 295
F.1 MarkdownBasics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
F.1.1 Headings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
F.1.2 Emphasis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
F.1.3 Links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
F.1.4 Lists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
F.1.5 Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
F.1.6 BlockQuotes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
F.1.7 CodeandSnippets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
G Glossary 299
H GNUFreeDocumentationLicense 301
Index 307
vii

viii

ProxmoxBackupDocumentation,Release4.2.8‐1
Copyright(C)2019-2025,ProxmoxServerSolutionsGmbH
Version4.2.8--Friday,02October2026
Permissionisgrantedtocopy,distributeand/ormodifythisdocumentunderthetermsoftheGNU
FreeDocumentationLicense,Version1.3oranylaterversionpublishedbytheFreeSoftwareFoun-
dation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
licenseisincludedinthesectionentitled”GNUFreeDocumentationLicense”.
TABLEOFCONTENTS 1

ProxmoxBackupDocumentation,Release4.2.8‐1
2 TABLEOFCONTENTS

CHAPTER
ONE
INTRODUCTION
1.1 What is Proxmox Backup Server?
ProxmoxBackupServerisanenterprise-class,client-serverbackupsolutionthatiscapableofback-
ing up virtual machines, containers, and physical hosts. It is specially optimized for the Proxmox
VirtualEnvironmentplatformandallowsyoutobackupyourdatasecurely,evenbetweenremote
sites,providingeasymanagementthroughaweb-baseduserinterface.
It supports deduplication, compression, and authenticated encryption (AE). Using Rust as the im-
plementationlanguageguaranteeshighperformance,lowresourceusage,andasafe,high-quality
codebase.
Proxmox Backup uses state of the art cryptography for both client-server communication and
backupcontentencryption. Allclient-servercommunicationusesTLS,andbackupdatacanbeen-
crypted on the client-side before sending, making it safer to back up data to targets that are not
fullytrusted.
1.2 Architecture
ProxmoxBackupServerusesaclient-servermodel. Theserverstoresthebackupdataandprovides
anAPItocreateandmanagedatastores. WiththeAPI,it’salsopossibletomanagedisksandother
server-sideresources.
The backup client uses this API to access the backed up data. You can use the
proxmox-backup-clientcommand-linetooltocreateandrestorefilebackups. ForQEMUand
LXCwithinProxmoxVirtualEnvironment,wedeliveranintegratedclient.
A single backup is allowed to contain several archives. For example, when you backup a virtual
machine,eachdiskisstoredasaseparatearchiveinsidethatbackup. TheVMconfigurationitself
isstoredasanextrafile. Thisway, it’seasytoaccessandrestoreonlytheimportantpartsofthe
backup,withouttheneedtoscanthewholebackup.
1.3 Main Features
SupportforProxmoxVE
The Proxmox Virtual Environment is fully supported, and you can easily backup
virtualmachinesandcontainers.
Performance
The whole software stack is written in Rust, in order to provide high speed and
memoryefficiency.
Deduplication
Periodicbackupsproducelargeamountsofduplicatedata. Thededuplicationlayer
avoidsredundancyandminimizesthestoragespaceused.
3

ProxmoxBackupDocumentation,Release4.2.8‐1
Incrementalbackups
Changes between backups are typically low. Reading and sending only the delta
reducesthestorageandnetworkimpactofbackups.
Dataintegrity
Thebuilt-inSHA-256checksumalgorithmensuresaccuracyandconsistencyinyour
backups.
Remotesync
Itispossibletoefficientlysynchronizedatatoremotesites. Onlydeltascontaining
newdataaretransferred.
Compression
Theultra-fastZstandardcompressionisabletocompressseveralgigabytesofdata
persecond.
Encryption
Backups can be encrypted on the client-side, using AES-256 GCM. This authenti-
catedencryption(AE)modeprovidesveryhighperformanceonmodernhardware.
Inadditiontoclient-sideencryption,alldataistransferredviaasecureTLSconnec-
tion.
Tapebackup
For long-term archiving of data, Proxmox Backup Server also provides extensive
supportforbackinguptotapeandmanagingtapelibraries.
Ransomwareprotection
ProtectyourcriticaldatafromransomwareattackswithProxmoxBackupServer’sfine-
grained access control, data integrity verification, and off-site backup through re-
motesyncandtapebackup.
Webinterface
ManagetheProxmoxBackupServerwiththeintegrated,web-baseduserinterface.
Opensource
Nosecrets. ProxmoxBackupServerisfreeandopen-sourcesoftware. Thesource
codeislicensedunderAGPL,v3.
Nolimits
ProxmoxBackupServerhasnoartificiallimitsforbackupstorageorbackup-clients.
Enterprisesupport
ProxmoxServerSolutionsGmbHoffersenterprisesupportintheformofProxmox
Backup Server Subscription Plans. Users at every subscription level get access to
the Proxmox Backup Enterprise Repository. In addition, with a Basic, Standard or
Premiumsubscription,usershaveaccesstotheProxmoxCustomerPortal.
1.4 Reasons for Data Backup?
The main purpose of a backup is to protect against data loss. Data loss can be caused by both
faultyhardwareandhumanerror.
Acommonmistakeistoaccidentallydeleteafileorfolderwhichisstillrequired. Virtualizationcan
evenamplifythisproblem,asdeletingawholevirtualmachinecanbeaseasyaspressingasingle
button.
Foradministrators,backupscanserveasausefultoolkitfortemporarilystoringdata. Forexample,
itiscommonpracticetoperformfullbackupsbeforeinstallingmajorsoftwareupdates. Ifsome-
thinggoeswrong,youcaneasilyrestorethepreviousstate.
Anotherreasonforbackupsarelegalrequirements. Somedata,especiallybusinessrecords,must
bekeptinasafeplaceforseveralyearsbylaw,sothattheycanbeaccessedifrequired.
4 Chapter1. Introduction

ProxmoxBackupDocumentation,Release4.2.8‐1
Ingeneral,datalossisverycostlyasitcanseverelydamageyourbusiness. Therefore,ensurethat
youperformregularbackupsandrunrestoretests.
1.5 Software Stack
ProxmoxBackupServerconsistsofmultiplecomponents:
• A server-daemon providing, among other things, a RESTful API, super-fast asynchronous
tasks,lightweightusagestatisticcollection,schedulingevents,strictseparationofprivileged
andunprivilegedexecutionenvironments
• AJavaScriptmanagementwebinterface
• AmanagementCLItoolfortheserver(proxmox-backup-manager)
• AclientCLItool(proxmox-backup-client)toaccesstheservereasilyfromanyLinuxamd64en-
vironment
Aside from the web interface, most parts of Proxmox Backup Server are written in the Rust pro-
gramminglanguage.
”TheRustprogramminglanguagehelpsyouwritefaster,morereliablesoftware. High-
levelergonomicsandlow-levelcontrolareoftenatoddsinprogramminglanguagede-
sign;Rustchallengesthatconflict. Throughbalancingpowerfultechnicalcapacityanda
greatdeveloperexperience,Rustgivesyoutheoptiontocontrollow-leveldetails(such
asmemoryusage)withoutallthehassletraditionallyassociatedwithsuchcontrol.”
—TheRustProgrammingLanguage
1.6 Getting Help
1.6.1 EnterpriseSupport
UserswithaProxmoxBackupServerBasic,StandardorPremiumSubscriptionPlanhaveaccessto
the Proxmox Customer Portal. The customer portal provides support with guaranteed response
timesfromtheProxmoxdevelopers. Formoreinformationorforvolumediscounts,pleasecontact
sales@proxmox.com.
1.6.2 CommunitySupportForum
WealwaysencourageouruserstodiscussandsharetheirknowledgeusingtheProxmoxCommu-
nityForum. TheforumismoderatedbytheProxmoxsupportteam. Thelargeuserbaseisspread
outallovertheworld. Needlesstosaythatsuchalargeforumisagreatplacetogetinformation.
1.6.3 MailingLists
ProxmoxBackup Serverisfullyopen-sourceandcontributionsarewelcome! Hereistheprimary
communicationchannelfordevelopers:
Mailinglistfordevelopers
ProxmoxBackupServerDevelopmentList
1.6.4 BugTracker
Proxmoxrunsapublicbugtrackerathttps://bugzilla.proxmox.com. Ifanissueappears, fileyour
reportthere. Anissuecanbeabug, aswellasarequestforanewfeatureorenhancement. The
bugtrackerhelpstokeeptrackoftheissueandwillsendanotificationonceithasbeensolved.
1.5. SoftwareStack 5

ProxmoxBackupDocumentation,Release4.2.8‐1
1.7 License
Copyright(C)2019-2025,ProxmoxServerSolutionsGmbH
ThissoftwareiswrittenbyProxmoxServerSolutionsGmbH<support@proxmox.com>
Proxmox Backup Server is free and open source software: you can use it, redistribute it, and/or
modifyitunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedbytheFreeSoft-
wareFoundation,eitherversion3oftheLicense,or(atyouroption)anylaterversion.
Thisprogramisdistributedinthehopethatitwillbeuseful,butWITHOUT ANY WARRANTY;without
eventheimpliedwarrantyofMERCHANTABILITYorFITNESS FOR A PARTICULAR PURPOSE.See
theGNUAfferoGeneralPublicLicenseformoredetails.
YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicensealongwiththisprogram.
Ifnot,seeAGPL3.
1.8 History
Backup is, and always has been, a central aspect of IT administration. The need to recover from
datalossisfundamentalandonlyincreaseswithvirtualization.
For this reason, we’ve been shipping a backup tool with Proxmox VE, from the beginning. This
tooliscalledvzdumpandisabletomakeconsistentsnapshotsofrunningLXCcontainersandKVM
virtualmachines.
However, vzdump only allows for full backups. While this is fine for small backups, it becomes a
burdenforuserswithlargeVMs. Bothbackupdurationandstorageusagearetoohighforthiscase,
especiallyforuserswhowanttokeepmanybackupsofthesameVMs. Tosolvetheseproblems,
weneededtoofferdeduplicationandincrementalbackups.
BackinOctober2018,developmentstarted. Weinvestigatedseveraltechnologiesandframeworks
andfinallydecidedtouseRustastheimplementationlanguage,inordertoprovidehighspeedand
memoryefficiency. The2018-editionofRustseemedpromisingforourrequirements.
In July 2020, we released the first beta version of Proxmox Backup Server, followed by the first
stableversioninNovember2020. Withsupportforencryptionandincremental,fullydeduplicated
backups,ProxmoxBackupoffersasecureenvironment,whichsignificantlyreducesnetworkload
andsavesvaluablestoragespace.
6 Chapter1. Introduction

CHAPTER
TWO
INSTALLATION
ProxmoxBackupissplitintoaserverandclientpart. Theserverpartcaneitherbeinstalledwitha
graphicalinstallerorontopofDebianfromtheprovidedpackagerepository.
2.1 System Requirements
WerecommendusinghighqualityserverhardwarewhenrunningProxmoxBackupServerinpro-
duction. To further decrease the impact of a failed host, you can set up periodic, efficient, incre-
mentaldatastoresynchronizationfromotherProxmoxBackupServerinstances.
2.1.1 MinimumServerRequirements,forEvaluation
Theseminimumrequirementsareforevaluationpurposesonlyandshouldnotbeusedinproduc-
tion.
• CPU:64bit(x86-64orAMD64),2+Cores
• Memory(RAM):2GBRAM
• Harddrive: morethan8GBofspace.
• Networkcard(NIC)
2.1.2 RecommendedServerSystemRequirements
• CPU:ModernAMDorIntel64-bitbasedCPU,withatleast4cores
• Memory: minimum4GiBfortheOS,filesystemcacheandProxmoxBackupServerdaemons.
AddatleastanotherGiBperTiBstoragespace.
• OSstorage:
– 32GiB,ormore,freestoragespace
– UseahardwareRAIDwithbatteryprotectedwritecache(BBU)oraredundantZFSsetup
(ZFSisnotcompatiblewithahardwareRAIDcontroller).
• Backupstorage:
– Prefer fast local storage that delivers high IOPS for random IO workloads; use only en-
terpriseSSDsforbestresults.
– If HDDs are used: Using a metadata cache is highly recommended, for example, add a
ZFSspecialdevicemirror.
• RedundantMulti-GBit/snetworkinterfacecards(NICs)
7

ProxmoxBackupDocumentation,Release4.2.8‐1
2.1.3 SupportedWebBrowsersforAccessingtheWebInterface
To access the server’s web-based user interface, we recommend using one of the following
browsers:
• Firefox,areleasefromthecurrentyear,orthelatestExtendedSupportRelease
• Chrome,areleasefromthecurrentyear
• Microsoft’scurrentlysupportedversionofEdge
• Safari,areleasefromthecurrentyear
2.2 Installation Medium
Proxmox Backup Server can be installed via different methods. The recommended method is the
usageofaninstallationmedium,tosimplyboottheinteractiveinstaller.
2.2.1 PrepareInstallationMedium
DownloadtheinstallerISOimagefromhttps://www.proxmox.com/downloads.
TheProxmoxBackupServerinstallationmediumisahybridISOimage. Itworksintwoways:
• AnISOimagefilereadytoburntoaDVD.
• Arawsector(IMG)imagefilereadytocopytoaUSBflashdrive(USBstick).
Using a USB flash drive to install Proxmox Backup Server is the recommended way since it is the
fasterandmorefrequentlyavailableoptionthesedays.
2.2.2 PrepareaUSBFlashDriveasInstallationMedium
Theflashdriveneedstohaveatleast2GBofstoragespace.
(cid:174) Note
DonotuseUNetbootin. ItdoesnotworkwiththeProxmoxBackupServerinstallationimage.
(cid:489) Important
ExistingdataontheUSBflashdrivewillbeoverwritten. Therefore,makesurethatitdoesnot
containanystillneededdataandunmountitafterwardsagainbeforeproceeding.
2.2.3 InstructionsforGNU/Linux
OnUnix-likeoperatingsystemsusetheddcommandtocopytheISOimagetotheUSBflashdrive.
FirstfindthecorrectdevicenameoftheUSBflashdrive(seebelow). Thenruntheddcommand.
Dependingonyourenvironment,youwillneedtohaverootprivilegestoexecutedd.
# dd bs=1M conv=fdatasync if=./proxmox-backup-server_*.iso of=/dev/XYZ
(cid:174) Note
Be sure to replace /dev/XYZ with the correct device name and adapt the input filename (if)
path.
8 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:1002) Caution
Beverycareful,anddonotoverwritethewrongdisk!
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
# hdiutil convert proxmox-backup-server_*.iso -format UDRW -o proxmox-backup-server_*.dmg
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
# sudo dd if=proxmox-backup-server_*.dmg bs=1M of=/dev/rdiskX
(cid:174) Note
rdiskX,insteadofdiskX,inthelastcommandisintended. Itwillincreasethewritespeed.
2.2. InstallationMedium 9

ProxmoxBackupDocumentation,Release4.2.8‐1
2.2.5 InstructionsforWindows
UsingEtcher
Etcherworksoutofthebox. DownloadEtcherfromhttps://etcher.io. Itwillguideyouthroughthe
processofselectingtheISOandyourUSBflashdrive.
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
2.3 Server Installation
The backup server stores the actual backed up data and provides a web based GUI for various
managementtaskssuchasdiskmanagement.
(cid:174) Note
Youalwaysneedabackupserver. ItisnotpossibletouseProxmoxBackupwithouttheserver
part.
Usingourprovideddiskimage(ISOfile)istherecommendedinstallationmethod,asitincludesa
convenientinstaller,acompleteDebiansystemaswellasallnecessarypackagesfortheProxmox
BackupServer.
Once you have created an installation_medium, the booted installer will guide you through the
setup process. It will help you to partition your disks, apply basic settings such as the language,
timezoneandnetworkconfiguration,andfinallyinstallallrequiredpackageswithinminutes.
As an alternative to the interactive installer, advanced users may wish to install Proxmox Backup
Serverunattended.
With sufficient Debian knowledge, you can also install Proxmox Backup Server on top of Debian
yourself.
Whilenotrecommended,ProxmoxBackupServercouldalsobeinstalledonProxmoxVE.
2.3.1 InstallProxmoxBackupServerusingtheInstaller
DownloadtheISOfromhttps://www.proxmox.com/downloads. Itincludesthefollowing:
• TheProxmoxBackup Server installer, which partitions the local disk(s) with ext4, xfs or ZFS,
andinstallstheoperatingsystem
• Completeoperatingsystem(DebianLinux,64-bit)
10 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
• ProxmoxLinuxkernelwithZFSsupport
• Completetoolsettoadministerbackupsandallnecessaryresources
• Web-basedmanagementinterface
(cid:174) Note
Anyexistingdataontheselecteddriveswillbeoverwrittenduringtheinstallationprocess. The
installerdoesnotaddbootmenuentriesforotheroperatingsystems.
Pleaseinserttheinstallation_medium(forexample,USBflashdriveorDVD)andbootfromit.
(cid:174) Note
Youmayneedtogointoyourserver’sfirmwaresettings,toenablebootingfromyourinstallation
medium(forexample,USB)andsetthedesiredbootorder. Whenbootinganinstallerpriorto
ProxmoxBackupServerversion3.1,SecureBootneedstobedisabled.
After choosing the correct entry (for example, Boot from USB) the Proxmox Backup Server menu
willbedisplayed,andoneofthefollowingoptionscanbeselected:
InstallProxmoxBackupServer(Graphical)
Startsthenormalinstallation.
TIP: It’s possible to use the installation wizard with a keyboard only. Buttons can be clicked by
pressing the ALT key combined with the underlined character from the respective button. For
example,ALT + NtopressaNextbutton.
2.3. ServerInstallation 11

ProxmoxBackupDocumentation,Release4.2.8‐1
InstallProxmoxBackupServer(Console)
Startstheterminal-modeinstallationwizard. Itprovidesthesameoverallinstallationexperienceas
thegraphicalinstaller,buthasgenerallybettercompatibilitywithveryoldandverynewhardware.
InstallProxmoxBackupServer(TerminalUI,SerialConsole)
Starts the terminal-mode installation wizard, additionally setting up the Linux kernel to use the
(first)serialportofthemachineforin-andoutput. Thiscanbeusedifthemachineiscompletely
headlessandonlyhasaserialconsoleavailable.
Bothmodesusethesamecodebasefortheactualinstallationprocesstobenefitfrommorethan
adecadeofbugfixesandensurefeatureparity.
TIP: The Console or Terminal UI option can be used in case the graphical installer does not work
correctly,duetoe.g. driverissues. Seealsonomodeset_kernel_param.
AdvancedOptions: InstallProxmoxBackupServer(DebugMode)
Startstheinstallationindebugmode. Aconsolewillbeopenedatseveralinstallationsteps. This
helpstodebugthesituationifsomethinggoeswrong. Toexitadebugconsole,pressCTRL-D.This
optioncanbeusedtobootalivesystemwithallbasictoolsavailable. Youcanuseit,forexample,
to repair a degraded ZFS rpool or fix the Host Bootloader for an existing Proxmox Backup Server
setup.
AdvancedOptions: InstallProxmoxBackupServer(TerminalUI,DebugMode)
Sameasthegraphicaldebugmode,butpreparingthesystemtoruntheterminal-basedinstaller
instead.
AdvancedOptions: InstallProxmoxBackupServer(SerialConsoleDebugMode)
Same the terminal-based debug mode, but additionally sets up the Linux kernel to use the (first)
serialportofthemachineforin-andoutput.
AdvancedOptions: RescueBoot
Withthisoptionyoucanbootanexistinginstallation. Itsearchesallattachedharddisks. Ifitfinds
anexistinginstallation,itbootsdirectlyintothatdiskusingtheLinuxkernelfromtheISO.Thiscan
12 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
be useful if there are problems with the bootloader (GRUB/systemd-boot) or the BIOS/UEFI is
unabletoreadthebootblockfromthedisk.
AdvancedOptions: TestMemory(memtest86+)
Runs memtest86+. This is useful to check if the memory is functional and free of errors. Secure
BootmustbeturnedoffintheUEFIfirmwaresetuputilitytorunthisoption.
YounormallyselectInstallProxmoxBackupServer(Graphical)tostarttheinstallation.
ThefirststepistoreadourEULA(EndUserLicenseAgreement). Followingthis,youcanselectthe
targetharddisk(s)fortheinstallation.
(cid:1002) Caution
By default, the whole server is used and all existing data is removed. Make sure there is no
importantdataontheserverbeforeproceedingwiththeinstallation.
TheOptionsbuttonletsyouselectthetargetfilesystem,whichdefaultstoext4. Theinstalleruses
LVMifyouselectext4orxfsasafilesystem,andoffersadditionaloptionstorestrictLVMspace
(seebelow).
Proxmox Backup Server can also be installed on ZFS. As ZFS offers several software RAID levels,
thisisanoptionforsystemsthatdon’thaveahardwareRAIDcontroller. Thetargetdisksmustbe
selectedintheOptionsdialog. MoreZFSspecificsettingscanbechangedunderAdvancedOptions.
(cid:193) Warning
ZFSontopofanyhardwareRAIDisnotsupportedandcanresultindataloss.
2.3. ServerInstallation 13

ProxmoxBackupDocumentation,Release4.2.8‐1
The next page asks for basic configuration options like your location, time zone, and keyboard
layout. The location is used to select a nearby download server, in order to increase the speed
ofupdates. Theinstallerisusuallyabletoauto-detectthesesettings,soyouonlyneedtochange
theminraresituationswhenauto-detectionfails,orwhenyouwanttouseakeyboardlayoutnot
commonlyusedinyourcountry.
Nextthepasswordofthesuperuser(root)andanemailaddressneedstobespecified. Thepass-
word must consist of at least 8 characters. It’s highly recommended to use a stronger password.
Someguidelinesare:
14 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
• Useaminimumpasswordlengthofatleast12characters.
• Includelowercaseanduppercasealphabeticcharacters,numbers,andsymbols.
• Avoid character repetition, keyboard patterns, common dictionary words, letter or number
sequences,usernames,relativeorpetnames,romanticlinks(currentorpast),andbiograph-
icalinformation(forexampleIDnumbers,ancestors’namesordates).
Theemailaddressisusedtosendnotificationstothesystemadministrator. Forexample:
• Informationaboutavailablepackageupdates.
• Errormessagesfromperiodiccronjobs.
Allthosenotificationmailswillbesenttothespecifiedemailaddress.
The last step is the network configuration. Network interfaces that are UP show a filled circle in
front of their name in the drop down menu. Please note that during installation you can either
specify an IPv4 or IPv6 address, but not both. To configure a dual stack node, add additional IP
addressesaftertheinstallation.
2.3. ServerInstallation 15

ProxmoxBackupDocumentation,Release4.2.8‐1
Thenextstepshowsasummaryofthepreviouslyselectedoptions. Pleasere-checkeverysetting
andusethePreviousbuttonifasettingneedstobechanged.
After clicking Install, the installer will begin to format the disks and copy packages to the target
disk(s). Please wait until this step has finished; then remove the installation medium and restart
yoursystem.
Copyingthepackagesusuallytakesseveralminutes,mostlydependingonthespeedoftheinstal-
lationmediumandthetargetdiskperformance.
16 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
When copying and setting up the packages has finished, you can reboot the server. This will be
doneautomaticallyafterafewsecondsbydefault.
InstallationFailure
Iftheinstallationfailed,checkoutspecificerrorsonthesecondTTY(CTRL + ALT + F2)anden-
surethatthesystemsmeetstheminimumrequirements.
Iftheinstallationisstillnotworking,lookatthehowtogethelpchapter.
AccessingtheManagementInterfacePost‐Installation
After a successful installation and reboot of the system you can use the Proxmox Backup Server
webinterfaceforfurtherconfiguration.
• PointyourbrowsertotheIPaddressgivenduringtheinstallationandport8007,forexample:
https://pbs.yourdomain.tld:8007
• Loginusingtheroot(realmLinuxPAMstandardauthentication)usernameandthepassword
chosenduringinstallation.
• UploadyoursubscriptionkeytogainaccesstotheEnterpriserepository. Otherwise,youwill
needtosetuponeofthepublic,lesstestedpackagerepositoriestogetupdatesforsecurity
fixes,bugfixes,andnewfeatures.
• ChecktheIPconfigurationandhostname.
• Checkthetimezone.
AdvancedLVMConfigurationOptions
TheinstallercreatesaVolumeGroup(VG)called pbs, andadditionalLogicalVolumes(LVs)called
rootandswap,if ext4orxfsasfilesystemisused. Tocontrolthesizeofthesevolumesuse:
• hdsize
Definesthetotalharddisksizetobeused. Thiswayyoucanreservefreespaceon
theharddiskforfurtherpartitioning.
• swapsize
Definesthesizeoftheswapvolume. Thedefaultisthesizeoftheinstalledmemory,
minimum 4 GB and maximum 8 GB. The resulting value cannot be greater than
hdsize/8.
Ifsetto0,noswapvolumewillbecreated.
• minfree
DefinestheamountoffreespacethatshouldbeleftintheLVMvolumegrouppbs.
Withmorethan128GBstorageavailable,thedefaultis16GB,otherwisehdsize/8
willbeused.
2.3. ServerInstallation 17

ProxmoxBackupDocumentation,Release4.2.8‐1
AdvancedZFSConfigurationOptions
The installer creates the ZFS pool rpool, if ZFS is used. No swap space is created but you can
reserve some unpartitioned space on the install disks for swap. You can also create a swap zvol
aftertheinstallation,althoughthiscanleadtoproblems(seeZFSswapnotes).
• ashift
Definesthe ashift valueforthe createdpool. The ashift needstobe setat leastto
thesector-sizeoftheunderlyingdisks(2tothepowerofashiftisthesector-size),or
anydiskwhichmightbeputinthepool(forexamplethereplacementofadefective
disk).
• compress
Defineswhethercompressionisenabledforrpool.
• checksum
Defineswhichchecksummingalgorithmshouldbeusedforrpool.
• copies
Defines the copies parameter for rpool. Check the zfs(8) manpage for the se-
mantics,andwhythisdoesnotreplaceredundancyondisk-level.
• hdsize
Definesthetotalharddisksizetobeused. Thisisusefultosavefreespaceonthe
harddisk(s)forfurtherpartitioning(forexample,tocreateaswappartition). hdsize
is only honored for bootable disks, that is only the first disk or mirror for RAID0,
RAID1orRAID10,andalldisksinRAID-Z[123].
ZFSPerformanceTips
ZFS works best with a lot of memory. If you intend to use ZFS make sure to have enough RAM
availableforit. Agoodcalculationis4GBplus1GBRAMforeachTBofrawdiskspace.
ZFScanuseadedicateddriveaswritecache,calledtheZFSIntentLog(ZIL).Useafastdrive(SSD)
forit. Itcanbeaddedafterinstallationwiththefollowingcommand:
# zpool add <pool-name> log </dev/path_to_fast_ssd>
AddingthenomodesetKernelParameter
Problems may arise on very old or very new hardware due to graphics drivers. If the installation
hangsduringboot,youcantryaddingthenomodesetparameter. ThispreventstheLinuxkernel
from loading any graphics drivers and forces it to continue using the BIOS/UEFI-provided frame-
buffer.
On the Proxmox Backup Server bootloader menu, navigate to Install ProxmoxBackup Server (Con-
sole)andpressetoedittheentry. Usingthearrowkeys,navigatetothelinestartingwithlinux,
movethecursortotheendofthatlineandaddtheparameternomodeset,separatedbyaspace
fromthepre-existinglastparameter.
ThenpressCtrl-XorF10toboottheconfiguration.
2.3.2 InstallProxmoxBackupServerUnattended
ItispossibletoinstallProxmoxBackupServerautomaticallyinanunattendedmanner. Thisenables
youtofullyautomatethesetupprocessonbare-metal. Oncetheinstallationiscompleteandthe
hosthasbootedup,automationtoolslikeAnsiblecanbeusedtofurtherconfiguretheinstallation.
Thenecessaryoptionsfortheinstallermustbeprovidedinananswerfile. Thisfileallowstheuse
offilterrulestodeterminewhichdisksandnetworkcardsshouldbeused.
18 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
Tousetheautomatedinstallation,itisfirstnecessarytoprepareaninstallationISO.Formoredetails
andinformationontheunattendedinstallationseeourwiki.
2.3.3 InstallProxmoxBackupServeronDebian
Proxmox ships as a set of Debian packages which can be installed on top of a standard Debian
installation. AfterconfiguringtheDebianPackageRepositories,youneedtorun:
# apt update
# apt install proxmox-backup-server
Theabovecommandskeepthecurrent(Debian)kernelandinstallaminimalsetofrequiredpack-
ages.
Ifyouwanttoinstallthesamesetofpackagesastheinstallerdoes,pleaseusethefollowing:
# apt update
# apt install proxmox-backup
Thiswillinstallallrequiredpackages,theProxmoxkernelwithZFSsupport,andasetofcommon
andusefulpackages.
(cid:1002) Caution
InstallingProxmoxBackupontopofanexistingDebianinstallationlookseasy,butitassumes
thatthebasesystemandlocalstoragehavebeensetupcorrectly. Ingeneralthisisnottrivial,
especiallywhenLVMorZFSisused. Thenetworkconfigurationiscompletelyuptoyouaswell.
(cid:174) Note
YoucanaccessthewebinterfaceoftheProxmoxBackupServerwithyourwebbrowser,using
HTTPSonport8007. Forexampleathttps://<ip-or-dns-name>:8007
2.3.4 InstallProxmoxBackupServeronProxmoxVE
AfterconfiguringtheDebianPackageRepositories,youneedtorun:
# apt update
# apt install proxmox-backup-server
(cid:1002) Caution
Installingthebackupserverdirectlyonthehypervisorisnotrecommended. Itissafertousea
separatephysicalservertostorebackups. Shouldthehypervisorserverfail,youcanstillaccess
thebackups.
(cid:174) Note
YoucanaccessthewebinterfaceoftheProxmoxBackupServerwithyourwebbrowser,using
HTTPSonport8007. Forexampleathttps://<ip-or-dns-name>:8007
2.3. ServerInstallation 19

ProxmoxBackupDocumentation,Release4.2.8‐1
2.4 Client Installation
2.4.1 InstallProxmoxBackupClientonDebian
ProxmoxshipsasasetofDebianpackagestobeinstalledontopofastandardDebianinstallation.
AfterconfiguringtheAPT-basedProxmoxBackupClientRepository,youneedtorun:
# apt update
# apt install proxmox-backup-client
2.4.2 InstallStaticallyLinkedProxmoxBackupClient
Proxmox provides a statically linked build of the Proxmox backup client that should run on any
modernx86-64Linuxsystem.
ItiscurrentlyavailableasaDebianpackage. AfterconfiguringtheAPT-basedProxmoxBackupClient
Repository,youneedtorun:
# apt update
# apt install proxmox-backup-client-static
This package conflicts with the proxmox-backup-client package, as both provide the client as an
executableinthe/usr/bin/proxmox-backup-clientpath.
Youcancopythisexecutabletoother,e.g. non-DebianbasedLinuxsystems.
FordetailsonusingtheProxmoxBackupClient,seeBackupClientUsage.
2.5 Debian Package Repositories
All Debian based systems use APT as a package management tool. The lists of repositories are
definedin/etc/apt/sources.list andthe.listor.sourcesfilesfoundinthe/etc/apt/
sources.d/ directory. Updates can be installed directly with the apt command-line tool, or via
theGUI.
2.5.1 RepositoryFormats
APTrepositoriescanbeconfiguredintwodistinctformats,theoldsinglelineformatandthenewer
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
20 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
2.5.2 DebianBaseRepositories
YouwillneedaDebianbaserepositoryasaminimumtogetupdatesforallpackagesprovidedby
Debianitself:
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
Inaddition,youneedapackagerepositoryfromProxmoxtogetProxmoxBackupupdates.
2.5.3 ProxmoxBackupEnterpriseRepository
This is the stable, recommended repository. It is available for all Proxmox Backup subscrip-
tion users. It contains the most stable packages, and is suitable for production use. The
pbs-enterpriserepositoryisenabledbydefault:
|     | Listing | 2:  | File: | /etc/apt/sources.list.d/ |
| --- | ------- | --- | ----- | ------------------------ |
pbs-enterprise.sources
Types: deb
URIs: https://enterprise.proxmox.com/debian/pbs
Suites: trixie
| Components: | pbs-enterprise                                  |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Signed-By:  | /usr/share/keyrings/proxmox-archive-keyring.gpg |     |     |     |
2.5. DebianPackageRepositories 21

ProxmoxBackupDocumentation,Release4.2.8‐1
Tonevermissimportantsecurityfixes,thesuperuser(root@pamuser)isnotifiedviaemailabout
new packages as soon as they are available. The change-log and details of each package can be
viewedintheGUI(ifavailable).
Please note that you need a valid subscription key to access this repository. More informa-
tion regarding subscription levels and pricing can be found at https://www.proxmox.com/en/
proxmox-backup-server/pricing
(cid:174) Note
YoucandisablethisrepositorybyaddingthelineEnabled: falsetothestanza.
2.5.4 ProxmoxBackupNo‐SubscriptionRepository
Asthenamesuggests,youdonotneedasubscriptionkeytoaccessthisrepository. Itcanbeused
fortestingandnon-productionuse. Itisnotrecommendedtouseitonproductionservers,because
thesepackagesarenotalwaysheavilytestedandvalidated.
Werecommendtoconfigurethisrepositoryin/etc/apt/sources.list.d/proxmox.sources.
Listing 3: File: /etc/apt/sources.list.d/proxmox.
sources
Types: deb
URIs: http://download.proxmox.com/debian/pbs
Suites: trixie
Components: pbs-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
2.5.5 ProxmoxBackupTestRepository
Thisrepositorycontainsthelatestpackagesandisheavilyusedbydeveloperstotestnewfeatures.
You can access this repository by adding the following stanza to /etc/apt/sources.list.d/
proxmox.sources:
Listing4: sources.listentryforpbstest
Types: deb
URIs: http://download.proxmox.com/debian/pbs
Suites: trixie
Components: pbs-test
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
2.5.6 ProxmoxBackupDebugSymbolRepository
Debugsymbolpackages,named<package>-dbgsym,containthedetacheddebuginformationfor
thematchingbinarypackage. Theyarenotneededfornormaloperation,butlettoolssuchasgdb,
systemd-coredump or crash produce useful backtraces when analyzing a crash or hang. They
areprovidedinadedicatedrepository,separatefromtheregularones,fortheDebianBookworm
andTrixiebasedProxmoxBackupreleases(andnewer).
Listing5: sources.listentryforpbs-dbgsym
Types: deb
URIs: https://dbgsym.proxmox.com/debian/pbs
Suites: trixie
Components: pbs-dbgsym
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
After enabling the repository, install the -dbgsym package that matches the binary you want to
debug.
22 Chapter2. Installation

ProxmoxBackupDocumentation,Release4.2.8‐1
2.5.7 ProxmoxBackupClient‐onlyRepository
If you want to use the Proxmox Backup Client on systems using a Linux distribution not based on
Proxmoxprojects,youcanusetheclient-onlyrepository.
Currentlythere’sonlyaclient-repositoryforAPTbasedsystems.
APT‐basedProxmoxBackupClientRepository
FormodernLinuxdistributionsusingaptaspackagemanager,likeallDebianandUbuntuDeriva-
tivedo,youmaybeabletousetheAPT-basedrepository.
InordertoconfigurethisrepositoryyouneedtofirstsetuptheProxmoxreleasekey. Afterthat,add
therepositoryURLtotheAPTsourceslists.
RepositoriesforDebian13(Trixie)basedreleases
Thisrepositoryistestedwith:
• DebianTrixie
Editthefile/etc/apt/sources.list.d/pbs-client.sourcesandaddthefollowingsnippet
Listing6: File: /etc/apt/sources.list.d/pbs
Types: deb
URIs: http://download.proxmox.com/debian/pbs-client
Suites: trixie
Components: main
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
RepositoriesforDebian12(Bookworm)basedreleases
Thisrepositoryistestedwith:
• DebianBookworm
Editthefile/etc/apt/sources.list.d/pbs-client.listandaddthefollowingsnippet
Listing7: File: /etc/apt/sources.list
deb http://download.proxmox.com/debian/pbs-client bookworm main
RepositoriesforDebian11(Bullseye)basedreleases
Thisrepositoryistestedwith:
• DebianBullseye
Editthefile/etc/apt/sources.list.d/pbs-client.listandaddthefollowingsnippet
Listing8: File: /etc/apt/sources.list
deb http://download.proxmox.com/debian/pbs-client bullseye main
RepositoriesforDebian10(Buster)basedreleases
Thisrepositoryistestedwith:
• DebianBuster
• Ubuntu20.04LTS
Itmayworkwitholder,andshouldworkwithmorerecentreleasedversions.
Editthefile/etc/apt/sources.list.d/pbs-client.listandaddthefollowingsnippet
2.5. DebianPackageRepositories 23

ProxmoxBackupDocumentation,Release4.2.8‐1
Listing9: File: /etc/apt/sources.list
deb http://download.proxmox.com/debian/pbs-client buster main
2.5.8 SecureApt
TheReleasefilesintherepositoriesaresignedwithGnuPG.APTisusingthesesignaturestoverify
thatallpackagesarefromatrustedsource.
Ifyou install ProxmoxBackupServer froman official ISOimage, theverification keyis alreadyin-
stalled.
IfyouinstallProxmoxBackupServerontopofDebian, downloadandinstallthekeywiththefol-
lowingcommands:
# wget https://enterprise.proxmox.com/debian/proxmox-archive-keyring-trixie.gpg -O /usr/share/
,→keyrings/proxmox-archive-keyring.gpg
(cid:174) Note
ThewgetcommandaboveaddsthekeyringforProxmoxreleasesbasedonDebianTrixie. Once
theproxmox-archive-keyringpackageisinstalled,itwillmanagethisfile. Atthatpoint,thehashes
belowmaynolongermatchthehashesofthisfile,askeysfornewProxmoxreleasesgetadded
orremoved. Thisisintended,aptwillensurethatonlytrustedkeysarebeingused. Modifying
thisfileisdiscouragedonce‘proxmox-archive-keyring‘isinstalled.
VerifytheSHA256checksumafterwardswiththeexpectedoutputbelow:
# sha256sum /usr/share/keyrings/proxmox-archive-keyring.gpg
136673be77aba35dcce385b28737689ad64fd785a797e57897589aed08db6e45 /usr/share/keyrings/proxmox-
,→archive-keyring.gpg
andthemd5sum,withtheexpectedoutputbelow:
# md5sum /usr/share/keyrings/proxmox-archive-keyring.gpg
77c8b1166d15ce8350102ab1bca2fcbf /usr/share/keyrings/proxmox-archive-keyring.gpg
(cid:174) Note
Make sure that the path that you download the key to, matches the path specified in the
Signed-By: linesinyourrepositorystanzasfromabove.
2.5.9 RepositoryAccessBehindHTTPProxy
Somesetupshaverestrictedaccesstotheinternet,sometimesonlythroughacentralproxy. You
cansetupaHTTPproxythroughtheProxmoxBackupServer’sweb-interfaceintheConfiguration->
Authenticationtab.
Once configured this proxy will be used for apt network requests and for checking a Proxmox
BackupServersupportsubscription.
StandardHTTPproxyconfigurationsareaccepted,[http://]<host>[:port]wherethe<host>partmay
includeanauthorization,forexample: http://user:pass@proxy.example.org:12345
24 Chapter2. Installation

CHAPTER
THREE
TERMINOLOGY
3.1 Backup Content
When doing deduplication, there are different strategies to get optimal results in terms of per-
formance and/or deduplication rates. Depending on the type of data, it can be split into fixed or
variablesizedchunks.
FixedsizedchunkingrequiresminimalCPUpower,andisusedtobackupvirtualmachineimages.
Variable sized chunking needs more CPU power, but is essential to get good deduplication rates
forfilearchives.
TheProxmoxBackupServersupportsbothstrategies.
3.1.1 ImageArchives: <name>.img
Thisisusedforvirtualmachineimagesandotherlargebinarydata. Contentissplitintofixed-sized
chunks.
3.1.2 FileArchives: <name>.pxar
A file archive stores a full directory tree. Content is stored using the Proxmox File Archive Format
(.pxar), split into variable-sized chunks. The format is optimized to achieve good deduplication
rates.
3.1.3 BinaryData(BLOBs)
This type is used to store smaller (< 16MB) binary data such as configuration files. Larger files
shouldbestoredasimagearchives.
(cid:1002) Caution
PleasedonotstoreallfilesasBLOBs. Instead,usethefilearchivetostoreentiredirectorytrees.
3.1.4 CatalogFile: catalog.pcat1
Thecatalogfileisanindexforfilearchives. Itcontainsthelistofincludedfilesandisusedtospeed
upsearchoperations.
3.1.5 TheManifest: index.json
Themanifestcontainsalistofallbackedupfiles,andtheirsizesandchecksums. Itisusedtoverify
theconsistencyofabackup.
25

ProxmoxBackupDocumentation,Release4.2.8‐1
3.2 Backup Namespace
Namespacesallowforthereuseofasinglechunkstorededuplicationdomainformultiplesources,
whileavoidingnamingconflictsandenablingmorefine-grainedaccesscontrol.
Essentially,they’reimplementedasasimpledirectorystructureanddon’trequireseparateconfig-
uration.
3.3 Backup Type
Thebackupservergroupsbackupsbytype,wheretypeisoneof:
vm
Thistypeisusedforvirtualmachines. Ittypicallyconsistsofthevirtualmachine’sconfiguration
fileandanimagearchiveforeachdisk.
ct
This type is used for containers. It consists of the container’s configuration and a single file
archiveforthefilesystem’scontents.
host
Thistypeisusedforfile/directorybackupscreatedfromwithinamachine. Typicallythiswould
beaphysicalhost,butcouldalsobeavirtualmachineorcontainer. Suchbackupsmaycontain
fileandimagearchives;therearenorestrictionsinthisregard.
3.4 Backup ID
A unique ID for a specific Backup Type and Backup Namespace. Usually the virtual machine or
containerID.hosttypebackupsnormallyusethehostname.
3.5 Backup Time
Thetimewhenthebackupwasmadewithsecondresolution.
3.6 Backup Group
Thetuple<type>/<id>iscalledabackupgroup. Suchagroupmaycontainoneormorebackup
snapshots.
3.7 Backup Snapshot
The triplet <type>/<ID>/<time> is called a backup snapshot. It uniquely identifies a specific
backupwithinanamespace.
Listing1: BackupSnapshotExamples
vm/104/2019-10-09T08:01:06Z
host/elsa/2019-11-08T09:48:14Z
Asyoucansee,thetimeformatisRFC3339withCoordinatedUniversalTime(UTC,identifiedbythe
trailingZ).
26 Chapter3. Terminology

CHAPTER
FOUR
GRAPHICAL USER INTERFACE
Proxmox Backup Server offers an integrated, web-based interface to manage the server. This
means that you can carry out all administration tasks through your web browser, and that you
don’t have to worry about installing extra management tools. The web interface also provides a
built-inconsole,soifyoupreferthecommandlineorneedsomeextracontrol,youhavethisoption.
The web interface can be accessed via https://youripaddress:8007. The default login is root, and
thepasswordiseithertheonespecifiedduringtheinstallationprocessorthepasswordoftheroot
user,incaseofinstallationontopofDebian.
4.1 Features
• SimplemanagementinterfaceforProxmoxBackupServer
• Monitoringoftasks,logsandresourceusage
• Managementofusers,permissions,datastores,etc.
• SecureHTML5console
• Supportformultipleauthenticationsources
• Supportformultiplelanguages
• BasedonExtJS6.xJavaScriptframework
4.2 Login
Whenyouconnecttothewebinterface,youwillfirstseetheloginwindow. ProxmoxBackupServer
supportsvariouslanguagesandauthenticationbackends(Realms),bothofwhichcanbeselected
here.
(cid:174) Note
For convenience, you can save the username on the client side, by selecting the ”Save User
name”checkboxatthebottomofthewindow.
27

ProxmoxBackupDocumentation,Release4.2.8‐1
4.2.1 ConsentBanner
AcustomconsentbannerthathastobeacceptedbeforelogincanbeconfiguredinConfiguration
-> Other -> General -> Consent Text. If there is no content, the consent banner will not be dis-
played. Thetextwillbestoredasabase64stringinthe/etc/proxmox-backup/node.cfgconfig
file.
4.3 GUI Overview
TheProxmoxBackupServerwebinterfaceconsistsof3mainsections:
• Header: Atthetop. Thisshowsversioninformationandcontainsbuttonstoviewdocumen-
tation,monitorrunningtasks,setthelanguage,configurevariousdisplaysettings,andlogout.
• Sidebar: Ontheleft. Thiscontainstheadministrationoptionsfortheserver.
• Configuration Panel: In the center. This contains the respective control interfaces for the
administrationoptionsintheSidebar.
4.4 Sidebar
Inthesidebar,ontheleftsideofthepage,youcanseevariousitemsrelatingtospecificmanage-
mentactivities.
28 Chapter4. GraphicalUserInterface

ProxmoxBackupDocumentation,Release4.2.8‐1
4.4.1 Dashboard
The Dashboard shows a summary of activity and resource usage on the server. Specifically, this
displays hardware usage, a summary of previous and currently running tasks, and subscription
information.
4.4.2 Configuration
The Configuration section contains some system options, such as time, network, WebAuthn, and
HTTPproxyconfiguration. Italsocontainsthefollowingsubsections:
• Access Control: Add and manage users, API tokens, and the permissions associated with
theseitems.
• Remotes: Add,editandremoveremotes(seeRemote).
• S3Endpoints: Add,editandremoveS3endpointstobeusedbydatastores.
• TrafficControl: Managerulesfortrafficlimitsonusers,networksandtimeframes.
• Certificates: ManageACMEaccountsandcreateSSLcertificates.
• EncryptioinKeys: Manageencryptionkeysfortapebackupsandsyncjobs.
• Notifications: Configurenotificationtargetsandcontrolwhennotificationsshouldbesend
bydefiningmatchrules.
• Subscription: Upload a subscription key, view subscription status and access a text-based
systemreport.
4.4.3 Administration
4.4. Sidebar 29

ProxmoxBackupDocumentation,Release4.2.8‐1
TheAdministrationsectioncontainsatoppanel,withfurtheradministrationtasksandinformation.
Theseare:
• ServerStatus: Provides access to the console, power options, and various resource usage
statistics
• Services: Manageandmonitorsystemservices
• Updates: Aninterfaceforupgradingpackages
• Repositories: AninterfaceforconfiguringAPTrepositories
• Syslog: Viewlogmessagesfromtheserver
• Tasks: Taskhistorywithmultiplefilteroptions
Theadministrationmenuitemalsocontainsadiskmanagementsubsection:
• Disks: Viewinformationonavailabledisks
– Directory: Createandviewinformationonext4andxfsdisks
– ZFS:CreateandviewinformationonZFSdisks
30 Chapter4. GraphicalUserInterface

ProxmoxBackupDocumentation,Release4.2.8‐1
4.4.4 TapeBackup
TheTapeBackupsectioncontainsatoppanel,withoptionsformanagingtapemediasets,invento-
ries,drives,changers,encryptionkeys,andthetapebackupjobsitself. Thetabsareasfollows:
• Content: Informationonthecontentsofthetapebackup
• Inventory: Managethetapesattachedtothesystem
• Changers: Managetapeloadingdevices
• Drives: Managedrivesusedforreadingandwritingtotapes
• MediaPools: Managelogicalpoolsoftapes
• EncryptionKeys: Managetapebackupencryptionkeys
• BackupJobs: Managetapebackupjobs
The section also contains a subsection per standalone drive and per changer, with a status and
managementviewforthosedevices.
4.4. Sidebar 31

ProxmoxBackupDocumentation,Release4.2.8‐1
4.4.5 Datastore
The Datastore section contains interfaces for creating and managing datastores. It also contains
abuttonforcreatinganewdatastoreontheserver,aswellasasubsectionforeachdatastoreon
thesystem,inwhichyoucanusethetoppaneltoview:
• Summary: Accessarangeofdatastoreusagestatistics
• Content: Informationonthedatastore’sbackupgroupsandtheirrespectivecontents
• Prune&GC:Schedulepruning andgarbagecollectionoperations,andrungarbagecollection
manually
• SyncJobs: Create,manageandrunSyncJobsfromremoteservers
• VerifyJobs: Create,manageandrunVerificationjobsonthedatastore
• Options: Configurenotificationandverificationsettings
• Permissions: Managepermissionsonthedatastore
32 Chapter4. GraphicalUserInterface

CHAPTER
FIVE
BACKUP STORAGE
5.1 Disk Management
ProxmoxBackupServercomeswithasetofdiskutilities,whichareaccessedusingthedisksub-
command or the web interface. This subcommand allows you to initialize disks, create various
filesystems,andgetinformationaboutthedisks.
To view the disks connected to the system, navigate to Administration -> Storage/Disks in the
webinterfaceorusethelistsubcommandof disk:
# proxmox-backup-manager disk list
┌──────┬────────┬─────┬───────────┬─────────────┬───────────────┬─────────┬────────┐
│ name │ used │ gpt │ disk-type │ size │ model │ wearout │ status │
╞══════╪════════╪═════╪═══════════╪═════════════╪═══════════════╪═════════╪════════╡
│ sda │ lvm │ 1 │ hdd │ 34359738368 │ QEMU_HARDDISK │ - │ passed │
├──────┼────────┼─────┼───────────┼─────────────┼───────────────┼─────────┼────────┤
│ sdb │ unused │ 1 │ hdd │ 68719476736 │ QEMU_HARDDISK │ - │ passed │
├──────┼────────┼─────┼───────────┼─────────────┼───────────────┼─────────┼────────┤
(continuesonnextpage)
33

ProxmoxBackupDocumentation,Release4.2.8‐1
(continuedfrompreviouspage)
│ sdc │ unused │ 1 │ hdd │ 68719476736 │ QEMU_HARDDISK │ - │ passed │
└──────┴────────┴─────┴───────────┴─────────────┴───────────────┴─────────┴────────┘
ToinitializeadiskwithanewGPT,usetheinitializesubcommand:
# proxmox-backup-manager disk initialize sdX
Youcancreateanext4orxfsfilesystemonadiskusingfs create,orbynavigatingtoAdmin-
istration -> Storage/Disks -> Directory in the web interface and creating one from there. The
followingcommandcreatesanext4filesystemandpassesthe--add-datastoreparameter,in
order to automatically create a datastore on the disk. This will create a datastore at the location
/mnt/datastore/store1:
# proxmox-backup-manager disk fs create store1 --disk sdX --filesystem ext4 --add-datastore␣
,→true
YoucanalsocreateazpoolwithvariousraidlevelsfromAdministration->Storage/Disks->ZFS
inthewebinterface,orbyusingzpool create. Thecommandbelowcreatesamirroredzpool
usingtwodisksandmountsitunder/mnt/datastore/zpool1:
# proxmox-backup-manager disk zpool create zpool1 --devices sdX,sdY --raidlevel mirror
(cid:174) Note
Youcanalsopassthe--add-datastoreparameterhere,toautomaticallycreateadatastore
fromthedisk.
Youcanusedisk fs listanddisk zpool listtokeeptrackofyourfilesystemsandzpools
respectively.
34 Chapter5. BackupStorage

ProxmoxBackupDocumentation,Release4.2.8‐1
Proxmox Backup Server uses the package smartmontools. This is a set of tools used to monitor
andcontroltheS.M.A.R.T.systemforlocalharddisks. IfadisksupportsS.M.A.R.T.capability, and
youhavethisenabled,youcandisplayS.M.A.R.T.attributesfromthewebinterfaceorbyusingthe
command:
# proxmox-backup-manager disk smart-attributes sdX
(cid:174) Note
This functionality may also be accessed directly through the use of the smartctl command,
whichcomesaspartofthesmartmontoolspackage(seeman smartctlformoredetails).
5.2 Datastore
Adatastorereferstoalocationatwhichbackupsarestored. Thecurrentimplementationusesa
directoryinsideastandardUnixfilesystem(ext4,xfsorzfs)tostorethebackupdata.
DatastoresareidentifiedbyasimpleID.Youcanconfigurethiswhensettingupthedatastore. The
configurationinformationfordatastoresisstoredinthefile/etc/proxmox-backup/datastore.
cfg.
(cid:174) Note
The File Layout requires the file system to support at least 65538 subdirectories per directory.
5.2. Datastore 35

ProxmoxBackupDocumentation,Release4.2.8‐1
Thatnumbercomesfromthe216 pre-createdchunknamespacedirectories,andthe.and..
defaultdirectoryentries. Thisrequirementexcludescertainfilesystemsandfilesystemconfig-
urationsfrombeingsupportedforadatastore. Forexample,ext3asawholeorext4withthe
dir_nlinkfeaturemanuallydisabled.
5.2.1 DatastoreConfiguration
Youcanconfiguremultipledatastores. Aminimumofonedatastoreneedstobeconfigured. The
datastoreisidentifiedbyasimplenameandpointstoadirectoryonthefilesystem. Eachdatastore
alsohasassociatedretentionsettingsofhowmanybackupsnapshotsforeachintervalofhourly,
daily, weekly, monthly, yearly as well as a time-independent number of backups to keep in
that store. Pruning and Removing Backups and garbage collection can also be configured to run
periodically,basedonaconfiguredschedule(seeCalendarEvents)perdatastore.
36 Chapter5. BackupStorage

ProxmoxBackupDocumentation,Release4.2.8‐1
CreatingaDatastore
Youcancreateanewdatastorefromthewebinterface,byclickingAddDatastoreinthesidemenu,
undertheDatastoresection. Inthesetupwindow:
• Namereferstothenameofthedatastore
• BackingPathisthepathtothedirectoryuponwhichyouwanttocreatethedatastore
• GCSchedulereferstothetimeandintervalsatwhichgarbagecollectionruns
• PruneSchedulereferstothefrequencyatwhichpruningtakesplace
• PruneOptions settheamountofbackupswhichyouwouldliketokeep(seePruningandRe-
movingBackups).
• Commentcanbeusedtoaddsomecontextualinformationtothedatastore.
Alternatively you can create a new datastore from the command line. The following command
createsanewdatastorecalledstore1on/backup/disk1/store1
# proxmox-backup-manager datastore create store1 /backup/disk1/store1
RemovableDatastores
Removabledatastoreshaveabacking-deviceassociatedwiththem,theycanbemountedand
unmounted. Otherthanthattheybehavethesamewayanormaldatastorewould.
Theycanbecreatedonalreadycorrectlyformattedpartitions,whichshouldbeeitherext4orxfs
aswithnormaldatastores,butmostmodernfilesystemssupportedbytheProxmoxLinuxkernel
shouldwork.
(cid:174) Note
FAT-basedfilesystemsdonotsupportthePOSIXfileownershipconceptandhaverelativelylow
limits on the number of files per directory. Therefore, creating a datastore is not supported
onFATfilesystems. BecausesomeexternaldrivesarepreformattedwithsuchaFAT-basedfile
system, you may need to reformat the drive before you can use it as a backing-device for a
removabledatastore.
It is also possible to create them on completely unused disks through ”Administration” > ”Disks /
Storage”>”Directory”,usingthismethodthediskwillbepartitionedandformattedautomatically
forthedatastore.
Devices with only one datastore on them will be mounted automatically. Unmounting has to be
donethroughtheUIbyclicking”Unmount”onthesummarypageorusingtheCLI.Ifunmounting
fails,thereasonisloggedintheunmounttasklog,andthedatastorewillstayinmaintenancemode
unmounting,whichpreventsanyIOoperations. Insuchcases,themaintenancemodehastobe
resetmanuallyusing:
# proxmox-backup-manager datastore update --maintenance-mode offline
5.2. Datastore 37

ProxmoxBackupDocumentation,Release4.2.8‐1
topreventanyIO,ortoclearituse:
# proxmox-backup-manager datastore update --delete maintenance-mode
Asingledevicecanhousemultipledatastores, theyonlylimitationisthattheyarenotallowedto
benested.
Removable datastores are created on the the device with the given relative path that is specified
oncreation. InordertouseadatastoreonmultiplePBSinstances,ithastobecreatedonone,and
addedwithReuse existing datastorecheckedontheothers. Thepathyousetoncreationis
howmultipledatastoresonasingledeviceareidentified. SowhenaddingonanewPBSinstance,
ithastomatchwhatwassetoncreation.
# proxmox-backup-manager datastore unmount store1
bothwillwaitforanyrunningtaskstofinishandunmountthedevice.
All removable datastores are mounted under /mnt/datastore/<name>, and the specified path
referstothepathonthedevice.
Alldatastorespresentonadevicecanbelistedusingproxmox-backup-debug.
# proxmox-backup-debug inspect device /dev/...
Verify,PruneandGarbageCollectionjobsareskippediftheremovabledatastoreisnotmounted
when they are scheduled. Sync jobs start, but fail with an error saying the datastore was not
mounted. Thereasonisthatsyncsnothappeningasscheduledshouldatleastbenoticeable.
Setupsthatrelyonunmount-on-done(seeSyncJobs)havenonaturalpointtorungarbagecollec-
tion,sincethedeviceisdetachedrightafterthesyncfinishes. Enablingthegc-on-unmountoption
onthedatastoremakestheunmounttriggeragarbagecollectionfirstandwaitforittocomplete
beforeactuallyunmounting. Ifagarbagecollectionrunisalreadyinprogresswhentheunmount
fires(forexamplefromanoverlappingscheduledGCjob),thatruniswaitedoninstead.
DatastoreswithS3Backend
ProxmoxBackupServersupportsS3compatibleobjectstoresasstoragebackendfordatastores.
Forthis,anS3endpointneedstobeset-upunder”Configuration”>”Remotes”>”S3Endpoints”.
(cid:489) Important
KeepinmindthatoperatingasS3backedobjectstoremightcauseadditionalcosts. Providers
might charge you for storage space and API requests performed to the buckets, egress and
bandwidthfeesmightbechargedaswell. Therefore,monitoringofthesevaluesandeventual
costsishighlyrecommended.
In the endpoint configuration, provide the REST API endpoint for the object store. The end-
point is provider dependent and allows for the bucket and region templating. For example,
configuring the endpoint as e.g. {{bucket}}.s3.{{region}}.amazonaws.com will be ex-
panded to my-pbs-bucket.s3.eu-central-1.amazonaws.com with a configured bucket of
namemy-pbs-bucketlocatedinregioneu-central-1.
Thebucketnameispartofthedatastorebackendconfigurationratherthantheendpointconfig-
uration, asthesameendpointmightbereusedformultiplebucket. Objectsplacedinthebucket
areprefixedbythedatastorename,thereforeitispossibletocreatemultipledatastoresusingthe
samebucket.
(cid:174) Note
38 Chapter5. BackupStorage

ProxmoxBackupDocumentation,Release4.2.8‐1
ProxmoxBackupServerdoesnothandlebucketcreationandaccesscontrol. Thebucketused
tostorethedatastore’sobjectsaswellastheaccesskeyhavetobesetupbeforehandinyourS3
providerinterface. TheProxmoxBackupServeractsasclientandrequirespermissionstoget,
putlistanddeleteobjectsinthebucket.
Mostprovidersallowtoaccessbucketseitherusingavhoststyleaddressing,thebucketnamebeing
partoftheendpointaddress,orviapathstyleaddressing,thebucketnamebeingtheprefixtothe
path components of requests. Proxmox Backup Server supports both styles, favoring the vhost
styleurlsoverthepathstyle. Tousepathstyleaddresses,setthecorrespondingconfigurationflag.
Proxmox Backup Server does not support plain text communication with the S3 API, all commu-
nication is encrypted using HTTPS in transit. Therefore, for self-hosted S3 object stores using a
self-signedcertificate,thematchingfingerprinthastobeprovidedtotheendpointconfiguration.
OtherwisetheclientrefusesconnectionstotheS3objectstore.
Thefollowingexampleshowsthesetupofanews3endpointconfiguration:
# proxmox-backup-manager s3 endpoint create my-s3-ep --access-key 'my-access-key' --secret-
,→key 'my-secret-key' --endpoint '{{bucket}}.s3.{{region}}.amazonaws.com' --region eu-
,→central-1
Tolistyours3endpointconfiguration,run:
# proxmox-backup-manager s3 endpoint list
A new datastore with S3 backend can be created using one of the configured S3 endpoints. Al-
thoughstoringallcontentsontheS3objectstore,thedatastorerequiresneverthelessalocalper-
sistentcache, usedtoincreaseperformanceandreducethenumberofrequeststothebackend.
For this, a local filesystem path has to be provided during datastore creation, just like for regular
datastoresetup. However,unlikeforregulardatastoresthesizeofthelocalcachecanbelimited,64
GiBto128GiBarerecommendedgiventhatcacheddatastorecontentsincludealsodatachunks.
Bestistouseadedicateddisk,partitionorZFSdatasetwithquotaaslocalcache. Notehowever,it
isnotpossibletouseapre-existingregulardatastoreforthis. Further,theuseofvolatilememory
onlyforthecacheiscurrentlynotpossible.
Tosetupanewdatastorecalledmy-s3-storeplacedinabucketcalledpbs-s3-bucket,run:
# proxmox-backup-manager datastore create my-s3-store /mnt/datastore/my-s3-store-cache --
,→backend type=s3,client=my-s3-ep,bucket=pbs-s3-bucket
A datastore cannot be shared between multiple Proxmox Backup Server instances, only one in-
stancecanoperateonthedatastoreatatime. However,datastorecontentsusedonaninstance
which is no longer available can be reused on a fresh installation. To recreate the datastore, you
mustpassthereuse-datastoreandoverwrite-in-useflags. Sincethedatastorenameisused
asprefix,thesamedatastorenamemustbeused.
# proxmox-backup-manager datastore create my-s3-store /mnt/datastore/my-new-s3-store-cache --
,→backend type=s3,client=my-s3-ep,bucket=pbs-s3-bucket --reuse-datastore true --overwrite-in-
,→use true
(cid:174) Note
If your S3 object store runs out of space while performing write operation to it, most likely
cleanupoperationssuchascleaningupofcontentswithinasnapshotdirectorywillfailaswell.
Therecommendedprocedureistocleanupanystrayobjectscorrespondingtothissnapshoton
theS3objectstoremanuallyandrefreshthecontentsviaanS3 refresh,eitherviatheCLIor
UI.
5.2. Datastore 39

ProxmoxBackupDocumentation,Release4.2.8‐1
S3DatastoreBackendConfigurationExamples
The following shows example configurations for some typical S3 object store providers as
excerpts (data relevant to S3 config only) from /etc/proxmox-backup/s3.cfg and /etc/
proxmox-backup/datastore.cfg:
Self hosted S3 object store with Ceph Rados Gateway using plain IP address, custom port, self-
signedcertificateandpath-stylebucket:
# cat /etc/proxmox-backup/s3.cfg
| s3-endpoint: | ceph-s3-rados-gw     |     |     |     |     |
| ------------ | -------------------- | --- | --- | --- | --- |
| access-key   | XXXXXXXXXXXXXXXXXXXX |     |     |     |     |
| endpoint     | 172.16.0.200         |     |     |     |     |
fingerprint␣
,→XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX
| path-style | true                                     |     |     |     |     |
| ---------- | ---------------------------------------- | --- | --- | --- | --- |
| port       | 7480                                     |     |     |     |     |
| secret-key | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |     |     |     |     |
# cat /etc/proxmox-backup/datastore.cfg
| datastore: | ceph-s3-rgw-store                                      |     |     |     |     |
| ---------- | ------------------------------------------------------ | --- | --- | --- | --- |
| backend    | bucket=pbs-ceph-bucket,client=ceph-s3-rados-gw,type=s3 |     |     |     |     |
| path       | /mnt/datastore/ceph-s3-rgw-store-local-cache           |     |     |     |     |
AWSS3withvhoststylebucketaddressing,usingbucketnameandregiontemplatingfortheend-
pointurl:
# cat /etc/proxmox-backup/s3.cfg
| s3-endpoint: | aws-s3                                   |     |     |     |     |
| ------------ | ---------------------------------------- | --- | --- | --- | --- |
| access-key   | XXXXXXXXXXXXXXXXXXXX                     |     |     |     |     |
| endpoint     | {{bucket}}.s3.{{region}}.amazonaws.com   |     |     |     |     |
| region       | eu-central-1                             |     |     |     |     |
| secret-key   | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |     |     |     |     |
# cat /etc/proxmox-backup/datastore.cfg
| datastore: | aws-s3-store                               |     |     |     |     |
| ---------- | ------------------------------------------ | --- | --- | --- | --- |
| backend    | bucket=pbs-s3-bucket,client=aws-s3,type=s3 |     |     |     |     |
| path       | /mnt/datastore/aws-s3-store-local-cache    |     |     |     |     |
CloudflareR2withpathstylebucketaddressing,notethatregionmustbesettoautoasotherwise
requestauthenticationmightfail:
# cat /etc/proxmox-backup/s3.cfg
| s3-endpoint: | cloudflare-r2                                             |     |     |     |     |
| ------------ | --------------------------------------------------------- | --- | --- | --- | --- |
| access-key   | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                          |     |     |     |     |
| endpoint     | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.r2.cloudflarestorage.com |     |     |     |     |
| path-style   | true                                                      |     |     |     |     |
| region       | auto                                                      |     |     |     |     |
secret-key XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# cat /etc/proxmox-backup/datastore.cfg
| datastore: | r2-s3-store                                       |     |     |     |     |
| ---------- | ------------------------------------------------- | --- | --- | --- | --- |
| backend    | bucket=pbs-r2-bucket,client=cloudflare-r2,type=s3 |     |     |     |     |
| path       | /mnt/datastore/r2-s3-store-local-cache            |     |     |     |     |
ManagingDatastores
Tolistexistingdatastoresfromthecommandline,run:
| # proxmox-backup-manager |     | datastore list |     |     |     |
| ------------------------ | --- | -------------- | --- | --- | --- |
┌────────┬──────────────────────┬─────────────────────────────┐
| │ name | │ path | │ comment |     | │   |     |
| ------ | ------ | --------- | --- | --- | --- |
╞════════╪══════════════════════╪═════════════════════════════╡
| │ store1 | │ /backup/disk1/store1 | │ This | is my default storage. | │   |     |
| -------- | ---------------------- | ------ | ---------------------- | --- | --- |
└────────┴──────────────────────┴─────────────────────────────┘
Youcanchangethegarbagecollectionandprunesettingsofadatastore,byeditingthedatastore
from the GUI or by using the update subcommand. For example, the below command changes
the garbage collection schedule using the update subcommand and prints the properties of the
datastorewiththeshowsubcommand:
# proxmox-backup-manager datastore update store1 --gc-schedule 'Tue 04:27'
| # proxmox-backup-manager |     | datastore show | store1 |     |     |
| ------------------------ | --- | -------------- | ------ | --- | --- |
┌────────────────┬─────────────────────────────┐
| │ Name | │ Value |     | │   |     |     |
| ------ | ------- | --- | --- | --- | --- |
╞════════════════╪═════════════════════════════╡
| │ name | │ store1 |     | │   |     |     |
| ------ | -------- | --- | --- | --- | --- |
├────────────────┼─────────────────────────────┤
(continuesonnextpage)
| 40  |     |     |     | Chapter5. | BackupStorage |
| --- | --- | --- | --- | --------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
(continuedfrompreviouspage)
| │ path | │ /backup/disk1/store1 |     |     | │   |     |
| ------ | ---------------------- | --- | --- | --- | --- |
├────────────────┼─────────────────────────────┤
| │ comment | │ This | is my | default | storage. │ |     |
| --------- | ------ | ----- | ------- | ---------- | --- |
├────────────────┼─────────────────────────────┤
| │ gc-schedule | │ Tue | 04:27 |     | │   |     |
| ------------- | ----- | ----- | --- | --- | --- |
├────────────────┼─────────────────────────────┤
| │ keep-last | │ 7 |     |     | │   |     |
| ----------- | --- | --- | --- | --- | --- |
├────────────────┼─────────────────────────────┤
| │ prune-schedule | │ daily |     |     | │   |     |
| ---------------- | ------- | --- | --- | --- | --- |
└────────────────┴─────────────────────────────┘
Finally,itispossibletoremovethedatastoreconfiguration:
| # proxmox-backup-manager |     | datastore | remove | store1 |     |
| ------------------------ | --- | --------- | ------ | ------ | --- |
(cid:174) Note
The above command removes only the datastore configuration. It does not delete any data
fromtheunderlyingdirectory.
FileLayout
Aftercreatingadatastore,thefollowingdefaultlayoutwillappear:
| # ls -arilh /backup/disk1/store1 |          |        |         |               |         |
| -------------------------------- | -------- | ------ | ------- | ------------- | ------- |
| 276493 -rw-r--r--                | 1 backup | backup |         | 0 Jul 8 12:35 | .lock   |
| 276490 drwxr-x---                | 1 backup | backup | 1064960 | Jul 8 12:35   | .chunks |
.lockisanemptyfileusedforprocesslocking.
The .chunks directory contains folders, starting from 0000 and increasing in hexadecimal values
until ffff. These directories will store the chunked data, categorized by checksum, after a backup
operationhasbeenexecuted.
| # ls -arilh /backup/disk1/store1/.chunks |          |        |      |             |      |
| ---------------------------------------- | -------- | ------ | ---- | ----------- | ---- |
| 545824 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | ffff |
| 545823 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fffe |
| 415621 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fffd |
| 415620 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fffc |
| 353187 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fffb |
| 344995 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fffa |
| 144079 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fff9 |
| 144078 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | fff8 |
| 1.4.4.077 drwxr-x---                     | 2 backup | backup | 4.0K | Jul 8 12:35 | fff7 |
| 403180 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 000c |
| 403179 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 000b |
| 403177 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 000a |
| 402530 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0009 |
| 402513 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0008 |
| 402509 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0007 |
| 276509 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0006 |
| 276508 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0005 |
| 276507 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0004 |
| 276501 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0003 |
| 276499 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0002 |
| 276498 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0001 |
| 276494 drwxr-x---                        | 2 backup | backup | 4.0K | Jul 8 12:35 | 0000 |
| 276489 drwxr-xr-x                        | 3 backup | backup | 4.0K | Jul 8 12:35 | ..   |
| 276490 drwxr-x---                        | 1 backup | backup | 1.1M | Jul 8 12:35 | .    |
Onceyou’veuploadedsomebackupsorcreatednamespaces,youmayseethebackuptype(ct,vm,
host)andthestartofthenamespacehierarchy(ns).
5.2.2 BackupNamespaces
Adatastorecanhostmanybackups,aslongastheunderlyingstorageislargeenoughandprovides
theperformancerequiredforauser’susecase. However,withoutanyhierarchyorseparation,it’s
5.2. Datastore 41

ProxmoxBackupDocumentation,Release4.2.8‐1
easytorunintonamingconflicts,especiallywhenusingthesamedatastoreformultipleProxmox
VEinstancesormultipleusers.
Thebackupnamespacehierarchyallowsyoutoclearlyseparatedifferentusersorbackupsources
ingeneral,avoidingnamingconflictsandprovidingawell-organizedbackupcontentview.
Eachnamespacelevelcanhostanybackuptype,CT,VMorHost,butalsoothernamespaces,upto
adepthof8levels,wheretherootnamespaceisthefirstlevel.
NamespacePermissions
Youcanmakethepermissionconfigurationofadatastoremorefine-grainedbysettingpermissions
onlyonaspecificnamespace.
To view a datastore, you need a permission that has at least an AUDIT, MODIFY, READ or BACKUP
privilegeonanynamespaceitcontains.
Tocreateordeleteanamespace,yourequirethemodifyprivilegeontheparentnamespace. Thus,
toinitiallycreatenamespaces,youneedtohaveapermissionwithanaccessrolethatincludesthe
MODIFY privilegeonthedatastoreitself.
For backup groups, the existing privilege rules still apply. You either need a privileged enough
permissionortobetheownerofthebackupgroup;nothingchangedhere.
MovingNamespacesandGroups
Backupgroupscanbemovedbetweennamespaceswithinthesamedatastore. Thisisusefulfor
reorganizingbackuphierarchieswithouthavingtore-runbackups.
Asinglegroupcanbemovedwithgroup move. Torelocateanentirenamespacesubtree(including
allchildnamespacesandtheirgroups),usenamespace move.
# proxmox-backup-client group move <type>/<id> --ns <source> --target-ns <target> --
,→repository <repo>
# proxmox-backup-client namespace move <source> --target-ns <target> --repository <repo>
Ifthetargetnamespacealreadyexists,groupsaremovedintoit. Whenagroupwiththesametype
andIDalreadyexistsinthetargetandmerge-groupsisenabled,thesnapshotsaremergedinto
theexistinggroupprovided:
• bothgroupshavethesameowner
• theoldestsourcesnapshotisnewerthanthenewesttargetsnapshot
Groupsthatcannotbemergedorlockedareskippedandreportedinthetasklog. Theyremainat
thesourceandcanberetriedindividuallywithgroup move.
(cid:174) Note
With defaults, namespace move merges into existing target groups (merge-groups=true)
and removes source namespaces once they are empty (delete-source=true). Pass
--merge-groups falseor--delete-source falsetooptout.
Optionalparametersfornamespace move:
merge-groups
Allowmergingsnapshotsintogroupsthatalreadyexistinthetargetnamespacewiththesame
typeandID.Defaultstotrue.
max-depth
Limits how many levels of child namespaces below the source are included. When not set,
theentiresubtreeismoved.
42 Chapter5. BackupStorage

ProxmoxBackupDocumentation,Release4.2.8‐1
delete-source
Controlswhetherthesourcenamespacedirectoriesareremovedafterallgroupshavebeen
movedout. Defaultstotrue. Settofalsetokeepthe(nowempty)sourcenamespacestructure.
Requiredprivileges:
• group move: DATASTORE_PRUNEonthesourcenamespaceandDATASTORE_BACKUPonthe
targetnamespace,plusownershipofthebackupgroup;orDATASTORE_MODIFYonboth.
• namespace move: DATASTORE_MODIFY on the parent of both the source and the target
namespace.
5.2.3 Options
Thereareafewper-datastoreoptions:
• Notificationmodeandlegacynotificationsettings
• MaintenanceMode
• MaintenanceMode
• NotificationThresholds(S3datastoresonly)
• ThresholdResetSchedule(S3datastoresonly)
• Verificationofincomingbackups
5.2. Datastore 43

ProxmoxBackupDocumentation,Release4.2.8‐1
Tuning
Therearesometuningrelatedoptionsforthedatastorethataremoreadvanced:
• chunk-order: Chunkorderforverify&tapebackup:
YoucanspecifytheorderinwhichProxmoxBackupServeriteratesthechunkswhendoinga
verifyorbackinguptotape. Thetwooptionsare:
– inode(default): Sortsthechunksbyinodenumberofthefilesystembeforeiteratingover
them. Thisshouldbefineformoststorages,especiallyspinningdisks.
– none Iterates the chunks in the order they appear in the index file (.fidx/.didx). While
this might slow down iterating on many slow storages, on very fast ones (for example:
NVMEs) the collecting and sorting can take more time than gained through the sorted
iterating. Thisoptioncanbesetwith:
# proxmox-backup-manager datastore update <storename> --tuning 'chunk-order=none'
• sync-level: Datastorefsynclevel:
Youcansetthelevelofsyncingonthedatastoreforchunks,whichinfluencesthecrashresis-
tanceofbackupsincaseofapowerlossorhardshutoff. Therearecurrentlythreelevels:
– none: Doesnotdoanysyncingwhenwritingchunks. ThisisfastandnormallyOK,since
thekerneleventuallyflusheswritesontothedisk. Thekernelsysctlsdirty_expire_centisecs
anddirty_writeback_centisecsareusedtotunethatbehaviour,whilethedefaultistoflush
olddataafter~30s.
– filesystem(default): Thistriggersasyncfs(2)afterabackup,butbeforethetaskreturns
OK. This way it is ensured that the written backups are on disk. This is a good balance
between speed and consistency. Note that the underlying storage device still needs to
protectitselfagainstpowerlosstoflushitsinternalephemeralcachestothepermanent
storagelayer.
– fileWiththismode,afsyncistriggeredoneverychunkinsertion,whichmakessureeach
and every chunk reaches the disk as soon as possible. While this reaches the highest
levelofconsistency,formanystorages(especiallyslowerones)thiscomesatthecostof
speed. Formanyusersthefilesystemmodeisbettersuited,butforveryfaststoragesthis
modecanbeOK.
Thiscanbesetwith:
# proxmox-backup-manager datastore update <storename> --tuning 'sync-level=filesystem'
• gc-atime-safety-check: Datastore GC atime update safety check: You can explicitly en-
ableordisabletheatimeupdatesafetycheckperformedondatastorecreationandgarbage
collection. This checks if atime updates are handled as expected by garbage collection and
thereforeavoidstheriskofdatalossbyunexpectedfilesystembehavior. Itisrecommended
tosetthistoenabled,whichisalsothedefaultvalue.
• gc-atime-cutoff: DatastoreGCatimecutoffforchunkcleanup: Thisallowstosetthecutoff
forwhichachunkisstillconsideredin-useduringphase2ofgarbagecollection(givennoolder
writers). Iftheatimeofthechunkisoutsidetherange,itwillberemoved.
• gc-cache-capacity: Datastore GC least recently used cache capacity: Allows to control
thecachecapacityusedtokeeptrackofchunksforwhichtheaccesstimehasalreadybeen
updatedduringphase1ofgarbagecollection. ThisavoidsmultipleupdatesandincreasesGC
runtimeperformance. HighervaluescanreduceGCruntimeatthecostofincreasememory
usage, settingthevalueto0disablescaching. Thegivenvaluesetsthenumberofavailable
cacheslots,1048576(=1024*1024)beingthedefault,8388608(=8192*1024)themaximum
value.
• default-verification-workers and default-verification-readers: Define the
default number of threads used for verification and reading of chunks, respectively. By de-
fault,4threadsareusedforverificationand1threadisusedforreading.
44 Chapter5. BackupStorage

ProxmoxBackupDocumentation,Release4.2.8‐1
Ifyouwanttosetmultipletuningoptionssimultaneously, youcanseparatethemwithacomma,
likethis:
# proxmox-backup-manager datastore update <storename> --tuning 'sync-level=filesystem,chunk-
,→order=none'
5.3 Ransomware Protection & Recovery
Ransomwareisatypeofmalwarethatencryptsfilesuntilaransomispaid. ProxmoxBackupServer
includes features that help mitigate and recover from ransomware attacks by offering off-server
andoff-sitesynchronizationandeasyrestorationfrombackups.
5.3.1 Built‐inProtection
ProxmoxBackupServerdoesnotrewritedataforexistingblocks. Thismeansthatacompromised
Proxmox VE host or any other compromised system that uses the client to back up data cannot
corruptormodifyexistingbackupsinanyway.
5.3.2 The3‐2‐1RulewithProxmoxBackupServer
The 3-2-1 rule is simple but effective in protecting important data from all sorts of threats, be it
fires, natural disasters or attacks on your infrastructure by adversaries. In short, the rule states
thatoneshouldcreate3backupsonatleast2differenttypesofstoragemedia,ofwhich1copyis
keptoff-site.
ProxmoxBackupServerprovidestoolsforstoringextracopiesofbackupsinremotelocationsand
onvarioustypesofmedia.
BysettinguparemoteProxmoxBackupServer,youcantakeadvantageoftheremotesyncjobsfea-
tureandeasilycreateoff-sitecopiesofyourbackups. Thisisrecommended,sinceoff-siteinstances
arelesslikelytobeinfectedbyransomwareinyourlocalnetwork. Youcanconfiguresyncjobsto
not remove snapshots if they vanished on the remote-source to avoid that an attacker that took
over the source can cause deletions of backups on the target hosts. If the source-host became
victim of a ransomware attack, there is a good chance that sync jobs will fail, triggering an error
notification.
It is also possible to create tape backups as a second storage medium. This way, you get an ad-
ditional copy of your data on a different storage medium designed for long-term storage. Addi-
tionally,itcaneasilybemovedaround,beittoanoff-sitelocationor,forexample,intoanon-site
fireproofvaultforquickeraccess.
5.3.3 RestrictiveUser&AccessManagement
ProxmoxBackupServeroffersacomprehensiveandfine-graineduserandaccessmanagementsys-
tem. The Datastore.Backup privilege, for example, allows only to create, but not to delete or alter
existingbackups.
Thebestwaytoleveragethisaccesscontrolsystemisto:
• UseseparateAPItokensforeachhostorProxmoxVEClusterthatshouldbeabletobackdata
uptoaProxmoxBackupServer.
• ConfigureonlyminimalpermissionsforsuchAPItokens. Theyshouldonlyhaveasingleper-
missionthatgrantstheDataStoreaccessroleonaverynarrowACLpaththatisrestrictedtoa
specificnamespaceonaspecificdatastore,forexample/datastore/tank/pve-abc-cluster.
5.3. RansomwareProtection&Recovery 45

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:98) Tip
Onebestpracticetoprotectagainstransomwareisnottograntdeletepermissions,buttoper-
formbackuppruningdirectlyonProxmoxBackupServerusingprunejobs.
Pleasenotethatthesamealsoappliesforsyncjobs. Bylimitingasyncuser’soranaccesstoken’s
righttoonlywritebackups,notdeletethem,compromisedclientscannotdeleteexistingbackups.
5.3.4 RansomwareDetection
AProxmoxBackupServermightstillgetcompromisedwithininsecurenetworks,ifphysicalaccess
to the server is attained, or due to weak or insufficiently protected credentials. If that happens,
and your on-site backups are encrypted by ransomware, the SHA-256 checksums of the backups
willnotmatchthepreviouslyrecordedonesanymore,hence,restoringthebackupwillfail.
Todetectransomwareinsideacompromisedguest,itisrecommendedtofrequentlytestrestoring
andbootingbackups. Makesuretorestoretoanewguestandnottooverwriteyourcurrentguest.
Inthecaseofmanybacked-upguests,itisrecommendedtoautomatethisrestoretesting. Ifthisis
notpossible,restoringrandomsamplesfromthebackupsperiodically(forexample,onceaweek
ormonth),isadvised’.
Inordertobeabletoreactquicklyincaseofaransomwareattack,itisrecommendedtoregularly
testrestoringfromyourbackups. Makesuretorestoretoanewguestandnottooverwriteyour
currentguest. Restoringmanyguestsatoncecanbecumbersome,whichiswhyitisadvisableto
automate this task and verify that your automated process works. If this is not feasible, it is rec-
ommendedtorestorerandomsamplesfromyourbackups. Whilecreatingbackupsisimportant,
verifyingthattheyworkisequallyimportant. Thisensuresthatyouareabletoreactquicklyincase
ofanemergencyandkeepsdisruptionofyourservicestoaminimum.
VerificationjobscanalsoassistindetectingaransomwarepresenceonaProxmoxBackupServer.
Sinceverificationjobsregularlycheckifallbackupsstillmatchthechecksumsonrecord,theywill
starttofailifaransomwarestartstoencryptexistingbackups. Pleasebeaware,thatanadvanced
enoughransomwarecouldcircumventthismechanism. Hence, considerverificationjobsonlyas
anadditional,butnotasufficientprotectionmeasure.
5.3.5 GeneralPreventionMethodsandBestPractices
Itisrecommendedtotakeadditionalsecuritymeasures,apartfromtheonesofferedbyProxmox
BackupServer. Theserecommendationsinclude,butarenotlimitedto:
• Keepingthefirmwareandsoftwareup-to-datetopatchexploitsandvulnerabilities(suchas
SpectreorMeltdown).
• Followingsafeandsecurenetworkpractices,forexampleusingloggingandmonitoringtools
and dividing your network so that infrastructure traffic and user or even public traffic are
separated,forexamplebysettingupVLANs.
• Setupalong-termretention. Sincesomeransomwaremightlaydormantacoupleofdaysor
weeksbeforestartingtoencryptdata,itcanbethatolder,existingbackupsarecompromised.
Thus,itisimportanttokeepatleastafewbackupsoverlongerperiodsoftime.
Formoreinformationonhowtoavoidransomwareattacksandwhattodoincaseofaransomware
infection, see official government recommendations like CISA’s (USA) guide or EU resources like
ENSIA’sThreatLandscapeforRansomwareAttacksornomoreransom.org.
46 Chapter5. BackupStorage

CHAPTER
SIX
USER MANAGEMENT
6.1 User Configuration
ProxmoxBackupServersupportsseveralauthenticationrealms,andyouneedtochoosetherealm
whenyouaddanewuser. Possiblerealmsare:
pam
LinuxPAMstandardauthentication. UsethisifyouwanttoauthenticateasaLinux
systemuser. Theusersneedstoalreadyexistonthehostsystem.
pbs
Proxmox Backup Server realm. This type stores hashed passwords in /etc/
proxmox-backup/shadow.json.
openid
OpenID Connect server. Users can authenticate against an external OpenID Con-
nectserver.
47

ProxmoxBackupDocumentation,Release4.2.8‐1
ldap
|     | LDAPserver. | UserscanauthenticateagainstexternalLDAPservers. |     |     |     |     |     |
| --- | ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
ad
Active Directory server. Users can authenticate against external Active Directory
servers.
Afterinstallation,thereisasingleuser,root@pam,whichcorrespondstotheUnixsuperuser. User
configurationinformationisstoredinthefile/etc/proxmox-backup/user.cfg. Youcanusethe
proxmox-backup-managercommand-linetooltolistormanipulateusers:
| # proxmox-backup-manager |     | user list |     |     |     |     |     |
| ------------------------ | --- | --------- | --- | --- | --- | --- | --- |
┌─────────────┬────────┬────────┬───────────┬──────────┬────────────────┬────────────────────┐
│ userid │ enable │ expire │ firstname │ lastname │ email │ comment │
╞═════════════╪════════╪════════╪═══════════╪══════════╪════════════════╪════════════════════╡
| │ root@pam | │   | 1 │ │ | │   | │   | │   | Superuser | │   |
| ---------- | --- | ----- | --- | --- | --- | --------- | --- |
└─────────────┴────────┴────────┴───────────┴──────────┴────────────────┴────────────────────┘
Thesuperuserhasfulladministrationrightsoneverything,soit’srecommendedtoaddotherusers
withlessprivileges. Youcanaddanewuserwiththeuser createsubcommandorthroughthe
webinterface,undertheUserManagementtabofConfiguration->AccessControl. Thecreate
subcommand lets you specify many options like --email or --password. You can update or
changeanyuserpropertiesusingtheuser updatesubcommandlater(EditintheGUI):
# proxmox-backup-manager user create john@pbs --email john@example.com
# proxmox-backup-manager user update john@pbs --firstname John --lastname Smith
# proxmox-backup-manager user update john@pbs --comment "An example user."
Theresultinguserlistlookslikethis:
| # proxmox-backup-manager |     | user list |     |     |     |     |     |
| ------------------------ | --- | --------- | --- | --- | --- | --- | --- |
┌──────────┬────────┬────────┬───────────┬──────────┬──────────────────┬──────────────────┐
│ userid │ enable │ expire │ firstname │ lastname │ email │ comment │
╞══════════╪════════╪════════╪═══════════╪══════════╪══════════════════╪══════════════════╡
│ john@pbs │ 1 │ │ John │ Smith │ john@example.com │ An example user. │
├──────────┼────────┼────────┼───────────┼──────────┼──────────────────┼──────────────────┤
| │ root@pam | │ 1 │ | │   | │   | │   | │   | Superuser | │   |
| ---------- | ----- | --- | --- | --- | --- | --------- | --- |
└──────────┴────────┴────────┴───────────┴──────────┴──────────────────┴──────────────────┘
Newlycreatedusersdonothaveanypermissions. PleasereadtheAccessControl sectiontolearn
howtosetaccesspermissions.
Youcandisableauseraccountbysetting--enableto0:
| # proxmox-backup-manager |     | user update | john@pbs --enable | 0   |     |     |     |
| ------------------------ | --- | ----------- | ----------------- | --- | --- | --- | --- |
Orcompletelyremoveauserwith:
| # proxmox-backup-manager |     | user remove | john@pbs |     |           |                |     |
| ------------------------ | --- | ----------- | -------- | --- | --------- | -------------- | --- |
| 48                       |     |             |          |     | Chapter6. | UserManagement |     |

ProxmoxBackupDocumentation,Release4.2.8‐1
6.2 API Tokens
Any authenticated user can generate API tokens, which can in turn be used to configure various
clients,insteadofdirectlyprovidingtheusernameandpassword.
APItokensservetwopurposes:
1. Easyrevocationincaseclientgetscompromised
2. Limitpermissionsforeachclient/tokenwithintheusers’permission
An API token consists of two parts: an identifier consisting of the user name, the realm and a
tokenname(user@realm!tokenname),andasecretvalue. Bothneedtobeprovidedtotheclient
inplaceoftheuserID(user@realm)andtheuserpassword,respectively.
TheAPItokenispassedfromtheclienttotheserverbysettingtheAuthorizationHTTPheader
withmethodPBSAPITokentothevalueTOKENID:TOKENSECRET.
YoucangeneratetokensfromtheGUIorbyusingproxmox-backup-manager:
# proxmox-backup-manager user generate-token john@pbs client1
Result: {
"tokenid": "john@pbs!client1",
"value": "d63e505a-e3ec-449a-9bc7-1da610d4ccde"
}
6.2. APITokens 49

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
Thedisplayedsecretvalueneedstobesaved,sinceitcannotbedisplayedagainaftergenerating
theAPItoken.
Theuser list-tokenssub-commandcanbeusedtodisplaytokensandtheirmetadata:
# proxmox-backup-manager user list-tokens john@pbs
┌──────────────────┬────────┬────────┬─────────┐
│ tokenid │ enable │ expire │ comment │
╞══════════════════╪════════╪════════╪═════════╡
│ john@pbs!client1 │ 1 │ │ │
└──────────────────┴────────┴────────┴─────────┘
Similarly,theuser delete-tokensubcommandcanbeusedtodeleteatokenagain.
(cid:193) Warning
Direct/manualeditstotoken.shadowmaytakeupto60seconds(orlongerinedgecases)to
takeeffectduetocaching. Restartservicesforimmediateeffectofmanualedits.
NewlygeneratedAPItokensdon’thaveanypermissions. Pleasereadthenextsectiontolearnhow
tosetaccesspermissions.
6.3 Access Control
By default, new users and API tokens do not have any permissions. Instead you need to specify
whatisallowedandwhatisnot.
ProxmoxBackupServerusesarole-andpath-basedpermissionmanagementsystem. Anentryin
the permissions table allows a user, group or token to take on a specific role when accessing an
’object’or’path’. Thismeansthatsuchanaccessrulecanberepresentedasatripleof’(path,user,
role)’, ’(path, group, role)’ or ’(path, token, role)’, with the role containing a set of allowed actions,
andthepathrepresentingthetargetoftheseactions.
6.3.1 Privileges
Privileges are the building blocks of access roles. They are internally used to enforce the actual
permissionchecksintheAPI.
Wecurrentlysupportthefollowingprivileges:
Sys.Audit
Sys.Auditallowsausertoknowaboutthesystemanditsstatus.
Sys.Modify
Sys.Modifyallowsausertomodifysystem-levelconfigurationandapplyupdates.
Sys.PowerManagement
Sys.Modifyallowsausertopower-offandrebootthesystem.
Datastore.Audit
Datastore.Auditallowsausertoknowaboutadatastore,includingreadingtheconfiguration
entryandlistingitscontents.
Datastore.Allocate
Datastore.Allocateallowsausertocreateordeletedatastores.
Datastore.Modify
Datastore.Modifyallowsausertomodifyadatastoreanditscontents,andtocreateordelete
namespacesinsideadatastore.
50 Chapter6. UserManagement

ProxmoxBackupDocumentation,Release4.2.8‐1
Datastore.Read
Datastore.Readallowsausertoreadarbitrarybackupcontents,independentofthebackup
groupowner.
Datastore.Verify
Allowsverifyingthebackupsnapshotsinadatastore.
Datastore.Backup
Datastore.Backupallowsausercreatenewbackupsnapshotsandalsoprovidestheprivileges
ofDatastore.ReadandDatastore.Verify,butonlyifthebackupgroupisownedbytheuseror
oneofitstokens.
Datastore.Prune
Datastore.Pruneallowsausertodeletesnapshots,butadditionallyrequiresbackupowner-
ship.
Permissions.Modify
Permissions.ModifyallowsausertomodifyACLs.
(cid:174) Note
AusercanalwaysconfigureprivilegesfortheirownAPItokens,astheywillbelimitedby
theusersprivilegesanyway.
Remote.Audit
Remote.Auditallowsausertoreadtheremoteandthesyncconfigurationentries.
Remote.Modify
Remote.Modifyallowsausertomodifytheremoteconfiguration.
Remote.Read
Remote.ReadallowsausertoreaddatafromaconfiguredRemote.
Sys.Console
Sys.Console allows a user to access the system’s console, note that for all but root@pam a
validsystemloginisstillrequired.
Tape.Audit
Tape.Audit allows a user to read the configuration and status of tape drives, changers and
backups.
Tape.Modify
Tape.Modifyallowsausertomodifytheconfigurationoftapedrives,changersandbackups.
Tape.Write
Tape.Writeallowsausertowritetoatapemedia.
Tape.Read
Tape.Readallowsausertoreadtapebackupconfigurationandcontentsfromatapemedia.
Realm.Allocate
Realm.Allocate allows a user to view, create, modify and delete authentication realms for
users.
6.3.2 AccessRoles
Anaccessrolecombinesoneormoreprivilegesintosomethingthatcanbeassignedtoauseror
APItokenonanobjectpath.
Currently,thereareonlybuilt-inroles,meaningyoucannotcreateyourown,customrole.
Thefollowingrolesexist:
6.3. AccessControl 51

ProxmoxBackupDocumentation,Release4.2.8‐1
NoAccess
DisableAccess-nothingisallowed.
Admin
Candoanything,ontheobjectpathassigned.
Audit
Canviewthestatusandconfigurationofthings,butisnotallowedtochangesettings.
DatastoreAdmin
Candoanythingonexistingdatastores.
DatastoreAudit
Can view datastore metrics, settings and list content. But is not allowed to read the actual
data.
DatastoreReader
Caninspectadatastore’sornamespace’scontentanddorestores.
DatastoreBackup
Canbackupandrestoreownedbackups.
DatastorePowerUser
Canbackup,restore,andpruneownedbackups.
RemoteAdmin
Candoanythingonremotes.
RemoteAudit
Canviewremotesettings.
RemoteSyncOperator
Isallowedtoreaddatafromaremote.
TapeAdmin
Candoanythingrelatedtotapebackup.
TapeAudit
Canviewtape-relatedmetrics,configurationandstatus.
TapeOperator
Candotapebackupandrestore,butcannotchangeanyconfiguration.
TapeReader
Canreadandinspecttapeconfigurationandmediacontent.
6.3.3 ObjectsandPaths
Access permissions are assigned to objects, such as a datastore, namespace or some system re-
sources.
We use filesystem-like paths to address these objects. These paths form a natural tree, and per-
missionsofhigherlevels(shorterpaths)canoptionallybepropagateddownwithinthishierarchy.
Pathscanbetemplated,meaningtheycanrefertotheactualidofaconfigurationentry. Whenan
APIcallrequirespermissionsonatemplatedpath,thepathmaycontainreferencestoparameters
oftheAPIcall. Thesereferencesarespecifiedincurlybrackets.
Someexamplesare:
52 Chapter6. UserManagement

ProxmoxBackupDocumentation,Release4.2.8‐1
/datastore AccesstoalldatastoresonaProxmoxBackupServer
/datastore/{store} AccesstoaspecificdatastoreonaProxmoxBackupServer
/datastore/{store}/{ns} Accesstoaspecificnamespaceonaspecificdatastore
/remote Accesstoallremoteentries
/system/network Accesstoconfigurethehostnetwork
/tape/ Accesstotapedevices,poolsandjobs
/access/users Useradministration
/access/openid/{id} AdministrativeaccesstoaspecificOpenIDConnectrealm
Inheritance
As mentioned earlier, object paths form a file system like tree, and permissions can be inherited
byobjectsdownthattreethroughthepropagateflag,whichissetbydefault. Weusethefollowing
inheritancerules:
• PermissionsforAPItokensarealwayslimitedtothoseoftheuser.
• Permissionsondeeper,morespecificlevelsreplacethoseinheritedfromanupperlevel.
6.3.4 Configuration&Management
Accesspermissioninformationisstoredin/etc/proxmox-backup/acl.cfg. Thefilecontains5
fields,separatedusingacolon(’:’) asadelimiter. Atypicalentrytakestheform:
acl:1:/datastore:john@pbs:DatastoreBackup
Thedatarepresentedineachfieldisasfollows:
1. aclidentifier
2. A1or0,representingwhetherpropagationisenabledordisabled,respectively
3. The object on which the permission is set. This can be a specific object (single datastore,
remote,etc.) oratoplevelobject,whichwithpropagationenabled,representsallchildrenof
theobjectalso.
4. Theuser(s)/token(s)forwhichthepermissionisset
5. Therolebeingset
YoucanmanagepermissionsviaConfiguration->AccessControl->Permissionsinthewebin-
terface. Likewise, you can use the acl subcommand to manage and monitor user permissions
fromthecommandline. Forexample,thecommandbelowwilladdtheuserjohn@pbsasaData-
storeAdminforthedatastorestore1,locatedat/backup/disk1/store1:
# proxmox-backup-manager acl update /datastore/store1 DatastoreAdmin --auth-id john@pbs
YoucanlisttheACLsofeachuser/tokenusingthefollowingcommand:
# proxmox-backup-manager acl list
┌──────────┬───────────────────┬───────────┬────────────────┐
│ ugid │ path │ propagate │ roleid │
╞══════════╪═══════════════════╪═══════════╪════════════════╡
(continuesonnextpage)
6.3. AccessControl 53

ProxmoxBackupDocumentation,Release4.2.8‐1
(continuedfrompreviouspage)
| │ john@pbs | │ /datastore/store1 | │   | 1 │ DatastoreAdmin | │   |     |
| ---------- | ------------------- | --- | ------------------ | --- | --- |
└──────────┴───────────────────┴───────────┴────────────────┘
Asingleuser/tokencanbeassignedmultiplepermissionsetsfordifferentdatastores.
(cid:174) Note
Namingconventionisimportanthere. Fordatastoresonthehost,youmustusetheconvention
/datastore/{storename}. For example, to set permissions for a datastore mounted at /
mnt/backup/disk4/store2, you would use /datastore/store2 for the path. For remote
stores,usetheconvention/remote/{remote}/{storename},where{remote}signifiesthe
nameoftheremote(seeRemotebelow)and{storename}isthenameofthedatastoreonthe
remote.
6.3.5 APITokenPermissions
APItokenpermissionsarecalculatedbasedonACLscontainingtheirID,independentlyofthoseof
theircorrespondinguser. Theresultingpermissionsetonagivenpathisthenintersectedwiththat
ofthecorrespondinguser.
Inpracticethismeans:
1. APItokensrequiretheirownACLentries
2. APItokenscanneverdomorethantheircorrespondinguser
6.3.6 EffectivePermissions
To calculate and display the effective permission set of a user or API token, you can use the
| proxmox-backup-manager |     | user | permissioncommand: |     |     |
| ---------------------- | --- | ---- | ------------------ | --- | --- |
# proxmox-backup-manager user permissions john@pbs --path /datastore/store1
| Privileges | with (*) have | the propagate | flag set |     |     |
| ---------- | ------------- | ------------- | -------- | --- | --- |
Path: /datastore/store1
| - Datastore.Audit  | (*) |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
| - Datastore.Backup | (*) |     |     |     |     |
| - Datastore.Modify | (*) |     |     |     |     |
| - Datastore.Prune  | (*) |     |     |     |     |
| - Datastore.Read   | (*) |     |     |     |     |
| - Datastore.Verify | (*) |     |     |     |     |
# proxmox-backup-manager acl update /datastore/store1 DatastoreBackup --auth-id 'john@pbs!
,→client1'
# proxmox-backup-manager user permissions 'john@pbs!client1' --path /datastore/store1
| Privileges | with (*) have | the propagate | flag set |     |     |
| ---------- | ------------- | ------------- | -------- | --- | --- |
Path: /datastore/store1
| - Datastore.Backup | (*) |                |     |     |     |
| ------------------ | --- | -------------- | --- | --- | --- |
| 6.4 Two‐Factor     |     | Authentication |     |     |     |
6.4.1 Introduction
Withsimpleauthentication,onlyapassword(singlefactor)isrequiredtosuccessfullyclaimaniden-
tity(authenticate),forexample,tobeabletologinasroot@pamonaspecificinstanceofProxmox
Backup Server. In this case, if the password gets leaked or stolen, anybody can use it to log in -
eveniftheyshouldnotbeallowedtodoso.
Withtwo-factorauthentication(TFA),auserisaskedforanadditionalfactortoverifytheirauthen-
ticity. Ratherthanrelyingonsomethingonlytheuserknows(apassword),thisextrafactorrequires
somethingonlytheuserhas,forexample,apieceofhardware(securitykey)orasecretsavedon
the user’s smartphone. This prevents a remote user from gaining unauthorized access to an ac-
count,aseveniftheyhavethepassword,theywillnothaveaccesstothephysicalobject(second
factor).
| 54  |     |     |     | Chapter6. | UserManagement |
| --- | --- | --- | --- | --------- | -------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
6.4.2 AvailableSecondFactors
You can set up multiple second factors, in order to avoid a situation in which losing your smart-
phoneorsecuritykeylocksyououtofyouraccountpermanently.
ProxmoxBackupServersupportsthreedifferenttwo-factorauthenticationmethods:
• TOTP(Time-basedOne-TimePassword). Ashortcodederivedfromasharedsecretandthe
currenttime,itchangesevery30seconds.
• WebAuthn (Web Authentication). A general standard for authentication. It is implemented
by various security devices, like hardware keys or trusted platform modules (TPM) from a
computerorsmartphone.
• Single use Recovery Keys. A list of keys which should either be printed out and locked in a
secureplaceorsaveddigitallyinanelectronicvault. Eachkeycanbeusedonlyonce. These
areperfectforensuringthatyouarenotlockedout, evenifallofyourothersecondfactors
arelostorcorrupt.
6.4.3 Setup
TOTP
There is no server setup required. Simply install a TOTP app on your smartphone (for example,
FreeOTP)andusetheProxmoxBackupServerweb-interfacetoaddaTOTPfactor.
6.4. Two‐FactorAuthentication 55

ProxmoxBackupDocumentation,Release4.2.8‐1
WebAuthn
ForWebAuthntowork,youneedtohavetwothings:
• AtrustedHTTPScertificate(forexample,byusingLet’sEncrypt). Whileitprobablyworkswith
anuntrustedcertificate,somebrowsersmaywarnorrefuseWebAuthnoperationsifitisnot
trusted.
• Setup the WebAuthn configuration (see Configuration -> Other in the Proxmox Backup
Serverwebinterface). Thiscanbeauto-filledinmostsetups.
Onceyouhavefulfilledbothoftheserequirements,youcanaddaWebAuthnconfigurationinthe
TwoFactorAuthenticationtaboftheAccessControlpanel.
RecoveryKeys
Recovery key codes do not need any preparation; you can simply createa set of recovery keys in
theTwoFactorAuthenticationtaboftheAccessControlpanel.
(cid:174) Note
Therecanonlybeonesetofsingle-userecoverykeysperuseratanytime.
6.4.4 TFAandAutomatedAccess
Two-factorauthenticationisonlyimplementedfortheweb-interface. YoushoulduseAPITokensfor
allotherusecases,especiallynon-interactiveones(forexample,addingaProxmoxBackupServer
toProxmoxVEasastorage).
6.4.5 LimitsandLockoutofTwo‐FactorAuthentication
Asecondfactorismeanttoprotectusersiftheirpasswordissomehowleakedorguessed. How-
ever, some factors could still be broken by brute force. For this reason, users will be locked out
aftertoomanyfailed2ndfactorloginattempts.
ForTOTP,8failedattemptswilldisabletheuser’sTOTPfactors. Theyareunlockedwhenloggingin
witharecoverykey. IfTOTPwastheonlyavailablefactor,admininterventionisrequired,anditis
highlyrecommendedtorequiretheusertochangetheirpasswordimmediately.
SinceFIDO2/Webauthnandrecoverykeysarelesssusceptibletobruteforceattacks,thelimitthere
ishigher(100tries),butallsecondfactorsareblockedforanhourwhenexceeded.
An admin can unlock a user’s Two-Factor Authentication at any time via the user list view in the
webUI,orusingthecommandline:
proxmox-backup-manager user tfa unlock joe@pbs
56 Chapter6. UserManagement

ProxmoxBackupDocumentation,Release4.2.8‐1
6.5 Authentication Realms
6.5.1 LinuxPAM
Linux PAM is a framework for system-wide user authentication. These users are created on the
hostsystemwithcommandssuchasadduser.
If PAM users exist on the host system, corresponding entries can be added to Proxmox Backup
Server,toallowtheseuserstologinviatheirsystemusernameandpassword.
6.5.2 ProxmoxBackupauthenticationserver
This is a Unix-like password store, which stores hashed passwords in /etc/proxmox-backup/
shadow.json. PasswordsarehashedusingtheSHA-256hashingalgorithm.
This is the most convenient realm for small-scale (or even mid-scale) installations, where users
do not need access to anything outside of Proxmox Backup Server. In this case, users are fully
managedbyProxmoxBackupServerandareabletochangetheirownpasswordsviatheGUI.
6.5.3 LDAP
ProxmoxBackupServercanutilizeexternalLDAPserversforuserauthentication. Toachievethis,
arealmofthetypeldaphastobeconfigured.
In LDAP, users are uniquely identified by their domain (dn). For instance, in the following
LDIF dataset, the user user1 has the unique domain uid=user1,ou=People,dc=ldap-test,
dc=com:
# user1 of People at ldap-test.com
dn: uid=user1,ou=People,dc=ldap-test,dc=com
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
uid: user1
cn: Test User 1
sn: Testers
description: This is the first test user.
In in similar manner, Proxmox Backup Server uses user identifiers (userid) to uniquely identify
users. Thus,itisnecessarytoestablishamappingbetweenaProxmoxBackupServeruseridand
anLDAPdn. Thismappingisestablishedbytheuser-attrconfigurationparameter-itcontains
thenameoftheLDAPattributecontainingavalidProxmoxBackupServeruseridentifier.
For the example above, setting user-attr to uid will have the effect that the user
user1@<realm-name> will be mapped to the LDAP entity uid=user1,ou=People,
dc=ldap-test,dc=com. On user login, Proxmox Backup Server will perform a subtree search
under the configured Base Domain (base-dn) to query the user’s dn. Once the dn is known, an
LDAPbindoperationisperformedtoauthenticatetheuseragainsttheLDAPserver.
AsnotallLDAPserversallowanonymoussearchoperations,itispossibletoconfigureabinddomain
(bind-dn)andabindpassword(password). Ifset,ProxmoxBackupServerwillbindtotheLDAP
serverusingthesecredentialsbeforeperforminganysearchoperations.
Afulllistofallconfigurationparameterscanbefoundatdomains.cfg.
(cid:174) Note
In order to allow a particular user to authenticate using the LDAP server, you must also add
themasauserofthatrealminProxmoxBackupServer. Thiscanbecarriedoutautomatically
withsyncing.
6.5. AuthenticationRealms 57

ProxmoxBackupDocumentation,Release4.2.8‐1
6.5.4 ActiveDirectory
ProxmoxBackupServercanalsoutilizeexternalMicrosoftActiveDirectoryserversforuserauthen-
tication. Toachievethis,arealmofthetypeadhastobeconfigured.
For an Active Directory realm, the authentication domain name and the server address must be
specified. Most options from LDAP apply to Active Directory as well, most importantly the bind
credentials bind-dn and password. This is typically required by default for Microsoft Active Di-
rectory. The bind-dn can be specified either in AD-specific user@company.net syntax or the
commonLDAP-DNsyntax.
Theauthenticationdomainnamemustonlybespecifiedifanonymousbindisrequested. Ifbind
credentialsaregiven,thedomainnameisautomaticallyinferredfromthebindusers’basedomain,
asreportedbytheActiveDirectoryserver.
Afulllistofallconfigurationparameterscanbefoundatdomains.cfg.
(cid:174) Note
In order to allow a particular user to authenticate using the Active Directory server, you must
alsoaddthemasauserofthatrealminProxmoxBackupServer. Thiscanbecarriedoutauto-
maticallywithsyncing.
(cid:174) Note
Currently,case-insensitiveusernamesarenotsupported.
UserSynchronizationinLDAP/ADrealms
It is possible to automatically sync users for LDAP and AD-based realms, rather than having to
add them to Proxmox Backup Server manually. Synchronization options can be set in the LDAP
realmconfigurationdialogwindowintheGUIandviatheproxmox-backup-manager ldapand
proxmox-backup-manager adcommands,respectively.
UsersynchronizationcanbestartedintheGUIunderConfiguration>AccessControl>Realms
by selecting a realm and pressing the Sync button. In the sync dialog, some of the default op-
tionssetintherealmconfigurationcanbeoverridden. Alternatively,usersynchronizationcanalso
be started via the proxmox-backup-manager ldap sync and proxmox-backup-manager ad
synccommand,respectively.
58 Chapter6. UserManagement

CHAPTER
SEVEN
|     |     |     | BACKUP | CLIENT | USAGE |
| --- | --- | --- | ------ | ------ | ----- |
Thecommand-lineclientforProxmoxBackupServeriscalledproxmox-backup-client.
| 7.1 Backup | Repository | Locations |     |     |     |
| ---------- | ---------- | --------- | --- | --- | --- |
Theclientusesthefollowingformattospecifyadatastorerepositoryonthebackupserver(where
usernameisspecifiedintheformofuser@realm):
[[username@]server[:port]:]datastore
Thedefaultvalueforusernameisroot@pam. Ifnoserverisspecified,thedefaultisthelocalhost
(localhost).
Youcanspecifyaportifyourbackupserverisonlyreachableonanon-defaultport(forexample,
withNATandportforwardingconfigurations).
NotethatiftheserverusesanIPv6address,youhavetowriteitwithsquarebrackets(forexample,
[fe80::01]).
You can pass the repository with the --repository command-line option, or by setting the
PBS_REPOSITORYenvironmentvariable.
Alternatively,youcanspecifytherepositorycomponentsasseparatecommand-lineoptions:
| --server <host> |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Backup server address (hostname or IP address). Defaults to localhost. Requires
--datastoretobesetaswell.
| --port <number>   |                 |     |     |     |     |
| ----------------- | --------------- | --- | --- | --- | --- |
| Backupserverport. | Defaultsto8007. |     |     |     |     |
| --datastore       | <name>          |     |     |     |     |
Name of the target datastore. Required when using component options instead of
--repository.
| --auth-id | <user@realm[!token]> |     |     |     |     |
| --------- | -------------------- | --- | --- | --- | --- |
Authentication identity, either a user (user@realm) or an API token (user@realm!
| tokenname). | Defaultstoroot@pam. |     |     |     |     |
| ----------- | ------------------- | --- | --- | --- | --- |
Theseoptionsaremutuallyexclusivewith--repository. Bothformsresolvetothesameinternal
representation, so cached login tickets and other session state are shared between them. For
example,logginginwith--repositoryandthenrunningabackupwith--server/--datastore
(orviceversa)reusesthesameticket,aslongastheserveraddressandusermatch.
Whencomponentoptionsareusedonthecommandline,theyaremergedwiththecorresponding
PBS_*environmentvariablesonaper-fieldbasis: CLIoptionstakeprecedence,whileunspecified
fieldsfallbacktotheirenvironmentvariable. Forexample,withPBS_SERVERandPBS_DATASTORE
set in the environment, passing --auth-id 'other@pam' on the command line overrides just
theidentitywhileinheritingtheserveranddatastorefromtheenvironment.
59

ProxmoxBackupDocumentation,Release4.2.8‐1
The component options make it easy to change individual parts of the connection, for example
switchingtoadifferentdatastoreorserverwithouthavingtorewritetheentirerepositorystring:
| # proxmox-backup-client | backup root.pxar:/ | \   |     |     |
| ----------------------- | ------------------ | --- | --- | --- |
--auth-id 'user@pbs!backup' --server pbs.example.com --datastore store1
(cid:174) Note
RemembertoquoteAPItokenidentifiersontheshell,sincetheexclamationmark(!)isaspecial
characterinmostshells.
ThewebinterfaceprovidescopyablerepositorytextinthedatastoresummarywiththeShowCon-
nectionInformationbutton.
Belowaresomeexamplesofvalidrepositoriesandtheircorrespondingrealvalues:
| ExampleRepository |     | Auth‐ID  | Host:Port      | Datastore |
| ----------------- | --- | -------- | -------------- | --------- |
| mydatastore       |     | root@pam | localhost:8007 | mydatas-  |
tore
| myhostname:mydatastore |     | root@pam | myhostname:8007 | mydatas- |
| ---------------------- | --- | -------- | --------------- | -------- |
tore
user@pbs@myhostname:mydatastore user@pbs myhostname:8007 mydatas-
tore
| user@pbs!token@host:store |     | user@pbs! | host:8007 | store |
| ------------------------- | --- | --------- | --------- | ----- |
token
192.168.55.55:1234:mydatastore root@pam 192.168.55.55:1234 mydatas-
tore
| [ff80::51]:mydatastore |     | root@pam | [ff80::51]:8007 | mydatas- |
| ---------------------- | --- | -------- | --------------- | -------- |
tore
[ff80::51]:1234:mydatastore root@pam [ff80::51]:1234 mydatas-
tore
| 7.2 Statically | Linked Backup | Client |     |     |
| -------------- | ------------- | ------ | --- | --- |
AstaticallylinkedversionoftheProxmoxBackupclientisavailableforLinuxbasedsystemswhere
theregularclientisnotavailable. Pleasenotethatitisrecommendedtousetheregularclientwhen
possible,asthestaticallylinkedclientisnotafullreplacement. Forexample,nameresolutionwill
not be performed via the mechanisms provided by libc, but uses a resolver written purely in the
Rustprogramminglanguage. Therefore, featuresandmodulesprovidedbyNameServiceSwitch
cannotbeused.
Thestaticallylinkedclientisavailableviathepbs-clientrepositoryasdescribedintheinstallation
section.
| 7.3 Environment | Variables |     |     |     |
| --------------- | --------- | --- | --- | --- |
PBS_REPOSITORY
Thedefaultbackuprepository.
PBS_SERVER
Backup server address. Provides a default that can be overridden by --server. Requires
PBS_DATASTOREtobesetaswell(unless--datastoreisgivenonthecommandline). Not
usedwhen--repositoryorPBS_REPOSITORYisset.
PBS_PORT
| Backupserverport. | Defaultsto8007ifunset. |     |           |                   |
| ----------------- | ---------------------- | --- | --------- | ----------------- |
| 60                |                        |     | Chapter7. | BackupClientUsage |

ProxmoxBackupDocumentation,Release4.2.8‐1
PBS_DATASTORE
Datastorename. Providesadefaultthatcanbeoverriddenby--datastore. Notusedwhen
--repositoryorPBS_REPOSITORYisset.
PBS_AUTH_ID
Authenticationidentity(user@realmoruser@realm!tokenname). Defaultstoroot@pamif
unset.
PBS_NAMESPACE
Backupnamespace. Usedasafallbackwhen--nsisnotgiven.
PBS_PASSWORD
Whenset, thisvalueisusedasthepasswordforthebackupserver. Youcanalsosetthisto
anAPItokensecret.
PBS_PASSWORD_FD,PBS_PASSWORD_FILE,PBS_PASSWORD_CMD
LikePBS_PASSWORD,butreaddatafromanopenfiledescriptor,afilenameorfromthestdout
ofacommand,respectively. Thefirstdefinedenvironmentvariablefromtheorderaboveis
preferred.
PBS_ENCRYPTION_PASSWORD
Whenset,thisvalueisusedtoaccessthesecretencryptionkey(ifprotectedbypassword).
PBS_ENCRYPTION_PASSWORD_FD,PBS_ENCRYPTION_PASSWORD_FILE,
PBS_ENCRYPTION_PASSWORD_CMD
LikePBS_ENCRYPTION_PASSWORD,butreaddatafromanopenfiledescriptor,afilenameor
fromthestdoutofacommand,respectively. Thefirstdefinedenvironmentvariablefromthe
orderaboveispreferred.
PBS_FINGERPRINT
Whenset,thisvalueisusedtoverifytheservercertificate(onlyusedifthesystemCAcertifi-
catescannotvalidatethecertificate).
ALL_PROXY
Whenset,theclientusesthespecifiedHTTPproxyforallconnectionstothebackupserver.
Currently only HTTP proxies are supported. Valid proxy configurations have the following
format: [http://][user:password@]<host>[:port]. Defaultportis1080,ifnototherwisespecified.
(cid:174) Note
The recommended solution for shielding hosts is using tunnels such as wireguard, instead of
usinganHTTPproxy.
(cid:174) Note
PasswordsmustbevalidUTF-8andmaynotcontainnewlines. Foryourconvenience,Proxmox
BackupServeronlyusesthefirstlineaspassword,soyoucanaddarbitrarycommentsafterthe
firstnewline.
7.4 System and Service Credentials
Someoftheenvironmentvariablesabovecanbesetusingsystemandservicecredentialsinstead.
7.4. SystemandServiceCredentials 61

ProxmoxBackupDocumentation,Release4.2.8‐1
EnvironmentVariable CredentialNameEquivalent
PBS_REPOSITORY proxmox-backup-client.repository
PBS_PASSWORD proxmox-backup-client.password
PBS_ENCRYPTION_PASSWORD proxmox-backup-client.encryption-password
PBS_FINGERPRINT proxmox-backup-client.fingerprint
Forexample,therepositorypasswordcanbestoredinanencryptedfileasfollows:
# systemd-ask-password -n | systemd-creds encrypt --name=proxmox-backup-client.password - my-
,→api-token.cred
Thecredentialcanthenbereusedinsideofunitfilesorinatransientscopeunitasfollows:
# systemd-run --pipe --wait \
--property=LoadCredentialEncrypted=proxmox-backup-client.password:/full/path/to/my-api-
,→token.cred \
--property=SetCredential=proxmox-backup-client.repository:'my_default_repository' \
proxmox-backup-client ...
Additionally, system credentials (e.g. passed down from the hypervisor to a virtual machine via
SMBIOStype11)canbeloadedonaserviceviaLoadCredential=asdescribedinthemanualpage
systemd.exec(5).
7.5 Output Format
Mostcommandsthatproduceoutputsupportthe--output-formatparameter. Thisacceptsthe
followingvalues:
text
Textformat(default). Structureddataisrenderedasatable.
json
JSON(singleline).
json-pretty
JSON(multiplelines,nicelyformatted).
Also,thefollowingenvironmentvariablescanmodifyoutputbehavior:
PROXMOX_OUTPUT_FORMAT
Definesthedefaultoutputformat.
PROXMOX_OUTPUT_NO_BORDER
Ifset(toanyvalue),donotrendertableborders.
PROXMOX_OUTPUT_NO_HEADER
Ifset(toanyvalue),donotrendertableheaders.
(cid:174) Note
Thetextformatisdesignedtobehumanreadable,andnotmeanttobeparsedbyautomation
tools. Pleaseusethejsonformatifyouneedtoprocesstheoutput.
7.6 Creating Backups
Thissectionexplainshowtocreateabackupfromwithinthemachine. Thiscanbeaphysicalhost,
avirtualmachine,oracontainer. Suchbackupsmaycontainfileandimagearchives. Thereareno
restrictionsinthiscase.
62 Chapter7. BackupClientUsage

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
IfyouwanttobackupvirtualmachinesorcontainersonProxmoxVE,seeProxmoxVEIntegration.
Forthefollowingexample,youneedtohaveabackupserversetup,haveworkingcredentials,and
knowtherepositoryname. Inthefollowingexamples,weusebackup-server:store1.
# proxmox-backup-client backup root.pxar:/ --repository backup-server:store1
| Starting backup:                    | host/elsa/2019-12-03T09:35:01Z |                 |        |
| ----------------------------------- | ------------------------------ | --------------- | ------ |
| Client name:                        | elsa                           |                 |        |
| skip mount                          | point: "/boot/efi"             |                 |        |
| skip mount                          | point: "/dev"                  |                 |        |
| skip mount                          | point: "/run"                  |                 |        |
| skip mount                          | point: "/sys"                  |                 |        |
| Uploaded 12129                      | chunks in                      | 87 seconds (564 | MB/s). |
| End Time: 2019-12-03T10:36:29+01:00 |                                |                 |        |
This will prompt you for a password, then upload a file archive named root.pxar containing all
thefilesinthe/directory.
(cid:1002) Caution
Please note that proxmox-backup-client does not automatically include mount points. In-
stead, youwill see a short skip mount point messagefor each ofthem. Theidea is to cre-
ate a separate file archive for each mounted disk. You can explicitly include them using the
--include-dev option (i.e. --include-dev /boot/efi). You can use this option multiple
timesforeachmountpointthatshouldbeincluded.
The--repositoryoptioncangetquitelongandisusedbyallcommands. Youcanavoidhavingto
enterthisvaluebysettingtheenvironmentvariablePBS_REPOSITORY.Notethatifyouwouldlike
thistoremainsetovermultiplesessions,youshouldinsteadaddthebelowlinetoyour.bashrc
file.
| # export PBS_REPOSITORY=backup-server:store1 |     |     |     |
| -------------------------------------------- | --- | --- | --- |
Afterthis,youcanexecuteallcommandswithouthavingtospecifythe--repositoryoption.
Asinglebackupisallowedtocontainmorethanonearchive. Forexample,ifyouwanttobackup
twodisksmountedat/mnt/disk1and/mnt/disk2:
# proxmox-backup-client backup disk1.pxar:/mnt/disk1 disk2.pxar:/mnt/disk2
Thiscreatesabackupofbothdisks.
Ifyouwanttouseanamespaceforthebackuptarget,youcanaddthe--nsparameter:
# proxmox-backup-client backup disk1.pxar:/mnt/disk1 disk2.pxar:/mnt/disk2 --ns a/b/c
Thebackupcommandtakesalistofbackupspecifications,whichincludethearchivenameonthe
server,thetypeofthearchive,andthearchivesourceattheclient. Theformatis:
<archive-name>.<type>:<source-path>
Thearchive-namemustcontainalphanumerics,hyphensandunderscoresonly. Commontypes
are.pxarforfilearchivesand.imgforblockdeviceimages. Tocreateabackupofablockdevice,
runthefollowingcommand:
| # proxmox-backup-client |     | backup mydata.img:/dev/mylvm/mydata |     |
| ----------------------- | --- | ----------------------------------- | --- |
7.6. CreatingBackups 63

ProxmoxBackupDocumentation,Release4.2.8‐1
7.6.1 ExcludingFiles/DirectoriesfromaBackup
Sometimes it is desired to exclude certain files or directories from a backup archive. To tell the
Proxmox Backup client when and how to ignore files and directories, place a text file named .
pxarexclude in the filesystem hierarchy. Whenever the backup client encounters such a file in
a directory, it interprets each line as a glob match pattern for files and directories that are to be
excludedfromthebackup.
Thefilemustcontainasingleglobpatternperline. Emptylinesandlinesstartingwith#(indicating
a comment) are ignored. A ! at the beginning of a line reverses the glob match pattern from an
exclusiontoanexplicitinclusion. Thismakesitpossibletoexcludeallentriesinadirectoryexcept
for a few single files/subdirectories. Lines ending in / match only on directories. The directory
containing the .pxarexclude file is considered to be the root of the given patterns. It is only
possibletomatchfilesinthisdirectoryanditssubdirectories.
(cid:174) Note
Patterns without a leading / will also match in subdirectories, while patterns with a leading /
willonlymatchinthecurrentdirectory.
\isusedtoescapespecialglobcharacters. ? matchesanysinglecharacter. *matchesanycharac-
ter,includinganemptystring. **isusedtomatchcurrentdirectoryandsubdirectories. Forexam-
ple,withthepattern**/*.tmp,itwouldexcludeallfilesendingin.tmpwithinadirectoryandits
subdirectories. [...]matchesasinglecharacterfromanyoftheprovidedcharacterswithinthe
brackets. [!...]doesthecomplementaryandmatchesanysinglecharacternotcontainedwithin
thebrackets. Itisalsopossibletospecifyrangeswithtwocharactersseparatedby-. Forexample,
[a-z]matchesanylowercasealphabeticcharacter,and[0-9]matchesanysingledigit.
Theorderoftheglobmatchpatternsdefineswhetherafileisincludedorexcluded,thatistosay,
laterentriesoverrideearlierones. Thisisalsotrueformatchpatternsencountereddeeperdown
thedirectorytree,whichcanoverrideapreviousexclusion.
(cid:174) Note
Excluded directories will not be read by the backup client. Thus, a .pxarexclude file in an
excludedsubdirectorywillhavenoeffect. .pxarexcludefilesaretreatedasregularfilesand
willbeincludedinthebackuparchive.
Forexample,considerthefollowingdirectorystructure:
# ls -aR folder
folder/:
. .. .pxarexclude subfolder0 subfolder1
folder/subfolder0:
. .. file0 file1 file2 file3 .pxarexclude
folder/subfolder1:
. .. file0 file1 file2 file3
Thedifferent.pxarexcludefilescontainthefollowing:
# cat folder/.pxarexclude
/subfolder0/file1
/subfolder1/*
!/subfolder1/file2
# cat folder/subfolder0/.pxarexclude
file3
Thiswouldexcludefile1andfile3insubfolder0andallof subfolder1exceptfile2.
Restoringthisbackupwillresultin:
64 Chapter7. BackupClientUsage

ProxmoxBackupDocumentation,Release4.2.8‐1
# ls -aR restored
restored/:
. .. .pxarexclude subfolder0 subfolder1
restored/subfolder0:
. .. file0 file2 .pxarexclude
restored/subfolder1:
. .. file2
Thesamesyntaxcanalsobeuseddirectlyinthecliwiththe--excludeparameter. Forexample:
# proxmox-backup-client backup archive-name.pxar:./linux --exclude /usr
Multiplepathscanbeexcludedlikethis:
# proxmox-backup-client backup archive-name.pxar:./linux --exclude=/usr --exclude=/rust
7.6.2 ChangeDetectionMode
File-based backups containing a lot of data can take a long time, as the default behavior for the
Proxmoxbackupclientistoreadalldataandencodeitintoapxararchive. Theencodedstreamis
splitintovariablesizedchunks. Foreachchunk,adigestiscalculatedandusedtodecidewhether
thechunkneedstobeuploadedorcanbeindexedwithoutupload,asitisalreadyavailableonthe
server(andthereforededuplicated). If thebackedupfilesarelargelyunchanged, re-readingand
then detecting the corresponding chunks don’t need to be uploaded after all is time consuming
andundesired.
Thebackupclient’schange-detection-modecanbeswitchedfromdefaulttometadatabased
detection to reduce limitations as described above, instructing the client to avoid re-reading files
withunchangedmetadatawheneverpossible. Whenusingthismode,insteadoftheregularpxar
archive,thebackupsnapshotisstoredintotwoseparatefiles: thempxarcontainingthearchive’s
metadataandtheppxarcontainingaconcatenationofthefilecontents. Thissplittingallowsfor
efficientmetadatalookups. Whencreatingthebackuparchives,thecurrentfilemetadataiscom-
pared to the one looked up in the previous mpxar archive. The operational details are explained
moreindepthinthetechnicaldocumentation.
Usingthechange-detection-modesettodataallowstocreatethesamesplitarchiveaswhen
usingthemetadatamode,butwithoutusingapreviousreferenceandthereforereencodingallfile
payloads. Fordetailsofthismodepleaseseethetechnicaldocumentation.
Mode Description
legacy (currentdefault): Encodeallfilesintoaselfcontainedpxararchive.
data Encodeallfilesintoasplitdataandmetadatapxararchive.
metadata Encode changed files, reuse unchanged from previous snapshot, creating a split
archive.
Thefollowingshowsanexamplefortheclientinvocationwiththemetadatamode:
# proxmox-backup-client backup archive-name.pxar:./linux --change-detection-mode=metadata
7.7 Encryption
Proxmox Backup supports client-side encryption with AES-256 in GCM mode. To set this up, you
firstneedtocreateanencryptionkey:
# proxmox-backup-client key create my-backup.key
Encryption Key Password: **************
The key is password protected by default. If you do not need this extra protection, you can also
createitwithoutapassword:
7.7. Encryption 65

ProxmoxBackupDocumentation,Release4.2.8‐1
| # proxmox-backup-client |     | key create | /path/to/my-backup.key | --kdf none |     |
| ----------------------- | --- | ---------- | ---------------------- | ---------- | --- |
Havingcreatedthiskey,itisnowpossibletocreateanencryptedbackup,bypassingthe--keyfile
parameter,withthepathtothekeyfile.
# proxmox-backup-client backup etc.pxar:/etc --keyfile /path/to/my-backup.key
| Password:     | *********     |                |     |     |     |
| ------------- | ------------- | -------------- | --- | --- | --- |
| E.n.c.ryption | Key Password: | ************** |     |     |     |
(cid:174)
Note
Ifyoudonotspecifythenameofthebackupkey,thekeywillbecreatedinthedefaultlocation
~/.config/proxmox-backup/encryption-key.json. proxmox-backup-clientwillalso
searchthislocationbydefault,incasethe--keyfileparameterisnotspecified.
You can avoid entering the passwords by setting the environment variables PBS_PASSWORD and
PBS_ENCRYPTION_PASSWORD.
7.7.1 UsingaMasterKeytoStoreandRecoverEncryptionKeys
You can also use proxmox-backup-client key to create an RSA public/private key pair, which
canbeusedtostoreanencryptedversionofthesymmetricbackupencryptionkeyalongsideeach
backupandrecoveritlater.
Tosetupamasterkey:
1. Createanencryptionkeyforthebackup:
| #   | proxmox-backup-client | key | create |     |     |
| --- | --------------------- | --- | ------ | --- | --- |
creating default key at: "~/.config/proxmox-backup/encryption-key.json"
| E.n.c.ryption | Key | Password: ********** |     |     |     |
| ------------- | --- | -------------------- | --- | --- | --- |
Theresultingfilewillbesavedto~/.config/proxmox-backup/encryption-key.json.
2. CreateanRSApublic/privatekeypair:
| #         | proxmox-backup-client | key       | create-master-key |     |     |
| --------- | --------------------- | --------- | ----------------- | --- | --- |
| M.a.s.ter | Key Password:         | ********* |                   |     |     |
This will create two files in your current directory, master-public.pem and
master-private.pem.
3. Import the newly created master-public.pem public certificate, so that
proxmox-backup-clientcanfindanduseituponbackup.
# proxmox-backup-client key import-master-pubkey /path/to/master-public.pem
Imported public master key to "~/.config/proxmox-backup/master-public.pem"
4. Withallthesefilesinplace,runabackupjob:
| #   | proxmox-backup-client | backup | etc.pxar:/etc |     |     |
| --- | --------------------- | ------ | ------------- | --- | --- |
Thekeywillbestoredinyourbackup,underthenamersa-encrypted.key.
| (cid:174) | Note |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
The--keyfileparametercanbeexcluded,iftheencryptionkeyisinthedefaultpath. If
youspecifiedanotherpathuponcreation,youmustpassthe--keyfileparameter.
5. Totestthateverythingworked,youcanrestorethekeyfromthebackup:
| 66  |     |     |     | Chapter7. | BackupClientUsage |
| --- | --- | --- | --- | --------- | ----------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
# proxmox-backup-client restore /path/to/backup/ rsa-encrypted.key /path/to/target
(cid:174) Note
Youshouldnotneedanencryptionkeytoextractthisfile. However,ifakeyexistsatthede-
faultlocation(~/.config/proxmox-backup/encryption-key.json)theprogramwill
promptyouforanencryptionkeypassword. Simplymovingencryption-key.jsonout
ofthisdirectorywillfixthisissue.
6. Then,usethepreviouslygeneratedmasterkeytodecryptthefile:
# proxmox-backup-client key import-with-master-key /path/to/target --master-keyfile /
,→path/to/master-private.pem --encrypted-keyfile /path/to/rsa-encrypted.key
Master Key Password: ******
New Password: ******
Verify Password: ******
7. Thetargetfilewillnowcontaintheencryptionkeyinformationinplaintext. Thesuccessofthis
can be confirmed by passing the resulting json file, with the --keyfile parameter, when
decryptingfilesfromthebackup.
(cid:193) Warning
Withouttheirkey,backedupfileswillbeinaccessible. Thus,youshouldkeepkeysorderedandin
aplacethatisseparatefromthecontentsbeingbackedup. Itcanhappen,forexample,thatyou
backupanentiresystem,usingakeyonthatsystem. Ifthesystemthenbecomesinaccessible
foranyreasonandneedstoberestored,thiswillnotbepossible,astheencryptionkeywillbe
lostalongwiththebrokensystem.
It is recommended that you keep your master key safe, but easily accessible, in order for quick
disaster recovery. For this reason, the best place to store it is in your password manager, where
it is immediately recoverable. As a backup to this, you should also save the key to a USB flash
drive and store that in a secure place. This way, it is detached from any system, but is still easy
to recover from, in case of emergency. Finally, in preparation for the worst case scenario, you
should also consider keeping a paper copy of your master key locked away in a safe place. The
paperkey subcommand can be used to create a QR encoded version of your master key. The
followingcommandsendstheoutputofthepaperkeycommandtoatextfile,foreasyprinting.
proxmox-backup-client key paperkey --output-format text > qrkey.txt
7.8 Restoring Data
Theregularcreationofbackupsisanecessarystepinavoidingdataloss. Moreimportantly,how-
ever, is the restoration. It is good practice to perform periodic recovery tests to ensure that you
canaccessthedataincaseofdisaster.
First,youneedtofindthesnapshotwhichyouwanttorestore. Thesnapshotlistcommandprovides
alistofallthesnapshotsontheserver:
# proxmox-backup-client snapshot list
┌────────────────────────────────┬─────────────┬────────────────────────────────────┐
│ snapshot │ size │ files │
╞════════════════════════════════╪═════════════╪════════════════════════════════════╡
│ host/elsa/2019-12-03T09:30:15Z │ 51788646825 │ root.pxar catalog.pcat1 index.json │
├────────────────────────────────┼─────────────┼────────────────────────────────────┤
│ host/elsa/2019-12-03T09:35:01Z │ 51790622048 │ root.pxar catalog.pcat1 index.json │
├────────────────────────────────┼─────────────┼────────────────────────────────────┤
...
7.8. RestoringData 67

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:98)
Tip
Listwillbydefaultonlyoutputthebackupsnapshotsoftherootnamespaceitself. Tolistback-
| upsfromanothernamespaceusethe--ns |     |     |     | <ns>option |     |     |     |
| --------------------------------- | --- | --- | --- | ---------- | --- | --- | --- |
Youcaninspectthecatalogtofindspecificfiles.
| #...proxmox-backup-client |     | catalog | dump host/elsa/2019-12-03T09:35:01Z |     |     |     |     |
| ------------------------- | --- | ------- | ----------------------------------- | --- | --- | --- | --- |
d "./root.pxar.didx/etc/cifs-utils"
l "./root.pxar.didx/etc/cifs-utils/idmap-plugin"
d..."./root.pxar.didx/etc/console-setup"
Therestorecommandletsyourestoreasinglearchivefromthebackup.
# proxmox-backup-client restore host/elsa/2019-12-03T09:35:01Z root.pxar /target/path/
When an encryption key is configured, including a default key, the backup manifest must have
a valid signature. This protects both encrypted and sign-only backups against tampering on the
server.
To read a genuinely unsigned backup while a key is configured, explicitly add
--ignore-missing-signature. The command warns that the backup’s integrity cannot
be verified. This option only accepts a missing signature, not an invalid one. It is also avail-
able for catalog inspection, mounting and mapping backups, proxmox-file-restore, and
| proxmox-backup-debug |     | diff | archive. |     |     |     |     |
| -------------------- | --- | ---- | -------- | --- | --- | --- | --- |
Forscriptedrestores,optoutonlyforbackupsyouknowareunsigned. Donotautomaticallyretry
signaturefailureswiththisoption.
To get the contents of any archive, you can restore the index.json file in the repository to the
| targetpath’-’. | Thiswilldumpthecontentstothestandardoutput. |     |     |     |     |     |     |
| -------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
# proxmox-backup-client restore host/elsa/2019-12-03T09:35:01Z index.json -
7.8.1 InteractiveRestores
If you only want to restore a few individual files, it is often easier to use the interactive recovery
shell.
# proxmox-backup-client catalog shell host/elsa/2019-12-03T09:35:01Z root.pxar
| Starting | interactive | shell |     |      |     |       |     |
| -------- | ----------- | ----- | --- | ---- | --- | ----- | --- |
| pxar:/   | > ls        |       |     |      |     |       |     |
| b.i.n.   | boot        | dev   | etc | home | lib | lib32 |     |
Theinteractiverecoveryshellisaminimalcommand-lineinterfacethatutilizesthemetadatastored
inthecatalogtoquicklylist,navigateandsearchforfilesinafilearchive. Torestorefiles,youcan
selectthemindividuallyormatchthemwithaglobpattern.
Usingthecatalogfornavigationreducestheoverheadconsiderablybecauseonlythecatalogneeds
tobedownloadedand,optionally,decrypted. Theactualchunksareonlyaccessedifthemetadata
inthecatalogisinsufficientorfortheactualrestore.
Similar to common UNIX shells, cd and ls are the commands used to change working directory
andlistdirectorycontentsinthearchive. pwdshowsthefullpathofthecurrentworkingdirectory
withrespecttothearchiveroot.
The ability to quickly search the contents of the archive is a commonly required feature. That’s
| wherethecatalogismostvaluable. |                     |          | Forexample: |     |     |     |     |
| ------------------------------ | ------------------- | -------- | ----------- | --- | --- | --- | --- |
| pxar:/                         | > find etc/**/*.txt | --select |             |     |     |     |     |
"/etc/X11/rgb.txt"
| pxar:/ | > list-selected |     |     |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- | --- | --- |
etc/**/*.txt
| p.x.a.r:/ | > restore-selected | /target/path |     |     |     |           |                   |
| --------- | ------------------ | ------------ | --- | --- | --- | --------- | ----------------- |
| 68        |                    |              |     |     |     | Chapter7. | BackupClientUsage |

ProxmoxBackupDocumentation,Release4.2.8‐1
This will find and print all files ending in .txt located in etc/ or its subdirectories, and add the
correspondingpatterntothelistforsubsequentrestores. list-selectedshowsthesepatterns
andrestore-selectedfinallyrestoresallfilesinthearchivematchingthepatternsto/target/
| pathonthelocalhost. |     | Thiswillscanthewholearchive. |     |     |     |
| ------------------- | --- | ---------------------------- | --- | --- | --- |
The restore command can be used to restore all the files contained within the backup archive.
Thisismosthelpfulwhenpairedwiththe--pattern <glob>option,asitallowsyoutorestoreall
filesmatchingaspecificpattern. Forexample,ifyouwantedtorestoreconfigurationfileslocated
in/etc,youcoulddothefollowing:
| p.x.a.r:/ | > restore target/ | --pattern | etc/**/*.conf |     |     |
| --------- | ----------------- | --------- | ------------- | --- | --- |
Theabovewillscanthroughallthedirectoriesbelow/etcandrestoreallfilesendingin.conf.
7.8.2 MountingofArchivesviaFUSE
The FUSE implementation for the pxar archive allows you to mount a file archive as a read-only
filesystemtoamountpointonyourhost.
# proxmox-backup-client mount host/backup-client/2020-01-29T11:29:22Z root.pxar /mnt/
,→mountpoint
# ls /mnt/mountpoint
| bin dev  | home lib32 | libx32     | media opt | root sbin | sys usr |
| -------- | ---------- | ---------- | --------- | --------- | ------- |
| boot etc | lib lib64  | lost+found | mnt proc  | run srv   | tmp var |
Thisallowsyoutoaccessthefullcontentsofthearchiveinaseamlessmanner.
(cid:174) Note
AstheFUSEconnectionneedstofetchanddecryptchunksfromthebackupserver’sdatastore,
thiscancausesomeadditionalnetworkandCPUloadonyourhost, dependingontheopera-
tionsyouperformonthemountedfilesystem.
Tounmountthefilesystem,usetheumountcommandonthemountpoint:
| # umount  | /mnt/mountpoint |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- |
| 7.9 Login | and Logout      |     |     |     |     |
Theclienttoolpromptsyoutoentertheloginpasswordassoonasyouwanttoaccessthebackup
server. The server checks your credentials and responds with a ticket that is valid for two hours.
Theclienttoolautomaticallystoresthatticketandusesitforfurtherrequeststothisserver.
Youcanalsomanuallytriggerthislogin/logoutusingtheloginandlogoutcommands:
| # proxmox-backup-client |            | login |     |     |     |
| ----------------------- | ---------- | ----- | --- | --- | --- |
| Password:               | ********** |       |     |     |     |
Toremovetheticket,issuealogout:
| # proxmox-backup-client |          | logout    |             |       |     |
| ----------------------- | -------- | --------- | ----------- | ----- | --- |
| 7.10                    | Changing | the Owner | of a Backup | Group |     |
Bydefault,theownerofabackupgroupistheuserwhichwasusedtooriginallycreatethatbackup
group(orinthecaseofsyncjobs,root@pam). Thismeansthatifausermike@pbscreatedabackup,
anotheruserjohn@pbscannotbeusedtocreatebackupsinthatsamebackupgroup. Incaseyou
wanttochangetheownerofabackup,youcandosowiththebelowcommand,usingauserthat
hasDatastore.Modifyprivilegesonthedatastore.
7.9. LoginandLogout 69

ProxmoxBackupDocumentation,Release4.2.8‐1
| # proxmox-backup-client | change-owner | vm/103 john@pbs |     |     |     |
| ----------------------- | ------------ | --------------- | --- | --- | --- |
This can also be done from within the web interface, by navigating to the Content section of the
datastore that contains the backup group and selecting the user icon under the Actions column.
Commoncasesforthiscouldbetochangetheownerofasyncjobfromroot@pam,ortorepurpose
abackupgroup.
| 7.11 Pruning | and Removing | Backups |     |     |     |
| ------------ | ------------ | ------- | --- | --- | --- |
Youcanmanuallydeleteabackupsnapshotusingtheforgetcommand:
| # proxmox-backup-client | snapshot | forget <snapshot> |     |     |     |
| ----------------------- | -------- | ----------------- | --- | --- | --- |
(cid:1002) Caution
Thiscommandremovesallarchivesinthisbackupsnapshot. Theywillbeinaccessibleandun-
recoverable.
Don’t forget to add the namespace --ns parameter if you want to forget a snapshot that is con-
tainedintherootnamespace:
| # proxmox-backup-client | snapshot | forget <snapshot> | --ns <ns> |     |     |
| ----------------------- | -------- | ----------------- | --------- | --- | --- |
Althoughmanualremovalissometimesrequired,theprunecommandisnormallyusedtosystem-
aticallydeleteolderbackups. Pruneletsyouspecifywhichbackupsnapshotsyouwanttokeep. The
followingretentionoptionsareavailable:
| --keep-last | <N> |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
Keepthelast<N>backupsnapshots.
| --keep-hourly | <N> |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
Keepbackupsforthelast<N>hours. Ifthereismorethanonebackupforasinglehour,only
| thelatestiskept. | Hourswithoutbackupsdonotcount. |     |     |     |     |
| ---------------- | ------------------------------ | --- | --- | --- | --- |
| --keep-daily     | <N>                            |     |     |     |     |
Keep backups for the last <N> days. If there is more than one backup for a single day, only
| thelatestiskept. | Dayswithoutbackupsdonotcount. |     |     |     |     |
| ---------------- | ----------------------------- | --- | --- | --- | --- |
| --keep-weekly    | <N>                           |     |     |     |     |
Keepbackupsforthelast<N>weeks. Ifthereismorethanonebackupforasingleweek,only
| thelatestiskept. | Weekswithoutbackupdonotcount. |     |     |     |     |
| ---------------- | ----------------------------- | --- | --- | --- | --- |
(cid:174)
Note
WeeksstartonMondayandendonSunday. ThesoftwareusestheISOweekdatesystem
andhandlesweeksattheendoftheyearcorrectly.
| --keep-monthly | <N> |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Keepbackupsforthelast<N>months. Ifthereismorethanonebackupforasinglemonth,
onlythelatestiskept. Monthswithoutbackupsdonotcount.
| --keep-yearly | <N> |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
Keepbackupsforthelast<N>years. Ifthereismorethanonebackupforasingleyear,only
| thelatestiskept. | Yearswithoutbackupsdonotcount. |     |     |     |     |
| ---------------- | ------------------------------ | --- | --- | --- | --- |
The retention options are processed in the order given above. Each option only covers backups
withinitstimeperiod. Thenextoptiondoesnottakecareofalreadycoveredbackups. Itwillonly
considerolderbackups.
| 70  |     |     |     | Chapter7. | BackupClientUsage |
| --- | --- | --- | --- | --------- | ----------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Unfinishedandincompletebackupswillberemovedbytheprunecommandunlesstheyarenewer
thanthelastsuccessfulbackup. Inthiscase,thelastfailedbackupisretained.
# proxmox-backup-client prune <group> --keep-daily 7 --keep-weekly 4 --keep-monthly 3
Youcanusethe--dry-runoptiontotestyoursettings. Thisonlyshowsthelistofexistingsnap-
shotsandwhatactionsprunewouldtake.
# proxmox-backup-client prune host/elsa --dry-run --keep-daily 1 --keep-weekly 3
┌────────────────────────────────┬──────┐
| │ snapshot | │ keep | │   |     |
| ---------- | ------ | --- | --- |
╞════════════════════════════════╪══════╡
| │ host/elsa/2019-12-04T13:20:37Z | │ 1 | │   |     |
| -------------------------------- | --- | --- | --- |
├────────────────────────────────┼──────┤
| │ host/elsa/2019-12-03T09:35:01Z | │ 0 | │   |     |
| -------------------------------- | --- | --- | --- |
├────────────────────────────────┼──────┤
| │ host/elsa/2019-11-22T11:54:47Z | │ 1 | │   |     |
| -------------------------------- | --- | --- | --- |
├────────────────────────────────┼──────┤
| │ host/elsa/2019-11-21T12:36:25Z | │ 0 | │   |     |
| -------------------------------- | --- | --- | --- |
├────────────────────────────────┼──────┤
| │ host/elsa/2019-11-10T10:42:20Z | │ 1 | │   |     |
| -------------------------------- | --- | --- | --- |
└────────────────────────────────┴──────┘
(cid:174) Note
Neither the prune command nor the forget command free space in the chunk-store. The
chunk-storestillcontainsthedatablocks. TofreespaceyouneedtoperformGarbageCollection.
Itisalsopossibletoprotectsinglesnapshotsfrombeingprunedordeleted:
| # proxmox-backup-client | snapshot protected | update <snapshot> | true |
| ----------------------- | ------------------ | ----------------- | ---- |
This will set the protected flag on the snapshot and prevent pruning or manual deletion of this
snapshotuntiltheflagisremovedagainwith:
| # proxmox-backup-client | snapshot protected | update <snapshot> | false |
| ----------------------- | ------------------ | ----------------- | ----- |
Whenagroupwithaprotectedsnapshotisdeleted,onlythenon-protectedonesareremoved,and
therestwillremain.
(cid:174) Note
Thisflagwillnotbesyncedwhenusingpullorsyncjobs. Ifyouwanttoprotectasyncedsnap-
shot,youhavetodothisagainmanuallyonthetargetbackupserver.
| 7.12 Garbage Collection |     |     |     |
| ----------------------- | --- | --- | --- |
Theprunecommandremovesonlythebackupindexfiles,notthedatafromthedatastore. Dele-
tionofunusedbackupdatafromthedatastoreisdonebygarbagecollection. Itisthereforerecom-
mendedtoschedulegarbagecollectiontasksonaregularbasis. Theworkingprincipleofgarbage
collectionisdescribedinmoredetailsintherelatedbackgroundsection.
Tostartgarbagecollectionfromtheclientside,runthefollowingcommand:
| # proxmox-backup-client | garbage-collect |     |     |
| ----------------------- | --------------- | --- | --- |
(cid:174) Note
7.12. GarbageCollection 71

ProxmoxBackupDocumentation,Release4.2.8‐1
This command needs to read all existing backup index files and touches the complete chunk-
store. This can take a long time depending on the number of chunks and the speed of the
underlyingdisks.
Theprogressofthegarbagecollectionwillbedisplayedasshownintheexamplebelow:
| # proxmox-backup-client |             |                     | garbage-collect |        |     |     |     |
| ----------------------- | ----------- | ------------------- | --------------- | ------ | --- | --- | --- |
| starting                | garbage     | collection          | on store        | store2 |     |     |     |
| Start GC                | phase1      | (mark               | used chunks)    |        |     |     |     |
| Start GC                | phase2      | (sweep              | unused chunks)  |        |     |     |     |
| percentage              | done:       | 1, chunk            | count:          | 219    |     |     |     |
| p.e.r.centage           | done:       | 2, chunk            | count:          | 453    |     |     |     |
| percentage              | done:       | 99, chunk           | count:          | 21188  |     |     |     |
| Removed                 | bytes:      | 411368505           |                 |        |     |     |     |
| Removed                 | chunks:     | 203                 |                 |        |     |     |     |
| Original                | data        | bytes: 327160886391 |                 |        |     |     |     |
| Disk bytes:             | 52767414743 |                     | (16 %)          |        |     |     |     |
| Disk chunks:            | 21221       |                     |                 |        |     |     |     |
| Average                 | chunk       | size: 2486565       |                 |        |     |     |     |
TASK OK
Garbagecollectioncanalsobescheduledusingproxmox-backup-managerorfromtheProxmox
BackupServer’swebinterface.
7.13 Benchmarking
The backup client also comes with a benchmarking tool. This tool measures various metrics re-
latingtocompressionandencryptionspeeds. IfaProxmoxBackuprepository(remoteorlocal)is
specified,theTLSuploadspeedwillgetmeasuredtoo.
Youcanrunabenchmarkusingthebenchmarksubcommandof proxmox-backup-client:
(cid:174) Note
TheTLSspeedtestisonlyincludedifabackupserverrepositoryisspecified.
| # proxmox-backup-client |          |             | benchmark     |     |     |     |     |
| ----------------------- | -------- | ----------- | ------------- | --- | --- | --- | --- |
| Uploaded                | 1517     | chunks in   | 5 seconds.    |     |     |     |     |
| Time per                | request: | 3309        | microseconds. |     |     |     |     |
| TLS speed:              | 1267.41  | MB/s        |               |     |     |     |     |
| SHA256                  | speed:   | 2066.73     | MB/s          |     |     |     |     |
| Compression             | speed:   | 775.11      | MB/s          |     |     |     |     |
| Decompress              | speed:   | 1233.35     | MB/s          |     |     |     |     |
| AES256/GCM              | speed:   | 3688.27     | MB/s          |     |     |     |     |
| Verify                  | speed:   | 783.43 MB/s |               |     |     |     |     |
┌───────────────────────────────────┬─────────────────────┐
| │ Name |     |     |     | │ Value |     | │   |     |
| ------ | --- | --- | --- | ------- | --- | --- | --- |
╞═══════════════════════════════════╪═════════════════════╡
| │ TLS (maximal |     | backup | upload speed) | │ 1267.41 | MB/s (103%) | │   |     |
| -------------- | --- | ------ | ------------- | --------- | ----------- | --- | --- |
├───────────────────────────────────┼─────────────────────┤
| │ SHA256 | checksum | computation | speed | │ 2066.73 | MB/s (102%) | │   |     |
| -------- | -------- | ----------- | ----- | --------- | ----------- | --- | --- |
├───────────────────────────────────┼─────────────────────┤
| │ ZStd | level 1 | compression | speed | │ 775.11 | MB/s (103%) | │   |     |
| ------ | ------- | ----------- | ----- | -------- | ----------- | --- | --- |
├───────────────────────────────────┼─────────────────────┤
| │ ZStd | level 1 | decompression | speed | │ 1233.35 | MB/s (103%) | │   |     |
| ------ | ------- | ------------- | ----- | --------- | ----------- | --- | --- |
├───────────────────────────────────┼─────────────────────┤
| │ Chunk | verification | speed |     | │ 783.43 | MB/s (103%) | │   |     |
| ------- | ------------ | ----- | --- | -------- | ----------- | --- | --- |
├───────────────────────────────────┼─────────────────────┤
| │ AES256 | GCM encryption |     | speed | │ 3688.27 | MB/s (101%) | │   |     |
| -------- | -------------- | --- | ----- | --------- | ----------- | --- | --- |
└───────────────────────────────────┴─────────────────────┘
(cid:174) Note
ThepercentagesgivenintheoutputtablecorrespondtoacomparisonagainstaRyzen72700X.
| 72  |     |     |     |     |     | Chapter7. | BackupClientUsage |
| --- | --- | --- | --- | --- | --- | --------- | ----------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Youcanalsopassthe--output-formatparametertooutputstatsinjson,ratherthanthedefault
tableformat.
7.13. Benchmarking 73

ProxmoxBackupDocumentation,Release4.2.8‐1
| 74  | Chapter7. | BackupClientUsage |
| --- | --------- | ----------------- |

CHAPTER
EIGHT
|     |     |     |     |     | PROXMOX |     | VE INTEGRATION |     |
| --- | --- | --- | --- | --- | ------- | --- | -------------- | --- |
ProxmoxBackupServercanbeintegratedintoaProxmoxVEstandaloneorclustersetup,byadding
itasastorageinProxmoxVE.
SeealsotheProxmoxVEStorage-ProxmoxBackupServersectionoftheProxmoxVEAdministra-
tionGuideforProxmoxVEspecificdocumentation.
| 8.1 Using | the | Proxmox | VE  | Web‐Interface |     |     |     |     |
| --------- | --- | ------- | --- | ------------- | --- | --- | --- | --- |
ProxmoxVEhasnativeAPIandwebinterfaceintegrationofProxmoxBackupServerasofProxmox
VE6.3.
| AProxmoxBackupServercanbeaddedunderDatacenter |     |         |     |         |      | -> Storage. |     |     |
| --------------------------------------------- | --- | ------- | --- | ------- | ---- | ----------- | --- | --- |
| 8.2 Using                                     | the | Proxmox | VE  | Command | Line |             |     |     |
Youneedtodefineanewstoragewithtype’pbs’onyourProxmoxVEnode. Thefollowingexample
usesstore2asthestorage’sname,andassumestheserveraddressislocalhostandyouwant
toconnectasuser1@pbs.
| # pvesm | add pbs store2 | --server   | localhost | --datastore | store2   |     |     |     |
| ------- | -------------- | ---------- | --------- | ----------- | -------- | --- | --- | --- |
| # pvesm | set store2     | --username | user1@pbs | --password  | <secret> |     |     |     |
(cid:174)
Note
If you would rather not enter your password as plain text, you can pass the --password pa-
rameter, without any arguments. This will cause the program to prompt you for a password
uponenteringthecommand.
If your backup server uses a self signed certificate, you need to add the certificate fingerprint to
the configuration. You can get the fingerprint by running the following command on the backup
server:
| # proxmox-backup-manager |           | cert                                       | info | | grep Fingerprint |     |     |     |     |
| ------------------------ | --------- | ------------------------------------------ | ---- | ------------------ | --- | --- | --- | --- |
| Fingerprint              | (sha256): | 64:d3:ff:3a:50:38:53:5a:9b:f7:50:...:ab:fe |      |                    |     |     |     |     |
Pleaseaddthatfingerprinttoyourconfigurationtoestablishatrustrelationship:
# pvesm set store2 --fingerprint 64:d3:ff:3a:50:38:53:5a:9b:f7:50:...:ab:fe
Afterthat,youshouldbeabletoviewstoragestatuswith:
| # pvesm | status --storage | store2 |        |            |            |      |            |        |
| ------- | ---------------- | ------ | ------ | ---------- | ---------- | ---- | ---------- | ------ |
| Name    | Type             |        | Status | Total      |            | Used | Available  | %      |
| store2  | pbs              |        | active | 3905109820 | 1336687816 |      | 2568422004 | 34.23% |
75

ProxmoxBackupDocumentation,Release4.2.8‐1
HavingaddedtheProxmoxBackupServerdatastoretoProxmoxVE,youcanbackupVMsandcon-
tainersinthesamewayyouwouldforanyotherstoragedevicewithintheenvironment(seeProx-
moxVEAdminGuide: BackupandRestore.
| 76  | Chapter8. | ProxmoxVEIntegration |
| --- | --------- | -------------------- |

CHAPTER
NINE
PXAR COMMAND‐LINE TOOL
pxar is a command-line utility for creating and manipulating archives in the Proxmox File Archive
Format (.pxar). It is inspired by casync file archive format, which caters to a similar use-case. The
.pxar format is adapted to fulfill the specific needs of the Proxmox Backup Server, for example,
efficientstorageofhardlinks. Theformatisdesignedtoreducetherequiredstorageontheserver
byachievingahighlevelofdeduplication.
9.1 Creating an Archive
Runthefollowingcommandtocreateanarchiveofafoldernamedsource:
# pxar create archive.pxar /path/to/source
Thiswillcreateanewarchivecalledarchive.pxarwiththecontentsofthesourcefolder.
(cid:174) Note
pxarwillnotoverwriteanyexistingarchives. Ifanarchivewiththesamenameisalreadypresent
inthetargetfolder,thecreationwillfail.
Bydefault,pxarwillskipcertainmountpointsandwillnotfollowdeviceboundaries. Thisdesign
decisionisbasedontheprimaryusecaseofcreatingarchivesforbackups. Itmakessensetoignore
the contents of certain temporary or system specific files in a backup. To alter this behavior and
followdeviceboundaries,usethe--all-file-systemsflag.
It is possible to exclude certain files and/or folders from the archive by passing the --exclude
parameterwithgitignore-stylematchpatterns.
Forexample,youcanexcludeallfilesendingin.txtfromthearchivebyrunning:
# pxar create archive.pxar /path/to/source --exclude '**/*.txt'
Be aware that the shell itself will try to expand glob patterns before invoking pxar. In order to
avoidthis,allglobshavetobequotedcorrectly.
Itispossibletopassthe--excludeparametermultipletimes, inordertomatchmorethanone
pattern. This allows you to use more complex file inclusion/exclusion behavior. However, it is
recommendedtouse.pxarexcludefilesinsteadforsuchcases.
Forexampleyoumightwanttoexcludeall.txtfilesexceptaspecificonefromthearchive. This
wouldbeachievedviathenegatedmatchpattern,prefixedby!. Alltheglobpatternsarerelative
tothesourcedirectory.
# pxar create archive.pxar /path/to/source --exclude '**/*.txt' --exclude '!/folder/file.txt'
77

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
Theorderoftheglobmatchpatternsmatters,aslateronesoverrideearlierones. Permutations
ofthesamepatternsleadtodifferentresults.
pxar will store the list of glob match patterns passed as parameters via the command line, in a
filecalled.pxarexclude-cli,attherootofthearchive. Ifafilewiththisnameisalreadypresent
in the source folder during archive creation, this file is not included in the archive, and the file
containingthenewpatternsisaddedtothearchiveinstead. Theoriginalfileisnotaltered.
Amoreconvenientandpersistentwaytoexcludefilesfromthearchiveisbyplacingtheglobmatch
patternsin.pxarexcludefiles. Itispossibletocreateandplacethesefilesinanydirectoryofthe
filesystem tree. These files must contain one pattern per line, and later patterns override earlier
ones. Thepatternscontrolfileexclusionsoffilespresentwithinthegivendirectoryorfurtherbelow
itinthetree. ThebehavioristhesameasdescribedinCreatingBackups.
| 9.2 Extracting |     | an Archive |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- |
Anexistingarchive,archive.pxar,isextractedtoatargetdirectorywiththefollowingcommand:
| # pxar | extract archive.pxar | /path/to/target |     |     |     |     |
| ------ | -------------------- | --------------- | --- | --- | --- | --- |
Ifnotargetisprovided,thecontentsofthearchiveisextractedtothecurrentworkingdirectory.
In order to restore only parts of an archive, single files, and/or folders, it is possible to pass the
correspondingglobmatchpatternsasadditionalparametersortousethepatternsstoredinafile:
| # pxar | extract etc.pxar | /restore/target/etc | --pattern | '**/*.conf' |     |     |
| ------ | ---------------- | ------------------- | --------- | ----------- | --- | --- |
The above example restores all .conf files encountered in any of the sub-folders in the archive
etc.pxartothetarget/restore/target/etc. Apathtothefilecontainingmatchpatternscan
bespecifiedusingthe--files-fromparameter.
| 9.3 List | the Contents | of  | an Archive |     |     |     |
| -------- | ------------ | --- | ---------- | --- | --- | --- |
Todisplaythefilesanddirectoriescontainedinanarchivearchive.pxar,runthefollowingcom-
mand:
| # pxar | list archive.pxar |     |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- | --- |
Thisdisplaysthefullpathofeachfileordirectorywithrespecttothearchive’sroot.
| 9.4 Mounting | an  | Archive |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- |
pxarallowsyoutomountandinspectthecontentsofanarchiveviaFUSE.Inordertomountan
archivenamedarchive.pxartothemountpoint/mnt,runthecommand:
| # pxar | mount archive.pxar | /mnt |     |     |     |     |
| ------ | ------------------ | ---- | --- | --- | --- | --- |
Oncethearchiveismounted,youcanaccessitscontentunderthegivenmountpoint.
# cd /mnt
# ls
| bin dev  | home lib32 | libx32     | media opt | root sbin | sys usr   |                      |
| -------- | ---------- | ---------- | --------- | --------- | --------- | -------------------- |
| boot etc | lib lib64  | lost+found | mnt proc  | run srv   | tmp var   |                      |
| 78       |            |            |           |           | Chapter9. | pxarCommand‐lineTool |

CHAPTER
TEN
TAPE BACKUP
Proxmoxtapebackupprovidesaneasywaytostoredatastorecontentontomagnetictapes. This
increasesdatasafetybecauseyouget:
• anadditionalcopyofthedata,
• onadifferentmediatype(tape),
• toanadditionallocation(youcanmovetapesoff-site)
Inmostrestorejobs,onlydatafromthelastbackupjobisrestored. Restorerequestsfurtherde-
cline, the older the data gets. Considering this, tape backup may also help to reduce disk usage,
becauseyoucansafelyremovedatafromdisk,onceit’sarchivedontape. Thisisespeciallytrueif
youneedtoretaindataforseveralyears.
Tapebackupsdonotproviderandomaccesstothestoreddata. Instead,youneedtorestorethe
datatodisk,beforeyoucanaccessitagain. Also,ifyoustoreyourtapesoff-site(usingsomekind
oftapevaultingservice),youneedtobringthembackon-site,beforeyoucandoanyrestores. So
pleaseconsiderthatrestoringfromtapecantakemuchlongerthanrestoringfromdisk.
79

ProxmoxBackupDocumentation,Release4.2.8‐1
10.1 Tape Technology Primer
Asof2021,theonlywidelyavailabletapetechnologystandardisLinearTape-Open(LTO).Different
vendorsofferLTOUltriumtapedrives,auto-loaders,andLTOtapecartridges.
There are a few vendors that offer proprietary drives with slight advantages in performance and
capacity. Nevertheless,theyhavesignificantdisadvantages:
• proprietary(singlevendor)
• amuchhigherpurchasecost
Sowecurrentlydonottestsuchdrives.
Ingeneral,LTOtapesofferthefollowingadvantages:
• Durability(30yearlifespan)
• HighCapacity(12TB)
• RelativelylowcostperTB
• ColdMedia
• Movable(storableinsidevault)
• Multiplevendors(forbothmediaanddrives)
• BuiltinAES-GCMEncryptionengine
NotethatProxmoxBackupServer alreadystorescompresseddata,sousingthetapecompression
featurehasnoadvantage.
10.2 Supported Hardware
Proxmox Backup Server supports Linear Tape-Open generation 5 (LTO-5) or later and has best-
effortsupportforgeneration4(LTO-4). WhilemanyLTO-4systemsareknowntowork,somemight
need firmware updates or do not implement necessary features to work with Proxmox Backup
Server.
TapechangingiscarriedoutusingtheSCSIMediumChangerprotocol,soallmoderntapelibraries
shouldwork.
(cid:174) Note
We use a custom user space tape driver written in Rust. This driver directly communicates
withthetapedriveusingtheSCSIgenericinterface. Thismayhavenegativesideeffectswhen
usedwiththeoldLinuxkerneltapedriver,soyoushouldnotusethatdriverwithProxmoxtape
backup.
10.2.1 DrivePerformance
CurrentLTO-8tapesprovideread/writespeedsofupto360MB/s. Thismeans,thatitstilltakesa
minimumof9hourstocompletelywriteorreadasingletape(evenatmaximumspeed).
The only way to speed that data rate up is to use more than one drive. That way, you can run
severalbackupjobsinparallel,orrunrestorejobswhiletheotherdivesareusedforbackups.
Alsoconsiderthatyoufirstneedtoreaddatafromyourdatastore(disk). However, asinglespin-
ning disk is unable to deliver data at this rate. We measured a maximum rate of about 60MB/s
to 100MB/s in practice, so it takes 33 hours to read the 12TB needed to fill up an LTO-8 tape. If
youwanttowritetoyourtapeatfullspeed,pleasemakesurethatthesourcedatastoreisableto
deliverthatperformance(forexample,byusingSSDs).
80 Chapter10. TapeBackup

ProxmoxBackupDocumentation,Release4.2.8‐1
10.2.2 LTO‐9+considerations
SinceLTO-9,itisnecessarytoinitializenewmediainyourdrives,thisiscalledMediaOptimization.
Thisusuallytakesbetween40and120minutespermedium. Itisrecommendedtoinitializeyour
mediainthismannerwiththetoolsprovidedbyyourhardwarevendorofyourdriveorchanger.
Sometapechangershaveamethodto’bulk’initializeyourmedia.
Because of this, formatting tapes is handled differently in Proxmox Backup Server to avoid re-
optimizing on each format/labelling. If you want to format your media for use with the Proxmox
BackupServerthefirsttimeorafterusewithanotherprogram,eitherusethefunctionalityofyour
drive/changer,orusethe’slow’formatonthecli:
# proxmox-tape format --drive your-drive --fast 0
Thiswillcompletelyremoveallpre-existingdataandtriggeraMediaOptimizationpass.
IfyouformatapartitionedLTO-9mediumwiththe’fast’method(thedefaultorbysetting--fast1),
onlythefirstpartitionwillbeformatted,somakesuretousethe’slow’method.
10.3 Terminology
TapeLabels:
are used to uniquely identify a tape. You would normally apply a sticky paper label to the
frontofthecartridge. Weadditionallystorethelabeltextmagneticallyonthetape(firstfile
ontape).
Barcodes:
are a special form of tape labels, which are electronically readable. Most LTO tape robots
usean8characterstringencodedasCode39,asdefinedintheLTOUltriumCartridgeLabel
Specification.
You can either buy such barcode labels from your cartridge vendor, or print them yourself.
YoucanuseourLTOBarcodeGeneratorapp,ifyouwouldliketoprintthemyourself.
(cid:174) Note
Physical labels and the associated adhesive should have an environmental performance
tomatchorexceedtheenvironmentalspecificationsofthecartridgetowhichitisapplied.
MediaPools:
Amediapoolisalogicalcontainerfortapes. Abackupjobtargetsonemediapool, soajob
only uses tapes from that pool. The pool additionally defines how long a backup job can
append data to tapes (allocation policy) and how long you want to keep the data (retention
policy).
MediaSet:
Agroupofcontinuouslywrittentapes(allfromthesamemediapool).
Tapedrive:
Thedeviceusedtoreadandwritedatatothetape. Therearestandalonedrives, butdrives
areusuallyshippedwithintapelibraries.
Tapechanger:
Adevicewhichcanchangethetapesinsideatapedrive(taperobot). Theyareusuallypartof
atapelibrary.
Tapelibrary:
A storage device that contains one or more tape drives, a number of slots to hold tape car-
tridges, abarcodereadertoidentifytapecartridges, andanautomatedmethodforloading
tapes(arobot).
10.3. Terminology 81

ProxmoxBackupDocumentation,Release4.2.8‐1
Thisisalsocommonlyknownasan’autoloader’,’taperobot’or’tapejukebox’.
Inventory:
Theinventorystoresthelistofknowntapes(withadditionalstatusinformation).
Catalog:
Amediacatalogstoresinformationaboutthemediacontent.
10.4 Tape Quick Start
1. Configureyourtapehardware(drivesandchangers)
2. Configureoneormoremediapools
3. Labelyourtapecartridges
4. Startyourfirsttapebackupjob...
10.5 Configuration
Pleasenotethatyoucanconfigureanythingusingthegraphicaluserinterfaceorthecommand-line
interface. Bothmethodsresultinthesameconfiguration.
10.5.1 Tapechangers
Tapechangers(robots)arepartofaTapeLibrary. Theycontainanumberofslotstoholdtapecar-
tridges,abarcodereadertoidentifytapecartridgesandanautomatedmethodforloadingtapes.
Youcanskipthisstepifyouareusingastandalonedrive.
82 Chapter10. TapeBackup

ProxmoxBackupDocumentation,Release4.2.8‐1
Linuxisabletoautodetectthesedevices,andyoucangetalistofavailabledevicesusing:
| # proxmox-tape | changer | scan |     |     |     |
| -------------- | ------- | ---- | --- | --- | --- |
┌─────────────────────────────┬─────────┬──────────────┬────────┐
| │ path |     | │ vendor | │ model | │ serial │ |     |
| ------ | --- | -------- | ------- | ---------- | --- |
╞═════════════════════════════╪═════════╪══════════════╪════════╡
| │ /dev/tape/by-id/scsi-CC2C52 |     | │ Quantum | │ Superloader3 | │ CC2C52 │ |     |
| ----------------------------- | --- | --------- | -------------- | ---------- | --- |
└─────────────────────────────┴─────────┴──────────────┴────────┘
InordertouseadevicewithProxmoxBackupServer,youneedtocreateaconfigurationentry:
| # proxmox-tape | changer | create sl3 --path | /dev/tape/by-id/scsi-CC2C52 |     |     |
| -------------- | ------- | ----------------- | --------------------------- | --- | --- |
Wheresl3isanarbitrarynameyoucanchoose.
(cid:174) Note
Please use the persistent device path names from inside /dev/tape/by-id/. Names like /
dev/sg0maypointtoadifferentdeviceafterreboot,andthatisnotwhatyouwant.
This operation can also be carried out from the GUI, by navigating to the Changers tab of Tape
BackupandclickingAdd.
Youcandisplaythefinalconfigurationwith:
| # proxmox-tape | changer | config sl3 |     |     |     |
| -------------- | ------- | ---------- | --- | --- | --- |
┌──────┬─────────────────────────────┐
| │ Name │ Value |     |     | │   |     |     |
| -------------- | --- | --- | --- | --- | --- |
╞══════╪═════════════════════════════╡
| │ name │ sl3 |     |     | │   |     |     |
| ------------ | --- | --- | --- | --- | --- |
├──────┼─────────────────────────────┤
| │ path │ /dev/tape/by-id/scsi-CC2C52 |     |     | │   |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- |
└──────┴─────────────────────────────┘
Orsimplylistallconfiguredchangerdevices(asseenintheChangerstaboftheGUI):
| # proxmox-tape | changer | list |     |     |     |
| -------------- | ------- | ---- | --- | --- | --- |
┌──────┬─────────────────────────────┬─────────┬──────────────┬────────────┐
| │ name │ path |     |     | │ vendor │ | model │ serial | │   |
| ------------- | --- | --- | ---------- | -------------- | --- |
╞══════╪═════════════════════════════╪═════════╪══════════════╪════════════╡
│ sl3 │ /dev/tape/by-id/scsi-CC2C52 │ Quantum │ Superloader3 │ CC2C52 │
└──────┴─────────────────────────────┴─────────┴──────────────┴────────────┘
TheVendor,ModelandSerialnumberareauto-detected,butonlyshownifthedeviceisonline.
Totestyoursetup,pleasequerythestatusofthechangerdevicewith:
| # proxmox-tape | changer | status sl3 |     |     |     |
| -------------- | ------- | ---------- | --- | --- | --- |
┌───────────────┬──────────┬────────────┬─────────────┐
| │ entry-kind | │ entry-id | │ changer-id | │ loaded-slot | │   |     |
| ------------ | ---------- | ------------ | ------------- | --- | --- |
╞═══════════════╪══════════╪════════════╪═════════════╡
| │ drive | │   | 0 │ vtape1 | │   | 1 │ |     |
| ------- | --- | ---------- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 1 │ | │   | │   |     |
| ------ | --- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 2 │ vtape2 | │   | │   |     |
| ------ | --- | ---------- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ ... | │   | ... │ | │   | │   |     |
| ----- | --- | ----- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
(continuesonnextpage)
10.5. Configuration 83

ProxmoxBackupDocumentation,Release4.2.8‐1
(continuedfrompreviouspage)
| │ slot | │   | 16 │ | │   | │   |     |     |
| ------ | --- | ---- | --- | --- | --- | --- |
└───────────────┴──────────┴────────────┴─────────────┘
Tapelibrariesusuallyprovidesomespecialimport/exportslots(alsocalled”mailslots”). Tapesin-
sidethoseslotsareaccessiblefromoutside,makingiteasytoadd/removetapesto/fromthelibrary.
Those tapes are considered to be ”offline”, so backup jobs will not use them. Those special slots
areauto-detectedandmarkedasanimport-exportslotinthestatuscommand.
It’s worth noting that some of the smaller tape libraries don’t have such slots. While they have
something called a ”Mail Slot”, that slot is just a way to grab the tape from the gripper. They are
unabletoholdmediawhiletherobotdoesotherthings. Theyalsodonotexposethat”MailSlot”
overtheSCSIinterface,soyouwon’tseetheminthestatusoutput.
Asaworkaround,youcanmarksomeofthenormalslotsasexportslot. Thesoftwaretreatsthose
slotslikerealimport-exportslots,andthemediainsidethoseslotsareconsideredtobe’offline’
(notavailableforbackup):
| # proxmox-tape | changer | update sl3 --export-slots |     | 15,16 |     |     |
| -------------- | ------- | ------------------------- | --- | ----- | --- | --- |
Afterthat,youcanseethoseartificialimport-exportslotsinthestatusoutput:
| # proxmox-tape | changer | status sl3 |     |     |     |     |
| -------------- | ------- | ---------- | --- | --- | --- | --- |
┌───────────────┬──────────┬────────────┬─────────────┐
| │ entry-kind | │ entry-id | │ changer-id | │ loaded-slot | │   |     |     |
| ------------ | ---------- | ------------ | ------------- | --- | --- | --- |
╞═══════════════╪══════════╪════════════╪═════════════╡
| │ drive | │   | 0 │ vtape1 | │   | 1 │ |     |     |
| ------- | --- | ---------- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ import-export | │   | 15 │ | │   | │   |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ import-export | │   | 16 │ | │   | │   |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 1 │ | │   | │   |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 2 │ vtape2 | │   | │   |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ ... | │   | ... │ | │   | │   |     |     |
| ----- | --- | ----- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 14 │ | │   | │   |     |     |
| ------ | --- | ---- | --- | --- | --- | --- |
└───────────────┴──────────┴────────────┴─────────────┘
Advancedoptions
Sincenotalltapechangerbehavethesame,thereissometimestheneedforconfiguringadvanced
options.
Currentlytherearethefollowing:
• eject-before-unload: Thisisneededforsomechangersthatrequireatapetobeejectedbefore
unloadingfromthedrive.
Youcansettheseoptionswithproxmox-tapelikethis:
| # proxmox-tape | changer | update sl3 --eject-before-unload |     | true |            |            |
| -------------- | ------- | -------------------------------- | --- | ---- | ---------- | ---------- |
| 84             |         |                                  |     |      | Chapter10. | TapeBackup |

ProxmoxBackupDocumentation,Release4.2.8‐1
10.5.2 Tapedrives
Linuxisabletoautodetecttapedrives,andyoucangetalistofavailabletapedrivesusing:
# proxmox-tape drive scan
┌────────────────────────────────┬────────┬─────────────┬────────┐
│ path │ vendor │ model │ serial │
╞════════════════════════════════╪════════╪═════════════╪════════╡
│ /dev/tape/by-id/scsi-12345-sg │ IBM │ ULT3580-TD4 │ 12345 │
└────────────────────────────────┴────────┴─────────────┴────────┘
InordertousethatdrivewithProxmox,youneedtocreateaconfigurationentry. Thiscanbedone
throughTapeBackup->DrivesintheGUIorbyusingthecommandbelow:
# proxmox-tape drive create mydrive --path /dev/tape/by-id/scsi-12345-sg
(cid:174) Note
Please use the persistent device path names from inside /dev/tape/by-id/. Names like /
dev/sg0maypointtoadifferentdeviceafterreboot,andthatisnotwhatyouwant.
10.5. Configuration 85

ProxmoxBackupDocumentation,Release4.2.8‐1
Ifyouhaveatapelibrary,youalsoneedtosettheassociatedchangerdevice:
# proxmox-tape drive update mydrive --changer sl3 --changer-drivenum 0
The--changer-drivenumisonlynecessaryifthetapelibraryincludesmorethanonedrive(the
changerstatuscommandlistsalldrivenumbers).
Youcandisplaythefinalconfigurationwith:
| # proxmox-tape | drive config | mydrive |     |     |     |     |
| -------------- | ------------ | ------- | --- | --- | --- | --- |
┌─────────┬────────────────────────────────┐
| │ Name | │ Value |     | │   |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
╞═════════╪════════════════════════════════╡
| │ name | │ mydrive |     | │   |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- |
├─────────┼────────────────────────────────┤
| │ path | │ /dev/tape/by-id/scsi-12345-sg |     | │   |     |     |     |
| ------ | ------------------------------- | --- | --- | --- | --- | --- |
├─────────┼────────────────────────────────┤
| │ changer | │ sl3 |     | │   |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
└─────────┴────────────────────────────────┘
(cid:174) Note
Thechanger-drivenumvalue0isnotstoredintheconfiguration,becauseitisthedefault.
Tolistallconfigureddrivesuse:
| # proxmox-tape | drive list |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- |
┌──────────┬────────────────────────────────┬─────────┬────────┬─────────────┬────────┐
| │ name | │ path |     | │ changer | │ vendor │ model | │   | serial │ |
| ------ | ------ | --- | --------- | ---------------- | --- | -------- |
╞══════════╪════════════════════════════════╪═════════╪════════╪═════════════╪════════╡
│ mydrive │ /dev/tape/by-id/scsi-12345-sg │ sl3 │ IBM │ ULT3580-TD4 │ 12345 │
└──────────┴────────────────────────────────┴─────────┴────────┴─────────────┴────────┘
TheVendor,ModelandSerialnumberareautodetectedandonlyshownifthedeviceisonline.
Fortesting,youcansimplyquerythedrivestatuswith:
| # proxmox-tape | status --drive | mydrive |     |     |     |     |
| -------------- | -------------- | ------- | --- | --- | --- | --- |
┌────────────────┬──────────────────────────┐
| │ Name | │ Value |     | │   |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
╞════════════════╪══════════════════════════╡
| │ blocksize | │ 0 |     | │   |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ density | │ LTO4 |     | │   |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ compression | │ 1 |     | │   |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ buffer-mode | │ 1 |     | │   |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ alert-flags | │ (empty) |     | │   |     |     |     |
| ------------- | --------- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ file-number | │ 0 |     | │   |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ block-number | │ 0 |     | │   |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ manufactured | │ Fri Dec | 13 01:00:00 | 2019 │ |     |     |     |
| -------------- | --------- | ----------- | ------ | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ bytes-written | │ 501.80 | GiB | │   |     |     |     |
| --------------- | -------- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ bytes-read | │ 4.00 | MiB | │   |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ medium-passes | │ 20 |     | │   |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ medium-wearout | │ 0.12% |     | │   |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- | --- |
├────────────────┼──────────────────────────┤
| │ volume-mounts | │ 2 |     | │   |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
└────────────────┴──────────────────────────┘
| 86  |     |     |     |     | Chapter10. | TapeBackup |
| --- | --- | --- | --- | --- | ---------- | ---------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
Blocksizeshouldalwaysbe0(variableblocksizemode). Thisisthedefaultanyway.
10.5.3 MediaPools
Amediapoolisalogicalcontainerfortapes. Abackupjobtargetsasinglemediapool,soajobonly
usestapesfromthatpool.
MediaSet
Amediasetisagroupofcontinuouslywrittentapes,usedtosplitthelargerpoolintosmaller,
restorableunits. Oneormorebackupjobswritetoamediaset,producinganorderedgroupof
tapes. Media sets are identified by a unique ID. That ID and the sequence number are stored
oneachtapeofthatset(tapelabel).
Mediasetsarethebasicunitforrestoretasks. Thismeansthatyouneedeverytapeintheset
torestorethemediasetcontents. Dataisfullydeduplicatedinsideamediaset.
MediaSetAllocationPolicy
The pool additionally defines how long backup jobs can append data to a media set. The fol-
lowingsettingsarepossible:
• Trytousethecurrentmediaset(continue).
Thissettingproducesonelargemediaset. Whilethisisveryspaceefficient(deduplication,
10.5. Configuration 87

ProxmoxBackupDocumentation,Release4.2.8‐1
nounusedspace),itcanleadtolongrestoretimes,becauserestorejobsneedtoreadall
tapesintheset.
(cid:174) Note
Data is fully deduplicated inside a media set. This also means that data is randomly
distributed over the tapes in the set. Thus, even if you restore a single VM, data may
havetobereadfromalltapesinsidethemediaset.
Largermediasetsarealsomoreerror-prone,becauseasingledamagedtapemakesthe
restorefail.
Usagescenario: Mostlyusedwithtapelibraries. Youmanuallytriggernewsetcreationby
runningabackupjobwiththe--exportoption.
(cid:174) Note
Retentionperiodstartswiththeexistenceofanewermediaset.
• Alwayscreateanewmediaset(always).
With this setting, each backup job creates a new media set. This is less space efficient,
becausethemediafromthelastsetmaynotbefullywritten,leavingtheremainingspace
unused.
The advantage is that this produces media sets of minimal size. Small sets are easier to
handle, can be moved more conveniently to an off-site vault, and can be restored much
faster.
(cid:174) Note
Retentionperiodstartswiththecreationtimeofthemediaset.
• CreateanewsetwhenthespecifiedCalendarEventtriggers.
ThisallowsyoutospecifypointsintimebyusingsystemdlikeCalendarEventspecifications
(seesystemd.timemanpage).
Forexample,thevalueweekly(orMon *-*-* 00:00:00)willcreateanewseteachweek.
Thisbalancesbetweenspaceefficiencyandmediacount.
(cid:174) Note
Retentionperiodstartsonthecreationtimeofthenextmedia-setor,ifthatdoesnot
exist,whenthecalendareventnexttriggersafterthecurrentmedia-setstarttime.
Additionally,thefollowingeventsmayallocateanewmediaset:
• Requiredtapeisoffline(andyouuseatapelibrary).
• Currentsetcontainsdamagedorretiredtapes.
• Mediapoolencryptionhaschanged
• Databaseconsistencyerrors,forexample,iftheinventorydoesnotcontaintherequired
mediainformation,oritcontainsconflictinginformation(outdateddata).
88 Chapter10. TapeBackup

ProxmoxBackupDocumentation,Release4.2.8‐1
RetentionPolicy
Defineshowlongwewanttokeepthedata.
• Alwaysoverwritemedia.
• Protectdataforthedurationspecified.
We use systemd like time spans to specify durations, e.g. 2 weeks (see systemd.time
manpage).
• Neveroverwritedata.
HardwareEncryption
LTO-4 (or later) tape drives support hardware encryption. If you configure the media pool to
useencryption,alldatawrittentothetapesisencryptedusingtheconfiguredkey.
Thisway,unauthorizeduserscannotreaddatafromthemedia,forexample,ifyoulooseatape
whileshippingtoanoffsitelocation.
(cid:174) Note
Ifthebackupclientalsoencryptsdata,dataonthetapewillbedoubleencrypted.
The password protected key is stored on each medium, so that it is possible to restore the key
usingthepassword. Pleasemakesuretorememberthepassword,incaseyouneedtorestore
thekey.
Tocreateanewmediapool, addonefromTapeBackup->MediaPoolsintheGUI,orenterthe
followingcommand:
// proxmox-tape pool create <name> [OPTIONS]
# proxmox-tape pool create daily
Additionaloptionscanbesetlater,usingtheupdatecommand:
# proxmox-tape pool update daily --allocation daily --retention 7days
Tolistallconfiguredpoolsuse:
# proxmox-tape pool list
┌───────┬──────────┬────────────┬───────────┬──────────┐
│ name │ drive │ allocation │ retention │ template │
╞═══════╪══════════╪════════════╪═══════════╪══════════╡
│ daily │ mydrive │ daily │ 7days │ │
└───────┴──────────┴────────────┴───────────┴──────────┘
10.5. Configuration 89

ProxmoxBackupDocumentation,Release4.2.8‐1
10.5.4 TapeBackupJobs
Toautomatetapebackup,youcanconfiguretapebackupjobswhichwritedatastorecontenttoa
mediapool,basedonaspecifictimeschedule. Therequiredsettingsare:
| • store:    | Thedatastoreyouwanttobackup                         |     |     |     |     |     |
| ----------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
| • pool:     | Themediapool-onlytapecartridgesfromthatpoolareused. |     |     |     |     |     |
| • drive:    | Thetapedrive.                                       |     |     |     |     |     |
| • schedule: | Jobschedule(seeCalendarEvents)                      |     |     |     |     |     |
Forexample,toconfigureatapebackupjobfordatastorevmstore1use:
| # proxmox-tape  | backup-job | create job2 | --store vmstore1 | \   |     |     |
| --------------- | ---------- | ----------- | ---------------- | --- | --- | --- |
| --pool yourpool | --drive    | yourdrive   | --schedule daily |     |     |     |
Thebackupincludesallsnapshotsfromabackupgroupbydefault. Youcansetthelatest-only
flagtoincludeonlythelatestsnapshots:
| # proxmox-tape | backup-job | update job2 | --latest-only |     |     |     |
| -------------- | ---------- | ----------- | ------------- | --- | --- | --- |
Backup jobs can use email to send tape request notifications or report errors. You can set the
notificationuserwith:
| # proxmox-tape | backup-job | update job2 | --notify-user | root@pam |     |     |
| -------------- | ---------- | ----------- | ------------- | -------- | --- | --- |
(cid:174) Note
Theemailaddressisapropertyoftheuser(seeUserManagement).
| 90  |     |     |     |     | Chapter10. | TapeBackup |
| --- | --- | --- | --- | --- | ---------- | ---------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Itissometimesusefultoejectthetapefromthedriveafterabackup. Forastandalonedrive,the
eject-mediaoptionejectsthetape, makingsurethatthefollowingbackupcannotusethetape
(unless someone manually loads the tape again). For tape libraries, this option unloads the tape
toafreeslot,whichprovidesbetterdustprotectionthaninsideadrive:
# proxmox-tape backup-job update job2 --eject-media
(cid:174) Note
Forfailedjobs,thetaperemainsinthedrive.
Fortapelibraries,theexport-media-setoptionmovesalltapesfromthemediasettoanexport
slot, makingsurethatthefollowingbackupcannotusethetapes. Anoperatorcanpickupthose
tapesandmovethemtoavault.
# proxmox-tape backup-job update job2 --export-media-set
(cid:174) Note
The export-media-set option can be used to force the start of a new media set, because
tapesfromthecurrentsetarenolongeronline.
Itisalsopossibletorunbackupjobsmanually:
# proxmox-tape backup-job run job2
Toremoveajob,pleaseuse:
# proxmox-tape backup-job remove job2
By default, all (recursive) namespaces of the datastore are included in a tape backup. You can
specifyasinglenamespacewithnsandadepthwithmax-depth. Forexample:
# proxmox-tape backup-job update job2 --ns mynamespace --max-depth 3
Ifnomax-depthisgiven,itwillincludeallrecursivenamespaces.
ThissamefunctionalityalsoexistsintheGUI,undertheBackupJobstabof TapeBackup,where
LocalDatastorerelatestothedatastoreyouwanttobackupandMediaPoolisthepooltobackup
to.
10.5. Configuration 91

ProxmoxBackupDocumentation,Release4.2.8‐1
10.6 Administration
Manysub-commandsoftheproxmox-tapecommand-linetoolstakeaparametercalled--drive,
whichspecifiesthetapedriveyouwanttoworkon. Forconvenience, youcansetthisinanenvi-
ronmentvariable:
| # export PROXMOX_TAPE_DRIVE=mydrive |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- |
You can then omit the --drive parameter from the command. If the drive has an associated
changer device, you may also omit the changer parameter from commands that need a changer
device,forexample:
| # proxmox-tape | changer status |     |     |     |     |     |
| -------------- | -------------- | --- | --- | --- | --- | --- |
shoulddisplaythechangerstatusofthechangerdeviceassociatedwithdrivemydrive.
10.6.1 LabelTapes
Bydefault,tapecartridgesalllookthesame,soyouneedtoputalabelonthemforuniqueidenti-
fication. First,putastickypaperlabelwithsomehumanreadabletextonthecartridge.
IfyouuseaTapeLibrary,youshouldusean8characterstringencodedasCode39,asdefinedin
the LTO Ultrium Cartridge Label Specification. You can either buy such barcode labels from your
cartridge vendor, or print them yourself. You can use our LTO Barcode Generator app to print
them.
Next,youneedtowritethatsamelabeltexttothetape,sothatthesoftwarecanuniquelyidentify
thetapetoo.
Forastandalonedrive,manuallyinsertthenewtapecartridgeintothedriveandrun:
| # proxmox-tape | label --changer-id | <label-text> | [--pool | <pool-name>] |     |     |
| -------------- | ------------------ | ------------ | ------- | ------------ | --- | --- |
Youmayomitthe--poolargumenttoallowthetapetobeusedbyanypool.
(cid:174) Note
Forsafetyreasons,thiscommandfailsifthetapecontainsanydata. Ifyouwanttooverwriteit
anyway,erasethetapefirst.
Youcanverifysuccessbyreadingbackthelabel:
| # proxmox-tape | read-label |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- |
┌─────────────────┬──────────────────────────────────────┐
| │ Name | │ Value |     |     | │   |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
╞═════════════════╪══════════════════════════════════════╡
| │ changer-id | │ vtape1 |     |     | │   |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- |
├─────────────────┼──────────────────────────────────────┤
| │ uuid | │ 7f42c4dd-9626-4d89-9f2b-c7bc6da7d533 |     |     | │   |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- |
├─────────────────┼──────────────────────────────────────┤
| │ ctime | │ Wed Jan | 6 09:07:51 | 2021 | │   |     |     |
| ------- | --------- | ---------- | ---- | --- | --- | --- |
├─────────────────┼──────────────────────────────────────┤
| │ pool | │ daily |     |     | │   |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
├─────────────────┼──────────────────────────────────────┤
| │ media-set-uuid | │ 00000000-0000-0000-0000-000000000000 |     |     | │   |     |     |
| ---------------- | -------------------------------------- | --- | --- | --- | --- | --- |
├─────────────────┼──────────────────────────────────────┤
| │ media-set-ctime | │ Wed Jan | 6 09:07:51 | 2021 | │   |     |     |
| ----------------- | --------- | ---------- | ---- | --- | --- | --- |
└─────────────────┴──────────────────────────────────────┘
(cid:174)
Note
Themedia-set-uuidusingallzerosindicatesanemptytape(notusedbyanymediaset).
| 92  |     |     |     |     | Chapter10. | TapeBackup |
| --- | --- | --- | --- | --- | ---------- | ---------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Ifyouhaveatapelibrary,applythestickybarcodelabeltothetapecartridgesfirst. Thenloadthose
emptytapesintothelibrary. Youcanthenlabelallunlabeledtapeswithasinglecommand:
| # proxmox-tape | barcode-label | [--pool | <pool-name>] |     |     |     |     |     |     |
| -------------- | ------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
10.6.2 RunTapeBackups
TomanuallyrunabackupjobclickRunNowintheGUIorusethecommand:
| # proxmox-tape | backup | <store> <pool> | [OPTIONS] |     |     |     |     |     |     |
| -------------- | ------ | -------------- | --------- | --- | --- | --- | --- | --- | --- |
Thefollowingoptionsareavailable:
| --eject-media |     | Ejectmediauponjobcompletion. |      |          |          |     |            |           |     |
| ------------- | --- | ---------------------------- | ---- | -------- | -------- | --- | ---------- | --------- | --- |
|               |     | It is normally               | good | practice | to eject | the | tape after | use. This | un- |
mountsthetapefromthedriveandpreventsthetapefromgetting
dusty.
| --export-media-set |     | Exportmediasetuponjobcompletion. |        |      |      |                          |           |               |     |
| ------------------ | --- | -------------------------------- | ------ | ---- | ---- | ------------------------ | --------- | ------------- | --- |
|                    |     | After a successful               | backup | job, | this | moves                    | all tapes | from the used |     |
|                    |     | mediasetintoimport-exportslots.  |        |      |      | Theoperatorcanthenpickup |           |               |     |
thosetapesandmovethemtoamediavault.
| --ns |     | Thenamespacetobackup.                        |     |     |     |     |     |            |     |
| ---- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
|      |     | Usedifyouonlywanttobackupaspecificnamespace. |     |     |     |     |     | Ifomitted, |     |
therootnamespaceisassumed.
| --max-depth |     | Thedepthtorecursenamespaces.                   |     |     |     |     |     |            |     |
| ----------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
|             |     | 0meansnorecursionatall(onlythegivennamespace). |     |     |     |     |     | Ifomitted, |     |
allnamespacesarerecursed(belowthegivenone).
10.6.3 RestorefromTape
Restoreisdoneatmedia-setgranularity,soyoufirstneedtofindoutwhichmediasetcontainsthe
datayouwanttorestore. Thisinformationisstoredinthemediacatalog. Ifyoudonothavemedia
catalogs,youneedtorestorethemfirst. Pleasenotethatyouneedthecatalogtofindyourdata,
butrestoringacompletemedia-setdoesnotneedmediacatalogs.
Thefollowingcommandliststhemediacontent(fromcatalog):
| # ┌────────────┬──────┬──────────────────────────┬────────┬────────────────────────────────┬──────────────────────────────────────┐ proxmox-tape | media    | content        |     |          |     |            |     |     |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- |
| │ label-text                                                                                                                                     | │ pool │ | media-set-name |     | │ seq-nr |     | │ snapshot |     |     | │␣  |
| ,→media-set-uuid                                                                                                                                 |          |                | │   |          |     |            |     |     |     |
╞════════════╪══════╪══════════════════════════╪════════╪════════════════════════════════╪══════════════════════════════════════╡
│ TEST01L8 │ p2 │ Wed Jan 13 13:55:55 2021 │ 0 │ vm/201/2021-01-11T10:43:48Z │␣
| ,→9da37a55-aac7-4deb-91c6-482b3b675f30 |     |     | │   |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
├────────────┼──────┼──────────────────────────┼────────┼────────────────────────────────┼──────────────────────────────────────┤
| │   | ... │ ... │ |     |     | ... │ | ... | │ ... |     |     | │ ␣ |
| --- | ----------- | --- | --- | ----- | --- | ----- | --- | --- | --- |
| ,→  |             | ... | │   |       |     |       |     |     |     |
└────────────┴──────┴──────────────────────────┴────────┴────────────────────────────────┴──────────────────────────────────────┘
Arestorejobreadsthedatafromthemediasetandmovesitbacktodatadisk(datastore):
| // proxmox-tape | restore | <media-set-uuid>                     | <datastore> |     |     |         |     |     |     |
| --------------- | ------- | ------------------------------------ | ----------- | --- | --- | ------- | --- | --- | --- |
| # proxmox-tape  | restore | 9da37a55-aac7-4deb-91c6-482b3b675f30 |             |     |     | mystore |     |     |     |
SingleSnapshotRestore
Sometimes it is not necessary to restore an entire media-set, but only some specific snapshots
| fromthetape.         | Thiscanbeachievedwiththesnapshotsparameter: |     |     |     |     |     |     |     |     |
| -------------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.6. Administration |                                             |     |     |     |     |     |     |     | 93  |

ProxmoxBackupDocumentation,Release4.2.8‐1
// proxmox-tape restore <media-set-uuid> <datastore> [<snapshot>]
# proxmox-tape restore 9da37a55-aac7-4deb-91c6-482b3b675f30 mystore sourcestore:host/hostname/
,→2022-01-01T00:01:00Z
Thisfirstrestoresthesnapshottoatemporarylocation,thenrestorestherelevantchunkarchives,
andfinallyrestoresthesnapshotdatatothetargetdatastore.
Thesnapshotparametercanbepassedmultipletimes,inordertorestoremultiplesnapshotswith
onerestoreaction.
(cid:174) Note
Whenusingthesinglesnapshotrestore,thetapemustbetraversedmorethanonce,which,if
yourestoremanysnapshotsatonce,cantakelongerthanrestoringthewholedatastore.
Namespaces
Itisalsopossibletoselectandmapspecificnamespacesfromamedia-setduringarestore. Thisis
possiblewiththenamespacesparameter. Theformatfortheparameteris:
store=<source-datastore>[,source=<source-ns>][,target=<target-ns>][,max-depth=<depth>]
If sourceortargetisnotgiven,therootnamespaceisassumed. Whennomax-depthisgiven,
thesourcenamespacewillbefullyrecursed.
Anexamplerestorecommand:
# proxmox-tape restore 9da37a55-aac7-4deb-91c6-482b3b675f30 mystore --namespaces␣
,→store=sourcedatastore,source=ns1,target=ns2,max-depth=2
Theparametercanbegivenmultipletimes. Itcanalsobecombinedwiththesnapshotsparameter
toonlyrestorethosesnapshotsandmapthemtodifferentnamespaces.
10.6.4 UpdateInventory
10.6.5 RestoreCatalog
Torestoreacatalogfromanexistingtape,justinsertthetapeintothedriveandexecute:
# proxmox-tape catalog
Youcanrestorefromatapeevenwithoutanexistingcatalog,butonlythewholemediaset. Ifyou
dothis,thecatalogwillbeautomaticallycreated.
94 Chapter10. TapeBackup

ProxmoxBackupDocumentation,Release4.2.8‐1
10.6.6 EncryptionKeyManagement
Proxmox Backup Server also provides an interface for handling encryption keys on the backup
server. EncryptionkeyscanbemanagedfromtheTapeBackup->EncryptionKeyssectionofthe
GUIorthroughtheproxmox-tape keycommand-linetool. Tocreateanewencryptionkeyfrom
thecommandline:
| # proxmox-tape   | key create    | --hint "tape | pw 2020" |     |     |
| ---------------- | ------------- | ------------ | -------- | --- | --- |
| Tape Encryption  | Key Password: | **********   |          |     |     |
| Verify Password: | **********    |              |          |     |     |
,→"14:f8:79:b9:f5:13:e5:dc:bf:b6:f9:88:48:51:81:dc:79:bf:a0:22:68:47:d1:73:35:2d:b6:20:e1:7f:f5:0f
,→"
Listexistingencryptionkeys:
| # proxmox-tape | key list |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
┌───────────────────────────────────────────────────┬───────────────┐
| │ fingerprint |     |     |     | │ hint | │   |
| ------------- | --- | --- | --- | ------ | --- |
╞═══════════════════════════════════════════════════╪═══════════════╡
│ 14:f8:79:b9:f5:13:e5:dc: ... :b6:20:e1:7f:f5:0f │ tape pw 2020 │
└───────────────────────────────────────────────────┴───────────────┘
Toshowencryptionkeydetails:
# proxmox-tape key show 14:f8:79:b9:f5:13:e5:dc:...:b6:20:e1:7f:f5:0f
┌─────────────┬───────────────────────────────────────────────┐
| │ Name | │ Value |     |     | │   |     |
| ------ | ------- | --- | --- | --- | --- |
╞═════════════╪═══════════════════════════════════════════════╡
| │ kdf | │ scrypt |     |     | │   |     |
| ----- | -------- | --- | --- | --- | --- |
├─────────────┼───────────────────────────────────────────────┤
| │ created | │ Sat Jan | 23 14:47:21 | 2021 | │   |     |
| --------- | --------- | ----------- | ---- | --- | --- |
├─────────────┼───────────────────────────────────────────────┤
| │ modified | │ Sat Jan | 23 14:47:21 | 2021 | │   |     |
| ---------- | --------- | ----------- | ---- | --- | --- |
├─────────────┼───────────────────────────────────────────────┤
| │ fingerprint | │ 14:f8:79:b9:f5:13:e5:dc:...:b6:20:e1:7f:f5:0f |     |     | │   |     |
| ------------- | ----------------------------------------------- | --- | --- | --- | --- |
(continuesonnextpage)
10.6. Administration 95

ProxmoxBackupDocumentation,Release4.2.8‐1
(continuedfrompreviouspage)
├─────────────┼───────────────────────────────────────────────┤
| │ hint | │ tape pw | 2020 |     | │   |     |     |
| ------ | --------- | ---- | --- | --- | --- | --- |
└─────────────┴───────────────────────────────────────────────┘
The paperkey subcommand can be used to create a QR encoded version of a tape encryption
key. The following command sends the output of thepaperkey command to a text file, for easy
printing:
proxmox-tape key paperkey <fingerprint> --output-format text > qrkey.txt
RestoringEncryptionKeys
You can restore the encryption key from the tape, using the password used to generate the key.
| First,loadthetapeyouwanttorestoreintothedrive. |               |             |     | Thenrun: |     |     |
| ---------------------------------------------- | ------------- | ----------- | --- | -------- | --- | --- |
| # proxmox-tape                                 | key restore   |             |     |          |     |     |
| Tape Encryption                                | Key Password: | *********** |     |          |     |     |
Ifthepasswordiscorrect,thekeywillgetimportedtothedatabase. Furtherrestorejobsautomat-
icallyuseanyavailablekey.
10.6.7 TapeCleaning
LTOtapedrivesrequireregularcleaning. Thisisdonebyloadingacleaningcartridgeintothedrive,
whichisamanualtaskforstandalonedrives.
Fortapelibraries,cleaningcartridgesareidentifiedusingspeciallabelsstartingwithletters”CLN”.
Forexample,ourtapelibraryhasacleaningcartridgeinsideslot3:
| # proxmox-tape | changer | status sl3 |     |     |     |     |
| -------------- | ------- | ---------- | --- | --- | --- | --- |
┌───────────────┬──────────┬────────────┬─────────────┐
| │ entry-kind | │ entry-id | │ changer-id | │ loaded-slot | │   |     |     |
| ------------ | ---------- | ------------ | ------------- | --- | --- | --- |
╞═══════════════╪══════════╪════════════╪═════════════╡
| │ drive | │   | 0 │ vtape1 | │   | 1 │ |     |     |
| ------- | --- | ---------- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 1 │ | │   | │   |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 2 │ vtape2 | │   | │   |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ slot | │   | 3 │ CLN001CU | │   | │   |     |     |
| ------ | --- | ------------ | --- | --- | --- | --- |
├───────────────┼──────────┼────────────┼─────────────┤
| │ ... | │   | ... │ | │   | │   |     |     |
| ----- | --- | ----- | --- | --- | --- | --- |
└───────────────┴──────────┴────────────┴─────────────┘
Toinitiateacleaningoperationsimplyrun:
| # proxmox-tape | clean |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
Thiscommanddoesthefollowing:
• findthecleaningtape(inslot3)
• unloadthecurrentmediafromthedrive(backtoslot1)
• loadthecleaningtapeintothedrive
• rundrivecleaningoperation
• unloadthecleaningtape(toslot3)
| 10.7 WORM | Tapes |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
WORM(writeonce,readmany)tapesarespecialcartridgesthatcannotbedeletedoroverwritten.
Thismaybeusefulforlegalorprotectionpurposes.
| 96  |     |     |     |     | Chapter10. | TapeBackup |
| --- | --- | --- | --- | --- | ---------- | ---------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Ifyouwanttousethem,youmustuseamediapoolwitharetentionpolicyofkeep. Otherwise,a
backupjobcanfailwhenittriestoeraseoroverwritethetape.
ProxmoxBackupServermakesnodistinctionbetweennormalandWORMtapes. Toavoidconfu-
sion,useadifferentnamingschemeforWORMbackupsandusededicatedmediapoolsforthem.
DonotmixWORMandnon-WORMtapesinthesamemediapool.
10.8 Example Setups
Hereareafewexamplesetupsformanagingmediapoolsandschedules. Thisisnotanexhaustive
list,andtherearemanymorepossiblecombinationsofusefulsettings.
10.8.1 SingleContinuedMediaSet
Themostsimplesetup: alwayscontinuethemedia-setandneverexpire.
Allocationpolicy:
continue
Retentionpolicy:
keep
Thissetuphastheadvantageofbeingeasytomanageandreusesthebenefitsfromdeduplication
as much as possible. But, it also provides no redundancy, meaning a failure of any single tape
wouldrenderallbackupsreferringtochunksfromthattapeunusable.
Ifyouwanttostartanewmedia-setmanually,youcansetthecurrentlywritablemediaoftheset
eitherto’full’,orsetthelocationtoanoff-sitevault.
10.8.2 WeekdayScheme
Aslightlymorecomplexscheme,wherethegoalistohaveanindependenttapeormediasetfor
eachweekday,forexamplefromMondaytoFriday. Thiscanbesolvedbyhavingaseparatemedia
poolforeachday,so’Monday’,’Tuesday’,etc.
Allocationpolicy:
shouldbe’mon’forthe’Monday’pool,’tue’fortheTuesdaypoolandsoon.
Retentionpolicy:
overwrite
Thereshouldbeoneormoretape-backupjobsforeachpoolonthecorrespondingweekday. This
schemeisstillverymanageablewithonemediasetperweekday,andcouldbemovedoff-siteeasily.
10.8.3 MultiplePoolswithDifferentPolicies
Complex setups are also possible, with multiple media pools configured with different allocation
andretentionpolicies.
Anexamplewouldbetohavetwomediapools. Thefirstconfiguredwithweeklyallocationanda
fewweeksofretention:
Allocationpolicy:
mon
Retentionpolicy:
3weeks
Thesecondpoolconfiguredwithyearlyallocationthatdoesnotexpire:
Allocationpolicy:
yearly
10.8. ExampleSetups 97

ProxmoxBackupDocumentation,Release4.2.8‐1
Retentionpolicy:
keep
Incombinationwithfittingprunesettingsandtapebackupschedules,thisachieveslong-termstor-
ageofsomebackups,whilekeepingtherecentbackupsonsmallermediasetsthatexpireroughly
every4weeks(thatis,threeplusthecurrentweek).
10.9 Disaster Recovery
In case of major disasters, important data, or even whole servers might be destroyed or at least
damaged up to the point where everything - sometimes including the backup server - has to be
restoredfromabackup. Forsuchcases,thefollowingstep-by-stepguidewillhelpyoutosetupthe
ProxmoxBackupServerandrestoreeverythingfromtapebackups.
ThefollowingguidewillexplainthenecessarystepsusingboththewebGUIandthecommandline
tools. Foranoverviewofthecommandlinetools,seeCommand-lineTools.
10.9.1 SettingUpaDatastore
AfteryousetupanewProxmoxBackupServer,asoutlinedintheInstallationchapter,firstsetup
adatastoresoatapecanberestoredtoit:
1. GotoAdministration->Storage/Disksandmakesurethatthediskthatwillbeusedasa
datastoreshowsup.
2. UndertheDirectoryorZFStabs,youcaneitherchoosetocreateadirectoryorcreateaZFS
zpool,respectively. HereyoucanalsodirectlyaddthenewlycreateddirectoryorZFSzpool
asadatastore.
Alternatively, the proxmox-backup-manager can be used to perform the same tasks. For more
information,checktheDatastoredocumentation.
10.9.2 SettingUptheTapeDrive
1. Makesureyouhaveaproperlyworkingtapedriveand/orchangermatchingtomediumyou
wanttorestorefrom.
2. Connect the tape changer(s) and the tape drive(s) to the backup server. These should be
detectedautomaticallybyLinux. Youcangetalistofavailabledrivesusing:
# proxmox-tape drive scan
┌────────────────────────────────┬────────┬─────────────┬────────┐
│ path │ vendor │ model │ serial │
╞════════════════════════════════╪════════╪═════════════╪════════╡
│ /dev/tape/by-id/scsi-12345-sg │ IBM │ ULT3580-TD4 │ 12345 │
└────────────────────────────────┴────────┴─────────────┴────────┘
Youcangetalistofavailablechangerswith:
# proxmox-tape changer scan
┌─────────────────────────────┬─────────┬──────────────┬────────┐
│ path │ vendor │ model │ serial │
╞═════════════════════════════╪═════════╪══════════════╪════════╡
│ /dev/tape/by-id/scsi-CC2C52 │ Quantum │ Superloader3 │ CC2C52 │
└─────────────────────────────┴─────────┴──────────────┴────────┘
Formoreinformation,pleasereadthechaptersonTapechangersandTapedrives.
3. Ifyouhaveatapechanger,gotothewebinterfaceoftheProxmoxBackupServer,gotoTape
Backup->Changersandaddit. Forexamplesusingthecommandline,readthechapteron
Tapechangers. IfthechangerhasbeendetectedcorrectlybyLinux,thechangershouldshow
upinthelist.
98 Chapter10. TapeBackup

ProxmoxBackupDocumentation,Release4.2.8‐1
4. In the web interface, go to Tape Backup -> Drives and add the tape drive that will be used
toreadthetapes. Forexamplesusingthecommandline,readthechapteronTapedrives. If
the tape drive has been detected correctly by Linux, the drive should show up in the list. If
the drive also has a tape changer, make sure to select the changer as well and assign it the
correctdrivenumber.
10.9.3 RestoringDataFromtheTape
The following guide will explain the steps necessary to restore data from a tape, which can be
done over either the web GUI or the command line. For details on the command line, read the
documentationontheproxmox-tapetool.
Torestoredatafromtapes,dothefollowing:
1. Insert the first tape (as displayed on the label) into the tape drive or, if a tape changer is
available,usethetapechangertoinsertthetapeintotherightdrive. ThewebGUIcanalso
beusedtoloadortransfertapesbetweentapedrivesbyselectingthechanger.
2. If the backup has been encrypted, the encryption keys need to be restored as well. In the
EncryptionKeystab,pressRestoreKey. Formoredetailsorexamplesthatusethecommand
line,readtheEncryptionKeyManagementchapter.
3. Theprocedurefor restoringdata is slightly differentdependingon whether you areusing a
standalonetapedriveorachanger:
• Forchangers,theprocedureissimple:
1. Insertalltapesfromthemediasetyouwanttorestorefrom.
2. ClickonthechangerinthewebGUI,clickInventory,makesureRestoreCatalogis
selectedandpressOK.
• Forstandalonedrives,theprocedurewouldbe:
1. Insertthefirsttapeofthemediaset.
2. ClickCatalog.
3. Ejectthetape,thenrepeatthestepsfortheremainingtapesofthemediaset.
4. GobacktoTapeBackup. IntheContenttab,pressRestoreandselectthedesiredmediaset.
Choosethesnapshotyouwanttorestore, pressNext, selectthedriveandtargetdatastore
andpressRestore.
5. By going to the datastore where the data has been restored, under the Content tab you
shouldbeabletoseetherestoredsnapshots. Inordertoaccessthebackupsfromanother
machine, you will need to configure the access to the backup server. Go to Configuration
-> Access Control and either create a new user, or a new API token (API tokens allow easy
revocation if the token is compromised). Under Permissions, add the desired permissions,
e.g. DatastoreBackup.
6. Youcannowperformvirtualmachine,containerorfilerestores. Younowhavethefollowing
options:
• IfyouwanttorestorefilesonLinuxdistributionsthatarenotbasedonProxmoxproducts
or you prefer using a command line tool, you can use the proxmox-backup-client, as
explained in the Restoring Data chapter. Use the newly created API token to be able to
accessthedata. Youcanthenrestoreindividualfilesormountanarchivetoyoursystem.
• If you want to restore virtual machines or containers on a Proxmox VE server, add the
datastore of the backup server as storage and go to Backups. Here you can restore
VMs and containers, including their configuration. For more information on restoring
backupsinProxmoxVE,visittheRestorechapteroftheProxmoxVEdocumentation.
10.9. DisasterRecovery 99

ProxmoxBackupDocumentation,Release4.2.8‐1
| 100 | Chapter10. | TapeBackup |
| --- | ---------- | ---------- |

CHAPTER
ELEVEN
|     |     |     | MANAGING | REMOTES | & SYNC |
| --- | --- | --- | -------- | ------- | ------ |
11.1 Remote
A remote refers to a separate Proxmox Backup Server installation and a user on that installa-
tion, from which you can sync datastores to a local datastore with a Sync Job. You can config-
ure remotes in the web interface, under Configuration -> Remotes. Alternatively, you can use
the remote subcommand. The configuration information for remotes is stored in the file /etc/
proxmox-backup/remote.cfg.
Toaddaremote,youneeditshostnameorIPaddress,auseridandpasswordontheremote,and
itscertificatefingerprint. Togetthefingerprint,usetheproxmox-backup-manager cert info
commandontheremote,ornavigatetoDashboardintheremote’swebinterfaceandselectShow
Fingerprint.
| # proxmox-backup-manager | cert                                       | info |grep Fingerprint |     |     |     |
| ------------------------ | ------------------------------------------ | ---------------------- | --- | --- | --- |
| Fingerprint (sha256):    | 64:d3:ff:3a:50:38:53:5a:9b:f7:50:...:ab:fe |                        |     |     |     |
Using the information specified above, you can add a remote from the Remotes configuration
panel,orbyusingthecommand:
# proxmox-backup-manager remote create pbs2 --host pbs2.mydomain.example --userid sync@pam --
,→password 'SECRET' --fingerprint 64:d3:ff:3a:50:38:53:5a:9b:f7:50:...:ab:fe
Use the list, show, update, remove subcommands of proxmox-backup-manager remote to
manageyourremotes:
| # proxmox-backup-manager | remote | update pbs2 --host | pbs2.example |     |     |
| ------------------------ | ------ | ------------------ | ------------ | --- | --- |
| # proxmox-backup-manager | remote | list               |              |     |     |
┌──────┬──────────────┬──────────┬───────────────────────────────────────────┬─────────┐
| │ name │ host | │ userid | │ fingerprint |     | │ comment | │   |
| ------------- | -------- | ------------- | --- | --------- | --- |
╞══════╪══════════════╪══════════╪═══════════════════════════════════════════╪═════════╡
│ pbs2 │ pbs2.example │ sync@pam │64:d3:ff:3a:50:38:53:5a:9b:f7:50:...:ab:fe │ │
└──────┴──────────────┴──────────┴───────────────────────────────────────────┴─────────┘
| # proxmox-backup-manager | remote | remove pbs2 |     |     |     |
| ------------------------ | ------ | ----------- | --- | --- | --- |
101

ProxmoxBackupDocumentation,Release4.2.8‐1
| 11.2 Sync | Jobs |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Sync jobs are configured to pull the contents of a datastore on a Remote to a local datas-
tore. You can manage sync jobs in the web interface, from the Sync Jobs tab of the Datas-
tore panel or from that of the Datastore itself. Alternatively, you can manage them with the
proxmox-backup-manager sync-job command. The configuration information for sync jobs
isstoredat/etc/proxmox-backup/sync.cfg. Tocreateanewsyncjob,clicktheaddbuttonin
theGUI,orusethecreatesubcommand. Aftercreatingasyncjob,youcanstartitmanuallyfrom
theGUI,usetherunsubcommand,orprovideitwithaschedule(seeCalendarEvents)torunreg-
ularly. Backupsnapshots, groupsandnamespaceswhicharenolongeravailableontheRemote
datastore can be removed from the local datastore as well by setting the remove-vanished op-
tionforthesyncjob. Settingtheverified-onlyorencrypted-onlyflagsallowstolimitthesync
jobstobackupsnapshotswhichhavebeenverifiedorencrypted,respectively. Thisisparticularly
ofinterestwhensendingbackupstoalesstrustedremotebackupserver.
# proxmox-backup-manager sync-job create pbs2-local --remote pbs2 --remote-store local --
| ,→store local | --schedule | 'Wed 02:30' |     |     |     |
| ------------- | ---------- | ----------- | --- | --- | --- |
# proxmox-backup-manager sync-job update pbs2-local --comment 'offsite'
| # proxmox-backup-manager |     | sync-job | list |     |     |
| ------------------------ | --- | -------- | ---- | --- | --- |
┌────────────┬───────┬────────┬──────────────┬───────────┬─────────┐
| │ id | │ store | │ remote │ remote-store | │ schedule | │ comment | │   |
| ---- | ------- | ----------------------- | ---------- | --------- | --- |
╞════════════╪═══════╪════════╪══════════════╪═══════════╪═════════╡
| │ pbs2-local | │ local | │ pbs2 │ local | │ Wed 02:30 | │ offsite | │   |
| ------------ | ------- | -------------- | ----------- | --------- | --- |
└────────────┴───────┴────────┴──────────────┴───────────┴─────────┘
| # proxmox-backup-manager |                | sync-job                           | run pbs2-local |     |     |
| ------------------------ | -------------- | ---------------------------------- | -------------- | --- | --- |
| Starting                 | datastore sync | job 'pbs2:local:local::pbs2-local' |                |     |     |
| sync datastore           | 'local'        | from 'pbs2/local'                  |                |     |     |
----
Syncing datastore 'local', root namespace into datastore 'local', root namespace
| found 0 groups | to sync | (out of 0 total) |     |     |     |
| -------------- | ------- | ---------------- | --- | --- | --- |
Finished syncing root namespace, current progress: 0 groups, 0 snapshots
| Summary:            | sync job found                            | no new data | to pull |     |     |
| ------------------- | ----------------------------------------- | ----------- | ------- | --- | --- |
| sync job            | 'pbs2:local:local::pbs2-local'            |             | end     |     |     |
| queued notification | (id=a8ce89b5-330a-4ad7-9906-3a876e7ed174) |             |         |     |     |
TASK OK
| # proxmox-backup-manager |     | sync-job | remove pbs2-local |     |     |
| ------------------------ | --- | -------- | ----------------- | --- | --- |
Tosetupsyncjobs,theconfiguringuserneedsthefollowingpermissions:
1. Remote.Readonthe/remote/{remote}/{remote-store}path
2. AtleastDatastore.Backuponthelocaltargetdatastore(/datastore/{store})
(cid:174) Note
Asyncjobcanonlysyncbackupgroupsthattheconfiguredremote’suser/APItokencanread. If
aremoteisconfiguredwithauser/APItokenthatonlyhasDatastore.Backupprivileges,only
thelimitedsetofaccessiblesnapshotsownedbythatuser/APItokencanbesynced.
If the remove-vanished option is set, Datastore.Prune is required on the local datastore as
well. Iftheowneroptionisnotset(defaultingtoroot@pam)orissettosomethingotherthanthe
configuringuser,Datastore.Modifyisrequiredaswell.
| 102 |     |     |     | Chapter11. | ManagingRemotes&Sync |
| --- | --- | --- | --- | ---------- | -------------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Ifthegroup-filteroptionisset,onlybackupgroupsmatchingatleastoneofthespecifiedcriteria
aresynced. Theavailablecriteriaare:
• Backuptype,forexample,toonlysyncgroupsofthect(Container)type:
# proxmox-backup-manager sync-job update ID --group-filter type:ct
• Fullgroupidentifier,tosyncaspecificbackupgroup:
# proxmox-backup-manager sync-job update ID --group-filter group:vm/100
• Regularexpression,matchedagainstthefullgroupidentifier
# proxmox-backup-manager sync-job update ID --group-filter regex:'^vm/1\d{2,3}$'
Thesamefilterisappliedtolocalgroups,forhandlingoftheremove-vanishedoption.
Agroup-filtercanbeinvertedbyprependingexclude: toit.
• Regularexpressionexample,excludingthematch:
# proxmox-backup-manager sync-job update ID --group-filter exclude:regex:'^vm/1\d{2,
,→3}$'
Formixingincludeandexcludefilter,followingrulesapply:
• nofilters: allbackupgroups
• include: onlythosematchingtheincludefilters
• exclude: allbutthosematchingtheexcludefilters
• both: thosematchingtheincludefilters,butwithoutthosematchingtheexcludefilters
(cid:174) Note
Theprotectedflagofremotebackupsnapshotswillnotbesynced.
Enabling the advanced option ’resync-corrupt’ will re-sync all snapshots that have failed to verify
duringthelastVerification. Hence,averificationjobneedstoberunbeforeasyncjobwith’resync-
corrupt’canbecarriedout. Beawarethata’resync-corrupt’-jobneedstocheckthemanifestsofall
snapshotsinadatastoreandmighttakemuchlongerthanregularsyncjobs.
If the run-on-mount flag is set, the sync job will be automatically started whenever a relevant
removable datastore is mounted. If mounting a removable datastore would start multiple sync
jobs,thesejobswillberunsequentiallyinalphabeticalorderbasedontheirID.
Iftheunmount-on-doneflagisset,thedatastorewillbeautomaticallyunmountedafterthesync
job finishes. This option is only available for sync jobs triggered by mounting (run-on-mount),
enablingfullyautomatedexternaldriveworkflows.
Setting the worker-threads option to a value greater than 1 (up to 32, default 1) synchronizes
multiplebackupgroupsinparallel. Thiscansignificantlyimprovethroughputonhigh-latencycon-
nections,whereasingleHTTP/2connectiontothesourceisotherwisebottleneckedbyhead-of-line
blocking. Log output from concurrent groups is prefixed with the group and buffered briefly to
keeprelatedlinestogether. Notethatthememoryandconnectioncountonbothendpointsgrow
roughlylinearlywiththenumberofworkers,sohighervaluesarenotalwaysbetter.
11.2.1 NamespaceSupport
Syncjobscanbeconfiguredtonotonlysyncdatastores,butalsosubsetsofdatastoresintheform
ofnamespacesornamespacesub-trees. Thefollowingparametersinfluencehownamespacesare
treatedaspartofasyncjob’sexecution:
• remote-ns: theremotenamespaceanchor(default: therootnamespace)
11.2. SyncJobs 103

ProxmoxBackupDocumentation,Release4.2.8‐1
• ns: thelocalnamespaceanchor(default: therootnamespace)
• max-depth: whethertorecursivelyiterateoversub-namespacesoftheremotenamespace
anchor(default: None)
Ifmax-depthissetto0,groupsaresyncedfromremote-nsintons,withoutanyrecursion. Ifitis
settoNone(leftempty), recursiondepthwilldependonthevalueof remote-nsandtheremote
side’savailabilityofnamespacesupport:
• remote-nssettosomethingotherthantherootnamespace: remotemust supportnames-
paces,fullrecursionstartingatremote-ns.
• remote-nssettorootnamespaceandremotesupportsnamespaces: fullrecursionstarting
atrootnamespace.
• remote-ns set to root namespace and remote does not support namespaces: backwards-
compatmode,onlyrootnamespacewillbesyncedintons,norecursion.
Any other value of max-depth will limit recursion to at most max-depth levels, for exam-
ple: remote-ns set to location_a/department_b and max-depth set to 1 will result in loca-
tion_a/department_bandatmostonemorelevelofsub-namespacesbeingsynced.
Thenamespacetreestartingatremote-nswillbemappedintonsuptoadepthof max-depth.
Forexample,withthefollowingnamespacesattheremoteside:
• location_a
– location_a/department_x
* location_a/department_x/team_one
* location_a/department_x/team_two
– location_a/department_y
* location_a/department_y/team_one
* location_a/department_y/team_two
• location_b
andremote-nsbeingsettolocation_a/department_xandnssettolocation_a_dep_xresultinginthe
followingnamespacetreeonthesynctarget:
• location_a_dep_x(containingtheremote’slocation_a/department_x)
– location_a_dep_x/team_one(containingtheremote’slocation_a/department_x/team_one)
– location_a_dep_x/team_two(containingtheremote’slocation_a/department_x/team_two)
withtherestoftheremotenamespacesandgroupsnotbeingsynced(bythissyncjob).
Ifaremotenamespaceisincludedinthesyncjobscope,butdoesnotexistlocally,itwillbecreated
(providedthesyncjobownerhassufficientprivileges).
If the remove-vanished option is set, namespaces that are included in the sync job scope but
onlyexistlocallyaretreatedasvanishedandremoved(providedthesyncjobownerhassufficient
privileges).
(cid:174) Note
Allotherlimitationsonsyncscope(suchasremoteuser/APItokenprivileges,groupfilters)also
applyforsyncjobsinvolvingoneormultiplenamespaces.
104 Chapter11. ManagingRemotes&Sync

ProxmoxBackupDocumentation,Release4.2.8‐1
11.2.2 BandwidthLimit
Syncing a datastore to an archive can produce a lot of traffic and impact other users of the
network. In order to avoid network or storage congestion, you can limit the bandwidth of a
sync job in pull direction by setting the rate-in option either in the web interface or using the
proxmox-backup-managercommand-linetool:
# proxmox-backup-manager sync-job update ID --rate-in 20MiB
For sync jobs in push direction use the rate-out option instead. To allow for traffic bursts, you
cansetthesizeofthetokenbucketfilterusedfortrafficlimitingviaburst-inorburst-outpa-
rameters.
11.2.3 SyncDirectionPush
Syncjobscanbeconfiguredforpullorpushdirection. Syncjobsinpushdirectionarenotidentical
inbehaviourbecauseofthelimitedaccesstothetargetdatastoreviatheremoteserversAPI.Most
notably,pushedcontentwillalwaysbeownedbytheuserconfiguredintheremoteconfiguration,
beingindependentfromthelocaluserasconfiguredinthesyncjob. Latterisusedexclusivelyfor
permissioncheckandscopechecksonthepushingside.
(cid:174) Note
Itisstronglyadvisedtocreateadedicatedremoteconfigurationforeachindividualsyncjobin
pushdirection,usingadedicateduserontheremote. Otherwise,syncjobspushingtothesame
targetmightremoveeachotherssnapshotsand/orgroups,iftheremovevanishedflagissetor
skipsnapshotsifthebackuptimeisnotincremental. Thisisbecausethebackupgroupsonthe
targetareownedbytheusergivenintheremoteconfiguration.
Thefollowingpermissionsarerequiredforasyncjobinpushdirection:
1. Remote.Audit on /remote/{remote} and Remote.DatastoreBackup on /remote/
{remote}/{remote-store}/{remote-ns}pathorsubnamespace.
2. AtleastDatastore.ReadandDatastore.Auditonthelocalsourcedatastorenamespace
(/datastore/{store}/{ns})orDatastore.Backupifownerofthesyncjob.
3. Remote.DatastorePrune on /remote/{remote}/{remote-store}/{remote-ns} path
to remove vanished snapshots and groups. Make sure to use a dedicated remote for each
syncjobinpushdirectionasnotedabove.
4. Remote.DatastoreModify on /remote/{remote}/{remote-store}/{remote-ns}
pathtoremovevanishednamespaces. Aremoteuserwithlimitedaccessshouldbeusedon
theremotebackupserverinstance. Considertheimplicationsasnotedbelow.
(cid:174) Note
Remote.DatastoreModifywillallowtoremovewholenamespacesontheremotetargetdata-
store, independent of ownership. Make sure the user as configured in remote.cfg has limited
permissionsontheremoteside.
(cid:174) Note
SyncjobsinpushdirectionrequirenamespacesupportontheremoteProxmoxBackupServer
instance(minimumversion2.2).
11.2. SyncJobs 105

ProxmoxBackupDocumentation,Release4.2.8‐1
11.2.4 ServerSideEncryption/DecryptionDuringSync
Syncjobinpushdirectionallowtoencryptunencryptedsnapshotswhensyncingtoalesstrusted
remote Proxmox Backup Server instance. For this, a server side encryption key can be assigned
to the sync job. This key will then be used to encrypt the contents before pushing them to the
remote, analogoustoperformingabackupwithanencryptionkey. Alreadyencryptedsnapshots
arenotre-encryptedbutratherpushedunmodified. Snapshotscontainingonlypartiallyencrypted
contentsareskippedforsecurityreasons.
Therefore,syncjobsusingtheencrypted-onlyflagwillneverusetheactive-encryption-key
whenpushingsnapshots,sinceonlyalreadyencryptedsnapshotsarebeingsynced.
Ontheotherhand,syncjobsinpulldirectionallowtoassignanumberofassociatedkeys,which
will be used to decrypt snapshot contents if the key fingerprint of one of the listed keys matches
theoneusedtoencryptthebackupsnapshot. Theactiveencryptionkeyhasnoeffectforsyncjobs
inpulldirectionandshouldnotbeset.
Inordertoconfigurethesyncjob,aswellasforsyncjobowner/localusertoaccessthekeysdur-
ingsync, System.Modifypermissionsarerequiredonthe/system/encryption-keys/{key}
path.
(cid:174) Note
Encryptionkeyhandlingcomeswithafewrisks,especiallywithkeyrotation. Therefore,onlyac-
tivekeyscanbeusedtoencryptnewsnapshotcontentsduringpushsync. Ifanactiveencryption
keyischanged,thekeyiskeptbackasassociatedkeyonthesyncjob,inordertoprotectitfrom
accidentalremoval. Further,anyencryptionkeycanbearchived,renderingitnolongerusable
for encryption, only to decrypt pre-existing contents. Any encryption key usable for sync jobs
mustthereforebemarkedasarchivedanddisassociatedfromanysyncjobstillassociatedtoit,
beforebeingabletoremoveit.
Thefollowingcommandcanbeusedtoassigntheactiveencryptionkeyforasyncjob.
# proxmox-backup-manager sync-job update pbs2-push --active-encryption-key key0
Setting the associated keys will drop any key not present in the given key list, with exception of
thepreviouslyassignedactiveencryptionkey,ifitisupdatedaswell. Thepreviouslyassigneden-
cryption key (in the example above key0) will always be pushed to the list of associated keys on
rotation. For example, since key0 is currently the active encryption key, below command would
assign key1 as the new active encryption key and result in key0,key2,key3 as associated keys
forthesyncjob.
# proxmox-backup-manager sync-job update pbs2-push --active-encryption-key key1 --associated-
,→key key2 --associated-key key3
106 Chapter11. ManagingRemotes&Sync

CHAPTER
TWELVE
MAINTENANCE TASKS
12.1 Pruning
Pruneletsyouspecifywhichbackupsnapshotsyouwanttokeep,removingothers. Whenpruning
asnapshot,onlythesnapshotmetadata(manifest,indices,blobs,logandnotes)isremoved. The
chunkscontainingtheactualbackupdataandpreviouslyreferencedbytheprunedsnapshot,have
toberemovedbyagarbagecollectionrun.
(cid:1002) Caution
Take into consideration that sensitive information stored in a given data chunk will outlive
pruned snapshots and remain present in the datastore as long as referenced by at least one
backupsnapshot. Further,evenifnosnapshotreferencesagivenchunk,itwillremainpresent
untilremovedbythegarbagecollection.
Moreover,file-levelbackupscreatedusingthechangedetectionmodemetadatacanreference
backup chunks containing files which have vanished since the previous backup. These files
mightstillbeaccessiblebyreadingthechunksrawdata(clientorserverside).
Toremovechunkscontainingsensitivedata,pruneanysnapshotmadewhilethedatawaspart
of the backup input and run a garbage collection. Further, if using file-based backups with
change detection mode metadata, additionally prune all snapshots since the sensitive data
wasnolongerpartofthebackupinputandrunagarbagecollection.
Thenolongerreferencedchunkswillthenbemarkedfordeletiononthenextgarbagecollection
runandremovedbyasubsequentrunafterthegraceperiod.
Thefollowingretentionoptionsareavailableforpruning:
keep-last <N>
Keepthelast<N>backupsnapshots.
keep-hourly <N>
Keepbackupsforthelast<N>hours. Ifthereismorethanonebackupforasinglehour,only
thelatestisretained. Hourswithoutbackupsdonotcount.
keep-daily <N>
Keep backups for the last <N> days. If there is more than one backup for a single day, only
thelatestisretained. Dayswithoutbackupsdonotcount.
keep-weekly <N>
Keepbackupsforthelast<N>weeks. Ifthereismorethanonebackupforasingleweek,only
thelatestisretained. Weekswithoutbackupdonotcount.
(cid:174) Note
107

ProxmoxBackupDocumentation,Release4.2.8‐1
WeeksstartonMondayandendonSunday. ThesoftwareusestheISOweekdatesystem
andhandlesweeksattheendoftheyearcorrectly.
keep-monthly <N>
Keepbackupsforthelast<N>months. Ifthereismorethanonebackupforasinglemonth,
onlythelatestisretained. Monthswithoutbackupsdonotcount.
keep-yearly <N>
Keepbackupsforthelast<N>years. Ifthereismorethanonebackupforasingleyear,only
thelatestisretained. Yearswithoutbackupsdonotcount.
The retention options are processed in the order given above. Each option only covers backups
withinitstimeperiod. Thenextoptiondoesnottakecareofalreadycoveredbackups. Itwillonly
considerolderbackups.
Old unfinished or incomplete backups will be removed by the prune command, unless they are
newerthanthelastsuccessfulbackup. Inthiscase,thelastfailedbackupisretained.
12.1.1 PruneSimulator
You can use the built-in prune simulator to explore the effect of different retention options with
variousbackupschedules.
12.1.2 PruneJobs
Prunejobsareconfiguredtoperiodicallypruneadatastoreorasubsetofit. Youcanmanageprune
108 Chapter12. MaintenanceTasks

ProxmoxBackupDocumentation,Release4.2.8‐1
jobsinthewebinterface,fromthePrune&GCtaboftheDatastorepanelorfromthatoftheDatas-
toreitself. Alternatively,youcanmanagethemwiththeproxmox-backup-manager prune-job
command. The configuration information for prune jobs is stored at /etc/proxmox-backup/
prune.cfg. Tocreateanewprunejob,clicktheaddbuttonintheGUI,orusethemanagerCLI’s
createsubcommand. Aftercreatingaprunejob,youcaneitherstartitmanuallyfromtheGUIor
provideitwithaschedule(seeCalendarEvents)torunregularly.
Eachprunejobhassettingsforretention,limitationofscopeandfrequency.
store <datastore>
Thedatastoreyouwanttorunthisprunejobon.
ns <namespace>
Limittheprunejobtoaspecificnamespace.
max-depth <N>
Configurethenamespacedepthitshouldprunefrombelowtheconfigurednamespace. For
example,0toonlyprunethebackupgroupsavailabledirectlyontheconfigurednamespace
itself. Omittheparametertoscantothefulldepthbelow.
schedule
Configureacalendareventintervalforwhentoautomaticallytriggerthisjob. Youcanomitthis
ifyouwanttotriggerajobonlymanually.
keep-X
Seethedescriptionofthevariousretentionoptionsabove.
disable
Settodisableajobtemporarilywhilekeepingitssettings.
comment
Youcanaddashortcommentforajob,forexampleaboutitintentions.
12.1.3 ManualPruning
12.1. Pruning 109

ProxmoxBackupDocumentation,Release4.2.8‐1
Tomanuallypruneaspecificbackupgroup,youcanuseproxmox-backup-client’sprunesub-
command,discussedinPruningandRemovingBackups,ornavigatetotheContenttabofthedata-
storeandclickthescissorsiconintheActionscolumnoftherelevantbackupgroup.
12.1.4 RetentionSettingsExample
Thebackupfrequencyandretentionofoldbackupsmaydependonhowoftendatachangesand
how important an older state may be in a specific workload. When backups act as a company’s
documentarchive,theremayalsobelegalrequirementsforhowlongbackupsnapshotsmustbe
kept.
Forthisexample,weassumethatyouaredoingdailybackups,havearetentionperiodof10years,
andtheperiodbetweenbackupsstoredgraduallygrows.
• keep-last: 3-evenifonlydailybackups,anadminmaywanttocreateanextraonejustbefore
orafterabigupgrade. Settingkeep-lastensuresthis.
• keep-hourly: notset-fordailybackupsthisisnotrelevant. Youcoverextramanualbackups
already,withkeep-last.
• keep-daily: 13-togetherwithkeep-last,whichcoversatleastoneday,thisensuresthatyou
haveatleasttwoweeksofbackups.
• keep-weekly: 8-ensuresthatyouhaveatleasttwofullmonthsofweeklybackups.
• keep-monthly: 11-togetherwiththepreviouskeepsettings, thisensuresthatyouhaveat
leastayearofmonthlybackups.
• keep-yearly: 9 - this is for the long term archive. As you covered the current year with the
previous options, you would set this to nine for the remaining ones, giving you a total of at
least10yearsofcoverage.
Werecommendthatyouuseahigherretentionperiodthanisminimallyrequiredbyyourenviron-
ment;youcanalwaysreduceitifyoufinditisunnecessarilyhigh,butyoucannotrecreatebackup
snapshotsfromthepast.
12.2 Garbage Collection
Garbage collection (GC) is the process that frees up space in a datastore by deleting all unused
backupchunksfromchunkstorage. GCcompletesthepruningofbackupsnapshots,whichdeletes
onlythemetadata,nottheunderlyingbackupdata.
It’srecommendedtosetupascheduletoensurethatunusedspaceiscleanedupperiodically. For
mostsetupsaweeklyscheduleprovidesagoodintervaltostart.
12.2.1 GCBackground
In Proxmox Backup Server, backup data is not saved directly, but rather as chunks that are re-
ferredtobytheindexesofeachbackupsnapshot. Thisapproachenablesreuseofchunksthrough
deduplication,amongotherbenefitsthataredetailedintheTechnicalOverview.
Whendeletingabackupsnapshot,ProxmoxBackupServercannotdirectlyremovethechunksas-
sociated with it because other backups, even ones that are still running, may have references to
thosechunks. Toavoidexcessiveloadandslowperformance,thewholedatastorecannotbelocked
toscanallotherindexesforreferencestothesamechunksoneverysnapshotdeletion. Moreover,
lockingtheentiredatastoreisnotfeasiblebecausenewbackupswouldbeblockeduntilthedele-
tionprocesswascomplete.
Therefore,ProxmoxBackupServerusesagarbagecollection(GC)processtoidentifyandremove
the unused backup chunks that are no longer needed by any snapshot in the datastore. The GC
processisdesignedtoefficientlyreclaimthespaceoccupiedbythesechunkswithlowimpacton
theperformanceofthedatastoreorinterferingwithotherbackups.
110 Chapter12. MaintenanceTasks

ProxmoxBackupDocumentation,Release4.2.8‐1
Thegarbagecollection(GC)processisperformedperdatastoreandissplitintotwophases:
• Phaseone(Mark):
Allindexfilesareread,andtheaccesstime(atime)ofthereferencedchunkfilesisupdated.
• Phasetwo(Sweep):
Thetaskiteratesoverallchunksandcheckstheirfileaccesstimeagainstacutofftime. The
cutofftimeisgivenbyeithertheoldestbackupwriterinstance,ifpresent,or24hoursand5
minutesbeforethestartofthegarbagecollection.
Garbage collection considers chunk files with access time older than the cutoff time to be
neitherreferencedbyanybackupsnapshot’sindex,norpartofanycurrentlyrunningbackup
job. Therefore,thesechunkscansafelybedeleted.
Chunks within the grace period will not be deleted and logged at the end of the garbage
collectiontaskasPendingremovals.
(cid:174) Note
Thegraceperiodforbackupchunkremovalisnotarbitrary,butstemsfromthefactthatfilesys-
temsaretypicallymountedwiththerelatimeoptionbydefault. Thisresultsinbetterperfor-
mancebyonlyupdatingtheatimepropertyifafilehasbeenmodifiedsincethelastaccessor
thelastaccesshasbeenatleast24hoursago.
12.2.2 ManuallyStartingGC
You can monitor and run garbage collection on the Proxmox Backup Server using the
garbage-collectionsubcommandofproxmox-backup-manager. Youcanusethestartsub-
command to manually start garbage collection on an entire datastore and the status subcom-
mandtoseeattributesrelatingtothegarbagecollection.
ThisfunctionalitycanalsobeaccessedinthewebUIusingtheStartGarbageCollectionbuttonfound
ineachdatastore’sPrune&GCtab.
12.2.3 ScheduledGC
Normally, datastore admins don’t want to bother triggering GC’s manually. That’s why you can
configureascheduletoletProxmoxBackupServerhandleit.
Setting or editing a datastore’s GC schedule can be either done by using the
proxmox-backup-manager datastore update <datastore> --gc-schedule
<schedule> CLI command or the edit window in the web UI in each datastore’s Prune &
GCtab.
TheGCschedulingusestheCalendarEventsformat.
(cid:98) Tip
You can disable automatic GC runs by clearing the schedule by either clearing the con-
tent of the field in the web UI or using the proxmox-backup-manager datastore update
<datastore> --delete gc-schedule CLI command. This might be, for example, useful
duringmaintenanceorifyouarchiveadatastoreforgood.
12.2. GarbageCollection 111

ProxmoxBackupDocumentation,Release4.2.8‐1
12.3 Verification
Proxmox Backup Server offers various verification options to ensure that backup data is intact.
Verificationisgenerallycarriedoutthroughthecreationofverifyjobs. Thesearescheduledtasks
thatrunverificationatagiveninterval(seeCalendarEvents). Withthese,youcanalsosetwhether
already verified snapshots are ignored, as well as set a time period, after which snapshots are
checkedagain. Thenumberofreadandverifythreadsusedforaverificationjobcanbespecified
via the read-threads and verify-threads parameters. Possible values range from 1 to 32 threads,
defaults being 1 reader and 4 verify threads. The interface for creating verify jobs can be found
undertheVerifyJobstabofthedatastore. Alternatively,youcanverifyallbackupsmanually. The
interfaceforthiscanbefoundundertheContenttabofthedatastoreorcanbedoneviatheCLI:
# proxmox-backup-manager verify <datastore> --read-threads 1 --verify-threads 4 --ignore-
,→verified false
(cid:174) Note
Itisrecommendedthatyoureverifyallbackupsatleastmonthly,evenifapreviousverification
wassuccessful. Thisisbecausephysicaldrivesaresusceptibletodamageovertime,whichcan
causeanold,workingbackuptobecomecorruptedinaprocessknownasbitrot/datadegrada-
tion. Itisgoodpracticetohavearegularlyrecurring(hourly/daily)verificationjob,whichchecks
newandexpiredbackups, thenanotherweekly/monthlyjobthatwillreverifyeverything. This
way,therewillbenosurpriseswhenitcomestorestoringdata.
Aside from using verify jobs, you can also run verification manually on entire datastores, backup
groupsorsnapshots. Todothis,navigatetotheContenttabofthedatastoreandeitherclickVerify
AllorselecttheV.iconfromtheActionscolumninthetable.
12.4 Notifications
Proxmox Backup Server can send you notifications about automatically scheduled verification,
garbage-collectionandsynchronizationtasksresults.
RefertotheNotificationschapterformoredetails.
112 Chapter12. MaintenanceTasks

ProxmoxBackupDocumentation,Release4.2.8‐1
12.5 Maintenance Mode
ProxmoxBackupServersupportssettingread-onlyandofflinemaintenancemodesonadatastore.
Once enabled, depending on the mode, new reads and/or writes to the datastore are blocked,
allowing an administrator to safely execute maintenance tasks, for example, on the underlying
storage.
InternallyProxmoxBackupServertrackswhethereachdatastoreaccessisawriteorreadoperation,
sothatitcangracefullyentertherespectivemode,byallowingconflictingoperationsthatstarted
beforeenablingthemaintenancemodetofinish.
Thesupportedmaintenancemodesare:
• read-only: Onlyreadoperationsareallowedonthedatastore.
• offline: Neitherreadnorwriteoperationsareallowedonthedatastore.
12.5. MaintenanceMode 113

ProxmoxBackupDocumentation,Release4.2.8‐1
| 114 | Chapter12. | MaintenanceTasks |
| --- | ---------- | ---------------- |

CHAPTER
THIRTEEN
HOST SYSTEM ADMINISTRATION
Proxmox Backup Server is based on the famous Debian Linux distribution. This means that you
haveaccesstotheentirerangeofDebianpackages,andthatthebasesystemiswelldocumented.
TheDebianAdministrator’sHandbookisavailableonline,andprovidesacomprehensiveintroduc-
tiontotheDebianoperatingsystem.
AstandardProxmoxBackupServerinstallationusesthedefaultrepositoriesfromDebian,soyou
getbugfixesandsecurityupdatesthroughthatchannel. Inaddition,weprovideourownpackage
repositorytorolloutallProxmoxrelatedpackages. ThisincludesupdatestosomeDebianpackages
whennecessary.
WealsodeliveraspeciallyoptimizedLinuxkernel,basedontheUbuntukernel. Thiskernelincludes
driversforZFS.
The following sections will concentrate on backup related topics. They will explain things which
aredifferentonProxmoxBackupServer, ortaskswhicharecommonlyusedonProxmoxBackup
Server. Forothertopics,pleaserefertothestandardDebiandocumentation.
13.1 ZFS on Linux
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
115

ProxmoxBackupDocumentation,Release4.2.8‐1
• OpenSource
• Encryption
13.1.1 Hardware
ZFS depends heavily on memory, so it’s recommended to have at least 8GB to start. In practice,
useasmuchyoucangetforyourhardware/budget. Topreventdatacorruption, werecommend
theuseofhighqualityECCRAM.
Ifyouuseadedicatedcacheand/orlogdisk,youshoulduseanenterpriseclassSSD(forexample,
IntelSSDDCS3700Series). Thiscanincreasetheoverallperformancesignificantly.
IMPORTANT:DonotuseZFSontopofahardwarecontrollerwhichhasitsowncachemanagement.
ZFSneedstodirectlycommunicatewithdisks. AnHBAadapterorsomethinglikeanLSIcontroller
flashedinITmodeisrecommended.
13.1.2 ZFSAdministration
This section gives you some usage examples for common tasks. ZFS itself is really powerful and
provides many options. The main commands to manage ZFS are zfs and zpool. Both commands
comewithextensivemanualpages,whichcanbereadwith:
# man zpool
# man zfs
Createanewzpool
To create a new pool, at least one disk is needed. The ashift should have the same sector-size (2
powerofashift)orlargerastheunderlyingdisk.
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
# zpool create -f -o ashift=12 <pool> raidz1 <device1> <device2> <device3>
116 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
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
(cid:489)
Important
AlwaysuseGPTpartitiontables.
The maximum size of a log device should be about half the size of physical memory, so this is
| usuallyquitesmall. | TherestoftheSSDcanbeusedascache. |                    |     |                      |
| ------------------ | -------------------------------- | ------------------ | --- | -------------------- |
| # zpool            | add -f <pool>                    | log <device-part1> |     | cache <device-part2> |
Changingafaileddevice
| # zpool | replace -f <pool> | <old | device> <new | device> |
| ------- | ----------------- | ---- | ------------ | ------- |
Changingafailedbootabledevice
DependingonhowProxmoxBackupwasinstalled,itiseitherusinggruborsystemd-bootasaboot-
loader.
Ineithercase,thefirststepsofcopyingthepartitiontable,reissuingGUIDsandreplacingtheZFS
partitionarethesame. Tomakethesystembootablefromthenewdisk,differentstepsareneeded
whichdependonthebootloaderinuse.
| # sgdisk | <healthy bootable | device> | -R <new        | device>             |
| -------- | ----------------- | ------- | -------------- | ------------------- |
| # sgdisk | -G <new device>   |         |                |                     |
| # zpool  | replace -f <pool> | <old    | zfs partition> | <new zfs partition> |
(cid:174) Note
Usethezpoolstatus-vcommandtomonitorhowfartheresilveringprocessofthenewdiskhas
progressed.
13.1. ZFSonLinux 117

ProxmoxBackupDocumentation,Release4.2.8‐1
Withsystemd-boot:
| # proxmox-boot-tool | format <new | ESP> |     |     |
| ------------------- | ----------- | ---- | --- | --- |
| # proxmox-boot-tool | init <new   | ESP> |     |     |
(cid:174)
Note
ESP stands for EFI System Partition, which is setup as partition #2 on bootable disks setup by
theProxmoxBackupServerinstaller. Fordetails,seeSettingupanewpartitionforuseassynced
ESP.
Withgrub:
Usuallygrub.cfgislocatedin/boot/grub/grub.cfg
| # grub-install <new | disk>                |     |     |     |
| ------------------- | -------------------- | --- | --- | --- |
| # grub-mkconfig     | -o /path/to/grub.cfg |     |     |     |
Activatee‐mailnotification
ZFScomeswithaneventdaemon,ZED,whichmonitorseventsgeneratedbytheZFSkernelmodule.
The daemon can also send emails upon ZFS events, such as pool errors. Newer ZFS packages
shipthedaemoninaseparatepackagezfs-zed, whichshouldalreadybeinstalledbydefaultin
ProxmoxBackup.
Youcanconfigurethedaemonviathefile/etc/zfs/zed.d/zed.rc,usingyourpreferrededitor.
TherequiredsettingforemailnotificationisZED_EMAIL_ADDR,whichissettorootbydefault.
ZED_EMAIL_ADDR="root"
Please note that Proxmox Backup Server forwards mails to root to the email address configured
fortherootuser.
LimitZFSmemoryusage
Itisgoodtouseatmost50percent(whichisthedefault)ofthesystemmemoryforZFSARC,topre-
ventperformancedegradationofthehost. Useyourpreferrededitortochangetheconfiguration
| in/etc/modprobe.d/zfs.conf         | andinsert: |     |     |     |
| ---------------------------------- | ---------- | --- | --- | --- |
| options zfs zfs_arc_max=8589934592 |            |     |     |     |
Theaboveexamplelimitstheusageto8GiB(’8*2^30^’).
(cid:489) Important
In case your desired zfs_arc_max value is lower than or equal to zfs_arc_min (which defaults to
1/32ofthesystemmemory), zfs_arc_max willbeignored. Thus, forittoworkinthiscase, you
mustsetzfs_arc_mintoatmostzfs_arc_max-1. Thiswouldrequireupdatingtheconfiguration
in/etc/modprobe.d/zfs.conf,with:
| options zfs zfs_arc_min=8589934591 |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- |
| options zfs zfs_arc_max=8589934592 |     |     |     |     |
Thisexamplesettinglimitstheusageto8GiB(’8*2^30^’)onsystemswithmorethan256GiBof
totalmemory,wheresimplysettingzfs_arc_maxalonewouldnotwork.
| 118 |     |     | Chapter13. | HostSystemAdministration |
| --- | --- | --- | ---------- | ------------------------ |

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:489) Important
IfyourrootfilesystemisZFS,youmustupdateyourinitramfseverytimethisvaluechanges.
# update-initramfs -u
SwaponZFS
Swap-spacecreatedonazvolmaycausesomeissues,suchasblockingtheserverorgeneratinga
highIOload.
Westronglyrecommendusingenoughmemory,sothatyounormallydonotrunintolowmemory
situations. Shouldyouneedorwanttoaddswap,itispreferredtocreateapartitiononaphysical
diskanduseitasaswapdevice. Youcanleavesomespacefreeforthispurposeintheadvanced
optionsoftheinstaller. Additionally,youcanlowertheswappinessvalue. Agoodvalueforservers
is10:
# sysctl -w vm.swappiness=10
Tomaketheswappinesspersistent,createanewfile/etc/sysctl.d/99-swappiness.conf withaneditor
ofyourchoiceandaddthefollowingline:
vm.swappiness = 10
Table1: Linuxkernelswappinessparametervalues
Value Strategy
vm.swappiness=0 Thekernelwillswaponlytoavoidan’outofmemory’condition
vm.swappiness=1 Minimumamountofswappingwithoutdisablingitentirely.
vm.swappiness=10 Sometimes recommended to improve performance when sufficient
memoryexistsinasystem.
vm.swappiness=60 Thedefaultvalue.
vm.swappiness=100 Thekernelwillswapaggressively.
ZFScompression
Toactivatecompression:
# zpool set compression=lz4 <pool>
We recommend using the lz4 algorithm, since it adds very little CPU overhead. Other algorithms
such as lzjb, zstd and gzip-N (where N is an integer from 1-9 representing the compression ratio,
where1isfastestand9isbestcompression)arealsoavailable. Dependingonthealgorithmand
howcompressiblethedatais,havingcompressionenabledcanevenincreaseI/Operformance.
Youcandisablecompressionatanytimewith:
# zfs set compression=off <dataset>
Onlynewblockswillbeaffectedbythischange.
ZFSspecialdevice
Sinceversion0.8.0,ZFSsupportsspecialdevices. Aspecialdeviceinapoolisusedtostoremetadata,
deduplicationtables,andoptionallysmallfileblocks.
A special device can improve the speed of a pool consisting of slow spinning hard disks with a
lot of metadata changes. For example, workloads that involve creating, updating or deleting a
13.1. ZFSonLinux 119

ProxmoxBackupDocumentation,Release4.2.8‐1
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
ZFSdatasetsexposethespecial_small_blocks=<size>property. sizecanbe0todisablestoringsmall
fileblocksonthespecialdevice,orapoweroftwointherangebetween512Bto128K.Aftersetting
thisproperty,newfileblockssmallerthansizewillbeallocatedonthespecialdevice.
(cid:489) Important
Ifthevalueforspecial_small_blocksisgreaterthanorequaltotherecordsize(default128K)ofthe
dataset,alldatawillbewrittentothespecialdevice,sobecareful!
Settingthespecial_small_blockspropertyonapoolwillchangethedefaultvalueofthatpropertyfor
allchildZFSdatasets(forexample,allcontainersinthepoolwilloptinforsmallfileblocks).
Optinforallfilessmallerthan4K-blockspool-wide:
# zfs set special_small_blocks=4K <pool>
Optinforsmallfileblocksforasingledataset:
# zfs set special_small_blocks=4K <pool>/<filesystem>
Optoutfromsmallfileblocksforasingledataset:
# zfs set special_small_blocks=0 <pool>/<filesystem>
Troubleshooting
Corruptcachefile
zfs-import-cache.serviceimportsZFSpoolsusingtheZFScachefile. Ifthisfilebecomescorrupted,
theservicewon’tbeabletoimportthepoolsthatit’sunabletoreadfromit.
Asaresult,incaseofacorruptedZFScachefile,somevolumesmaynotbemountedduringboot
andmustbemountedmanuallylater.
Foreachpool,run:
120 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
# zpool set cachefile=/etc/zfs/zpool.cache POOLNAME
then,updatetheinitramfsbyrunning:
# update-initramfs -u -k all
andfinally,rebootthenode.
Another workaround to this problem is enabling the zfs-import-scan.service, which searches and
importspoolsviadevicescanning(usuallyslower).
13.2 Host Bootloader
Proxmox Backup Server currently uses one of two bootloaders, depending on the disk setup se-
lectedintheinstaller.
ForEFISystemsinstalledwithZFSastherootfilesystemsystemd-bootisused,unlessSecureBoot
is enabled. All other deployments use the standard grub bootloader (this usually also applies to
systemswhichareinstalledontopofDebian).
13.2.1 PartitioningSchemeUsedbytheInstaller
TheProxmoxBackupServerinstallercreates3partitionsonalldisksselectedforinstallation.
Thecreatedpartitionsare:
• A1MBBIOSBootPartition(gdisktypeEF02)
• A512MBEFISystemPartition(ESP,gdisktypeEF00)
• Athirdpartitionspanningtheconfiguredhdsizeparameterortheremainingspaceavailable
forthechosenstoragetype
Systems using ZFS as a root filesystem are booted with a kernel and initrd image stored on the
512MBEFISystemPartition. ForlegacyBIOSsystems,andEFIsystemswithSecureBootenabled,
grubisused,forEFIsystemswithoutSecureBoot,systemd-bootisused. Bothareinstalledand
configuredtopointtotheESPs.
grubinBIOSmode(--target i386-pc)isinstalledontotheBIOSBootPartitionofallselected
disksonallsystemsbootedwithgrub(thatis,allinstallswithrootonext4orxfs,andinstallswith
rootonZFSonnon-EFIsystems).
13.2.2 SynchronizingtheContentoftheESPwithproxmox-boot-tool
proxmox-boot-tool is a utility used to keep the contents of the EFI System Partitions properly
configured and synchronized. It copies certain kernel versions to all ESPs and configures the re-
spectivebootloadertobootfromthevfatformattedESPs. InthecontextofZFSasrootfilesystem,
thismeansthatyoucanusealltheoptionalfeaturesonyourrootpool,insteadofthesubsetwhich
isalsopresentintheZFSimplementationingruborhavingtocreateasmall,separateboot-pool
(see: BootingZFSonrootwithgrub).
Insetupswithredundancy,alldisksarepartitionedwithanESPbytheinstaller. Thisensuresthe
systemboots,evenifthefirstbootdevicefailsoriftheBIOScanonlybootfromaparticulardisk.
TheESPsarenotkeptmountedduringregularoperation. Thishelpstopreventfilesystemcorrup-
tioninthevfatformattedESPsincaseofasystemcrash,andremovestheneedtomanuallyadapt
/etc/fstabincasetheprimarybootdevicefails.
proxmox-boot-toolhandlesthefollowingtasks:
• Formattingandsettingupanewpartition
• CopyingandconfiguringnewkernelimagesandinitrdimagestoalllistedESPs
13.2. HostBootloader 121

ProxmoxBackupDocumentation,Release4.2.8‐1
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
To setup an existing, unmounted ESP located on /dev/sda2 for inclusion in Proxmox Backup
Server’skernelupdatesynchronizationmechanism,usethefollowing:
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
(cid:174) Note
Bothupdate-initramfsandapt(whennecessary)willautomaticallytriggerarefresh.
KernelVersionsConsideredbyproxmox-boot-tool
Thefollowingkernelversionsareconfiguredbydefault:
• Thecurrentlyrunningkernel
• Theversionbeingnewlyinstalledonpackageupdates
122 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
• Thetwolatest,alreadyinstalledkernels
• Thelatestversionofthesecond-to-lastkernelseries(e.g. 5.0,5.3),ifapplicable
• Anymanuallyselectedkernels
ManuallyKeepingaKernelBootable
Should you wish to add a certain kernel and initrd image to the list of bootable kernels, use
| proxmox-boot-tool | kernel | add. |
| ----------------- | ------ | ---- |
For example, run the following to add the kernel with ABI version 5.0.15-1-pve to the list of
kernelstokeepinstalledandsyncedtoallESPs:
| # proxmox-boot-tool | kernel | add 5.0.15-1-pve |
| ------------------- | ------ | ---------------- |
proxmox-boot-tool kernel listwilllistallkernelversionscurrentlyselectedforbooting:
| # proxmox-boot-tool | kernel   | list |
| ------------------- | -------- | ---- |
| Manually selected   | kernels: |      |
5.0.15-1-pve
| Automatically selected | kernels: |     |
| ---------------------- | -------- | --- |
5.0.12-1-pve
4.15.18-18-pve
Runproxmox-boot-tool kernel removetoremoveakernelfromthelistofmanuallyselected
kernels,forexample:
| # proxmox-boot-tool | kernel | remove 5.0.15-1-pve |
| ------------------- | ------ | ------------------- |
(cid:174) Note
It’s required to run proxmox-boot-tool refresh to update all EFI System Partitions (ESPs)
afteramanualkerneladditionorremovalfromabove.
13.2. HostBootloader 123

ProxmoxBackupDocumentation,Release4.2.8‐1
13.2.3 DeterminewhichBootloaderisUsed
The simplest and most reliable way to determine which bootloader is used, is to watch the boot
processoftheProxmoxBackupServernode.
Youwilleitherseetheblueboxof gruborthesimpleblackonwhitesystemd-boot.
124 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
Determiningthebootloaderfromarunningsystemmightnotbe100%accurate. Themostreliable
wayistorunthefollowingcommand:
# efibootmgr -v
IfitreturnsamessagethatEFIvariablesarenotsupported,grubisusedinBIOS/Legacymode.
Iftheoutputcontainsalinethatlookssimilartothefollowing,grubisusedinUEFImode.
Boot0005* proxmox [...] File(\EFI\proxmox\grubx64.efi)
Iftheoutputcontainsalinesimilartothefollowing,systemd-bootisused.
Boot0006* Linux Boot Manager [...] File(\EFI\systemd\systemd-bootx64.efi)
Byrunningthefollowingcommand,youcanfindoutif proxmox-boot-toolisconfigured,which
isagoodindicationofhowthesystemisbooted:
# proxmox-boot-tool status
13.2.4 Grub
grub has been the de facto standard for booting Linux systems for many years and is quite well
documented(seetheGrubManual).
Configuration
Changestothegrubconfigurationaredoneviathedefaultsfile/etc/default/gruborviaconfig
snippets in /etc/default/grub.d. To regenerate the configuration file after a change to the
configuration,run:
13.2. HostBootloader 125

ProxmoxBackupDocumentation,Release4.2.8‐1
# update-grub
(cid:174) Note
Systems using proxmox-boot-tool will call proxmox-boot-tool refresh upon
update-grub
13.2.5 Systemd‐boot
systemd-bootisalightweightEFIbootloader. Itreadsthekernelandinitrdimagesdirectlyfrom
the EFI Service Partition (ESP) where it is installed. The main advantage of directly loading the
kernelfromtheESPisthatitdoesnotneedtoreimplementthedriversforaccessingthestorage.
InProxmoxBackup,proxmox-boot-toolisusedtokeeptheconfigurationontheESPssynchronized.
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
13.2.6 EditingtheKernelCommandline
Youcanmodifythekernelcommandlineinthefollowingplaces,dependingonthebootloaderused:
Grub
The kernel commandline needs to be placed in the variable GRUB_CMDLINE_LINUX_DEFAULT in
thefile/etc/default/grub. Runningupdate-grubappendsitscontenttoalllinuxentriesin
/boot/grub/grub.cfg.
systemd‐boot
Thekernelcommandlineneedstobeplacedasonelinein/etc/kernel/cmdline. Toapplyyour
changes,runproxmox-boot-tool refresh,whichsetsitastheoptionlineforallconfigfilesin
loader/entries/proxmox-*.conf.
13.2.7 OverridetheKernel‐VersionfornextBoot
Toselectakernelthatisnotcurrentlythedefaultkernel,youcaneither:
• Usethebootloadermenuthatisdisplayedatthebeginningofthebootprocess
• Use the proxmox-boot-tool to pin the system to a kernel version either once or perma-
nently(untilpinisreset).
Thisshouldhelpyouworkaroundincompatibilitiesbetweenanewerkernelversionandthehard-
ware.
126 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
Suchapinshouldberemovedassoonaspossible,sothatallrecentsecuritypatchesfromthe
latestkernelarealsoappliedtothesystem.
Forexample,topermanentlyselecttheversion5.15.30-1-pveforbooting,youwouldrun:
# proxmox-boot-tool kernel pin 5.15.30-1-pve
(cid:98) Tip
The pinning functionality works for all Proxmox Backup Server systems, not only those using
proxmox-boot-tool to synchronize the contents of the ESPs, if your system does not use
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
(cid:98) Tip
Youwillbepromptedtoautomaticallydoforproxmox-boot-toolmanagedsystemsifyoucall
thetoolinteractively.
# proxmox-boot-tool refresh
13.2.8 SecureBoot
SinceProxmoxBackupServer3.1,SecureBootissupportedoutoftheboxviasignedpackagesand
integrationinproxmox-boot-tool.
ThefollowingpackagesneedtobeinstalledforSecureBoottobeenabled:
• shim-signed(shimbootloadersignedbyMicrosoft)
• shim-helpers-amd64-signed(fallbackbootloaderandMOKManager,signedbyProxmox)
• grub-efi-amd64-signed(GrubEFIbootloader,signedbyProxmox)
• proxmox-kernel-6.X.Y-Z-pve-signed(Kernelimage,signedbyProxmox)
Only Grub as bootloader is supported out of the box, since there are no other pre-signed boot-
loaderpackagesavailable. AnynewinstallationofProxmoxBackupServerwillautomaticallyhave
alloftheabovepackagesincluded.
13.2. HostBootloader 127

ProxmoxBackupDocumentation,Release4.2.8‐1
MoredetailsabouthowSecureBootworks, andhowtocustomizethesetup, areavailableinour
wiki.
SwitchinganExistingInstallationtoSecureBoot
(cid:193) Warning
Thiscanleadtoanunbootableinstallationinsomecasesifnotdonecorrectly. Reinstallingthe
hostwillsetupSecureBootautomaticallyifavailable,withoutanyextrainteractions. Makesure
youhaveaworkingandwell-testedbackupofyourProxmoxBackupServerhost!
AnexistingUEFIinstallationcanbeswitchedovertoSecureBootifdesired,withouthavingtorein-
stallProxmoxBackupServerfromscratch.
First,ensureallyoursystemisup-to-date. Next,installalltherequiredpre-signedpackagesaslisted
above. GrubautomaticallycreatestheneededEFIbootentryforbootingviathedefaultshim.
systemd‐boot
Ifsystemd-bootisusedasabootloader(seeDeterminewhichBootloaderisused),someadditional
setupisneeded. ThisisonlythecaseifProxmoxBackupServerwasinstalledwithZFS-on-root.
Tocheckthelatter,run:
| # findmnt / |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
IfthehostisindeedusingZFSasrootfilesystem,theFSTYPEcolumnshouldcontainzfs:
| TARGET SOURCE      |     | FSTYPE OPTIONS              |     |     |     |
| ------------------ | --- | --------------------------- | --- | --- | --- |
| / rpool/ROOT/pbs-1 |     | zfs rw,relatime,xattr,noacl |     |     |     |
Next, a suitable potential ESP (EFI system partition) must be found. This can be done using the
lsblkcommandasfollowing:
| # lsblk -o | +FSTYPE |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
Theoutputshouldlooksomethinglikethis:
| NAME MAJ:MIN | RM SIZE | RO TYPE MOUNTPOINTS | FSTYPE     |     |     |
| ------------ | ------- | ------------------- | ---------- | --- | --- |
| sda 8:0      | 0 32G   | 0 disk              |            |     |     |
| ├─sda1 8:1   | 0 1007K | 0 part              |            |     |     |
| ├─sda2 8:2   | 0 512M  | 0 part              | vfat       |     |     |
| └─sda3 8:3   | 0 31.5G | 0 part              | zfs_member |     |     |
| sdb 8:16     | 0 32G   | 0 disk              |            |     |     |
| ├─sdb1 8:17  | 0 1007K | 0 part              |            |     |     |
| ├─sdb2 8:18  | 0 512M  | 0 part              | vfat       |     |     |
| └─sdb3 8:19  | 0 31.5G | 0 part              | zfs_member |     |     |
Inthiscase,thepartitionssda2andsdb2arethetargets. Theycanbeidentifiedbythetheirsize
of512MandtheirFSTYPEbeingvfat,inthiscaseonaZFSRAID-1installation.
These partitions must be properly set up for booting through Grub using proxmox-boot-tool.
Thiscommand(usingsda2asanexample)mustberunseparatelyforeachindividualESP:
| # proxmox-boot-tool | init | /dev/sda2 grub |     |     |     |
| ------------------- | ---- | -------------- | --- | --- | --- |
Afterwards,youcansanity-checkthesetupbyrunningthefollowingcommand:
| # efibootmgr | -v  |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
Thislistshouldcontainanentrylookingsimilartothis:
[..]
Boot0009* proxmox HD(2,GPT,..,0x800,0x100000)/File(\EFI\proxmox\shimx64.efi)
[..]
| 128 |     |     |     | Chapter13. | HostSystemAdministration |
| --- | --- | --- | --- | ---------- | ------------------------ |

ProxmoxBackupDocumentation,Release4.2.8‐1
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
(cid:174) Note
SomeUEFIfirmwaresareknowntodroptheproxmoxbootoptiononreboot. Thiscanhappen
iftheproxmoxbootentryispointingtoaGrubinstallationonadisk,wherethediskitselfisnot
abootoption. Ifpossible,tryaddingthediskasabootoptionintheUEFIfirmwaresetuputility
andrunproxmox-boot-toolagain.
(cid:98) Tip
Toenrollcustomkeys,seetheaccompanyingSecureBootwikipage.
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
13.2. HostBootloader 129

ProxmoxBackupDocumentation,Release4.2.8‐1
13.3 Certificate Management
Access to the API and thus the web-based administration interface is always encrypted through
https. EachProxmoxBackupServerhostcreatesbydefaultitsown(self-signed)certificate. This
certificateisusedforencryptedcommunicationwiththehost’sproxmox-backup-proxyservice,
foranyAPIcallbetweenauserorbackup-clientandtheweb-interface.
Certificate verification when sending backups to a Proxmox Backup Server is either done based
onpinningthecertificatefingerprintsinthestorage/remoteconfiguration,orbyusingcertificates,
signedbyatrustedcertificateauthority.
13.3.1 CertificatesfortheAPIandSMTP
ProxmoxBackupServerstoresitscertificateandkeyin:
• /etc/proxmox-backup/proxy.pem
• /etc/proxmox-backup/proxy.key
Youhavethefollowingoptionsforthecertificate:
1. Keepusingthedefaultself-signedcertificatein/etc/proxmox-backup/proxy.pem.
2. Use an externally provided certificate (for example, signed by a commercial Certificate Au-
thority(CA)).
3. Use an ACME provider like Let’s Encrypt to get a trusted certificate with automatic renewal;
thisisalsointegratedintheProxmoxBackupAPIandwebinterface.
Certificates are managed through the Proxmox Backup web-interface/API or using the
proxmox-backup-managerCLItool.
13.3.2 UploadCustomCertificate
IfyoualreadyhaveacertificatewhichyouwanttouseforaProxmoxBackuphost,youcansimply
uploadthatcertificateoverthewebinterface.
Notethatanycertificatekeyfilesmustnotbepasswordprotected.
13.3.3 TrustedcertificatesviaLet’sEncrypt(ACME)
Proxmox Backup Server includes an implementation of the Automatic Certificate Management
Environment(ACME)protocol,allowingProxmoxBackupServeradminstouseanACMEprovider
likeLet’sEncryptforeasysetupofTLScertificates,whichareacceptedandtrustedbymodernop-
eratingsystemsandwebbrowsersoutofthebox.
130 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
Currently,thetwoACMEendpointsimplementedaretheLet’sEncrypt(LE)productionandstaging
environments. Our ACME client supports validation of http-01 challenges using a built-in web
serverandvalidationofdns-01challengesusingaDNSpluginsupportingalltheDNSAPIendpoints
acme.shdoes.
ACMEAccount
YouneedtoregisteranACMEaccountpercluster, withtheendpointyouwanttouse. Theemail
addressusedforthataccountwillserveasthecontactpointforrenewal-dueorsimilarnotifications
fromtheACMEendpoint.
You can register or deactivate ACME accounts over the web interface Certificates -> ACME
Accountsorusingtheproxmox-backup-managercommand-linetool.
proxmox-backup-manager acme account register <account-name> <mail@example.com>
(cid:98) Tip
Becauseofrate-limitsyoushoulduseLEstagingforexperimentsorifyouuseACMEforthe
veryfirsttimeuntilallisworkingthere,andonlythenswitchovertotheproductiondirectory.
ACMEPlugins
TheACMEplugin’sroleistoprovideautomaticverificationthatyou,andthustheProxmoxBackup
Server under your operation, are the real owner of a domain. This is the basic building block of
automaticcertificatemanagement.
TheACMEprotocolspecifiesdifferenttypesofchallenges,forexamplethehttp-01,whereaweb
serverprovidesafilewithaspecifictokentoprovethatitcontrolsadomain. Sometimesthisisn’t
possible,eitherbecauseoftechnicallimitationsoriftheaddressofarecordisnotreachablefrom
thepublicinternet. Thedns-01challengecanbeusedinsuchcases. Thischallengeisfulfilledby
creatingacertainDNSrecordinthedomain’szone.
ProxmoxBackupServersupportsbothofthosechallengetypesoutofthebox,youcanconfigure
pluginseitheroverthewebinterfaceunderCertificates -> ACME Challenges,orusingthe
13.3. CertificateManagement 131

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager acme plugin addcommand.
ACMEPluginconfigurationsarestoredin/etc/proxmox-backup/acme/plugins.cfg.
Domains
You can add new or manage existing domain entries under Certificates, or using the
proxmox-backup-managercommand.
Afterconfiguringthedesireddomain(s)foranodeandensuringthatthedesiredACMEaccountis
selected,youcanorderyournewcertificateovertheweb-interface. Onsuccess,theinterfacewill
reloadafterroughly10seconds.
Renewalwillhappenautomatically
13.3.4 ACMEHTTPChallengePlugin
Thereisalwaysanimplicitlyconfiguredstandalonepluginforvalidatinghttp-01challengesvia
thebuilt-inwebserverspawnedonport80.
(cid:174) Note
Thename standalone meansthat it can providethe validation on its own, without any third
partyservice.
ThereareafewprerequisitestousethisforcertificatemanagementwithLet’sEncryptsACME.
• YouhavetoaccepttheToSofLet’sEncrypttoregisteranaccount.
• Port80ofthenodeneedstobereachablefromtheinternet.
• Theremustbenootherlisteneronport80.
• The requested (sub)domain needs to resolve to a public IP of the Proxmox Backup Server
host.
13.3.5 ACMEDNSAPIChallengePlugin
Onsystemswhereexternalaccessforvalidationviathehttp-01methodisnotpossibleordesired,
itispossibletousethedns-01validationmethod. ThisvalidationmethodrequiresaDNSserver
thatallowsprovisioningof TXTrecordsviaanAPI.
ConfiguringACMEDNSAPIsforvalidation
ProxmoxBackupServerreusestheDNSpluginsdevelopedfortheacme.sh1 project. Pleaserefer
toitsdocumentationfordetailsonconfigurationofspecificAPIs.
The easiest way to configure a new plugin with the DNS API is using the web interface
(Certificates -> ACME Accounts/Challenges).
1acme.shhttps://github.com/acmesh-official/acme.sh
132 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
HereyoucanaddanewchallengepluginbyselectingyourAPIproviderandenteringthecredential
datatoaccessyouraccountovertheirAPI.
(cid:98) Tip
Seetheacme.shHowtouseDNSAPIwikiformoredetailedinformationaboutgettingAPIcre-
dentialsforyourprovider. Configurationvaluesdonotneedtobequotedwithsingleordouble
quotes;forsomepluginsthatisevenanerror.
AstherearemanyDNSprovidersandAPIendpoints,ProxmoxBackupautomaticallygeneratesthe
form for the credentials, but not all providers are annotated yet. For those you will see a bigger
textarea,intowhichyousimplyneedtocopyallthecredential’sKEY=VALUEpairs.
DNSValidationthroughCNAMEAlias
A special alias mode can be used to handle validation on a different domain/DNS server, in
case your primary/real DNS does not support provisioning via an API. Manually set up a perma-
nent CNAME record for _acme-challenge.domain1.example pointing to _acme-challenge.
domain2.example, and set the alias property in the Proxmox Backup Server node configu-
ration file /etc/proxmox-backup/node.cfg to domain2.example to allow the DNS server of
domain2.exampletovalidateallchallengesfordomain1.example.
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
13.3.6 AutomaticrenewalofACMEcertificates
If a node has been successfully configured with an ACME-provided certificate (either via
proxmox-backup-managerorviatheweb-interface/API),thecertificatewillberenewedautomat-
ically by the proxmox-backup-daily-update.service. Currently, renewal is triggered if the
certificateeitherhasalreadyexpiredorifitwillexpireinthenext30days.
13.3.7 ManuallyChangeCertificateovertheCommandLine
Ifyouwanttogetridofcertificateverificationwarnings,youhavetogenerateavalidcertificatefor
yourserver.
LogintoyourProxmoxBackupServerviasshorusetheconsole:
13.3. CertificateManagement 133

ProxmoxBackupDocumentation,Release4.2.8‐1
| openssl | req -newkey rsa:2048 | -nodes -keyout | key.pem | -out req.pem |     |
| ------- | -------------------- | -------------- | ------- | ------------ | --- |
Followtheinstructionsonthescreen,forexample:
| Country  | Name (2 letter  | code) [AU]: AT                  |     |     |     |
| -------- | --------------- | ------------------------------- | --- | --- | --- |
| State or | Province Name   | (full name) [Some-State]:Vienna |     |     |     |
| Locality | Name (eg, city) | []:Vienna                       |     |     |     |
Organization Name (eg, company) [Internet Widgets Pty Ltd]: Proxmox GmbH
| Organizational | Unit Name                 | (eg, section) []:Proxmox             | Backup |     |     |
| -------------- | ------------------------- | ------------------------------------ | ------ | --- | --- |
| Common Name    | (eg, YOUR                 | name) []: yourproxmox.yourdomain.com |        |     |     |
| Email Address  | []:support@yourdomain.com |                                      |        |     |     |
Please enter the following 'extra' attributes to be sent with your certificate request
| A challenge | password     | []: not necessary |     |     |     |
| ----------- | ------------ | ----------------- | --- | --- | --- |
| An optional | company name | []: not necessary |     |     |     |
After you have finished the certificate request, you have to send the file req.pem to your Certifi-
cationAuthority(CA).TheCAwillissuethecertificate(BASE64encoded),basedonyourrequest–
savethisfileascert.pemtoyourProxmoxBackup.
Toactivatethenewcertificate,dothefollowingonyourProxmoxBackup
| cp key.pem  | /etc/proxmox-backup/proxy.key |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
| cp cert.pem | /etc/proxmox-backup/proxy.pem |     |     |     |     |
ThenrestarttheAPIservers:
| systemctl | restart proxmox-backup-proxy |     |     |     |     |
| --------- | ---------------------------- | --- | --- | --- | --- |
Testyournewcertificate,usingyourbrowser.
(cid:174) Note
To transfer files to and from your Proxmox Backup, you can use secure copy: If your desktop
runsLinux,youcanusethescpcommand-linetool. IfyourdesktopPCrunswindows,please
useanscpclientlikeWinSCP(seehttps://winscp.net/).
| 13.4 External | Metric | Server |     |     |     |
| ------------- | ------ | ------ | --- | --- | --- |
ProxmoxBackupServerperiodicallysendsvariousmetricsaboutyourhost’smemory,networkand
diskactivitytoconfiguredexternalmetricservers.
Currentlysupportedare:
• InfluxDB(HTTP)(seehttps://docs.influxdata.com/influxdb/v2/)
• InfluxDB(UDP)(seehttps://docs.influxdata.com/influxdb/v1/)
Theexternalmetricserverdefinitionsaresavedin’/etc/proxmox-backup/metricserver.cfg’,andcan
beeditedthroughthewebinterface.
(cid:174) Note
UsingHTTPisrecommendedasUDPsupporthasbeendroppedinInfluxDBv2.
13.4.1 InfluxDB(HTTP)pluginconfiguration
TheplugincanbeconfiguredtousetheHTTP(s)APIofInfluxDB2.x. InfluxDB1.8.xdoescontaina
forwardscompatibleAPIendpointforthisv2API.
SinceInfluxDB’sv2APIisonlyavailablewithauthentication,youhavetogenerateatokenthatcan
writeintothecorrectbucketandsetit.
| 134 |     |     |     | Chapter13. | HostSystemAdministration |
| --- | --- | --- | --- | ---------- | ------------------------ |

ProxmoxBackupDocumentation,Release4.2.8‐1
Inthev2compatibleAPIof1.8.x,youcanuse’user:password’astoken(ifrequired),andcanomit
the’organization’sincethathasnomeaninginInfluxDB1.x.
Youcanalsosetthemaximumbatchsize(default25000000bytes)withthe’max-body-size’setting
(thiscorrespondstotheInfluxDBsettingwiththesamename).
13.4.2 InfluxDB(UDP)pluginconfiguration
ProxmoxBackupServercanalsosenddataviaUDP.ThisrequirestheInfluxDBservertobeconfig-
uredcorrectly. TheMTUcanalsobeconfiguredhereifnecessary.
HereisanexampleconfigurationforInfluxDB(onyourInfluxDBserver):
[[udp]]
enabled = true
bind-address = "0.0.0.0:8089"
database = "proxmox"
batch-size = 1000
batch-timeout = "1s"
Withthisconfiguration,theInfluxDBserverlistensonallIPaddressesonport8089,andwritesthe
dataintheproxmoxdatabase.
13.5 Service Daemons
13.5.1 proxmox-backup-proxy
This daemon exposes the whole Proxmox Backup Server API on TCP port 8007 using HTTPS. It
runs as user backup and has very limited permissions. Operations requiring more permissions
areforwardedtothelocalproxmox-backupservice.
13.5.2 proxmox-backup
ThisdaemonexposestheProxmoxBackupServermanagementAPIon127.0.0.1:82. Itrunsas
rootandhaspermissiontodoallprivilegedoperations.
NOTE: The daemon listens to a local address only, so you cannot access it from outside. The
proxmox-backup-proxydaemonexposestheAPItotheoutsideworld.
13.6 Command‐line Tools
13.6.1 proxmox-backup-client
Thistoolimplementsabackupserverclient,i.e. itcanconnecttoabackupserverstoissueman-
agementcommandsandtocreateorrestorebackups.
13.6.2 proxmox-backup-manager
ThistoolexposesthewholebackupservermanagementAPIonthecommandline.
13.6.3 proxmox-tape
Thistoolcanconfigureandmanagetapebackups.
13.6.4 pmt
ThepmtcommandcontrolsLinuxtapedevices.
13.5. ServiceDaemons 135

ProxmoxBackupDocumentation,Release4.2.8‐1
13.6.5 pmtx
ThepmtxcommandcontrolsSCSImediachangerdevices(tapeautoloader).
13.6.6 pxar
pxar is a command-line utility for creating and manipulating archives in the Proxmox File Archive
Format (.pxar). It is inspired by casync file archive format, which caters to a similar use-case. The
.pxar format is adapted to fulfill the specific needs of the Proxmox Backup Server, for example,
efficientstorageofhardlinks. Theformatisdesignedtoreducetherequiredstorageontheserver
byachievingahighlevelofdeduplication.
CreatinganArchive
Runthefollowingcommandtocreateanarchiveofafoldernamedsource:
# pxar create archive.pxar /path/to/source
Thiswillcreateanewarchivecalledarchive.pxarwiththecontentsofthesourcefolder.
(cid:174) Note
pxarwillnotoverwriteanyexistingarchives. Ifanarchivewiththesamenameisalreadypresent
inthetargetfolder,thecreationwillfail.
Bydefault,pxarwillskipcertainmountpointsandwillnotfollowdeviceboundaries. Thisdesign
decisionisbasedontheprimaryusecaseofcreatingarchivesforbackups. Itmakessensetoignore
the contents of certain temporary or system specific files in a backup. To alter this behavior and
followdeviceboundaries,usethe--all-file-systemsflag.
It is possible to exclude certain files and/or folders from the archive by passing the --exclude
parameterwithgitignore-stylematchpatterns.
Forexample,youcanexcludeallfilesendingin.txtfromthearchivebyrunning:
# pxar create archive.pxar /path/to/source --exclude '**/*.txt'
Be aware that the shell itself will try to expand glob patterns before invoking pxar. In order to
avoidthis,allglobshavetobequotedcorrectly.
Itispossibletopassthe--excludeparametermultipletimes, inordertomatchmorethanone
pattern. This allows you to use more complex file inclusion/exclusion behavior. However, it is
recommendedtouse.pxarexcludefilesinsteadforsuchcases.
Forexampleyoumightwanttoexcludeall.txtfilesexceptaspecificonefromthearchive. This
wouldbeachievedviathenegatedmatchpattern,prefixedby!. Alltheglobpatternsarerelative
tothesourcedirectory.
# pxar create archive.pxar /path/to/source --exclude '**/*.txt' --exclude '!/folder/file.txt'
(cid:174) Note
Theorderoftheglobmatchpatternsmatters,aslateronesoverrideearlierones. Permutations
ofthesamepatternsleadtodifferentresults.
pxar will store the list of glob match patterns passed as parameters via the command line, in a
filecalled.pxarexclude-cli,attherootofthearchive. Ifafilewiththisnameisalreadypresent
in the source folder during archive creation, this file is not included in the archive, and the file
containingthenewpatternsisaddedtothearchiveinstead. Theoriginalfileisnotaltered.
136 Chapter13. HostSystemAdministration

ProxmoxBackupDocumentation,Release4.2.8‐1
Amoreconvenientandpersistentwaytoexcludefilesfromthearchiveisbyplacingtheglobmatch
patternsin.pxarexcludefiles. Itispossibletocreateandplacethesefilesinanydirectoryofthe
filesystem tree. These files must contain one pattern per line, and later patterns override earlier
ones. Thepatternscontrolfileexclusionsoffilespresentwithinthegivendirectoryorfurtherbelow
itinthetree. ThebehavioristhesameasdescribedinCreatingBackups.
ExtractinganArchive
Anexistingarchive,archive.pxar,isextractedtoatargetdirectorywiththefollowingcommand:
# pxar extract archive.pxar /path/to/target
Ifnotargetisprovided,thecontentsofthearchiveisextractedtothecurrentworkingdirectory.
In order to restore only parts of an archive, single files, and/or folders, it is possible to pass the
correspondingglobmatchpatternsasadditionalparametersortousethepatternsstoredinafile:
# pxar extract etc.pxar /restore/target/etc --pattern '**/*.conf'
The above example restores all .conf files encountered in any of the sub-folders in the archive
etc.pxartothetarget/restore/target/etc. Apathtothefilecontainingmatchpatternscan
bespecifiedusingthe--files-fromparameter.
ListtheContentsofanArchive
Todisplaythefilesanddirectoriescontainedinanarchivearchive.pxar,runthefollowingcom-
mand:
# pxar list archive.pxar
Thisdisplaysthefullpathofeachfileordirectorywithrespecttothearchive’sroot.
MountinganArchive
pxarallowsyoutomountandinspectthecontentsofanarchiveviaFUSE.Inordertomountan
archivenamedarchive.pxartothemountpoint/mnt,runthecommand:
# pxar mount archive.pxar /mnt
Oncethearchiveismounted,youcanaccessitscontentunderthegivenmountpoint.
# cd /mnt
# ls
bin dev home lib32 libx32 media opt root sbin sys usr
boot etc lib lib64 lost+found mnt proc run srv tmp var
13.6.7 proxmox-file-restore
Command-line tool for restoringfiles and directories fromProxmoxBackup archives. In contrast
toproxmox-backup-client,thissupportsbothcontainer/hostandVMbackups.
13.6.8 proxmox-backup-debug
ImplementsdebuggingfunctionalitytoinspectProxmoxBackupdatastorefiles,verifytheintegrity
ofchunks.
The ’diff’ subcommand allows comparing .pxar archives for two arbitrary snapshots. A list of
added/modified/deletedfileswillbedisplayed.
Alsocontainsan’api’subcommandwherearbitraryapipathscanbecalled(get/create/set/delete)
aswellasdisplaytheirparameters(usage)andtheirchild-links(ls).
13.6. Command‐lineTools 137

ProxmoxBackupDocumentation,Release4.2.8‐1
Bydefault,itconnectstotheproxmox-backup-proxyonlocalhostviahttps,butbysettingtheen-
vironmentvariablePROXMOX_DEBUG_API_CODEto1thetooldirectlycallsthecorrespondingcode.
(cid:193) Warning
Using PROXMOX_DEBUG_API_CODE can be dangerous and is only intended for debugging pur-
poses. Itisnotintendedforuseonaproductionsystem.
138 Chapter13. HostSystemAdministration

CHAPTER
FOURTEEN
NETWORK MANAGEMENT
ProxmoxBackupServerprovidesbothawebinterfaceandacommand-linetoolfornetworkconfig-
uration. YoucanfindtheconfigurationoptionsinthewebinterfaceundertheNetworkInterfaces
sectionoftheConfigurationmenutreeitem. Thecommand-linetoolisaccessedviathenetwork
subcommand. These interfaces allow you to carry out some basic network management tasks,
suchasadding,configuring,andremovingnetworkinterfaces.
(cid:174) Note
Anychangesmadetothenetworkconfigurationarenotapplied,untilyouclickonApplyCon-
figuration or enter the network reload command. This allows you to make many changes
at once. It also allows you to ensure that your changes are correct before applying them, as
makingamistakeherecanrendertheserverinaccessibleoverthenetwork.
Togetalistofavailableinterfaces,usethefollowingcommand:
139

ProxmoxBackupDocumentation,Release4.2.8‐1
| # proxmox-backup-manager |     | network list |     |     |     |     |
| ------------------------ | --- | ------------ | --- | --- | --- | --- |
┌───────┬────────┬───────────┬────────┬─────────────┬──────────────┬──────────────┐
│ name │ type │ autostart │ method │ address │ gateway │ ports/slaves │
╞═══════╪════════╪═══════════╪════════╪═════════════╪══════════════╪══════════════╡
│ bond0 │ bond │ 1 │ static │ x.x.x.x/x │ x.x.x.x │ ens18 ens19 │
├───────┼────────┼───────────┼────────┼─────────────┼──────────────┼──────────────┤
| │ ens18 │ eth | │   | 1 │ manual | │   | │   | │   | │   |
| ------------- | --- | ---------- | --- | --- | --- | --- |
├───────┼────────┼───────────┼────────┼─────────────┼──────────────┼──────────────┤
| │ ens19 │ eth | │   | 1 │ manual | │   | │   | │   | │   |
| ------------- | --- | ---------- | --- | --- | --- | --- |
└───────┴────────┴───────────┴────────┴─────────────┴──────────────┴──────────────┘
Toaddanewnetworkinterface,usethecreatesubcommandwiththerelevantparameters. For
example, youmaywanttosetupabond, forthepurposeofnetworkredundancy. Thefollowing
commandshowsatemplateforcreatingthebondshowninthelistabove:
--slaves␣
# proxmox-backup-manager network create bond0 --type bond --bond_mode active-backup
| ,→ens18,ens19 | --autostart | true --cidr | x.x.x.x/x | --gateway | x.x.x.x |     |
| ------------- | ----------- | ----------- | --------- | --------- | ------- | --- |
Youcanmakechangestotheconfigurationofanetworkinterfacewiththeupdatesubcommand:
| # proxmox-backup-manager |     | network update | bond0 --cidr | y.y.y.y/y |     |     |
| ------------------------ | --- | -------------- | ------------ | --------- | --- | --- |
Youcanalsoremoveanetworkinterface:
| # proxmox-backup-manager |     | network remove | bond0 |     |     |     |
| ------------------------ | --- | -------------- | ----- | --- | --- | --- |
Thependingchangesforthenetworkconfigurationfilewillappearatthebottomofthewebinter-
face. Youcanalsoviewthesechanges,byusingthecommand:
| # proxmox-backup-manager |     | network changes |     |     |     |     |
| ------------------------ | --- | --------------- | --- | --- | --- | --- |
Ifyouwouldliketocancelallchangesatthispoint,youcaneitherclickontheRevertbuttonoruse
thefollowingcommand:
| # proxmox-backup-manager |     | network revert |     |     |     |     |
| ------------------------ | --- | -------------- | --- | --- | --- | --- |
If you are happy with the changes and would like to write them into the configuration file, select
| ApplyConfiguration.      |     | Thecorrespondingcommandis: |     |     |     |     |
| ------------------------ | --- | -------------------------- | --- | --- | --- | --- |
| # proxmox-backup-manager |     | network reload             |     |     |     |     |
(cid:174) Note
ThiscommandandcorrespondingGUIbuttonrelyontheifreloadcommand,fromthepack-
ageifupdown2. ThispackageisincludedwithintheProxmoxBackupServerinstallation,how-
ever,youmayhavetoinstallityourself,ifyouhaveinstalledProxmoxBackupServerontopof
DebianoraProxmoxVEversionpriortoversion7.
YoucanalsoconfigureDNSsettings,fromtheDNSsectionof Configurationorbyusingthedns
| subcommandof | proxmox-backup-manager. |     |     |     |            |                   |
| ------------ | ----------------------- | --- | --- | --- | ---------- | ----------------- |
| 140          |                         |     |     |     | Chapter14. | NetworkManagement |

ProxmoxBackupDocumentation,Release4.2.8‐1
14.1 Traffic Control
Creatingandrestoringbackupscanproducealotoftraffic, canimpactsharedstorageandother
usersonthenetwork.
WithProxmoxBackupServer,youcanconstrainnetworktrafficforclientswithinspecifiednetworks
usingatokenbucketfilter(TBF).
Thisallowsyoutoavoidnetworkcongestionandprioritizetrafficfromcertainhosts.
You can manage the traffic controls either via the web-interface or using the traffic-control
commands of the proxmox-backup-manager command-line tool. Traffic is limited by rate
(rate-inandrate-out)andallowsforshortburstsbysettingthetokenbucketsize(burst-in
andburst-out).
(cid:174) Note
Sync jobs on the server are not affected by the configured rate limits. If you want to limit the
incoming traffic of pull-based or outgoing traffic of push-based sync job, you need to setup a
job-specificrate-inlimit. SeeSyncJobs.
ThefollowingcommandaddsatrafficcontrolruletolimitallIPv4clients(network0.0.0.0/0)to
100MB/s:
# proxmox-backup-manager traffic-control create rule0 --network 0.0.0.0/0 \
--rate-in 100MB --rate-out 100MB \
--comment "Default rate limit (100MB/s) for all clients"
14.1. TrafficControl 141

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
To limit both IPv4 and IPv6 network spaces, you need to pass two network parameters ::/0
and0.0.0.0/0.
Itispossibletorestrictrulestocertaintimeframes,forexamplethecompany’sofficehours:
(cid:98)
Tip
| YoucanuseSI(base10:      |     |           | KB,MB,...)      | orIEC(base2: |        | KiB,MiB,...) |     | units. |     |
| ------------------------ | --- | --------- | --------------- | ------------ | ------ | ------------ | --- | ------ | --- |
| # proxmox-backup-manager |     |           | traffic-control |              | update | rule0        | \   |        |     |
| --timeframe              |     | "mon..fri | 8-12"           | \            |        |              |     |        |     |
| --timeframe              |     | "mon..fri | 14:30-18"       |              |        |              |     |        |     |
Iftherearemultiplerules,theserverchoosestheonewiththesmallernetwork. Forexample,we
canoverwritethesettingforourprivatenetwork(andtheserveritself)with:
| # proxmox-backup-manager |                |            | traffic-control |       | create   | rule1 | \   |     |     |
| ------------------------ | -------------- | ---------- | --------------- | ----- | -------- | ----- | --- | --- | --- |
| --network                | 192.168.2.0/24 |            | \               |       |          |       |     |     |     |
| --network                | 127.0.0.0/8    |            | \               |       |          |       |     |     |     |
| --rate-in                | 20GB           | --rate-out | 20GB            | \     |          |       |     |     |     |
| --comment                | "Use           | 20GB/s     | for the         | local | network" |       |     |     |     |
(cid:174) Note
Thebehaviorisundefinedifthereareseveralrulesforthesamenetwork.
Iftherearemultipleruleswhichmatchaspecificnetwork,theywillallbeapplied,whichmeansthat
thesmallestonewins,asit’sbucketfillsupthefastest.
Tolistthecurrentrules,use:
| # proxmox-backup-manager |     |     | traffic-control |     | list |     |     |     |     |
| ------------------------ | --- | --- | --------------- | --- | ---- | --- | --- | --- | --- |
┌───────┬─────────────┬─────────────┬─────────────────────────┬────────────...─┐
| │ name | │   | rate-in | │ rate-out | │   | network |     |     | │ timeframe | ... │ |
| ------ | --- | ------- | ---------- | --- | ------- | --- | --- | ----------- | ----- |
╞═══════╪═════════════╪═════════════╪═════════════════════════╪════════════...═╡
| │ rule0 | │   | 100 MB | │   | 100 MB │ | ["0.0.0.0/0"] |     |     | │ ["mon..fri | ... │ |
| ------- | --- | ------ | --- | -------- | ------------- | --- | --- | ------------ | ----- |
├───────┼─────────────┼─────────────┼─────────────────────────┼────────────...─┤
| │ rule1 | │   | 20 GB | │   | 20 GB │ | ["192.168.2.0/24", |     | ...] | │   | ... │ |
| ------- | --- | ----- | --- | ------- | ------------------ | --- | ---- | --- | ----- |
└───────┴─────────────┴─────────────┴─────────────────────────┴────────────...─┘
Rulescanalsoberemoved:
| # proxmox-backup-manager |     |     | traffic-control |     | remove | rule1 |     |     |     |
| ------------------------ | --- | --- | --------------- | --- | ------ | ----- | --- | --- | --- |
Toshowthestate(currentdatarate)ofallconfiguredrulesuse:
| # proxmox-backup-manager |     |     | traffic-control |     | traffic |     |     |     |     |
| ------------------------ | --- | --- | --------------- | --- | ------- | --- | --- | --- | --- |
┌───────┬─────────────┬──────────────┐
| │ name | │ cur-rate-in |     | │ cur-rate-out |     | │   |     |     |     |     |
| ------ | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
╞═══════╪═════════════╪══════════════╡
| │ rule0 | │   | 0 B | │   | 0 B | │   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
├───────┼─────────────┼──────────────┤
| │ rule1 | │ 1.161 | GiB | │ 19.146 | KiB | │   |     |     |     |     |
| ------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
└───────┴─────────────┴──────────────┘
| 14.2 Overriding |     |     | network | device | names |     |     |     |     |
| --------------- | --- | --- | ------- | ------ | ----- | --- | --- | --- | --- |
Whenupgradingkernels,addingPCIedevicesorupdatingyourBIOS,automaticallygeneratednet-
workinterfacenamescanchange. Toalleviatethisissues,ProxmoxBackupServerprovidesatool
forautomaticallygeneratingsystemd.linkfilesforoverridingthenameofnetworkdevices. Italso
automaticallyreplacestheoccurrencesoftheoldinterfacenamein/etc/network/interfaces.
| 142 |     |     |     |     |     |     |     | Chapter14. | NetworkManagement |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Thegeneratedlinkfilesarestoredin/usr/local/lib/systemd/network. Fortheinterfacesfile
a new file will be generated in the same place with a .new suffix. This way you can inspect the
changesmadetotheconfigurationbyusingdiff(oranotherdiffviewerofyourchoice):
diff -y /etc/network/interfaces /etc/network/interfaces.new
If you see any problematic changes or want to revert the changes made by the pinning tool be-
fore rebooting, simply delete all .new files and the respective link files from /usr/local/lib/
systemd/network.
Thefollowingcommandwillgeneratea.linkfileforallphysicalnetworkinterfacesthatdonotyet
havea.linkfileandupdateselectedProxmoxVEconfigurationfiles(seeabove). Thegenerated
nameswillusethedefaultprefixnic,sotheresultinginterfacenameswillbenic1,nic2,...
proxmox-network-interface-pinning generate
Youcanoverridethedefaultprefixwiththe--prefixflag:
proxmox-network-interface-pinning generate --prefix myprefix
Itisalsopossibletopinonlyaspecificinterface:
proxmox-network-interface-pinning generate --interface enp1s0
When pinning a specific interface, you can specify the exact name that the interface should be
pinnedto:
proxmox-network-interface-pinning generate --interface enp1s0 --target-name if42
Inordertoapplythechangesmadebyproxmox-network-interface-pinningtothenetwork
configuration,thehostneedstoberebooted.
14.2. Overridingnetworkdevicenames 143

ProxmoxBackupDocumentation,Release4.2.8‐1
| 144 | Chapter14. | NetworkManagement |
| --- | ---------- | ----------------- |

CHAPTER
FIFTEEN
NOTIFICATIONS
15.1 Overview
• ProxmoxBackupServeremitsNotificationEventsincaseofnoteworthyeventsinthesystem.
Theseeventsareprocessedbasedontheglobalnotificationsettings. Eachnotificationevent
includes metadata, such as a timestamp, severity level, type, and additional event-specific
fields.
• NotificationMatchersrouteanotificationeventtooneormorenotificationtargets. Amatcher
canhavematchrulestoselectivelyroutebasedonthemetadataofanotificationevent.
• NotificationTargetsareadestinationtowhichanotificationeventisroutedtobyamatcher.
Therearemultipletypesoftarget,mail-based(SendmailandSMTP)andGotify.
Global notification settings can be configured in the GUI under Configuration ￿ Notifications. The
configurationisstoredinnotifications.cfgandnotifications-priv.cfg-thelattercontainssensitivecon-
figurationoptionssuchaspasswordsorauthenticationtokensfornotificationtargetsandcanonly
bereadbyroot.
15.2 Notification Targets
ProxmoxBackupServeroffersmultipletypesofnotificationtargets.
15.2.1 Sendmail
The sendmail binary is a program commonly found on Unix-like operating systems that handles
the sending of email messages. It is a command-line utility that allows users and applications to
sendemailsdirectlyfromthecommandlineorfromwithinscripts.
The sendmail notification target uses the sendmail binary to send emails to a list of configured
usersoremailaddresses. Ifauserisselectedasarecipient,theemailaddressconfiguredinuser’s
settings will be used. For the root@pam user, this is the email address entered during installa-
tion. Auser’semailaddresscanbeconfiguredinConfiguration → Access Control → User
Management. Ifauserhasnoassociatedemailaddress,noemailwillbesent.
(cid:174) Note
In standard Proxmox Backup Server installations, the sendmail binary is provided by Postfix.
It may be necessary to configure Postfix so that it can deliver mails correctly - for example by
settinganexternalmailrelay(smarthost). Incaseoffaileddelivery,checkthesystemlogsfor
messagesloggedbythePostfixdaemon.
Seenotifications.cfgforallconfigurationoptions.
145

ProxmoxBackupDocumentation,Release4.2.8‐1
15.2.2 SMTP
SMTPnotificationtargetscansendemailsdirectlytoanSMTPmailrelay. Thistargetdoesnotuse
thesystem’sMTAtodeliveremails. Similartosendmailtargets,ifauserisselectedasarecipient,
theuser’sconfiguredemailaddresswillbeused.
(cid:174) Note
Unlike sendmail targets, SMTP targets do not have any queuing/retry mechanism in case of a
failedmaildelivery.
Seenotifications.cfgforallconfigurationoptions.
15.2.3 Gotify
Gotifyisanopen-sourceself-hostednotificationserverthatallowsyoutosendpushnotifications
tovariousdevicesandapplications. ItprovidesasimpleAPIandwebinterface, makingiteasyto
integratewithdifferentplatformsandservices.
(cid:174) Note
GotifytargetswillrespecttheHTTPproxysettingsfromConfiguration￿Other￿HTTPproxy
Seenotifications.cfgforallconfigurationoptions.
15.2.4 Webhook
WebhooknotificationtargetsperformHTTPrequeststoaconfigurableURL.
Thefollowingconfigurationoptionsareavailable:
• url: TheURLtowhichtoperformtheHTTPrequests. Supportstemplatingtoinjectmessage
contents,metadataandsecrets.
• method: HTTPMethodtouse(POST/PUT/GET)
• header: Array of HTTP headers that should be set for the request. Supports templating to
injectmessagecontents,metadataandsecrets.
• body: HTTPbodythatshouldbesent. Supportstemplatingtoinjectmessagecontents,meta-
dataandsecrets.
• secret: Array of secret key-value pairs. These will be stored in a protected configuration
file only readable by root. Secrets can be accessed in body/header/URL templates via the
secretsnamespace.
• comment: Commentforthistarget.
For configuration options that support templating, the Handlebars syntax can be used to access
thefollowingproperties:
• {{ title }}: Therenderednotificationtitle
• {{ message }}: Therenderednotificationbody
• {{ severity }}: Theseverityofthenotification(info,notice,warning,error,unknown)
• {{ timestamp }}: Thenotification’stimestampasaUNIXepoch(inseconds).
• {{ fields.<name> }}: Sub-namespaceforanymetadatafieldsofthenotification. Forin-
stance,fields.typecontainsthenotificationtype-forallavailablefieldsrefertoNotification
Events.
146 Chapter15. Notifications

ProxmoxBackupDocumentation,Release4.2.8‐1
• {{ secrets.<name> }}: Sub-namespaceforsecrets. Forinstance,asecretnamedtoken
isaccessibleviasecrets.token.
Forconvenience,thefollowinghelpersareavailable:
• {{ url-encode <value/property> }}: URL-encodeaproperty/literal.
• {{ escape <value/property> }}: Escape any control characters that cannot be safely
representedasaJSONstring.
• {{ json <value/property> }}: Render a value as JSON. This can be useful to pass a
wholesub-namespace(e.g. fields)asapartofaJSONpayload(e.g. {{ json fields }}).
(cid:174) Note
WebhooktargetswillrespecttheHTTPproxysettingsfromConfiguration￿Other￿HTTPproxy
Example‐ntfy.sh
| • Method:                | POST |                 |     |     |
| ------------------------ | ---- | --------------- | --- | --- |
| • URL:https://ntfy.sh/{{ |      | secrets.channel | }}  |     |
• Headers:
| – Markdown: | Yes |     |     |     |
| ----------- | --- | --- | --- | --- |
• Body:
```
| {{ message | }}  |     |     |     |
| ---------- | --- | --- | --- | --- |
```
• Secrets:
| – channel: | <your ntfy.sh | channel> |     |     |
| ---------- | ------------- | -------- | --- | --- |
Example‐Discord
| • Method:                                 | POST |     |               |     |
| ----------------------------------------- | ---- | --- | ------------- | --- |
| • URL:https://discord.com/api/webhooks/{{ |      |     | secrets.token | }}  |
• Headers:
| – Content-Type: | application/json |     |     |     |
| --------------- | ---------------- | --- | --- | --- |
• Body:
{
| "content": | "``` {{ escape | message }}```" |     |     |
| ---------- | -------------- | -------------- | --- | --- |
}
• Secrets:
| – token: | <token> |     |     |     |
| -------- | ------- | --- | --- | --- |
Example‐Slack
| • Method:                                 | POST |     |               |     |
| ----------------------------------------- | ---- | --- | ------------- | --- |
| • URL:https://hooks.slack.com/services/{{ |      |     | secrets.token | }}  |
• Headers:
| – Content-Type: | application/json |     |     |     |
| --------------- | ---------------- | --- | --- | --- |
• Body:
15.2. NotificationTargets 147

ProxmoxBackupDocumentation,Release4.2.8‐1
{
| "text": "``` | {{escape message}}```", |     |     |     |
| ------------ | ----------------------- | --- | --- | --- |
"type": "mrkdwn"
}
• Secrets:
| – token: <token>  |          |     |     |     |
| ----------------- | -------- | --- | --- | --- |
| 15.3 Notification | Matchers |     |     |     |
Notification matchers route notifications to notification targets based on their matching
rules. These rules can match certain properties of a notification, such as the timestamp
(match-calendar), the severity of the notification (match-severity) or metadata fields
(match-field). If a notification is matched by a matcher, all targets configured for the matcher
willreceivethenotification.
An arbitrary number of matchers can be created, each with with their own matching rules and
targets to notify. Every target is notified at most once for every notification, even if the target is
usedinmultiplematchers.
Amatcherwithoutrulesmatchesanynotification;theconfiguredtargetswillalwaysbenotified.
Seenotifications.cfgforallconfigurationoptions.
15.3.1 CalendarMatchingRules
Acalendarmatchermatchesanotification’stimestamp.
Examples:
| • match-calendar | 8-12               |      |     |     |
| ---------------- | ------------------ | ---- | --- | --- |
| • match-calendar | 8:00-15:30         |      |     |     |
| • match-calendar | mon-fri 9:00-17:00 |      |     |     |
| • match-calendar | sun,tue-wed,fri    | 9-17 |     |     |
15.3.2 FieldMatchingRules
Notifications have a selection of metadata fields that can be matched. When using exact as a
matchingmode,a,canbeusedasaseparator. Thematchingrulethenmatchesifthemetadata
fieldhasanyofthespecifiedvalues.
Examples:
• match-field exact:type=gcOnlymatchnotificationsforgarbagecollectionjobs
• match-field exact:type=prune,verify Match prune job and verification job notifica-
tions.
• match-field regex:datastore=^backup-.*$ Match any datastore starting with
backup.
If a notification does not have the matched field, the rule will not match. For instance, a
match-field regex:datastore=.*directivewillmatchanynotificationthathasadatastore
metadatafield,butwillnotmatchifthefielddoesnotexist.
| 148 |     |     | Chapter15. | Notifications |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
15.3.3 SeverityMatchingRules
Anotificationhasaassociatedseveritythatcanbematched.
Examples:
| • match-severity | error:         | Onlymatcherrors |                       |     |
| ---------------- | -------------- | --------------- | --------------------- | --- |
| • match-severity | warning,error: |                 | Matchwarningsanderror |     |
Thefollowingseveritiesareinuse: info,notice,warning,error,unknown.
| 15.4 Notification | Events |     |     |     |
| ----------------- | ------ | --- | --- | --- |
The following table contains a list of all notification events in Proxmox Backup Server, their type,
severityandadditionalmetadatafields. typeaswellasanyothermetadatafieldmaybeusedin
match-fieldmatchrules.
| Event |     | type | Sever‐ | Metadatafields(inadditiontotype) |
| ----- | --- | ---- | ------ | -------------------------------- |
ity
| ACME certificate | renewal | acme | error | hostname |
| ---------------- | ------- | ---- | ----- | -------- |
failed
| Garbagecollectionfailure |      | gc  | error | datastore,hostname |
| ------------------------ | ---- | --- | ----- | ------------------ |
| Garbage collection       | suc- | gc  | info  | datastore,hostname |
cess
| Package updates | avail- | package-updatesinfo |     | hostname |
| --------------- | ------ | ------------------- | --- | -------- |
able
| Prunejobfailure   |     | prune | error | datastore,hostname,job-id |
| ----------------- | --- | ----- | ----- | ------------------------- |
| Prunejobsuccess   |     | prune | info  | datastore,hostname,job-id |
| Remotesyncfailure |     | sync  | error | datastore,hostname,job-id |
| Remotesyncsuccess |     | sync  | info  | datastore,hostname,job-id |
Tapebackupjobfailure tape-backup error datastore, hostname, media-pool,
job-id
Tapebackupjobsuccess tape-backup info datastore, hostname, media-pool,
job-id
| Tapeloadingrequest |     | tape-load | notice | hostname |
| ------------------ | --- | --------- | ------ | -------- |
Verificationjobfailure verification error datastore,hostname,job-id
Verificationjobsuccess verification info datastore,hostname,job-id
The following table contains a description of all use metadata fields. All of these can be used in
match-fieldmatchrules.
|     | Metadatafield |     | Description                  |     |
| --- | ------------- | --- | ---------------------------- | --- |
|     | datastore     |     | Thenameofthedatastore        |     |
|     | hostname      |     | Thehostnameofthebackupserver |     |
|     | job-id        |     | JobID                        |     |
|     | media-pool    |     | Thenameofthetapemediapool    |     |
|     | type          |     | Notificationeventtype        |     |
(cid:174) Note
The daily task checking for any available system updates only sends notifications if the node
hasanactivesubscription.
15.4. NotificationEvents 149

ProxmoxBackupDocumentation,Release4.2.8‐1
15.5 System Mail Forwarding
Certain local system daemons, such as smartd, send notification emails to the local root user.
Thesemailsareconvertedintonotificationeventswiththetypesystem-mailandwithaseverity
of unknown.
Whentheemailisforwardedtoasendmailtarget, themail’scontentandheadersareforwarded
as-is. For all other targets, the system tries to extract both a subject line and the main text body
from the email content. In instances where emails solely consist of HTML content, they will be
transformedintoplaintextformatduringthisprocess.
15.6 Permissions
In order to modify/view the configuration for notification targets, the Sys.Modify/Sys.Audit
permissionsarerequiredforthe/system/notificationsACLnode.
15.7 Notification Mode
Datastoresandtapebackup/restorejobconfigurationhaveanotification-modeoptionwhich
canhaveoneoftwovalues:
• Sendnotificationsbasedontheglobalnotificationsettings(notification-system).
• Sendnotificationemailsviathesystem’ssendmailcommand(legacy-sendmail). Anytar-
getsormatchersfromtheglobalnotificationsettingsareignored. Thismodeisequivalentto
thenotificationbehaviorforProxmoxBackupServerversionsbefore3.2. Itmightberemoved
inalaterreleaseofProxmoxBackupServer.
15.7.1 Settingsforlegacy-sendmailnotificationmode
Ifnotification-modeissettolegacy-sendmail,ProxmoxBackupServerwillsendnotification
emailsviathesystem’ssendmailcommandtotheemailaddressconfiguredfortheusersetinthe
notify-useroption(fallingbacktoroot@pamifnotset).
Fordatastores,youcanalsochangethelevelofnotificationsreceivedpertasktypeviathenotify
option.
• Always: sendanotificationforanyscheduledtask,independentoftheoutcome
• Errors: sendanotificationforanyscheduledtaskthatresultsinanerror
• Never: donotsendanynotificationatall
The notify-user and notify options are ignored when using the global notification settings
(notification-modeissettonotification-system).
15.8 Overriding Notification Templates
ProxmoxBackupServerusesHandlebarstemplatestorendernotifications. Theoriginaltemplates
provided by Proxmox Backup Server are stored in /usr/share/proxmox-backup/templates/
default/.
Notification templates can be overridden by providing a custom template file in the override di-
rectory at /etc/proxmox-backup/notification-templates/default/. When rendering a
notificationofagiventype,ProxmoxBackupServerwillfirstattempttoloadatemplatefromthe
overridedirectory. Ifthisonedoesnotexistorfailstorender,theoriginaltemplatewillbeused.
The template files follow the naming convention of <type>-<body|subject>.txt.hbs. For
instance, the file gc-err-body.txt.hbs contains the template for rendering notifications for
150 Chapter15. Notifications

ProxmoxBackupDocumentation,Release4.2.8‐1
garbagecollectionerrors,whilepackage-updates-subject.txt.hbsisusedtorenderthesub-
jectlineofnotificationsforavailablepackageupdates.
15.9 Notification Thresholds and Reset Schedule (S3 Datastores Only)
Datastores of type S3 keep track of the number of requests being send to the corresponding S3
endpointandtheamountofdatabeingsend. ProxmoxBackupServerallowstoconfigurethreshold
fortheserequestandtrafficcounterstosendoutnotificationsifoneofthesetthresholdvaluesis
exceeded.
Thenotificationthresholdvaluecanbesetindividuallybyrequestmethodortrafficvolume. No-
tifications will be send out only once per threshold when the threshold has been exceeded. A
counterresetisrequiredtobringitbelowthethresholdagaininordertogetfurthernotifications.
Therefore, it is possible to define a threshold reset schedule so request and traffic counters get
periodicallyreset.
Per datastore notification thresholds and their reset schedule are configurable in the Datastore
OptionsforS3backeddatastores.
Thefollowingcountersthresholdsareavailableforconfiguration:
Counter DescriptionandUsage
Thresh‐
old
s3-get Number of GET requests: Mainly used for download of data and metadata among
thefollowingoperations: restore,verification,S3refresh,garbagecollection.
s3-put Numberof PUTrequests: Mainlyusedforuploadofdataandmetadataamongthe
followingoperations: backup,syncs,metadatachanges,contentmoves.
s3-post Number of POST requests: Mainly used for modification of data and metadata
among the following operations: bulk deletion during garbage collection, content
moves.
s3-head Number of HEAD requests: Mainly used to check for access and existence among
whichthefollowingoperations: checkingbucketaccess,fetchingofmetadata.
s3-deleteNumberofDELETErequests: Mainlyusedfordeletingsingleobjectsbythefollowing
operations: garbagecollection,contentmoves.
s3-uploadAmountofbytesuploadedtotheS3endpoint,independentofrequestmethod.
s3-downloAamdountofbytesdownloadedfromtheS3endpoint,independentofrequestmethod.
15.9. NotificationThresholdsandResetSchedule(S3DatastoresOnly) 151

ProxmoxBackupDocumentation,Release4.2.8‐1
| 152 | Chapter15. | Notifications |
| --- | ---------- | ------------- |

CHAPTER
SIXTEEN
TECHNICAL OVERVIEW
16.1 Datastores
A Datastore is the logical place where Backup Snapshots and their chunks are stored. Snapshots
consist of a manifest, blobs, and dynamic- and fixed-indexes (see Terminology), and are stored in
thefollowingdirectorystructure:
<datastore-root>/<type>/<id>/<time>/
Thededuplicationofdatastoresisbasedonreusingchunks,whicharereferencedbytheindexes
inabackupsnapshot. Thismeansthatmultipleindexescanreferencethesamechunks,reducing
theamountofspaceneededtocontainthedata(evenacrossbackupsnapshots).
16.2 Snapshots
ASnapshotisthecollectionofmanifest,blobsandindexesthatrepresentabackup. Whenaclient
createsasnapshot, itcanuploadblobs(singlefileswhicharenotchunked,e.g. theclientlog), or
oneormoreindexes(fixedordynamic).
Whenuploadinganindex,theclientfirsthastoreadthesourcedata,chunkitandsendthedata
aschunkswiththeiridentifyingchecksumtotheserver. Whenusingthechangedetectionmode
payload chunks for unchanged files are reused from the previous snapshot, thereby not reading
thesourcedataagain.
IfthereisapreviousSnapshotinthebackupgroup,theclientcanfirstdownloadthechunklistof
thepreviousSnapshot. Ifitdetectsachunkthatalreadyexistsontheserver,itcansendonlythe
checksuminsteadofdataandchecksum. ThiswaytheactualuploadofSnapshotsisincremental
whileeachSnapshotreferencesallchunksandisthusafullbackup.
Afteruploadingalldata,theclienthastosignaltotheserverthatthebackupisfinished. Ifthatis
notdonebeforetheconnectioncloses,theserverwillremovetheunfinishedsnapshot.
16.3 Chunks
Achunkissome(possiblyencrypted)datawithaCRC-32checksumattheendandatypemarker
atthebeginning. ItisidentifiedbytheSHA-256checksumofitscontent.
To generate such chunks, backup data is split either into fixed-size or dynamically sized chunks.
Thesamecontentwillbehashedtothesamechecksum.
Thechunksofadatastorearefoundin
<datastore-root>/.chunks/
This chunk directory is further subdivided into directories grouping chunks by their checksums 2
byteprefix(givenas4hexadecimaldigits),soachunkwiththechecksum
a342e8151cbf439ce65f3df696b54c67a114982cc0aa751f2852c2f7acc19a8b
153

ProxmoxBackupDocumentation,Release4.2.8‐1
livesin
<datastore-root>/.chunks/a342/
Thisisdonetoreducethenumberoffilesperdirectory,ashavingmanyfilesperdirectorycanbe
badforfilesystemperformance.
Thesechunkdirectories(’0000’-’ffff’)willbepreallocatedwhenadatastoreiscreated.
16.3.1 Fixed‐SizedChunks
Forblockbasedbackups(likeVMs),fixed-sizedchunksareused. Thecontent(diskimage),issplit
intochunksofthesamelength(typically4MiB).
ThisworksverywellforVMimages,sincethefilesystemontheguestmostoftentriestoallocate
filesincontiguouspieces,sonewfilesgetnewblocks,andchangingexistingfileschangesonlytheir
ownblocks.
Asanoptimization,VMsinProxmoxVEcanmakeuseof’dirtybitmaps’,whichcantrackthechanged
blocksofanimage. Sincethesebitmapsarealsoarepresentationoftheimagesplitintochunks,
there is a direct relation between the dirty blocks of the image and chunks which need to be up-
loaded. Thus,onlymodifiedchunksofthediskneedtobeuploadedtoabackup.
Sincetheimageisalwayssplitintochunksofthesamesize,unchangedblockswillresultinidentical
checksumsforthosechunks,sosuchchunksdonotneedtobebackedupagain. Thiswaystorage
snapshotsarenotneededtofindthechangedblocks.
For consistency, Proxmox VE uses a QEMU internal snapshot mechanism, that does not rely on
storagesnapshotseither.
16.3.2 DynamicallySizedChunks
Whenworkingwithfile-basedsystemsratherthanblock-basedsystems,usingfixed-sizedchunks
isnotagoodidea,sinceeverytimeafilewouldchangeinsize,theremainingdatawouldbeshifted
around,resultinginmanychunkschangingandtheamountofdeduplicationbeingreduced.
Toimprovethis,ProxmoxBackupServerusesdynamicallysizedchunksinstead. Insteadofsplitting
an image into fixed sizes, it first generates a consistent file archive (pxar) and uses a rolling hash
overthison-the-flygeneratedarchivetocalculatechunkboundaries.
WeuseavariantofBuzhashwhichisacyclicpolynomialalgorithm. Itworksbycontinuouslycal-
culating a checksum while iterating over the data, and on certain conditions, it triggers a hash
boundary.
Assumingthatmostfilesonthesystemthatistobebackeduphavenotchanged,eventuallythe
algorithmtriggerstheboundaryonthesamedataasapreviousbackup, resultinginchunksthat
canbereused.
16.3.3 EncryptedChunks
Encryptedchunksareaspecialcase. Bothfixed-anddynamicallysizedchunkscanbeencrypted,
andtheyarehandledinaslightlydifferentmannerthannormalchunks.
Thehashesofencryptedchunksarecalculatednotwiththeactual(encrypted)chunkcontent,but
withthe plain-textcontent, concatenated withthe encryptionkey. This way, twochunks withthe
same data but encrypted with different keys generate two different checksums and no collisions
occurformultipleencryptionkeys.
Thisisdonetospeeduptheclientpartofthebackup, sinceitonlyneedstoencryptchunksthat
areactuallygettinguploaded. Chunksthatexistalreadyinthepreviousbackup,donotneedtobe
encryptedanduploaded.
154 Chapter16. TechnicalOverview

ProxmoxBackupDocumentation,Release4.2.8‐1
16.3.4 ChangeDetectionModeforFile‐BasedBackups
The change detection mode controls how to detect and act for files which did not change in-
betweensubsequent backup runs as well as the archivefile format used to encode the directory
entries.
Thereare3modesavailable,thecurrentdefaultlegacymode,aswellasthedataandmetadata
mode. Whilethelegacymodeencodesallcontentsinasinglepxararchive,thelattertwomodes
splitdataandmetadataintoppxarandmpxararchives. Thisisdonetoallowforfastcomparison
ofmetadatawiththeprevioussnapshot,usedbythemetadatamodetodetectreusablefiles. The
datamoderefrainsfromreusingunchangedfilesbyrechunkingthefileunconditionally. Thismode
thereforeassuresthatnofilechangesaremissedevenifthemetadataareunchanged.
(cid:174) Note
pxarandmpxar/ppxarfileformatsaredifferentandcannotbededuplicatedasefficientlyifa
datastorestoresarchivesnapshotsofbothtypes.
Asthechangedetectionmodesareclientsidechanges,theyarebackwardscompatiblewitholder
versionsofProxmoxBackupServer. Exploringthebackupcontentsforthenewarchiveformatvia
thewebinterfacerequireshoweveraProxmoxBackupServerwithversion3.2.5orhigher. Upgrad-
ingtothelatestversionisrecommendedforfullfeaturecompatibility.
LegacyMode
Backupsnapshotsoffilesystemsarecreatedbyrecursivelyscanningthedirectoryentries. Allen-
triestobeincludedinthesnapshotarereadandserializedbyencodingthemusingthepxararchive
format. TheresultingstreamischunkedintodynamicallysizedchunksanduploadedtotheProx-
moxBackupServer,deduplicatingchunksbasedontheircontentdigestforspaceefficientstorage.
File contents are read and chunked unconditionally, no check is performed to detect unchanged
files.
DataMode
Likeforlegacymodefilecontentsarereadandchunkedunconditionally,nocheckisperformed
todetectunchangedfiles.
However, in contrast to legacy mode, which stores entries metadata and data in a single self-
contained pxar archive, the data mode encodes metadata and file contents into two separate
streams. Theresultingbackupsnapshotsthereforecontainsplitarchives,anarchiveinmpxarfor-
mat containingtheentriesmetadataandanarchivewithppxarformat ,containingtheactualfile
contents,separatedbypayloadheadersforconsistencychecks. Themetadataarchivestoresaref-
erenceoffsettothecorrespondingpayloadarchiveentrysothefilecontentscanbeaccessed. Both
ofthesearchivesarechunkedanduploadedbytheProxmoxbackupclient,resultinginseparated
indicesandindependentchunks.
The mpxar archive can be used to efficiently fetch the associated metadata for archive entries
without the overhead of payload data stored within the same chunks. This is used for example
for entry lookups to list the archive contents or to navigate the mounted filesystem via the FUSE
implementation. Nodedicatedcatalogisthereforecreatedforarchivesencodedusingthismode.
Bynotcomparingmetadatatothepreviousbackupsnapshot,nofileswillbeconsideredreusable
bythismode, incontrasttothemetadatamode. Lattercanreusefileswhichhavechanged, but
filesizeandmtimedidnotchangebecauserestoredafterchangingthefilescontents.
16.3. Chunks 155

ProxmoxBackupDocumentation,Release4.2.8‐1
MetadataMode
The metadata mode detects files whose file metadata did not change in-between subsequent
backup runs. The metadata comparison includes file size, file type, ownership and permission
information, as well as acls and attributes and most importantly the file’s mtime, for details see
thepxarmetadataarchiveformat. Filesctimeandinodenumberarenotstoredandusedforcom-
parison,sincesometools(e.g. vzdump)mightsyncthecontentsofthefilesystemtoatemporary
location before actually performing the backup via the Proxmox backup client. For these cases,
ctimeandinodenumberwillalwayschange.
Thismodewillavoidreadingandrechunkingthefilecontentswheneverpossiblebyreusingthefile
contentchunksofunchangedfilesfromthepreviousbackupsnapshot.
Tocomparethemetadata,theprevioussnapshotsmpxarmetadataarchiveisdownloadedatthe
startofthebackuprunandusedasareference. Further,theindexofthepayloadarchiveppxar
is fetched and used to lookup the file content chunk’s digests, which will be used to reindex pre-
existingchunkswithouttheneedtorereadandrechunkthefilecontents.
During backup, the metadata and payload archives are encoded in the same manner as for the
datamode,butforthemetadatamodeeachentryisadditionallylookedupinthemetadataref-
erence archive for comparison first. If the file did not change as compared to the reference, the
fileisconsideredasunchangedandtheProxmoxbackupcliententersalook-aheadcachingmode.
In this mode, the client will keep reading and comparing then following entries in the filesystem
aslongastheyarereusable. Further, itkeepstrackofthepayloadarchiveoffsetrangethesefile
contentsarestoredin. Theadditionallook-aheadcachingisneeded,asfileboundariesarenotre-
quiredtobealignedwithchunkboundaries,thereforereusedchunkscancontainpossiblywasted
chunkcontent(alsocalledpadding)ifreusedunconditionally.
The look-ahead cache will greedily cache all unchanged entries up to the point where either the
cache size limit is reached, a file entry with changed metadata is encountered, or the range of
payload chunks considered for reuse is not continuous. An example for the latter is a file which
disappeared in-between subsequent backup runs, leaving a hole in the range. At this point, the
cachingmodeisdisabledandtheclientcalculatesthewastedpaddingsizewhichwouldbeintro-
duced by reusing the payload chunks for all the unchanged files cached up to this point. If the
paddingisacceptable(belowapresetlimitof10%oftheactuallyreusedchunkcontent),thefiles
arereusedbyencodingtheminthemetadataarchiveusingupdatedoffsetreferencestothecon-
tentsandreindexingthepre-existingchunksinthenewppxararchive. Ifhoweverthepaddingis
not acceptable, exceeding the limit, all cached entries are reencoded, not reusing any of the pre-
existingdata. Themetadataascachedwillbeencodedinthemetadataarchive,nomatterifcached
filecontentsaretobereusedorreencoded.
Thiscombinationoflook-aheadcachingandreuseofpre-existingpayloadarchivechunksforfiles
with unchanged contents therefore speeds up the backup process by avoiding rereading and
rechunkingfilecontentswheneverpossible.
Toreducepaddingsandincreasechunkreusability,duringcreationofthearchivesindatamode
and metadata mode the pxar encoder signals encountered file boundaries as suggested chunk
boundariestotheslidingwindowchunker. Thechunkerthendecidesbasedontheinternalstate
ifthesuggestedboundaryisacceptedordisregarded.
16.4 Caveats and Limitations
16.4.1 NotesonHashCollisions
Everyhashingalgorithmhasachancetoproducecollisions,meaningtwo(ormore)inputsgenerate
the same checksum. For SHA-256, this chance is negligible. To calculate the chances of such a
collision,onecanusetheideasofthe’birthdayproblem’fromprobabilitytheory. Forbignumbers,
thisisactuallyunfeasibletocalculatewithregularcomputers,butthereisagoodapproximation:
p(n,d)=1−e −n2/(2d)
156 Chapter16. TechnicalOverview

ProxmoxBackupDocumentation,Release4.2.8‐1
Wherenisthenumberoftries,andd isthenumberofpossibilities. Foraconcreteexample,lets
assumealargedatastoreof1PiBandanaveragechunksizeof4MiB.Thatmeansn = 268435456
tries,andd=2256 possibilities. Insertingthosevaluesintheformulafromearlieryouwillseethat
theprobabilityofacollisioninthatscenariois:
3.1115∗10 −61
Forcontext,inalotterygameofguessing6numbersoutof45,thechancetocorrectlyguessall6
numbers is only
1.2277∗10−7.
This means the chance of a collision is lower than winning 8 such
lotterygamesinarow:
(1.2277∗10−7)8 =5.1623∗10−56.
In conclusion, it is extremely unlikely that such a collision would occur by accident in a normal
datastore.
Additionally,SHA-256ispronetolengthextensionattacks,butsincethereisanupperlimitforhow
bigthechunksare,thisisnotaproblem,becauseapotentialattackercannotarbitrarilyaddcontent
tothedatabeyondthatlimit.
16.4.2 File‐BasedBackup
Since dynamically sized chunks (for file-based backups) are created on a custom archive format
(pxar)andnotoverthefilesdirectly,thereisnorelationbetweenthefilesandchunks. Thismeans
thattheProxmoxBackupClienthastoreadallfilesagainforeverybackup,otherwiseitwouldnot
bepossibletogenerateaconsistent, independentpxararchivewheretheoriginalchunkscanbe
reused. Notethatinspiteofthis,onlyneworchangedchunkswillbeuploaded.
Inordertoavoidtheselimitations,theChangeDetectionModemetadatawasintroduced.
16.4.3 VerificationofEncryptedChunks
Forencryptedchunks,onlythechecksumoftheoriginal(plaintext)dataisavailable,makingitim-
possiblefortheserver(withouttheencryptionkey)toverifyitscontentagainstit. Insteadonlythe
CRC-32checksumgetschecked.
16.5 Troubleshooting
Indexfiles(.fidx,.didx)containinformationabouthowtorebuildafile. Moreprecisely,theycontain
anorderedlistofreferencestothechunksthattheoriginalfilewassplitinto. Ifthereissomething
wrongwithasnapshot,itmightbeusefultofindoutwhichchunksarereferencedinit,andcheck
whethertheyarepresentandintact. Theproxmox-backup-debugcommand-linetoolcanbeused
toinspectsuchfilesandrecovertheircontents. Forexample,togetalistofthereferencedchunks
ofa.fidxindex:
# proxmox-backup-debug inspect file drive-scsi0.img.fidx
Thesamecommandcanbeusedtoinspect.blobfiles. Withoutthe--decodeparameter,justthe
size and the encryption type, if any, are printed. If --decode is set, the blob file is decoded into
thespecifiedfile(’-’willdecodeitdirectlytostdout).
Thefollowingexamplewouldprintthedecodedcontentsofqemu-server.conf.blob. Ifthefileyou’re
tryingtoinspectisencrypted,apathtothekeyfilemustbeprovidedusing--keyfile.
# proxmox-backup-debug inspect file qemu-server.conf.blob --decode -
Youcanalsocheckinwhichindexfilesaspecificchunkfileisreferencedwith:
# proxmox-backup-debug inspect chunk␣
,→b531d3ffc9bd7c65748a61198c060678326a431db7eded874c327b7986e595e0 --reference-filter /path/
,→in/a/datastore/directory
16.5. Troubleshooting 157

ProxmoxBackupDocumentation,Release4.2.8‐1
Here--reference-filterspecifieswhereindexfilesshouldbesearched. Thiscanbeanarbi-
trarypath. If, forsomereason, thefilenameofthechunkwaschanged, youcanexplicitlyspecify
thedigestusing--digest. Bydefault,thechunkfilenameisusedasthedigesttolookfor. Ifno
--reference-filter is specified, it will only print the CRC and encryption status of the chunk.
Youcanalsodecodechunks,bysettingthe--decodeflag. Ifthechunkisencrypted,a--keyfile
mustbeprovided,inordertodecodeit.
16.5.1 RestorewithoutaRunningProxmoxBackupServer
It’s possible to restore specific files from a snapshot, without a running Proxmox Backup Server
instance,usingtherecoversubcommand,providedyouhaveaccesstotheintactindexandchunk
files. Notethatyoualsoneedthecorrespondingkeyfileifthebackupwasencrypted.
# proxmox-backup-debug recover index drive-scsi0.img.fidx /path/to/.chunks
Intheaboveexample,the/path/to/.chunksargumentisthepathtothedirectorythatcontainsthe
chunks, and drive-scsi0.img.fidx is the index file of the file you’d like to restore. Both paths can
be absolute or relative. With --skip-crc, it’s possible to disable the CRC checks of the chunks.
Thiswillspeeduptheprocessslightlyandallowfortryingtorestore(partially)corruptchunks. It’s
recommendedtoalwaystrywithouttheskip-CRCoptionfirst.
158 Chapter16. TechnicalOverview

CHAPTER
SEVENTEEN
FAQ
17.1 What distribution is Proxmox Backup Server (PBS) based on?
ProxmoxBackupServerisbasedonDebianGNU/Linux.
17.2 Which platforms are supported as a backup source (client)?
TheclienttoolworksonmostmodernLinuxsystems,meaningyouarenotlimitedtoDebian-based
backups.
| 17.3 Will | Proxmox | Backup | Server run | on a 32‐bit | processor? |     |
| --------- | ------- | ------ | ---------- | ----------- | ---------- | --- |
Proxmox Backup Server only supports 64-bit CPUs (AMD or Intel). There are no future plans to
support32-bitprocessors.
17.4 How long will my Proxmox Backup Server version be supported?
| ProxmoxBackupVersion |     | DebianVersion      |     | First Re‐ | Debian  | Proxmox   |
| -------------------- | --- | ------------------ | --- | --------- | ------- | --------- |
|                      |     |                    |     | lease     | EOL     | BackupEOL |
| ProxmoxBackup4       |     | Debian13(Trixie)   |     | 2025-08   | TBA     | TBA       |
| ProxmoxBackup3       |     | Debian12(Bookworm) |     | 2023-06   | 2026-07 | 2026-08   |
| ProxmoxBackup2       |     | Debian11(Bullseye) |     | 2021-07   | 2024-07 | 2024-07   |
| ProxmoxBackup1       |     | Debian10(Buster)   |     | 2020-11   | 2022-08 | 2022-07   |
17.5 How can I upgrade Proxmox Backup Server to the next point re‐
lease?
Minorversionupgrades,forexampleupgradingfromProxmoxBackupServerinversion3.1to3.2
or 3.3, can be done just like any normal update. But, you should still check the release notes for
anyrelevantnotable,orbreakingchange.
FortheupdateitselfuseeithertheWebUINode->UpdatespanelorthroughtheCLIwith:
apt update
apt full-upgrade
159

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:193) Warning
As Proxmox Backup Server uses a rolling release model on top of Debian, performing an apt
upgrade may result in a partially upgraded or broken package state. This is because apt full-
upgradecanalsoremoveexistingpackagestosatisfydependenciesifneeded,whileaptupgrade
cannot.
(cid:174) Note
Always ensure you correctly setup the package repositories and only continue with the actual
upgradeifaptupdatedidnothitanyerror.
17.6 How can I upgrade Proxmox Backup Server to the next major re‐
lease?
Majorversionupgrades,forexamplegoingfromProxmoxBackupServer2.4to3.1,arealsosup-
ported. Theymustbecarefullyplannedandtestedandshouldneverbestartedwithouthavingan
off-sitecopyoftheimportantbackups,e.g.,viaremotesyncortape,ready.
Althoughthespecificupgradestepsdependonyourrespectivesetup,weprovidegeneralinstruc-
tionsandadviceofhowaupgradeshouldbeperformed:
• UpgradefromProxmoxBackupServer3to4
• UpgradefromProxmoxBackupServer2to3
• UpgradefromProxmoxBackupServer1to2
17.7 Can I copy or synchronize my datastore to another location?
ProxmoxBackupServerallowsyoutocopyorsynchronizedatastorestootherlocations,through
theuseofRemotesandSyncJobs. Remoteisthetermgiventoaseparateserver,whichhasadatas-
torethatcanbesyncedtoalocalstore. ASyncJobistheprocesswhichisusedtopullthecontents
ofadatastorefromaRemotetoalocaldatastore.
17.8 Can Proxmox Backup Server verify data integrity of a backup
archive?
Proxmox Backup Server uses a built-in SHA-256 checksum algorithm, to ensure data integrity.
Within each backup, a manifest file (index.json) is created, which contains a list of all the backup
files,alongwiththeirsizesandchecksums. Thismanifestfileisusedtoverifytheintegrityofeach
backup.
17.9 When backing up to remote servers, do I have to trust the remote
server?
ProxmoxBackupServertransfersdataviaTransportLayerSecurity(TLS)andadditionallysupports
client-side encryption. This means that data is transferred securely and can be encrypted before
itreachestheserver. Thus,intheeventthatanattackergainsaccesstotheserveroranypointof
thenetwork,theywillnotbeabletoreadthedata.
160 Chapter17. FAQ

ProxmoxBackupDocumentation,Release4.2.8‐1
(cid:174) Note
Encryption is not enabled by default. To set up encryption, see the backup client encryption
section.
17.10 Is the backup incremental/deduplicated/full?
WithProxmoxBackupServer,backupsaresentincrementallytotheserver,anddataisthendedu-
plicatedontheserver. Thisminimizesboththestorageconsumedandtheimpactonthenetwork.
Eachbackupstillreferencesalldataandsuchisafullbackup. FordetailsseetheTechnicalOverview
17.10. Isthebackupincremental/deduplicated/full? 161

ProxmoxBackupDocumentation,Release4.2.8‐1
| 162 | Chapter17. | FAQ |
| --- | ---------- | --- |

APPENDIX
A
COMMAND SYNTAX
(cid:174) Note
Logging verbosity for the command-line tools can be controlled with the PBS_LOG (for pxar:
PXAR_LOG)environmentvariable. Possiblevaluesareoff,error,warn,info,debugandtracewith
infobeingthedefault.
A.1 proxmox-backup-client
proxmox-backup-client backup {<backupspec>} [OPTIONS]
Create(host)backup.
<backupspec>
[<string>]Listofbackupsourcespecifications:
[<archive-name>.<type>:<source-path>]...
The ’archive-name’ must only contain alphanumerics, hyphens and underscores while the
’type’mustbeeither’pxar’,’img’,’conf’or’log’. Canbespecifiedmorethanonce.
Optionalparameters:
--all-file-systems<boolean> (default=false)
Includeallmountedsubdirectories.
--auth-id<string>
AuthenticationID
--backup-id<string>
BackupID.
--backup-time<integer> (1 - N)
Backuptime(Unixepoch.)
--backup-typevm|ct|host
Backuptype.
--burst<string>
Sizeofthetokenbucket(forTokenbucketfilter)inbyteswithoptionalunit(B,KB(base10),
MB,GB,...,KiB(base2),MiB,Gib,...).
--change-detection-modelegacy|data|metadata (default=legacy)
Modetodetectfilechangessincelastbackuprun
--chunk-size<integer> (64 - 4096) (default=4096)
ChunksizeinKB.Mustbeapowerof2.
--crypt-modenone|encrypt|sign-only (default=encrypt)
Defineswhetherdataisencrypted(usinganAEADcipher),onlysigned,orneither.
163

ProxmoxBackupDocumentation,Release4.2.8‐1
--datastore<string>
Datastorename.
| --dry-run<boolean> | (default=false) |     |     |     |
| ------------------ | --------------- | --- | --- | --- |
Justshowwhatbackupwoulddo,butdonotuploadanything.
| --entries-max<integer> | (default=1048576) |     |     |     |
| ---------------------- | ----------------- | --- | --- | --- |
Maxnumberofentriestoholdinmemory.
--exclude<string>
Listofpathsorpatternsformatchingfilestoexclude. Canbespecifiedmorethanonce.
--include-dev<string>
Include mountpoints with same st_dev number (see man fstat) as specified files. Can be
specifiedmorethanonce.
| --keyfd<integer> | (0 - N) |     |     |     |
| ---------------- | ------- | --- | --- | --- |
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
| Pathtoencryptionkey.        | Alldatawillbeencryptedusingthiskey. |         |     |     |
| --------------------------- | ----------------------------------- | ------- | --- | --- |
| --master-pubkey-fd<integer> |                                     | (0 - N) |     |     |
Passamasterpublickeyviaanalreadyopenedfiledescriptor.
--master-pubkey-file<string>
Pathtomasterpublickey. Theencryptionkeyusedforabackupwillbeencryptedusingthis
keyandappendedtothebackup.
| --no-cache<boolean> | (default=false) |     |     |     |
| ------------------- | --------------- | --- | --- | --- |
Bypasslocaldatastorecachefornetworkstorages.
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--rate<string>
Ratelimit(forTokenbucketfilter)inbytes/swithoptionalunit(B,KB(base10),MB,GB,...,KiB
(base2),MiB,Gib,...).
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
| --skip-e2big-xattr<boolean> |     | (default=false) |     |     |
| --------------------------- | --- | --------------- | --- | --- |
Ignore the E2BIG error when retrieving xattrs. This includes the file, but discards the meta-
data.
| --skip-lost-and-found<boolean> |     | (default=false) |     |     |
| ------------------------------ | --- | --------------- | --- | --- |
Skiplost+founddirectory.
| proxmox-backup-client | benchmark | [OPTIONS] |     |     |
| --------------------- | --------- | --------- | --- | --- |
Runbenchmarktests
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
| 164 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--keyfile<string>
| Pathtoencryptionkey. | Alldatawillbeencryptedusingthiskey. |     |     |
| -------------------- | ----------------------------------- | --- | --- |
| --no-cache<boolean>  | (default=false)                     |     |     |
Bypasslocaldatastorecachefornetworkstorages.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |
| ----------------- | ----------- | -------------- | --- |
| Backupserverport. | Default:    | 8007           |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |         | localhost       |           |
| ------------------------------------------ | ------- | --------------- | --------- |
| proxmox-backup-client                      | catalog | dump <snapshot> | [OPTIONS] |
Dumpcatalog.
<snapshot>
[<string>]Snapshotpath.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ignore-missing-signature<boolean> (default=false)
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
| --keyfd<integer> | (0 - N) |     |     |
| ---------------- | ------- | --- | --- |
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
Pathtoencryptionkey.
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |
| ----------------- | ----------- | -------------- | --- |
| Backupserverport. | Default:    | 8007           |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |     | localhost |     |
| ------------------------------------------ | --- | --------- | --- |
proxmox-backup-client catalog shell <snapshot> <archive-name> [OPTIONS]
Shelltointeractivelyinspectandrestoresnapshots.
<snapshot>
[<string>]Group/Snapshotpath.
<archive-name>
[<string>]Backuparchivename.
Optionalparameters:
A.1. proxmox-backup-client 165

ProxmoxBackupDocumentation,Release4.2.8‐1
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
| --ignore-missing-signature<boolean> |     |     | (default=false) |     |     |
| ----------------------------------- | --- | --- | --------------- | --- | --- |
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
| --keyfd<integer> | (0 - N) |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
Pathtoencryptionkey.
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |     |     | localhost |     |     |
| ------------------------------------------ | --- | --- | --------- | --- | --- |
proxmox-backup-client change-owner <group> <new-owner> [OPTIONS]
Changeownerofabackupgroup
<group>
[<string>]Backupgroup.
<new-owner>
[<string>]AuthenticationID
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |                 |     | localhost |     |     |
| ------------------------------------------ | --------------- | --- | --------- | --- | --- |
| proxmox-backup-client                      | garbage-collect |     | [OPTIONS] |     |     |
Startgarbagecollectionforaspecificrepository.
Optionalparameters:
--auth-id<string>
AuthenticationID
| 166 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--datastore<string>
Datastorename.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client group forget <group> [OPTIONS]
Forget(remove)backupsnapshots.
<group>
[<string>]Backupgroup
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client group move <group> --target-ns <string> [OPTIONS]
Moveabackupgrouptoadifferentnamespacewithinthesamedatastore.
<group>
[<string>]Backupgroup.
--target-ns<string>
Namespace.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--merge-group<boolean> (default=true)
Ifthegroupalreadyexistsinthetargetnamespace,mergesnapshotsintoit. Requiresmatch-
ingownershipandnon-overlappingsnapshottimes.
--ns<string>
Namespace.
A.1. proxmox-backup-client 167

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |      |               | localhost |     |     |
| ------------------------------------------ | ---- | ------------- | --------- | --- | --- |
| proxmox-backup-client                      | help | [{<command>}] | [OPTIONS] |     |     |
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-backup-client key change-passphrase [<path>] [OPTIONS]
Changetheencryptionkey’spassword.
<path>
[<string>]Keyfile. Withoutthisthedefaultkey’spasswordwillbechanged.
Optionalparameters:
--hint<string>
Passwordhint.
| --kdfnone|scrypt|pbkdf2 | (default=scrypt) |     |     |     |     |
| ----------------------- | ---------------- | --- | --- | --- | --- |
Keyderivationfunctionforpasswordprotectedencryptionkeys.
| proxmox-backup-client | key | create [<path>] | [OPTIONS] |     |     |
| --------------------- | --- | --------------- | --------- | --- | --- |
Createanewencryptionkey.
<path>
[<string>]Outputfile. Withoutthisthekeywillbecomethenewdefaultencryptionkey.
Optionalparameters:
--hint<string>
Passwordhint.
| --kdfnone|scrypt|pbkdf2 | (default=scrypt) |     |     |     |     |
| ----------------------- | ---------------- | --- | --- | --- | --- |
Keyderivationfunctionforpasswordprotectedencryptionkeys.
| proxmox-backup-client | key | create-master-key |     |     |     |
| --------------------- | --- | ----------------- | --- | --- | --- |
Create an RSA public/private key pair used to put an encrypted version of the symmetric backup
encryptionkeyontothebackupserveralongwitheachbackup.
| proxmox-backup-client | key | import-master-pubkey | <path> |            |               |
| --------------------- | --- | -------------------- | ------ | ---------- | ------------- |
| 168                   |     |                      |        | AppendixA. | CommandSyntax |

ProxmoxBackupDocumentation,Release4.2.8‐1
Import an RSA public key used to put an encrypted version of the symmetric backup encryption
keyontothebackupserveralongwitheachbackup.
Theimportedkeywillbeusedasdefaultmasterkeyforfutureinvocationsbythesamelocaluser.
<path>
[<string>]PathtothePEMformattedRSApublickey.
proxmox-backup-client key import-with-master-key [<path>]
--encrypted-keyfile <string> --master-keyfile <string> [OPTIONS]
Importanencryptedbackupofanencryptionkeyusinga(private)masterkey.
<path>
[<string>]Outputfile. Withoutthisthekeywillbecomethenewdefaultencryptionkey.
--encrypted-keyfile<string>
RSA-encryptedkeyfiletoimport.
--master-keyfile<string>
(Private)masterkeytouse.
Optionalparameters:
--hint<string>
Passwordhint.
--kdfnone|scrypt|pbkdf2 (default=scrypt)
Keyderivationfunctionforpasswordprotectedencryptionkeys.
proxmox-backup-client key paperkey [<path>] [OPTIONS]
Generateaprintable,humanreadabletextfilecontainingtheencryptionkey.
ThisalsoincludesascanableQRcodeforfastkeyrestore.
<path>
[<string>]Keyfile. Withoutthisthedefaultkey’swillbeused.
Optionalparameters:
--output-formattext|html
Paperkeyoutputformat
--subject<string>
Includethespecifiedsubjectastitletext.
proxmox-backup-client key show [<path>] [OPTIONS]
Printtheencryptionkey’smetadata.
<path>
[<string>]Keyfile. Withoutthisthedefaultkey’smetadatawillbeshown.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-client key show-master-pubkey [<path>] [OPTIONS]
Listinformationaboutmasterkey
A.1. proxmox-backup-client 169

ProxmoxBackupDocumentation,Release4.2.8‐1
<path>
[<string>] Path to the PEM formatted RSA public key. Default location will be used if not
specified.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-client list [OPTIONS]
Listbackupgroups.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client login [OPTIONS]
Trytologin. Ifsuccessful,storeticket.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client logout [OPTIONS]
Logout(deletestoredticket).
Optionalparameters:
--auth-id<string>
AuthenticationID
170 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--datastore<string>
Datastorename.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client map <snapshot> <archive-name> [OPTIONS]
MapadriveimagefromaVMbackuptoalocalloopbackdevice. Use’unmap’toundo. WARNING:
Onlydothiswithtrustedbackups!
<snapshot>
[<string>]Group/Snapshotpath.
<archive-name>
[<string>]Backuparchivename.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ignore-missing-signature<boolean> (default=false)
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
--keyfile<string>
Pathtoencryptionkey.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
--verbose<boolean> (default=false)
Verboseoutputandstayinforeground.
proxmox-backup-client mount <snapshot> <archive-name> <target> [OPTIONS]
Mountpxararchive.
<snapshot>
[<string>]Group/Snapshotpath.
<archive-name>
[<string>]Backuparchivename.
<target>
[<string>]Targetdirectorypath.
A.1. proxmox-backup-client 171

ProxmoxBackupDocumentation,Release4.2.8‐1
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ignore-missing-signature<boolean> (default=false)
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
--keyfile<string>
Pathtoencryptionkey.
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |                 | localhost |     |     |
| ------------------------------------------ | --------------- | --------- | --- | --- |
| --verbose<boolean>                         | (default=false) |           |     |     |
Verboseoutputandstayinforeground.
| proxmox-backup-client | namespace | create [<ns>] | [OPTIONS] |     |
| --------------------- | --------- | ------------- | --------- | --- |
Createanewnamespace.
<ns>
[<string>]Namespace.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |           | localhost     |           |     |
| ------------------------------------------ | --------- | ------------- | --------- | --- |
| proxmox-backup-client                      | namespace | delete [<ns>] | [OPTIONS] |     |
Deleteanexistingnamespace.
<ns>
[<string>]Namespace.
Optionalparameters:
--auth-id<string>
AuthenticationID
| 172 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--datastore<string>
Datastorename.
--delete-groups<boolean>
Destroysallgroupsinthehierarchy.
| --port<integer>   | (1 - 65535) | (default=8007) |     |
| ----------------- | ----------- | -------------- | --- |
| Backupserverport. | Default:    | 8007           |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |           |             | localhost |
| ------------------------------------------ | --------- | ----------- | --------- |
| proxmox-backup-client                      | namespace | list [<ns>] | [OPTIONS] |
Listnamespacesinarepository.
<ns>
[<string>]Namespace.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
| --max-depth<integer> | (0 - | N)  |     |
| -------------------- | ---- | --- | --- |
maximumrecursiondepth
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |
| ----------------- | ----------- | -------------- | --- |
| Backupserverport. | Default:    | 8007           |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |     |     | localhost |
| ------------------------------------------ | --- | --- | --------- |
proxmox-backup-client namespace move [<ns>] --target-ns <string> [OPTIONS]
Moveabackupnamespacetoanewlocationwithinthesamedatastore.
<ns>
[<string>]Namespace.
--target-ns<string>
Namespace.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
| --delete-source<boolean> |     | (default=true) |     |
| ------------------------ | --- | -------------- | --- |
Removethesourcenamespaceaftermovingallcontents. Defaultstotrue.
A.1. proxmox-backup-client 173

ProxmoxBackupDocumentation,Release4.2.8‐1
| --max-depth<integer> | (0 - | 7) (default=7) |     |     |
| -------------------- | ---- | -------------- | --- | --- |
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
| --merge-groups<boolean> | (default=true) |     |     |     |
| ----------------------- | -------------- | --- | --- | --- |
Ifagroupwiththesamenamealreadyexistsinthetargetnamespace,mergesnapshotsinto
it. Requiresmatchingownershipandnon-overlappingsnapshottimes.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
| proxmox-backup-client | prune | <group> [OPTIONS] |     |     |
| --------------------- | ----- | ----------------- | --- | --- |
Pruneabackuprepository.
<group>
[<string>]Backupgroup
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--dry-run<boolean>
Justshowwhatprunewoulddo,butdonotdeleteanything.
| --keep-daily<integer> | (1  | - N) |     |     |
| --------------------- | --- | ---- | --- | --- |
Numberofdailybackupstokeep.
| --keep-hourly<integer> | (1  | - N) |     |     |
| ---------------------- | --- | ---- | --- | --- |
Numberofhourlybackupstokeep.
| --keep-last<integer> | (1 - | N)  |     |     |
| -------------------- | ---- | --- | --- | --- |
Numberofbackupstokeep.
| --keep-monthly<integer> | (1  | - N) |     |     |
| ----------------------- | --- | ---- | --- | --- |
Numberofmonthlybackupstokeep.
| --keep-weekly<integer> | (1  | - N) |     |     |
| ---------------------- | --- | ---- | --- | --- |
Numberofweeklybackupstokeep.
| --keep-yearly<integer> | (1  | - N) |     |     |
| ---------------------- | --- | ---- | --- | --- |
Numberofyearlybackupstokeep.
| --max-depth<integer> | (0 - | 7)  |     |     |
| -------------------- | ---- | --- | --- | --- |
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion, empty==auto-
maticfullrecursion,namespacedepthsreducemaximumallowedvalue)
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |            |               |
| ----------------- | ----------- | -------------- | ---------- | ------------- |
| Backupserverport. | Default:    | 8007           |            |               |
| 174               |             |                | AppendixA. | CommandSyntax |

ProxmoxBackupDocumentation,Release4.2.8‐1
--quiet<boolean> (default=false)
Minimaloutput-onlyshowremovals.
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client restore <snapshot> <archive-name> <target> [OPTIONS]
Restorebackuprepository.
<snapshot>
[<string>]Group/Snapshotpath.
<archive-name>
[<string>]Backuparchivename.
<target>
[<string>]Targetdirectorypath. Use’-’towritetostandardoutput.
Wedonotextract’.pxar’archiveswhenwritingtostandardoutput.
Optionalparameters:
--allow-existing-dirs<boolean> (default=false)
Donotfailifdirectoriesalreadyexists.
--auth-id<string>
AuthenticationID
--burst<string>
Sizeofthetokenbucket(forTokenbucketfilter)inbyteswithoptionalunit(B,KB(base10),
MB,GB,...,KiB(base2),MiB,Gib,...).
--crypt-modenone|encrypt|sign-only (default=encrypt)
Defineswhetherdataisencrypted(usinganAEADcipher),onlysigned,orneither.
--datastore<string>
Datastorename.
--ignore-acls<boolean> (default=false)
ignoreaclsettings
--ignore-extract-device-errors<boolean> (default=false)
ignoreerrorsthatoccurduringdevicenodeextraction
--ignore-missing-signature<boolean> (default=false)
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
--ignore-ownership<boolean> (default=false)
ignoreownersettings(nochown)
--ignore-permissions<boolean> (default=false)
ignorepermissionsettings(nochmod)
--ignore-xattrs<boolean> (default=false)
ignorexattrsettings
--keyfd<integer> (0 - N)
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
Pathtoencryptionkey. Alldatawillbeencryptedusingthiskey.
A.1. proxmox-backup-client 175

ProxmoxBackupDocumentation,Release4.2.8‐1
--ns<string>
Namespace.
| --overwrite<boolean> | (default=false) |     |     |     |     |
| -------------------- | --------------- | --- | --- | --- | --- |
overwritealreadyexistingfiles
| --overwrite-files<boolean> |     | (default=false) |     |     |     |
| -------------------------- | --- | --------------- | --- | --- | --- |
overwritealreadyexistingfiles
| --overwrite-hardlinks<boolean> |     | (default=false) |     |     |     |
| ------------------------------ | --- | --------------- | --- | --- | --- |
overwritealreadyexistingentriesbyarchiveshardlink
| --overwrite-symlinks<boolean> |     | (default=false) |     |     |     |
| ----------------------------- | --- | --------------- | --- | --- | --- |
overwritealreadyexistingentriesbyarchivessymlink
--pattern<string>
Pathormatchpatterntolimitfilesthatgetrestored. Canbespecifiedmorethanonce.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--prelude-target<string>
Pathtorestorepreludeto,(pxarv2archivesonly).
--rate<string>
Ratelimit(forTokenbucketfilter)inbytes/swithoptionalunit(B,KB(base10),MB,GB,...,KiB
(base2),MiB,Gib,...).
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |                 |     | localhost |     |     |
| ------------------------------------------ | --------------- | --- | --------- | --- | --- |
| proxmox-backup-client                      | server-identity |     | [OPTIONS] |     |     |
ReturntheserveridentityinformationforthisProxmoxBackupServer.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |          |       | localhost  |           |     |
| ------------------------------------------ | -------- | ----- | ---------- | --------- | --- |
| proxmox-backup-client                      | snapshot | files | <snapshot> | [OPTIONS] |     |
Listsnapshotfiles.
<snapshot>
[<string>]Snapshotpath.
Optionalparameters:
| 176 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot forget <snapshot> [OPTIONS]
Forget(remove)backupsnapshots.
<snapshot>
[<string>]Snapshotpath.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot list [<group>] [OPTIONS]
Listbackupsnapshots.
<group>
[<string>]Backupgroup.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
A.1. proxmox-backup-client 177

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot notes show <snapshot> [OPTIONS]
Shownotes
<snapshot>
[<string>]Snapshotpath.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot notes update <snapshot> <notes> [OPTIONS]
UpdateNotes
<snapshot>
[<string>]Snapshotpath.
<notes>
[<string>]TheNotes.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
178 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot protected show <snapshot> [OPTIONS]
Showprotectionstatusofthespecifiedsnapshot
<snapshot>
[<string>]Snapshotpath.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client snapshot protected update <snapshot> <protected>
[OPTIONS]
UpdateProtectionStatusofasnapshot
<snapshot>
[<string>]Snapshotpath.
<protected>
[<boolean>]Theprotectionstatus.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
A.1. proxmox-backup-client 179

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-client snapshot upload-log <snapshot> <logfile> [OPTIONS]
Uploadbackuplogfile.
<snapshot>
[<string>]Group/Snapshotpath.
<logfile>
[<string>]Thepathtothelogfileyouwanttoupload.
Optionalparameters:
--auth-id<string>
AuthenticationID
--crypt-modenone|encrypt|sign-only (default=encrypt)
Defineswhetherdataisencrypted(usinganAEADcipher),onlysigned,orneither.
--datastore<string>
Datastorename.
--keyfd<integer> (0 - N)
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
Pathtoencryptionkey. Alldatawillbeencryptedusingthiskey.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client status [OPTIONS]
Getrepositorystatus.
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
180 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-client task list [OPTIONS]
Listrunningservertasksforthisrepouser
Optionalparameters:
--all<boolean>
Alsoliststoppedtasks.
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--limit<integer> (1 - 1000) (default=50)
Themaximalnumberoftaskstolist.
--output-formattext|json|json-pretty
Outputformat.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client task log <upid> [OPTIONS]
Displaythetasklog.
<upid>
[<string>]UniqueProcess/TaskIdentifier
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-client task stop <upid> [OPTIONS]
Trytostopaspecifictask.
<upid>
[<string>]UniqueProcess/TaskIdentifier
Optionalparameters:
--auth-id<string>
AuthenticationID
A.1. proxmox-backup-client 181

ProxmoxBackupDocumentation,Release4.2.8‐1
--datastore<string>
Datastorename.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
| proxmox-backup-client | unmap | [<name>] |     |     |
| --------------------- | ----- | -------- | --- | --- |
Unmapaloopdevicemappedwith’map’andreleaseallresources.
<name>
[<string>]Archivename,pathtoloopdev(/dev/loopX)orloopdevicenumber. Omittolist
allcurrentmappingsandforcecleaningupleftoverinstances.
| proxmox-backup-client | version | [OPTIONS] |     |     |
| --------------------- | ------- | --------- | --- | --- |
Showclientandoptionalserverversion
Optionalparameters:
--auth-id<string>
AuthenticationID
--datastore<string>
Datastorename.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |
| ----------------- | ----------- | -------------- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
A.1.1 CatalogShellCommands
Thefollowingcommandsareavailableinaninteractiverestoreshell:
| proxmox-backup-client | shell <snapshot> | <name.pxar> |     |     |
| --------------------- | ---------------- | ----------- | --- | --- |
cd [<path>]
Changethecurrentworkingdirectorytothenewdirectory
<path>
[<string>]targetpath.
clear-selected
Clearthelistoffilesselectedforrestore.
deselect <path>
| 182 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Deselectanentryforrestore.
Thiswillreturnanerroriftheentrywasnotfoundinthelistofentriesselectedforrestore.
<path>
[<string>]pathtoentrytoremovefromlist.
exit
Exittheshell
find <pattern> [OPTIONS]
Findentriesinthecatalogmatchingthegivenmatchpattern.
<pattern>
[<string>]Pathormatchpatternformatchingfilenames.
Optionalparameters:
--select<boolean> (default=false)
Addmatchingfilenamestolistforrestore.
help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
list-selected [OPTIONS]
Listentriescurrentlyselectedforrestore.
Optionalparameters:
--patterns<boolean> (default=false)
Listmatchpatternsinsteadofthematchingfiles.
ls [<path>]
Listthecontentofworkingdirectoryorgivenpath.
<path>
[<string>]targetpath.
pwd
Listthecurrentworkingdirectory.
restore <target> [OPTIONS]
Restorethesub-archivegivenbythecurrentworkingdirectorytotarget.
Byfurtherprovidingapattern,therestorecanbelimitedtoanarrowersubsetofthissub-archive.
Ifpatternisnotpresentorempty,thefullarchiveisrestoredtotarget.
A.1. proxmox-backup-client 183

ProxmoxBackupDocumentation,Release4.2.8‐1
<target>
[<string>]targetpathforrestoreonlocalfilesystem.
Optionalparameters:
--pattern<string>
Pathormatchpatternformatchingfilenames.
restore-selected <target>
Restoretheselectedentriestothegiventargetpath.
Targetmustnotexistontheclientsfilesystem.
<target>
[<string>]targetpathforrestoreonlocalfilesystem.
select <path>
Selectanentryforrestore.
Thiswillreturnanerroriftheentryisalreadypresentinthelistorifaninvalidpathwasprovided.
<path>
[<string>]targetpath.
stat <path>
Readthemetadataforagivendirectoryentry.
Thisisexpensivebecausethedatahastobereadfromthepxararchive,whichmeansreadingover
thenetwork.
<path>
[<string>]targetpath.
A.2 proxmox-backup-manager
proxmox-backup-manager acl list [OPTIONS]
AccessControllist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager acl update <path> <role> [OPTIONS]
UpdateAccessControlList(ACLs).
<path>
[<string>]Accesscontrolpath.
<role>
[<role>]Enumrepresentingrolesviatheir[PRIVILEGES]combination.
Sinceprivilegesareimplementedasbitflags,eachuniquecombinationofprivilegesmapsto
asingle,uniqueu64valuethatisusedinthisenumdefinition.
Optionalparameters:
184 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--auth-id<string>
AuthenticationID
--delete<boolean>
Removepermissions(insteadofaddingit).
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--group<string>
GroupID
--propagate<boolean> (default=true)
Allowtopropagate(inherit)permissions.
proxmox-backup-manager acme account deactivate <name> [OPTIONS]
DeactivateanACMEaccount.
<name>
[<string>]ACMEaccountname.
Optionalparameters:
--force<boolean> (default=false)
Deleteaccountdataeveniftheserverrefusestodeactivatetheaccount.
proxmox-backup-manager acme account info <name> [OPTIONS]
Showacmeaccountinformation.
<name>
[<string>]ACMEaccountname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager acme account list [OPTIONS]
Listacmeaccounts.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager acme account register <name> <contact> [OPTIONS]
RegisteranACMEaccount.
<name>
[<string>]ACMEaccountname.
<contact>
[<string>]Listofemailaddresses.
Optionalparameters:
--directory<string>
TheACMEDirectory.
A.2. proxmox-backup-manager 185

ProxmoxBackupDocumentation,Release4.2.8‐1
| proxmox-backup-manager | acme account | update | <name> | [OPTIONS] |     |
| ---------------------- | ------------ | ------ | ------ | --------- | --- |
UpdateanACMEaccount.
<name>
[<string>]ACMEaccountname.
Optionalparameters:
--contact<string>
Listofemailaddresses.
| proxmox-backup-manager | acme cert | order | [OPTIONS] |     |     |
| ---------------------- | --------- | ----- | --------- | --- | --- |
OrderanewACMEcertificate.
Optionalparameters:
| --force<boolean> (default=false) |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- |
Forcerenewalevenifthecertificatedoesnotexpiresoon.
| proxmox-backup-manager | acme cert | revoke |     |     |     |
| ---------------------- | --------- | ------ | --- | --- | --- |
OrderanewACMEcertificate.
proxmox-backup-manager acme plugin add <type> <id> --api <string> --data
<string> [OPTIONS]
Showacmeaccountinformation.
<type>
[<string>]TheACMEchallengeplugintype.
<id>
[<string>]ACMEChallengePluginID.
--api<string>
DNSAPIPluginId.
--data<string>
Filecontainingtheplugindata.
Optionalparameters:
| --disable<boolean> (default=false) |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- |
Flagtodisabletheconfig.
| --validation-delay<integer> | (0  | - 172800) | (default=30) |     |     |
| --------------------------- | --- | --------- | ------------ | --- | --- |
Extradelayinsecondstowaitbeforerequestingvalidation.
AllowstocopewithlongTTLofDNSrecords.
| proxmox-backup-manager | acme plugin | config | <id> | [OPTIONS] |     |
| ---------------------- | ----------- | ------ | ---- | --------- | --- |
Showacmeaccountinformation.
<id>
[<string>]PluginID
Optionalparameters:
| 186 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager acme plugin list [OPTIONS]
Listacmeplugins.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager acme plugin remove <id>
DeleteanACMEpluginconfiguration.
<id>
[<string>]ACMEChallengePluginID.
proxmox-backup-manager acme plugin set <id> [OPTIONS]
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
proxmox-backup-manager ad create <realm> --server1 <string> [OPTIONS]
CreateanewADrealm
<realm>
[<string>]Realmname.
--server1<string>
ADserveraddress
Optionalparameters:
--base-dn<string>
LDAPDomain
A.2. proxmox-backup-manager 187

ProxmoxBackupDocumentation,Release4.2.8‐1
--bind-dn<string>
LDAPDomain
--capath<string>
CA certificate to use for the server. The path can point to either a file, or a directory. If it
points to a file, the PEM-formatted X.509 certificate stored at the path will be added as a
trustedcertificate. Ifthepathpointstoadirectory,thedirectoryreplacesthesystem’sdefault
certificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrustedcertificate.
--comment<string>
Comment.
| --default<boolean> (default=false) |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- |
Trueifyouwantthistobethedefaultrealmselectedonlogin.
--filter<string>
CustomLDAPsearchfilterforusersync
| --modeldap|ldap+starttls|ldaps |     | (default=ldap) |     |     |
| ------------------------------ | --- | -------------- | --- | --- |
LDAPconnectiontype
--password<string>
ADbindpassword
| --port<integer> (0 - | 65535) |     |     |     |
| -------------------- | ------ | --- | --- | --- |
ADserverPort
--server2<string>
FallbackADserveraddress
| --sync-attributes[[email=<string>] |     | [,firstname=<string>] |     |     |
| ---------------------------------- | --- | --------------------- | --- | --- |
[,lastname=<string>]]
Comma-separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhich
PBS user field. For example, to map the LDAP attribute mail to PBS’s email, write
email=mail.
--sync-defaults-options[[enable-new=<1|0>] [,remove-vanished=<string>]]
syncdefaultsoptions
| --user-classes[<string>, | ...] |     |     |     |
| ------------------------ | ---- | --- | --- | --- |
(default=inetorgperson,posixaccount,person,user)
Comma-separated list of allowed objectClass values for user synchronization. For instance,
if user-classes is set to person,user, then user synchronization will consider all LDAP
| entitieswhereobjectClass:         | personorobjectClass: |     | user. |     |
| --------------------------------- | -------------------- | --- | ----- | --- |
| --verify<boolean> (default=false) |                      |     |       |     |
Verifyservercertificate
| proxmox-backup-manager | ad delete | <realm> [OPTIONS] |     |     |
| ---------------------- | --------- | ----------------- | --- | --- |
RemoveanLDAPrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| proxmox-backup-manager | ad list | [OPTIONS] |     |     |
| ---------------------- | ------- | --------- | --- | --- |
ListconfiguredADrealms
Optionalparameters:
| 188 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager ad show <realm> [OPTIONS]
ShowADrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager ad sync <realm> [OPTIONS]
SyncagivenLDAPrealm
<realm>
[<string>]AuthenticationdomainID
Optionalparameters:
--dry-run<boolean> (default=false)
Ifset,donotcreate/deleteanything
--enable-new<boolean>
Enablenewlysyncedusersimmediately
--remove-vanished[acl|entry|properties, ...]
A semicolon-separated list of things to remove when they or the user vanishes during user
synchronization. The following values are possible: entry removes the user when not re-
turnedfromthesync;propertiesremovesanypropertiesonexistinguserthatdonotap-
pearinthesource. aclremovesACLswhentheuserisnotreturnedfromthesync.
proxmox-backup-manager ad update <realm> [OPTIONS]
UpdateanADrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--base-dn<string>
LDAPDomain
--bind-dn<string>
LDAPDomain
--capath<string>
CA certificate to use for the server. The path can point to either a file, or a directory. If it
points to a file, the PEM-formatted X.509 certificate stored at the path will be added as a
trustedcertificate. Ifthepathpointstoadirectory,thedirectoryreplacesthesystem’sdefault
certificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrustedcertificate.
--comment<string>
Comment.
--default<boolean> (default=false)
Trueifyouwantthistobethedefaultrealmselectedonlogin.
A.2. proxmox-backup-manager 189

ProxmoxBackupDocumentation,Release4.2.8‐1
--delete
server2|port|comment|default|verify|mode|bind-dn|password|filter|sync-defaults-options|sync-attributes|user-classes
| Listofpropertiestodelete. | Canbespecifiedmorethanonce. |     |     |     |
| ------------------------- | --------------------------- | --- | --- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--filter<string>
CustomLDAPsearchfilterforusersync
| --modeldap|ldap+starttls|ldaps | (default=ldap) |     |     |     |
| ------------------------------ | -------------- | --- | --- | --- |
LDAPconnectiontype
--password<string>
ADbindpassword
| --port<integer> (0 - | 65535) |     |     |     |
| -------------------- | ------ | --- | --- | --- |
ADserverPort
--server1<string>
ADserveraddress
--server2<string>
FallbackADserveraddress
| --sync-attributes[[email=<string>] |     | [,firstname=<string>] |     |     |
| ---------------------------------- | --- | --------------------- | --- | --- |
[,lastname=<string>]]
Comma-separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhich
PBS user field. For example, to map the LDAP attribute mail to PBS’s email, write
email=mail.
--sync-defaults-options[[enable-new=<1|0>] [,remove-vanished=<string>]]
syncdefaultsoptions
| --user-classes[<string>, | ...] |     |     |     |
| ------------------------ | ---- | --- | --- | --- |
(default=inetorgperson,posixaccount,person,user)
Comma-separated list of allowed objectClass values for user synchronization. For instance,
if user-classes is set to person,user, then user synchronization will consider all LDAP
| entitieswhereobjectClass:         | personorobjectClass: |     | user. |     |
| --------------------------------- | -------------------- | --- | ----- | --- |
| --verify<boolean> (default=false) |                      |     |       |     |
Verifyservercertificate
| proxmox-backup-manager | cert info |     |     |     |
| ---------------------- | --------- | --- | --- | --- |
Displaynodecertificateinformation.
| proxmox-backup-manager | cert update | [OPTIONS] |     |     |
| ---------------------- | ----------- | --------- | --- | --- |
Updatenodecertificatesandgenerateallneededfiles/directories. Ifeithertheauthenticationkey
orCSRFsecretkeydoesnotexist,eachwillbegenerated. Thesetwokeyswillgointoeffectthenext
timetheproxmox-backup.serviceisstarted.
Optionalparameters:
--force<boolean>
ForcegenerationofnewSSLcertificate.
proxmox-backup-manager datastore create <name> <path> [OPTIONS]
Createnewdatastoreconfig.
| 190 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
<name>
[<string>]Datastorename.
<path>
[<string>] Either the absolute path to the datastore directory, or a relative on-device path
forremovabledatastores.
Optionalparameters:
--backend<backend-config>
Datastorebackendconfig
--backing-device<string>
TheUUIDofthefilesystempartitionforremovabledatastores.
--comment<string>
Comment.
--counter-reset-schedule<calendar-event>
Resetnotificationthresholdrelatedcountersatspecifiedschedule.
--gc-on-unmount<boolean>
Rungarbagecollectionbeforeunmountingaremovabledatastore.
--gc-schedule<calendar-event>
Rungarbagecollectionjobatspecifiedschedule.
--keep-daily<integer> (1 - N)
Numberofdailybackupstokeep.
--keep-hourly<integer> (1 - N)
Numberofhourlybackupstokeep.
--keep-last<integer> (1 - N)
Numberofbackupstokeep.
--keep-monthly<integer> (1 - N)
Numberofmonthlybackupstokeep.
--keep-weekly<integer> (1 - N)
Numberofweeklybackupstokeep.
--keep-yearly<integer> (1 - N)
Numberofyearlybackupstokeep.
--maintenance-mode[type=<enum> [,message=<string>]]
Maintenancemode,typeiseither’offline’or’read-only’,messageshouldbeenclosedin”
--notification-modelegacy-sendmail|notification-system
(default=notification-system)
Configure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
--notification-thresholds[[s3-delete=<integer>] [,s3-download=<string>]
[,s3-get=<integer>] [,s3-head=<integer>] [,s3-post=<integer>]
[,s3-put=<integer>] [,s3-upload=<string>]]
Thresholdvaluesfornotifications
--notify[[gc=<enum>] [,prune=<enum>] [,sync=<enum>] [,verify=<enum>]]
Datastorenotificationsetting,enumcanbeoneof’always’,’never’,or’error’.
--notify-user<string>
UserID
--output-formattext|json|json-pretty
Outputformat.
A.2. proxmox-backup-manager 191

ProxmoxBackupDocumentation,Release4.2.8‐1
--overwrite-in-use<boolean> (default=false)
Overwriteinusemarker(S3backeddatastoresonly).
--prune-schedule<calendar-event>
Runprunejobatspecifiedschedule.
--reuse-datastore<boolean> (default=false)
Re-useexistingdatastoredirectory.
--tuning[[chunk-order=<enum>] [,default-verification-readers=<integer>]
[,default-verification-workers=<integer>] [,gc-atime-cutoff=<integer>]
[,gc-atime-safety-check=<1|0>] [,gc-cache-capacity=<integer>]
[,sync-level=<enum>]]
Datastoretuningoptions
--verify-new<boolean>
Ifenabled,allnewbackupswillbeverifiedrightaftercompletion.
proxmox-backup-manager datastore list [OPTIONS]
Datastorelist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager datastore mount <store> [OPTIONS]
Mountaremovabledatastore.
<store>
[<string>]Datastorename.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager datastore remove <name> [OPTIONS]
Removeadatastoreconfiguration.
<name>
[<string>]Datastorename.
Optionalparameters:
--destroy-data<boolean> (default=false)
Deletethedatastore’sunderlyingcontents
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--keep-job-configs<boolean> (default=false)
Ifenabled,thejobconfigurationsrelatedtothisdatastorewillbekept.
192 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager datastore s3-refresh <store>
RefreshdatastorecontentsfromS3tolocalcachestore.
<store>
[<string>]Datastorename.
proxmox-backup-manager datastore show <name> [OPTIONS]
Showdatastoreconfiguration
<name>
[<string>]Datastorename.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager datastore unmount <store> [OPTIONS]
Unmountaremovabledatastore.
<store>
[<string>]Datastorename.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager datastore update <name> [OPTIONS]
Updatedatastoreconfiguration.
<name>
[<string>]Datastorename.
Optionalparameters:
--comment<string>
Comment.
--counter-reset-schedule<calendar-event>
Resetnotificationthresholdrelatedcountersatspecifiedschedule.
--delete
comment|gc-schedule|gc-on-unmount|prune-schedule|keep-last|keep-hourly|keep-daily|keep-weekly|keep-monthly|keep-yearly|verify-new|notify-user|notify|notification-mode|tuning|maintenance-mode|notification-thresholds|counter-reset-schedule
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--gc-on-unmount<boolean>
Rungarbagecollectionbeforeunmountingaremovabledatastore.
--gc-schedule<calendar-event>
Rungarbagecollectionjobatspecifiedschedule.
--keep-daily<integer> (1 - N)
Numberofdailybackupstokeep.
A.2. proxmox-backup-manager 193

ProxmoxBackupDocumentation,Release4.2.8‐1
--keep-hourly<integer> (1 - N)
Numberofhourlybackupstokeep.
--keep-last<integer> (1 - N)
Numberofbackupstokeep.
--keep-monthly<integer> (1 - N)
Numberofmonthlybackupstokeep.
--keep-weekly<integer> (1 - N)
Numberofweeklybackupstokeep.
--keep-yearly<integer> (1 - N)
Numberofyearlybackupstokeep.
--maintenance-mode[type=<enum> [,message=<string>]]
Maintenancemode,typeiseither’offline’or’read-only’,messageshouldbeenclosedin”
--notification-modelegacy-sendmail|notification-system
(default=notification-system)
Configure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
--notification-thresholds[[s3-delete=<integer>] [,s3-download=<string>]
[,s3-get=<integer>] [,s3-head=<integer>] [,s3-post=<integer>]
[,s3-put=<integer>] [,s3-upload=<string>]]
Thresholdvaluesfornotifications
--notify[[gc=<enum>] [,prune=<enum>] [,sync=<enum>] [,verify=<enum>]]
Datastorenotificationsetting,enumcanbeoneof’always’,’never’,or’error’.
--notify-user<string>
UserID
--output-formattext|json|json-pretty
Outputformat.
--prune-schedule<calendar-event>
Runprunejobatspecifiedschedule.
--tuning[[chunk-order=<enum>] [,default-verification-readers=<integer>]
[,default-verification-workers=<integer>] [,gc-atime-cutoff=<integer>]
[,gc-atime-safety-check=<1|0>] [,gc-cache-capacity=<integer>]
[,sync-level=<enum>]]
Datastoretuningoptions
--verify-new<boolean>
Ifenabled,allnewbackupswillbeverifiedrightaftercompletion.
proxmox-backup-manager datastore uuid-mount <uuid> [OPTIONS]
TrymountingaremovabledatastoregiventheUUID.
<uuid>
[<string>]TheUUIDofthedevicethatshouldbemounted
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager disk fs create <name> --disk <string> [OPTIONS]
CreateaFilesystemonanunuseddisk. Willbemountedunder/mnt/datastore/<name>.
194 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
<name>
[<string>]Datastorename.
--disk<string>
Blockdevicename(/sys/block/<name>).
Optionalparameters:
--add-datastore<boolean>
Configureadatastoreusingthedirectory.
--filesystemext4|xfs
Afilesystemtypesupportedbyourtooling.
proxmox-backup-manager disk fs delete <name>
RemoveaFilesystemmountedunder/mnt/datastore/<name>.
<name>
[<string>]Datastorename.
proxmox-backup-manager disk fs list [OPTIONS]
Listsystemddatastoremountunits.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager disk initialize <disk> [OPTIONS]
InitializeemptyDiskwithGPT
<disk>
[<string>]Blockdevicename(/sys/block/<name>).
Optionalparameters:
--uuid<string>
UUIDfortheGPTtable.
proxmox-backup-manager disk list [OPTIONS]
Localdisklist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager disk smart-attributes <disk> [OPTIONS]
ShowSMARTattributes.
<disk>
[<string>]Blockdevicename(/sys/block/<name>).
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
A.2. proxmox-backup-manager 195

ProxmoxBackupDocumentation,Release4.2.8‐1
| proxmox-backup-manager | disk | wipe <disk> |     |     |
| ---------------------- | ---- | ----------- | --- | --- |
wipedisk
<disk>
[<string>](Partition)blockdevicename(/sys/class/block/<name>).
proxmox-backup-manager disk zpool create <name> --devices [<string>, ...]
--raidlevel single|mirror|raid10|raidz|raidz2|raidz3 [OPTIONS]
createazfspool
<name>
[<string>]Datastorename.
| --devices[<string>, | ...] |     |     |     |
| ------------------- | ---- | --- | --- | --- |
Alistofdisknames,commaseparated.
--raidlevelsingle|mirror|raid10|raidz|raidz2|raidz3
TheZFSRAIDleveltouse.
Optionalparameters:
--add-datastore<boolean>
Configureadatastoreusingthezpool.
| --ashift<integer> | (9 - 16) | (default=12) |     |     |
| ----------------- | -------- | ------------ | --- | --- |
Poolsectorsizeexponent.
--compressiongzip|lz4|lzjb|zle|zstd|on|off (default=On)
TheZFScompressionalgorithmtouse.
| proxmox-backup-manager | disk | zpool list [OPTIONS] |     |     |
| ---------------------- | ---- | -------------------- | --- | --- |
Localzfspools.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | dns | get [OPTIONS] |     |     |
| ---------------------- | --- | ------------- | --- | --- |
ReadDNSsettings
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | dns | set [OPTIONS] |     |     |
| ---------------------- | --- | ------------- | --- | --- |
UpdateDNSsettings.
Optionalparameters:
--deletedns1|dns2|dns3
| Listofpropertiestodelete. |     | Canbespecifiedmorethanonce. |     |     |
| ------------------------- | --- | --------------------------- | --- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| 196 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--dns1<string>
FirstnameserverIPaddress.
--dns2<string>
SecondnameserverIPaddress.
--dns3<string>
ThirdnameserverIPaddress.
--search<string>
Searchdomainforhost-namelookup.
proxmox-backup-manager garbage-collection list [OPTIONS]
Listgarbagecollectionjobstatusforalldatastores,includingdatastoreswithoutgcjobs.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager garbage-collection start <store> [OPTIONS]
Startgarbagecollectionforaspecificdatastore.
<store>
[<string>]Datastorename.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager garbage-collection status <store> [OPTIONS]
Showgarbagecollectionstatusforaspecificdatastore.
<store>
[<string>]Datastorename.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-backup-manager ldap create <realm> --base-dn <string> --server1
<string> --user-attr <string> [OPTIONS]
CreateanewLDAPrealm
A.2. proxmox-backup-manager 197

ProxmoxBackupDocumentation,Release4.2.8‐1
<realm>
[<string>]Realmname.
--base-dn<string>
LDAPDomain
--server1<string>
LDAPserveraddress
--user-attr<string>
| Usernameattribute. | UsedtomapauseridtoLDAPtoanLDAPdn. |     |     |     |
| ------------------ | --------------------------------- | --- | --- | --- |
Optionalparameters:
--bind-dn<string>
LDAPDomain
--capath<string>
CA certificate to use for the server. The path can point to either a file, or a directory. If it
points to a file, the PEM-formatted X.509 certificate stored at the path will be added as a
trustedcertificate. Ifthepathpointstoadirectory,thedirectoryreplacesthesystem’sdefault
certificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrustedcertificate.
--comment<string>
Comment.
| --default<boolean> (default=false) |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- |
Trueifyouwantthistobethedefaultrealmselectedonlogin.
--filter<string>
CustomLDAPsearchfilterforusersync
| --modeldap|ldap+starttls|ldaps | (default=ldap) |     |     |     |
| ------------------------------ | -------------- | --- | --- | --- |
LDAPconnectiontype
--password<string>
LDAPbindpassword
| --port<integer> (0 - | 65535) |     |     |     |
| -------------------- | ------ | --- | --- | --- |
Port
--server2<string>
FallbackLDAPserveraddress
| --sync-attributes[[email=<string>] |     | [,firstname=<string>] |     |     |
| ---------------------------------- | --- | --------------------- | --- | --- |
[,lastname=<string>]]
Comma-separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhich
PBS user field. For example, to map the LDAP attribute mail to PBS’s email, write
email=mail.
--sync-defaults-options[[enable-new=<1|0>] [,remove-vanished=<string>]]
syncdefaultsoptions
| --user-classes[<string>, | ...] |     |     |     |
| ------------------------ | ---- | --- | --- | --- |
(default=inetorgperson,posixaccount,person,user)
Comma-separated list of allowed objectClass values for user synchronization. For instance,
if user-classes is set to person,user, then user synchronization will consider all LDAP
| entitieswhereobjectClass:         | personorobjectClass: |     | user. |     |
| --------------------------------- | -------------------- | --- | ----- | --- |
| --verify<boolean> (default=false) |                      |     |       |     |
Verifyservercertificate
| proxmox-backup-manager | ldap delete | <realm> [OPTIONS] |     |     |
| ---------------------- | ----------- | ----------------- | --- | --- |
RemoveanLDAPrealmconfiguration
| 198 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
<realm>
[<string>]Realmname.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager ldap list [OPTIONS]
ListconfiguredLDAPrealms
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager ldap show <realm> [OPTIONS]
ShowLDAPrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager ldap sync <realm> [OPTIONS]
SyncagivenLDAPrealm
<realm>
[<string>]AuthenticationdomainID
Optionalparameters:
--dry-run<boolean> (default=false)
Ifset,donotcreate/deleteanything
--enable-new<boolean>
Enablenewlysyncedusersimmediately
--remove-vanished[acl|entry|properties, ...]
A semicolon-separated list of things to remove when they or the user vanishes during user
synchronization. The following values are possible: entry removes the user when not re-
turnedfromthesync;propertiesremovesanypropertiesonexistinguserthatdonotap-
pearinthesource. aclremovesACLswhentheuserisnotreturnedfromthesync.
proxmox-backup-manager ldap update <realm> [OPTIONS]
UpdateanLDAPrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--base-dn<string>
LDAPDomain
A.2. proxmox-backup-manager 199

ProxmoxBackupDocumentation,Release4.2.8‐1
--bind-dn<string>
LDAPDomain
--capath<string>
CA certificate to use for the server. The path can point to either a file, or a directory. If it
points to a file, the PEM-formatted X.509 certificate stored at the path will be added as a
trustedcertificate. Ifthepathpointstoadirectory,thedirectoryreplacesthesystem’sdefault
certificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrustedcertificate.
--comment<string>
Comment.
--default<boolean> (default=false)
Trueifyouwantthistobethedefaultrealmselectedonlogin.
--delete
server2|port|comment|default|verify|mode|bind-dn|password|filter|sync-defaults-options|sync-attributes|user-classes
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--filter<string>
CustomLDAPsearchfilterforusersync
--modeldap|ldap+starttls|ldaps (default=ldap)
LDAPconnectiontype
--password<string>
LDAPbindpassword
--port<integer> (0 - 65535)
Port
--server1<string>
LDAPserveraddress
--server2<string>
FallbackLDAPserveraddress
--sync-attributes[[email=<string>] [,firstname=<string>]
[,lastname=<string>]]
Comma-separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhich
PBS user field. For example, to map the LDAP attribute mail to PBS’s email, write
email=mail.
--sync-defaults-options[[enable-new=<1|0>] [,remove-vanished=<string>]]
syncdefaultsoptions
--user-attr<string>
Usernameattribute. UsedtomapauseridtoLDAPtoanLDAPdn.
--user-classes[<string>, ...]
(default=inetorgperson,posixaccount,person,user)
Comma-separated list of allowed objectClass values for user synchronization. For instance,
if user-classes is set to person,user, then user synchronization will consider all LDAP
entitieswhereobjectClass: personorobjectClass: user.
--verify<boolean> (default=false)
Verifyservercertificate
proxmox-backup-manager network changes
Showpendingconfigurationchanges(diff)
200 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager network create <iface> [OPTIONS]
Createnetworkinterfaceconfiguration.
<iface>
[<string>]Networkinterfacename.
Optionalparameters:
--autostart<boolean>
Autostartinterface.
--bond-primary<string>
Networkinterfacename.
--bond_modebalance-rr|active-backup|balance-xor|broadcast|802.
3ad|balance-tlb|balance-alb
LinuxBondMode
--bond_xmit_hash_policylayer2|layer2+3|layer3+4
BondTransmitHashPolicyforLACP(802.3ad)
--bridge_ports[<string>, ...]
Alistofnetworkdevices,commaseparated.
--bridge_vlan_aware<boolean>
Enablebridgevlansupport.
--cidr<string>
IPv4addresswithnetmask(CIDRnotation).
--cidr6<string>
IPv6addresswithnetmask(CIDRnotation).
--comments<string>
Comments(inet,mayspanmultiplelines)
--comments6<string>
Comments(inet5,mayspanmultiplelines)
--gateway<string>
IPv4address.
--gateway6<string>
IPv6address.
--methodmanual|static|dhcp|loopback|auto
Interfaceconfigurationmethod
--method6manual|static|dhcp|loopback|auto
Interfaceconfigurationmethod
--mtu<integer> (46 - 65535) (default=1500)
MaximumTransmissionUnit.
--slaves[<string>, ...]
Alistofnetworkdevices,commaseparated.
--typeloopback|eth|bridge|bond|vlan|alias|unknown
Networkinterfacetype
--vlan-id<integer>
VLANID.
--vlan-raw-device<string>
Networkinterfacename.
proxmox-backup-manager network list [OPTIONS]
A.2. proxmox-backup-manager 201

ProxmoxBackupDocumentation,Release4.2.8‐1
Networkdevicelist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager network reload
Reloadnetworkchanges
proxmox-backup-manager network remove <iface> [OPTIONS]
Removenetworkinterfaceconfiguration.
<iface>
[<string>]Networkinterfacename.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager network revert
Revertnetworkconfiguration(rm/etc/network/interfaces.new).
proxmox-backup-manager network update <iface> [OPTIONS]
Updatenetworkinterfaceconfig.
<iface>
[<string>]Networkinterfacename.
Optionalparameters:
--autostart<boolean>
Autostartinterface.
--bond-primary<string>
Networkinterfacename.
--bond_modebalance-rr|active-backup|balance-xor|broadcast|802.
3ad|balance-tlb|balance-alb
LinuxBondMode
--bond_xmit_hash_policylayer2|layer2+3|layer3+4
BondTransmitHashPolicyforLACP(802.3ad)
--bridge_ports[<string>, ...]
Alistofnetworkdevices,commaseparated.
--bridge_vlan_aware<boolean>
Enablebridgevlansupport.
--cidr<string>
IPv4addresswithnetmask(CIDRnotation).
--cidr6<string>
IPv6addresswithnetmask(CIDRnotation).
202 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--comments<string>
Comments(inet,mayspanmultiplelines)
--comments6<string>
Comments(inet5,mayspanmultiplelines)
--delete
cidr|cidr6|gateway|gateway6|method|method6|comments|comments6|mtu|autostart|bridge_ports|bridge_vlan_aware|slaves|bond-primary|bond_xmit_hash_policy
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--gateway<string>
IPv4address.
--gateway6<string>
IPv6address.
--methodmanual|static|dhcp|loopback|auto
Interfaceconfigurationmethod
--method6manual|static|dhcp|loopback|auto
Interfaceconfigurationmethod
--mtu<integer> (46 - 65535) (default=1500)
MaximumTransmissionUnit.
--slaves[<string>, ...]
Alistofnetworkdevices,commaseparated.
--typeloopback|eth|bridge|bond|vlan|alias|unknown
Networkinterfacetype
--vlan-id<integer>
VLANID.
--vlan-raw-device<string>
Networkinterfacename.
proxmox-backup-manager node server-identity [OPTIONS]
ReturntheserveridentityinformationforthisProxmoxBackupServer.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager node show [OPTIONS]
Shownodeconfiguration
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager node update [OPTIONS]
Updatethenodeconfiguration
Optionalparameters:
A.2. proxmox-backup-manager 203

ProxmoxBackupDocumentation,Release4.2.8‐1
--acme[account=<string>]
Theacmeaccounttouseonthisnode.
--acmedomain0[domain=<string> [,alias=<string>] [,plugin=<string>]]
ACMEdomainconfigurationstring
--acmedomain1[domain=<string> [,alias=<string>] [,plugin=<string>]]
ACMEdomainconfigurationstring
--acmedomain2[domain=<string> [,alias=<string>] [,plugin=<string>]]
ACMEdomainconfigurationstring
--acmedomain3[domain=<string> [,alias=<string>] [,plugin=<string>]]
ACMEdomainconfigurationstring
--acmedomain4[domain=<string> [,alias=<string>] [,plugin=<string>]]
ACMEdomainconfigurationstring
--ciphers-tls-1.2<string>
OpenSSLcipherlistusedbytheproxyforTLS<=1.2
--ciphers-tls-1.3<string>
OpenSSLciphersuiteslistusedbytheproxyforTLS1.3
--consent-text<string>
Consentbannertext
--default-lang
ar|ca|da|de|en|es|eu|fa|fr|gl|he|hu|it|ja|kr|nb|nl|nn|pl|pt_BR|ru|sl|sv|tr|zh_CN|zh_TW
AllavailablelanguagesinProxmox. Takenfromproxmox-i18nrepository. pt_BR,zh_CN,and
zh_TWusethesamecaseinthetranslationfiles.
--delete
acme|acmedomain0|acmedomain1|acmedomain2|acmedomain3|acmedomain4|http-proxy|email-from|ciphers-tls-1.
3|ciphers-tls-1.
2|default-lang|description|task-log-max-days|consent-text|location
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--description<string>
Comment(multiplelines).
--digest<string>
Digesttoprotectagainstconcurrentupdates
--email-from<string>
E-MailAddress.
--http-proxy[http://]<host>[:port]
HTTPproxyconfiguration[http://]<host>[:port]
--location<string>
ThelocationofthePBSinstance.
--task-log-max-days<integer> (0 - N)
MaximumdaystokeepTasklogs
proxmox-backup-manager notification endpoint gotify create <name> --server
<string> --token <string> [OPTIONS]
Addanewgotifyendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
--server<string>
GotifyServerURL.
204 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--token<string>
Authenticationtoken
Optionalparameters:
--comment<string>
Comment.
--disable<boolean>
Disablethistarget.
--filter<string>
Deprecated.
--originuser-created|builtin|modified-builtin
Theoriginofanotificationconfigurationentry.
proxmox-backup-manager notification endpoint gotify delete <name>
Deletegotifyendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager notification endpoint gotify list [OPTIONS]
Listallendpoints.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint gotify show <name> [OPTIONS]
Showasingleendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint gotify update <name> [OPTIONS]
Updategotifyendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--comment<string>
Comment.
--deletecomment|disable
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
A.2. proxmox-backup-manager 205

ProxmoxBackupDocumentation,Release4.2.8‐1
--disable<boolean>
Disablethistarget.
--server<string>
GotifyServerURL.
--token<string>
Authenticationtoken
proxmox-backup-manager notification endpoint sendmail create <name>
[OPTIONS]
Addanewsendmailendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--author<string>
Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
--comment<string>
Comment.
--disable<boolean>
Disablethistarget.
--filter<string>
Deprecated.
--from-address<string>
From address for sent E-Mails. If the parameter is not set, the plugin will fall back to the
email-from setting from node.cfg (PBS). If that is also not set, the plugin will default to
root@$hostname,where$hostnameisthehostnameofthenode.
--mailto<string>
Mailaddresstosendamailto. Canbespecifiedmorethanonce.
--mailto-user<string>
Userstosendamailto. Theemailaddressoftheuserwillbelookedupinusers.cfg. Canbe
specifiedmorethanonce.
--originuser-created|builtin|modified-builtin
Theoriginofanotificationconfigurationentry.
proxmox-backup-manager notification endpoint sendmail delete <name>
Deletesendmailendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager notification endpoint sendmail list [OPTIONS]
Listallendpoints.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
206 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager notification endpoint sendmail show <name> [OPTIONS]
Showasingleendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint sendmail update <name>
[OPTIONS]
Updatesendmailendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--author<string>
Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
--comment<string>
Comment.
--deleteauthor|comment|disable|from-address|mailto|mailto-user
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean>
Disablethistarget.
--from-address<string>
From address for sent E-Mails. If the parameter is not set, the plugin will fall back to the
email-from setting from node.cfg (PBS). If that is also not set, the plugin will default to
root@$hostname,where$hostnameisthehostnameofthenode.
--mailto<string>
Mailaddresstosendamailto. Canbespecifiedmorethanonce.
--mailto-user<string>
Userstosendamailto. Theemailaddressoftheuserwillbelookedupinusers.cfg. Canbe
specifiedmorethanonce.
proxmox-backup-manager notification endpoint smtp create <name>
--from-address <string> --server <string> [OPTIONS]
Addanewsmtpendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
--from-address<string>
Fromaddressforthemail. SMTPrelaysmightrequirethatthisaddressisownedbytheuserin
ordertoavoidspoofing. TheFromheaderintheemailwillbesetto$author<$from-address>.
A.2. proxmox-backup-manager 207

ProxmoxBackupDocumentation,Release4.2.8‐1
--server<string>
HostnameorIPoftheSMTPrelay.
Optionalparameters:
--author<string>
Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
--comment<string>
Comment.
--disable<boolean>
Disablethistarget.
--mailto<string>
Mailaddresstosendamailto. Canbespecifiedmorethanonce.
--mailto-user<string>
Userstosendamailto. Theemailaddressoftheuserwillbelookedupinusers.cfg. Canbe
specifiedmorethanonce.
--modeinsecure|starttls|tls (default=tls)
Connectionsecurity
--originuser-created|builtin|modified-builtin
Theoriginofanotificationconfigurationentry.
--password<string>
SMTPauthenticationpassword
--port<integer> (0 - 65535)
The port to connect to. If not set, the used port defaults to 25 (insecure), 465 (tls) or 587
(starttls),dependingonthevalueofmode
--username<string>
Usernametouseduringauthentication. Ifnousernameisset,noauthenticationwillbeper-
formed. ThePLAINandLOGINauthenticationmethodsaresupported
proxmox-backup-manager notification endpoint smtp delete <name>
Deletesmtpendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager notification endpoint smtp list [OPTIONS]
Listallendpoints.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint smtp show <name> [OPTIONS]
Showasingleendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
208 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager notification endpoint smtp update <name> [OPTIONS]
Updatesmtpendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--author<string>
Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
--comment<string>
Comment.
--deleteauthor|comment|disable|mailto|mailto-user|password|port|username
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean>
Disablethistarget.
--from-address<string>
Fromaddressforthemail. SMTPrelaysmightrequirethatthisaddressisownedbytheuserin
ordertoavoidspoofing. TheFromheaderintheemailwillbesetto$author<$from-address>.
--mailto<string>
Mailaddresstosendamailto. Canbespecifiedmorethanonce.
--mailto-user<string>
Userstosendamailto. Theemailaddressoftheuserwillbelookedupinusers.cfg. Canbe
specifiedmorethanonce.
--modeinsecure|starttls|tls (default=tls)
Connectionsecurity
--password<string>
SMTPauthenticationpassword
--port<integer> (0 - 65535)
The port to connect to. If not set, the used port defaults to 25 (insecure), 465 (tls) or 587
(starttls),dependingonthevalueofmode
--server<string>
HostnameorIPoftheSMTPrelay.
--username<string>
Usernametouseduringauthentication. Ifnousernameisset,noauthenticationwillbeper-
formed. ThePLAINandLOGINauthenticationmethodsaresupported
proxmox-backup-manager notification endpoint webhook create <name> --method
post|put|get --url <string> [OPTIONS]
Addanewwebhookendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
--methodpost|put|get (default=post)
HTTPMethodtouse.
A.2. proxmox-backup-manager 209

ProxmoxBackupDocumentation,Release4.2.8‐1
--url<string>
HTTP(s)urlwithoptionalport.
Optionalparameters:
--body<string>
TheHTTPbodytosend. Supportstemplating.
--comment<string>
Comment.
--disable<boolean>
Disablethistarget.
--header[name=<string> [,value=<string>]]
Array of HTTP headers. Each entry is a property string with a name and a value. The value
property contains the header in base64 encoding. Supports templating. Can be specified
morethanonce.
--originuser-created|builtin|modified-builtin
Theoriginofanotificationconfigurationentry.
--secret[name=<string> [,value=<string>]]
Array of secrets. Each entry is a property string with a name and an optional value. The
valuepropertycontainsthesecretinbase64encoding. ForanyAPIendpointsreturningthe
endpointconfig,onlythesecretnamebutnotthevaluewillbereturned. Whenupdatingthe
config, alsosendallsecretsthatyouwanttokeep, settingonlythenamebutnotthevalue.
Canbeaccessedfromtemplates. Canbespecifiedmorethanonce.
proxmox-backup-manager notification endpoint webhook delete <name>
Deletewebhookendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager notification endpoint webhook list [OPTIONS]
Listallendpoints.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint webhook show <name> [OPTIONS]
Showasingleendpoint.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification endpoint webhook update <name>
[OPTIONS]
Updatewebhookendpoint.
210 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--body<string>
TheHTTPbodytosend. Supportstemplating.
--comment<string>
Comment.
--deletecomment|disable|header|body|secret
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean>
Disablethistarget.
--header[name=<string> [,value=<string>]]
Array of HTTP headers. Each entry is a property string with a name and a value. The value
property contains the header in base64 encoding. Supports templating. Can be specified
morethanonce.
--methodpost|put|get (default=post)
HTTPMethodtouse.
--secret[name=<string> [,value=<string>]]
Array of secrets. Each entry is a property string with a name and an optional value. The
valuepropertycontainsthesecretinbase64encoding. ForanyAPIendpointsreturningthe
endpointconfig,onlythesecretnamebutnotthevaluewillbereturned. Whenupdatingthe
config, alsosendallsecretsthatyouwanttokeep, settingonlythenamebutnotthevalue.
Canbeaccessedfromtemplates. Canbespecifiedmorethanonce.
--url<string>
HTTP(s)urlwithoptionalport.
proxmox-backup-manager notification matcher create <name> [OPTIONS]
Addanewnotificationmatcher.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--comment<string>
Comment.
--disable<boolean>
Disablethismatcher.
--invert-match<boolean>
Invertmatchofthewholefilter.
--match-calendar<string>
Listofmatchedseveritylevels. Canbespecifiedmorethanonce.
--match-field<string>
Listofmatchedmetadatafields. Canbespecifiedmorethanonce.
--match-severity<string>
Listofmatchedseveritylevels. Canbespecifiedmorethanonce.
A.2. proxmox-backup-manager 211

ProxmoxBackupDocumentation,Release4.2.8‐1
--modeall|any (default=all)
Themodeinwhichtheresultsofmatchesarecombined.
--originuser-created|builtin|modified-builtin
Theoriginofanotificationconfigurationentry.
--target<string>
Targetstonotify. Canbespecifiedmorethanonce.
proxmox-backup-manager notification matcher delete <name>
Deletenotificationmatcher.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager notification matcher list [OPTIONS]
Listnotificationmatchers.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification matcher show <name> [OPTIONS]
Showasinglematcher.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager notification matcher update <name> [OPTIONS]
Updatenotificationmatcher.
<name>
[<string>]Nameschemafortargetsandmatchers
Optionalparameters:
--comment<string>
Comment.
--delete
comment|disable|invert-match|match-calendar|match-field|match-severity|mode|target
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean>
Disablethismatcher.
--invert-match<boolean>
Invertmatchofthewholefilter.
212 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--match-calendar<string>
| Listofmatchedseveritylevels. |     | Canbespecifiedmorethanonce. |     |     |
| ---------------------------- | --- | --------------------------- | --- | --- |
--match-field<string>
| Listofmatchedmetadatafields. |     | Canbespecifiedmorethanonce. |     |     |
| ---------------------------- | --- | --------------------------- | --- | --- |
--match-severity<string>
| Listofmatchedseveritylevels. |               | Canbespecifiedmorethanonce. |     |     |
| ---------------------------- | ------------- | --------------------------- | --- | --- |
| --modeall|any                | (default=all) |                             |     |     |
Themodeinwhichtheresultsofmatchesarecombined.
--target<string>
| Targetstonotify.       | Canbespecifiedmorethanonce. |              |             |           |
| ---------------------- | --------------------------- | ------------ | ----------- | --------- |
| proxmox-backup-manager |                             | notification | target list | [OPTIONS] |
Listtargets.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager |     | notification | target test | <name> |
| ---------------------- | --- | ------------ | ----------- | ------ |
Testagivennotificationtarget.
<name>
[<string>]Nameschemafortargetsandmatchers
proxmox-backup-manager openid create <realm> --client-id <string>
| --issuer-url | <string> | [OPTIONS] |     |     |
| ------------ | -------- | --------- | --- | --- |
CreateanewOpenIdrealm
<realm>
[<string>]Realmname.
--client-id<string>
OpenIDClientID
--issuer-url<string>
OpenIDIssuerUrl
Optionalparameters:
| --acr-values[<string>, |     | ...] |     |     |
| ---------------------- | --- | ---- | --- | --- |
OpenIDACRList
| --audiences[<string>, |     | ...] |     |     |
| --------------------- | --- | ---- | --- | --- |
OpenIDaudiencelist.
| --autocreate<boolean> |     | (default=false) |     |     |
| --------------------- | --- | --------------- | --- | --- |
Automaticallycreateusersiftheydonotexist.
--client-key<string>
OpenIDClientKey
--comment<string>
Comment.
| --default<boolean> |     | (default=false) |     |     |
| ------------------ | --- | --------------- | --- | --- |
Trueifyouwantthistobethedefaultrealmselectedonlogin.
A.2. proxmox-backup-manager 213

ProxmoxBackupDocumentation,Release4.2.8‐1
--prompt<string>
OpenIDPrompt
| --scopes[<string>, | ...] (default=email | profile) |     |     |
| ------------------ | ------------------- | -------- | --- | --- |
OpenIDScopeList
--username-claim<string>
Usethevalueofthisattribute/claimasuniqueusername. Itisuptotheidentityproviderto
guarantee the uniqueness. The OpenID specification only guarantees that Subject (’sub’) is
unique. Alsomakesurethattheuserisnotallowedtochangethatattributebyhimself!
| proxmox-backup-manager | openid delete | <realm> [OPTIONS] |     |     |
| ---------------------- | ------------- | ----------------- | --- | --- |
RemoveaOpenIDrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| proxmox-backup-manager | openid list | [OPTIONS] |     |     |
| ---------------------- | ----------- | --------- | --- | --- |
ListconfiguredOpenIdrealms
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | openid show | <realm> [OPTIONS] |     |     |
| ---------------------- | ----------- | ----------------- | --- | --- |
ShowOpenIDrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | openid update | <realm> [OPTIONS] |     |     |
| ---------------------- | ------------- | ----------------- | --- | --- |
UpdateanOpenIDrealmconfiguration
<realm>
[<string>]Realmname.
Optionalparameters:
| --acr-values[<string>, | ...] |     |     |     |
| ---------------------- | ---- | --- | --- | --- |
OpenIDACRList
| --audiences[<string>, | ...] |     |     |     |
| --------------------- | ---- | --- | --- | --- |
OpenIDaudiencelist.
| --autocreate<boolean> | (default=false) |     |     |     |
| --------------------- | --------------- | --- | --- | --- |
Automaticallycreateusersiftheydonotexist.
| 214 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--client-id<string>
OpenIDClientID
--client-key<string>
OpenIDClientKey
--comment<string>
Comment.
| --default<boolean> | (default=false) |     |
| ------------------ | --------------- | --- |
Trueifyouwantthistobethedefaultrealmselectedonlogin.
--delete
client-key|comment|default|autocreate|scopes|prompt|acr-values|audiences
| Listofpropertiestodelete. | Canbespecifiedmorethanonce. |     |
| ------------------------- | --------------------------- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--issuer-url<string>
OpenIDIssuerUrl
--prompt<string>
OpenIDPrompt
| --scopes[<string>, | ...] (default=email | profile) |
| ------------------ | ------------------- | -------- |
OpenIDScopeList
proxmox-backup-manager prune-job create <id> --schedule <calendar-event>
| --store <string> | [OPTIONS] |     |
| ---------------- | --------- | --- |
Createanewprunejob.
<id>
[<string>]JobID.
--schedule<calendar-event>
Runprunejobatspecifiedschedule.
--store<string>
Datastorename.
Optionalparameters:
--comment<string>
Comment.
| --disable<boolean> | (default=false) |     |
| ------------------ | --------------- | --- |
Disablethisjob.
| --keep-daily<integer> | (1 - N) |     |
| --------------------- | ------- | --- |
Numberofdailybackupstokeep.
| --keep-hourly<integer> | (1 - N) |     |
| ---------------------- | ------- | --- |
Numberofhourlybackupstokeep.
| --keep-last<integer> | (1 - N) |     |
| -------------------- | ------- | --- |
Numberofbackupstokeep.
| --keep-monthly<integer> | (1 - N) |     |
| ----------------------- | ------- | --- |
Numberofmonthlybackupstokeep.
| --keep-weekly<integer> | (1 - N) |     |
| ---------------------- | ------- | --- |
Numberofweeklybackupstokeep.
| --keep-yearly<integer> | (1 - N) |     |
| ---------------------- | ------- | --- |
Numberofyearlybackupstokeep.
A.2. proxmox-backup-manager 215

ProxmoxBackupDocumentation,Release4.2.8‐1
--max-depth<integer> (0 - 7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion, empty==auto-
maticfullrecursion,namespacedepthsreducemaximumallowedvalue)
--ns<string>
Namespace.
proxmox-backup-manager prune-job list [OPTIONS]
Listallprunejobs
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager prune-job remove <id> [OPTIONS]
Removeaprunejobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager prune-job run <id> [OPTIONS]
Runthespecifiedprunejob
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager prune-job show <id> [OPTIONS]
Showprunejobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager prune-job update <id> [OPTIONS]
Updateprunejobconfig.
<id>
[<string>]JobID.
Optionalparameters:
216 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--comment<string>
Comment.
--delete
comment|disable|ns|max-depth|keep-last|keep-hourly|keep-daily|keep-weekly|keep-monthly|keep-yearly
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--disable<boolean> (default=false)
Disablethisjob.
--keep-daily<integer> (1 - N)
Numberofdailybackupstokeep.
--keep-hourly<integer> (1 - N)
Numberofhourlybackupstokeep.
--keep-last<integer> (1 - N)
Numberofbackupstokeep.
--keep-monthly<integer> (1 - N)
Numberofmonthlybackupstokeep.
--keep-weekly<integer> (1 - N)
Numberofweeklybackupstokeep.
--keep-yearly<integer> (1 - N)
Numberofyearlybackupstokeep.
--max-depth<integer> (0 - 7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion, empty==auto-
maticfullrecursion,namespacedepthsreducemaximumallowedvalue)
--ns<string>
Namespace.
--schedule<calendar-event>
Runprunejobatspecifiedschedule.
--store<string>
Datastorename.
proxmox-backup-manager pull <remote> <remote-store> <store> [OPTIONS]
Syncdatastorebypullingfromanotherrepository
<remote>
[<string>]RemoteID.
<remote-store>
[<string>]Datastorename.
<store>
[<string>]Datastorename.
Optionalparameters:
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--encrypted-only<boolean>
Onlysynchronizeencryptedbackupsnapshots,excludeothers.
A.2. proxmox-backup-manager 217

ProxmoxBackupDocumentation,Release4.2.8‐1
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--max-depth<integer> (0 - 7) (default=7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--remote-ns<string>
Namespace.
--remove-vanished<boolean> (default=false)
Deletevanishedbackups. Thisremovesthelocalcopyiftheremotebackupwasdeleted.
--resync-corrupt<boolean>
Iftheverificationfailedforalocalsnapshot,trytopullitagain.
--transfer-last<integer> (1 - N)
LimittransfertolastNsnapshots(pergroup),skippingothers
--verified-only<boolean>
Onlysynchronizeverifiedbackupsnapshots,excludeothers.
proxmox-backup-manager push <store> <remote> <remote-store> [OPTIONS]
Syncdatastorebypushingtoanotherrepository
<store>
[<string>]Datastorename.
<remote>
[<string>]RemoteID.
<remote-store>
[<string>]Datastorename.
Optionalparameters:
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--encrypted-only<boolean>
Onlysynchronizeencryptedbackupsnapshots,excludeothers.
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--max-depth<integer> (0 - 7) (default=7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--ns<string>
Namespace.
218 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--remote-ns<string>
Namespace.
--remove-vanished<boolean> (default=false)
Deletevanishedbackups. Thisremovesthelocalcopyiftheremotebackupwasdeleted.
--transfer-last<integer> (1 - N)
LimittransfertolastNsnapshots(pergroup),skippingothers
--verified-only<boolean>
Onlysynchronizeverifiedbackupsnapshots,excludeothers.
proxmox-backup-manager remote create <name> --auth-id <string> --host
<string> --password <string> [OPTIONS]
Createnewremote.
<name>
[<string>]RemoteID.
--auth-id<string>
AuthenticationID
--host<string>
DNSnameorIPaddress.
--password<string>
Passwordorauthtokenforremotehost.
Optionalparameters:
--comment<string>
Comment.
--fingerprint<string>
X509certificatefingerprint(sha256).
--port<integer>
The(optional)port
--use-node-proxy<boolean> (default=false)
Usethehttpproxyconfigurationofthenodeforremoteconnections.
proxmox-backup-manager remote list [OPTIONS]
Listconfiguredremotes.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager remote remove <name> [OPTIONS]
Removearemotefromtheconfigurationfile.
A.2. proxmox-backup-manager 219

ProxmoxBackupDocumentation,Release4.2.8‐1
<name>
[<string>]RemoteID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager remote show <name> [OPTIONS]
Showremoteconfiguration
<name>
[<string>]RemoteID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager remote update <name> [OPTIONS]
Updateremoteconfiguration.
<name>
[<string>]RemoteID.
Optionalparameters:
--auth-id<string>
AuthenticationID
--comment<string>
Comment.
--deletecomment|fingerprint|port|use-node-proxy
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--fingerprint<string>
X509certificatefingerprint(sha256).
--host<string>
DNSnameorIPaddress.
--password<string>
Passwordorauthtokenforremotehost.
--port<integer>
The(optional)port
--use-node-proxy<boolean> (default=false)
Usethehttpproxyconfigurationofthenodeforremoteconnections.
proxmox-backup-manager report
Systemreport
proxmox-backup-manager s3 check <s3-endpoint-id> <bucket> [OPTIONS]
PerformbasicsanitychecksforgivenS3clientconfiguration
220 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
<s3-endpoint-id>
[<string>]IDtouniquelyidentifys3clientconfig.
<bucket>
[<string>]BucketnameforS3objectstore.
Optionalparameters:
--store-prefix<string>
StoreprefixwithinbucketforS3objectkeys(commonlydatastorename)
proxmox-backup-manager s3 endpoint create <id> --access-key <string>
--endpoint <string> --secret-key <string> [OPTIONS]
Createanews3clientconfiguration.
<id>
[<string>]IDtouniquelyidentifys3clientconfig.
--access-key<string>
AccesskeyforS3objectstore.
--endpoint<string>
EndpointtoaccessS3objectstore.
--secret-key<string>
S3secretkey
Optionalparameters:
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--fingerprint<string>
X509certificatefingerprint(sha256).
--limit-active-requests<integer> (0 - N)
CombinedratelimitforPUT,POSTandDELETErequestsgivenas#request/s.
--limit-passive-requests<integer> (0 - N)
CombinedratelimitforGETandHEADrequestsgivenas#request/s.
--path-style<boolean> (default=false)
Usepathstylebucketaddressingovervhoststyle.
--port<integer>
PorttoaccessS3objectstore.
--provider-quirks
skip-if-none-match-header|delete-objects-via-delete-object
Listofproviderspecificfeatureimplementationquirks. Canbespecifiedmorethanonce.
--put-rate-limit<integer>
Rate limit for put requests given as #request/s (deprecated: use limit-active- requests in-
stead).
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--region<string>
RegiontoaccessS3objectstore.
A.2. proxmox-backup-manager 221

ProxmoxBackupDocumentation,Release4.2.8‐1
--use-node-proxy<boolean> (default=false)
Usenodeproxyforclientconnections
proxmox-backup-manager s3 endpoint list [OPTIONS]
Listconfigureds3clients.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager s3 endpoint list-buckets <s3-endpoint-id>
ListbucketsaccessiblebythegivenS3clientconfiguration
<s3-endpoint-id>
[<string>]IDtouniquelyidentifys3clientconfig.
proxmox-backup-manager s3 endpoint remove <id> [OPTIONS]
Removeans3clientconfiguration.
<id>
[<string>]JobID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager s3 endpoint reset-counters <s3-endpoint-id> <bucket>
[OPTIONS]
ResettheS3requestcountersformatchingendpoint,bucketordatastore(ifprefixisgiven).
<s3-endpoint-id>
[<string>]IDtouniquelyidentifys3clientconfig.
<bucket>
[<string>]BucketnameforS3objectstore.
Optionalparameters:
--store-prefix<string>
StoreprefixwithinbucketforS3objectkeys(commonlydatastorename)
proxmox-backup-manager s3 endpoint update <id> [OPTIONS]
Updateans3clientconfiguration.
<id>
[<string>]JobID.
Optionalparameters:
--access-key<string>
AccesskeyforS3objectstore.
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
222 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--delete
port|region|fingerprint|path-style|rate-in|burst-in|rate-out|burst-out|limit-active-requests|limit-passive-requests|provider-quirks|use-node-proxy
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--endpoint<string>
EndpointtoaccessS3objectstore.
--fingerprint<string>
X509certificatefingerprint(sha256).
--limit-active-requests<integer> (0 - N)
CombinedratelimitforPUT,POSTandDELETErequestsgivenas#request/s.
--limit-passive-requests<integer> (0 - N)
CombinedratelimitforGETandHEADrequestsgivenas#request/s.
--path-style<boolean> (default=false)
Usepathstylebucketaddressingovervhoststyle.
--port<integer>
PorttoaccessS3objectstore.
--provider-quirks
skip-if-none-match-header|delete-objects-via-delete-object
Listofproviderspecificfeatureimplementationquirks. Canbespecifiedmorethanonce.
--put-rate-limit<integer>
Rate limit for put requests given as #request/s (deprecated: use limit-active- requests in-
stead).
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--region<string>
RegiontoaccessS3objectstore.
--secret-key<string>
S3clientsecretkey.
--use-node-proxy<boolean> (default=false)
Usenodeproxyforclientconnections
proxmox-backup-manager subscription get [OPTIONS]
Readsubscriptioninfo.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager subscription remove
Deletesubscriptioninfo.
A.2. proxmox-backup-manager 223

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager subscription set <key>
Setasubscriptionkeyandcheckit.
<key>
[<string>]Thesubscriptionkeytoinstall.
proxmox-backup-manager subscription set-offline-key <data>
(Internaluseonly!) Setasignedsubscriptioninfoblobasofflinekey
<data>
[<string>]base64-encodedsignedsubscriptioninfo
proxmox-backup-manager subscription update [OPTIONS]
Checkandupdatesubscriptionstatus.
Optionalparameters:
--force<boolean> (default=false)
Alwaysconnecttoserver,evenifinformationincacheisuptodate.
proxmox-backup-manager sync-job create <id> --remote-store <string> --store
<string> [OPTIONS]
Createanewsyncjob.
<id>
[<string>]JobID.
--remote-store<string>
Datastorename.
--store<string>
Datastorename.
Optionalparameters:
--active-encryption-key<string>
IDtouniquelyidentifyencryption/decriptionkey
--associated-key<string>
Listofcryptographickeysassociatedwithsyncjob. Canbespecifiedmorethanonce.
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--comment<string>
Comment.
--encrypted-only<boolean>
Onlysynchronizeencryptedbackupsnapshots,excludeothers.
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--max-depth<integer> (0 - 7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion, empty==auto-
maticfullrecursion,namespacedepthsreducemaximumallowedvalue)
224 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--ns<string>
Namespace.
--owner<string>
AuthenticationID
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--remote<string>
RemoteID.
--remote-ns<string>
Namespace.
--remove-vanished<boolean> (default=false)
Deletevanishedbackups. Thisremovesthelocalcopyiftheremotebackupwasdeleted.
--resync-corrupt<boolean>
Iftheverificationfailedforalocalsnapshot,trytopullitagain.
--run-on-mount<boolean>
Runthisjobwhenarelevantdatastoreismounted.
--schedule<calendar-event>
Runsyncjobatspecifiedschedule.
--sync-directionpull|push (default=pull)
Directionofthesyncjob,pushorpull
--transfer-last<integer> (1 - N)
LimittransfertolastNsnapshots(pergroup),skippingothers
--unmount-on-done<boolean>
Unmountinvolvedremovabledatastoreafterthesyncjobfinishes. Requires’run-on-mount’
tobeenabled.
--verified-only<boolean>
Onlysynchronizeverifiedbackupsnapshots,excludeothers.
--worker-threads<integer> (1 - 32) (default=1)
Thenumberofworkerthreadstoprocessgroupsinparallel.
proxmox-backup-manager sync-job list [OPTIONS]
Syncjoblist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
--sync-directionall|push|pull (default=pull)
Thedirectionofthelistedsyncjobs: push,pullorall.
proxmox-backup-manager sync-job remove <id> [OPTIONS]
Removeasyncjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
A.2. proxmox-backup-manager 225

ProxmoxBackupDocumentation,Release4.2.8‐1
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager sync-job run <id> [OPTIONS]
Runthespecifiedsyncjob
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager sync-job show <id> [OPTIONS]
Showsyncjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager sync-job update <id> [OPTIONS]
Updatesyncjobconfig.
<id>
[<string>]JobID.
Optionalparameters:
--active-encryption-key<string>
IDtouniquelyidentifyencryption/decriptionkey
--associated-key<string>
Listofcryptographickeysassociatedwithsyncjob. Canbespecifiedmorethanonce.
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--comment<string>
Comment.
--delete
remote|owner|comment|schedule|remove-vanished|group-filter|rate-in|burst-in|rate-out|burst-out|ns|remote-ns|max-depth|transfer-last|encrypted-only|verified-only|run-on-mount|unmount-on-done|sync-direction|worker-threads|active-encryption-key|associated-key
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--encrypted-only<boolean>
Onlysynchronizeencryptedbackupsnapshots,excludeothers.
226 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--max-depth<integer> (0 - 7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion, empty==auto-
maticfullrecursion,namespacedepthsreducemaximumallowedvalue)
--ns<string>
Namespace.
--owner<string>
AuthenticationID
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--remote<string>
RemoteID.
--remote-ns<string>
Namespace.
--remote-store<string>
Datastorename.
--remove-vanished<boolean> (default=false)
Deletevanishedbackups. Thisremovesthelocalcopyiftheremotebackupwasdeleted.
--resync-corrupt<boolean>
Iftheverificationfailedforalocalsnapshot,trytopullitagain.
--run-on-mount<boolean>
Runthisjobwhenarelevantdatastoreismounted.
--schedule<calendar-event>
Runsyncjobatspecifiedschedule.
--store<string>
Datastorename.
--sync-directionpull|push (default=pull)
Directionofthesyncjob,pushorpull
--transfer-last<integer> (1 - N)
LimittransfertolastNsnapshots(pergroup),skippingothers
--unmount-on-done<boolean>
Unmountinvolvedremovabledatastoreafterthesyncjobfinishes. Requires’run-on-mount’
tobeenabled.
--verified-only<boolean>
Onlysynchronizeverifiedbackupsnapshots,excludeothers.
--worker-threads<integer> (1 - 32) (default=1)
Thenumberofworkerthreadstoprocessgroupsinparallel.
proxmox-backup-manager task list [OPTIONS]
Listrunningservertasks.
Optionalparameters:
--all<boolean>
Alsoliststoppedtasks.
A.2. proxmox-backup-manager 227

ProxmoxBackupDocumentation,Release4.2.8‐1
--limit<integer> (1 - 1000) (default=50)
Themaximalnumberoftaskstolist.
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager task log <upid>
Displaythetasklog.
<upid>
[<string>]UniqueProcess/TaskIdentifier
proxmox-backup-manager task stop <upid>
Trytostopaspecifictask.
<upid>
[<string>]UniqueProcess/TaskIdentifier
proxmox-backup-manager traffic-control create <name> --network <string>
[OPTIONS]
Createnewtrafficcontrolrule.
<name>
[<string>]RuleID.
--network<string>
RuleappliestoSourceIPswithinthisnetworksCanbespecifiedmorethanonce.
Optionalparameters:
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--comment<string>
Comment.
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--timeframe<string>
EnabletheruleatspecifictimesCanbespecifiedmorethanonce.
--users<string>
RuleappliestoauthenticatedAPIrequestsofanyoftheseusers(overridesIP-onlyrules)Can
bespecifiedmorethanonce.
proxmox-backup-manager traffic-control list [OPTIONS]
Listconfiguredtrafficcontrolrules.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
228 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-backup-manager traffic-control remove <name> [OPTIONS]
Removeatrafficcontrolrulefromtheconfigurationfile.
<name>
[<string>]RuleID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager traffic-control show <name> [OPTIONS]
Showtrafficcontrolconfiguration
<name>
[<string>]RuleID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager traffic-control traffic [OPTIONS]
Showcurrenttrafficforallrules.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager traffic-control update <name> [OPTIONS]
Updatetrafficcontrolconfiguration.
<name>
[<string>]RuleID.
Optionalparameters:
--burst-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--burst-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--comment<string>
Comment.
--deleterate-in|burst-in|rate-out|burst-out|comment|timeframe|users
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--network<string>
RuleappliestoSourceIPswithinthisnetworksCanbespecifiedmorethanonce.
A.2. proxmox-backup-manager 229

ProxmoxBackupDocumentation,Release4.2.8‐1
--rate-in<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--rate-out<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
--timeframe<string>
EnabletheruleatspecifictimesCanbespecifiedmorethanonce.
--users<string>
RuleappliestoauthenticatedAPIrequestsofanyoftheseusers(overridesIP-onlyrules)Can
bespecifiedmorethanonce.
proxmox-backup-manager user create <userid> [OPTIONS]
Createnewuser.
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
--password<string>
UserPassword.
proxmox-backup-manager user delete-token <userid> <token-name> [OPTIONS]
Deleteauser’sAPItoken
<userid>
[<string>]UserID
<token-name>
[<string>]ThetokenIDpartofanAPItokenauthenticationid.
ThisalonedoesNOTuniquelyidentifytheAPItoken-useafullAuthidforsuchusecases.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager user generate-token <userid> <token-name> [OPTIONS]
GenerateanewAPItokenwithgivenmetadata
230 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
<userid>
[<string>]UserID
<token-name>
[<string>]ThetokenIDpartofanAPItokenauthenticationid.
ThisalonedoesNOTuniquelyidentifytheAPItoken-useafullAuthidforsuchusecases.
Optionalparameters:
--comment<string>
Comment.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--enable<boolean> (default=true)
Enabletheaccount(default). Youcansetthisto’0’todisabletheaccount.
--expire<integer> (0 - N) (default=0)
Accountexpirationdate(secondssinceepoch). ’0’meansnoexpirationdate.
proxmox-backup-manager user list [OPTIONS]
Listconfiguredusers.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager user list-tokens <userid> [OPTIONS]
Listtokensassociatedwithuser.
<userid>
[<string>]UserID
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager user permissions <auth-id> [OPTIONS]
Listpermissionsofuser/token.
<auth-id>
[<string>]AuthenticationID
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
--path<string>
Accesscontrolpath.
proxmox-backup-manager user remove <userid> [OPTIONS]
Removeauserfromtheconfigurationfile.
A.2. proxmox-backup-manager 231

ProxmoxBackupDocumentation,Release4.2.8‐1
<userid>
[<string>]UserID
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-backup-manager user tfa delete <userid> <id> [OPTIONS]
DeleteasingleTFAentry.
<userid>
[<string>]UserID
<id>
[<string>]thetfaentryid
Optionalparameters:
--password<string>
Password.
proxmox-backup-manager user tfa list <userid> [OPTIONS]
Listalltfamethodsforauser.
<userid>
[<string>]UserID
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-manager user tfa unlock <userid>
Unlockauser’sTFAauthentication.
<userid>
[<string>]UserID
proxmox-backup-manager user update <userid> [OPTIONS]
Updateuserconfiguration. Tochangeauser’spasswordusethe’PUT/access/password’endpoint.
<userid>
[<string>]UserID
Optionalparameters:
--comment<string>
Comment.
--deletecomment|firstname|lastname|email
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--email<string>
E-MailAddress.
232 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
| --enable<boolean> (default=true) |     |     |
| -------------------------------- | --- | --- |
Enabletheaccount(default). Youcansetthisto’0’todisabletheaccount.
| --expire<integer> (0 | - N) (default=0) |     |
| -------------------- | ---------------- | --- |
Accountexpirationdate(secondssinceepoch). ’0’meansnoexpirationdate.
--firstname<string>
Firstname.
--lastname<string>
Lastname.
--password<string>
Thisparameterisignored,pleaseuse’PUT/access/password’tochangeauser’spassword
| proxmox-backup-manager | verify <store> | [OPTIONS] |
| ---------------------- | -------------- | --------- |
Verifybackups
<store>
[<string>]Datastorename.
Optionalparameters:
| --ignore-verified<boolean> | (default=true) |     |
| -------------------------- | -------------- | --- |
Donotverifybackupsthatarealreadyverifiediftheirverificationisnotoutdated.
| --outdated-after<integer> | (0 - | N)  |
| ------------------------- | ---- | --- |
Daysafterthataverificationbecomesoutdated. (0isdeprecated)’
--output-formattext|json|json-pretty
Outputformat.
| --read-threads<integer> | (1 - 32) | (default=1) |
| ----------------------- | -------- | ----------- |
Thenumberofthreadstouseforreadingchunksinverifyjob.
| --verify-threads<integer> | (1 - | 32) (default=4) |
| ------------------------- | ---- | --------------- |
Thenumberofthreadstouseforverifyingchunksinverifyjob.
proxmox-backup-manager verify-job create <id> --store <string> [OPTIONS]
Createanewverificationjob.
<id>
[<string>]JobID.
--store<string>
Datastorename.
Optionalparameters:
--comment<string>
Comment.
| --ignore-verified<boolean> | (default=true) |     |
| -------------------------- | -------------- | --- |
Donotverifybackupsthatarealreadyverifiediftheirverificationisnotoutdated.
| --max-depth<integer> | (0 - 7) (default=7) |     |
| -------------------- | ------------------- | --- |
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--ns<string>
Namespace.
| --outdated-after<integer> | (0 - | N)  |
| ------------------------- | ---- | --- |
Daysafterthataverificationbecomesoutdated. (0isdeprecated)’
A.2. proxmox-backup-manager 233

ProxmoxBackupDocumentation,Release4.2.8‐1
| --read-threads<integer> | (1 - 32) | (default=1) |     |     |     |
| ----------------------- | -------- | ----------- | --- | --- | --- |
Thenumberofthreadstouseforreadingchunksinverifyjob.
--schedule<calendar-event>
Runverifyjobatspecifiedschedule.
| --verify-threads<integer> | (1 - | 32) (default=4) |     |     |     |
| ------------------------- | ---- | --------------- | --- | --- | --- |
Thenumberofthreadstouseforverifyingchunksinverifyjob.
| proxmox-backup-manager | verify-job | list [OPTIONS] |     |     |     |
| ---------------------- | ---------- | -------------- | --- | --- | --- |
Listallverificationjobs
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | verify-job | remove | <id> [OPTIONS] |     |     |
| ---------------------- | ---------- | ------ | -------------- | --- | --- |
Removeaverificationjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| proxmox-backup-manager | verify-job | run <id> | [OPTIONS] |     |     |
| ---------------------- | ---------- | -------- | --------- | --- | --- |
Runthespecifiedverificationjob
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | verify-job | show <id> | [OPTIONS] |     |     |
| ---------------------- | ---------- | --------- | --------- | --- | --- |
Showverificationjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-backup-manager | verify-job | update | <id> [OPTIONS] |     |     |
| ---------------------- | ---------- | ------ | -------------- | --- | --- |
Updateverificationjobconfig.
<id>
[<string>]JobID.
| 234 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
Optionalparameters:
--comment<string>
Comment.
--delete
ignore-verified|comment|schedule|outdated-after|ns|max-depth|read-threads|verify-threads
| Listofpropertiestodelete. |     |     | Canbespecifiedmorethanonce. |     |
| ------------------------- | --- | --- | --------------------------- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| --ignore-verified<boolean> |     |     | (default=true) |     |
| -------------------------- | --- | --- | -------------- | --- |
Donotverifybackupsthatarealreadyverifiediftheirverificationisnotoutdated.
| --max-depth<integer> |     | (0 - | 7) (default=7) |     |
| -------------------- | --- | ---- | -------------- | --- |
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--ns<string>
Namespace.
| --outdated-after<integer> |     |     | (0 - | N)  |
| ------------------------- | --- | --- | ---- | --- |
Daysafterthataverificationbecomesoutdated. (0isdeprecated)’
| --read-threads<integer> |     | (1  | - 32) | (default=1) |
| ----------------------- | --- | --- | ----- | ----------- |
Thenumberofthreadstouseforreadingchunksinverifyjob.
--schedule<calendar-event>
Runverifyjobatspecifiedschedule.
--store<string>
Datastorename.
| --verify-threads<integer> |     |     | (1 - | 32) (default=4) |
| ------------------------- | --- | --- | ---- | --------------- |
Thenumberofthreadstouseforverifyingchunksinverifyjob.
| proxmox-backup-manager |     | versions |     | [OPTIONS] |
| ---------------------- | --- | -------- | --- | --------- |
ListpackageversionsforimportantProxmoxBackupServerpackages.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| --verbose<boolean> | (default=false) |     |     |     |
| ------------------ | --------------- | --- | --- | --- |
Outputverbosepackageinformation. Itisignoredifoutput-formatisspecified.
A.3 proxmox-tape
| proxmox-tape | backup | <store> | <pool> | [OPTIONS] |
| ------------ | ------ | ------- | ------ | --------- |
Backupdatastoretotapemediapool
<store>
[<string>]Datastorename.
<pool>
[<string>]Mediapoolname.
Optionalparameters:
--drive<string>
DriveIdentifier.
A.3. proxmox-tape 235

ProxmoxBackupDocumentation,Release4.2.8‐1
--eject-media<boolean>
Ejectmediauponjobcompletion.
--export-media-set<boolean>
Exportmediasetuponjobcompletion.
--force-media-set<boolean> (default=false)
Ignoretheallocationpolicyandstartanewmedia-set.
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--latest-only<boolean>
Backuplatestsnapshotsonly.
--max-depth<integer> (0 - 7) (default=7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--notify-user<string>
UserID
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape backup-job create <id> --drive <string> --pool <string>
--store <string> [OPTIONS]
Createanewtapebackupjob.
<id>
[<string>]JobID.
--drive<string>
DriveIdentifier.
--pool<string>
Mediapoolname.
--store<string>
Datastorename.
Optionalparameters:
--comment<string>
Comment.
--eject-media<boolean>
Ejectmediauponjobcompletion.
--export-media-set<boolean>
Exportmediasetuponjobcompletion.
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--latest-only<boolean>
Backuplatestsnapshotsonly.
--max-depth<integer> (0 - 7) (default=7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
236 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--notification-modelegacy-sendmail|notification-system
(default=notification-system)
Configure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
--notify-user<string>
UserID
--ns<string>
Namespace.
--schedule<calendar-event>
Runsyncjobatspecifiedschedule.
--worker-threads<integer> (1 - 32) (default=1)
Thenumberofthreadstouseforthetapebackupjob.
proxmox-tape backup-job list [OPTIONS]
Tapebackupjoblist.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape backup-job remove <id> [OPTIONS]
Removeatapebackupjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-tape backup-job run <id>
RunTHapeBackupJob
<id>
[<string>]JobID.
proxmox-tape backup-job show <id> [OPTIONS]
Showtapebackupjobconfiguration
<id>
[<string>]JobID.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape backup-job update <id> [OPTIONS]
Updatethetapebackupjob
A.3. proxmox-tape 237

ProxmoxBackupDocumentation,Release4.2.8‐1
<id>
[<string>]JobID.
Optionalparameters:
--comment<string>
Comment.
--delete
comment|schedule|eject-media|export-media-set|latest-only|notify-user|notification-mode|group-filter|max-depth|ns|worker-threads
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--drive<string>
DriveIdentifier.
--eject-media<boolean>
Ejectmediauponjobcompletion.
--export-media-set<boolean>
Exportmediasetuponjobcompletion.
--group-filter
[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>
Listofgroupfilters. Canbespecifiedmorethanonce.
--latest-only<boolean>
Backuplatestsnapshotsonly.
--max-depth<integer> (0 - 7) (default=7)
Howmanylevelsofnamespacesshouldbeoperatedon(0==norecursion)
--notification-modelegacy-sendmail|notification-system
(default=notification-system)
Configure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
--notify-user<string>
UserID
--ns<string>
Namespace.
--pool<string>
Mediapoolname.
--schedule<calendar-event>
Runsyncjobatspecifiedschedule.
--store<string>
Datastorename.
--worker-threads<integer> (1 - 32) (default=1)
Thenumberofthreadstouseforthetapebackupjob.
proxmox-tape barcode-label [OPTIONS]
Labelmediawithbarcodesfromchangerdevice
Optionalparameters:
--drive<string>
DriveIdentifier.
238 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|json|json-pretty
Outputformat.
--pool<string>
Mediapoolname.
proxmox-tape cartridge-memory [OPTIONS]
ReadCartridgeMemory(Mediumauxiliarymemoryattributes)
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape catalog [OPTIONS]
Scanmediaandrecordcontent
Optionalparameters:
--drive<string>
DriveIdentifier.
--force<boolean>
Forceoverridingexistingindex.
--output-formattext|json|json-pretty
Outputformat.
--scan<boolean>
Re-readthewholetapetoreconstructthecataloginsteadofrestoringsavedversions.
--verbose<boolean>
Verbosemode-logallfoundchunks.
proxmox-tape changer config <name> [OPTIONS]
Gettapechangerconfiguration
<name>
[<string>]TapeChangerIdentifier.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape changer create <name> --path <string> [OPTIONS]
Createanewchangerdevice
<name>
[<string>]TapeChangerIdentifier.
--path<string>
PathtoLinuxgenericSCSIdevice(e.g. ’/dev/sg4’)
Optionalparameters:
A.3. proxmox-tape 239

ProxmoxBackupDocumentation,Release4.2.8‐1
| --eject-before-unload<boolean> |     | (default=false) |     |     |     |
| ------------------------------ | --- | --------------- | --- | --- | --- |
ifsettotrue,tapesareejectedmanuallybeforeunloading
| --export-slots[<integer>, |     | ...] |     |     |     |
| ------------------------- | --- | ---- | --- | --- | --- |
Alistofslotnumbers,commaseparated. ThoseslotsarereservedforImport/Export,i.e. any
mediainthoseslotsareconsideredtobe’offline’.
| proxmox-tape | changer list | [OPTIONS] |     |     |     |
| ------------ | ------------ | --------- | --- | --- | --- |
Listchangers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | changer remove | <name> |     |     |     |
| ------------ | -------------- | ------ | --- | --- | --- |
Deleteatapechangerconfiguration
<name>
[<string>]TapeChangerIdentifier.
| proxmox-tape | changer scan | [OPTIONS] |     |     |     |
| ------------ | ------------ | --------- | --- | --- | --- |
ScanforSCSItapechangers
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | changer status | [<name>] | [OPTIONS] |     |     |
| ------------ | -------------- | -------- | --------- | --- | --- |
Gettapechangerstatus
<name>
[<string>]TapeChangerIdentifier.
Optionalparameters:
| --cache<boolean> | (default=true) |     |     |     |     |
| ---------------- | -------------- | --- | --- | --- | --- |
Usecachedvalue.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape changer transfer [<name>] --from <integer> (1 - N) --to
| <integer> | (1 - N) |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
Transfersmediafromoneslottoanother
<name>
[<string>]TapeChangerIdentifier.
| --from<integer> | (1 - N) |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- |
Sourceslotnumber
| --to<integer> | (1 - N) |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
Destinationslotnumber
| 240 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
| proxmox-tape | changer update | <name> [OPTIONS] |     |     |
| ------------ | -------------- | ---------------- | --- | --- |
Updateatapechangerconfiguration
<name>
[<string>]TapeChangerIdentifier.
Optionalparameters:
--deleteexport-slots|eject-before-unload
| Listofpropertiestodelete. |     | Canbespecifiedmorethanonce. |     |     |
| ------------------------- | --- | --------------------------- | --- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
| --eject-before-unload<boolean> |     | (default=false) |     |     |
| ------------------------------ | --- | --------------- | --- | --- |
ifsettotrue,tapesareejectedmanuallybeforeunloading
| --export-slots[<integer>, |     | ...] |     |     |
| ------------------------- | --- | ---- | --- | --- |
Alistofslotnumbers,commaseparated. ThoseslotsarereservedforImport/Export,i.e. any
mediainthoseslotsareconsideredtobe’offline’.
--path<string>
| PathtoLinuxgenericSCSIdevice(e.g. |                 | ’/dev/sg4’) |     |     |
| --------------------------------- | --------------- | ----------- | --- | --- |
| proxmox-tape                      | clean [OPTIONS] |             |     |     |
Cleandrive
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | drive config | <name> [OPTIONS] |     |     |
| ------------ | ------------ | ---------------- | --- | --- |
Getpoolconfiguration
<name>
[<string>]DriveIdentifier.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | drive create | <name> --path | <string> | [OPTIONS] |
| ------------ | ------------ | ------------- | -------- | --------- |
Createanewdrive
<name>
[<string>]DriveIdentifier.
--path<string>
| ThepathtoaLTOSCSI-generictapedevice(i.e. |     |     | ’/dev/sg0’) |     |
| ---------------------------------------- | --- | --- | ----------- | --- |
Optionalparameters:
A.3. proxmox-tape 241

ProxmoxBackupDocumentation,Release4.2.8‐1
--changer<string>
TapeChangerIdentifier.
| --changer-drivenum<integer> |     | (0 - 255) | (default=0) |     |     |
| --------------------------- | --- | --------- | ----------- | --- | --- |
Associatedchangerdrivenumber(requiresoptionchanger)
| proxmox-tape | drive list | [OPTIONS] |     |     |     |
| ------------ | ---------- | --------- | --- | --- | --- |
Listdrives
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | drive remove | <name> |     |     |     |
| ------------ | ------------ | ------ | --- | --- | --- |
Deleteadriveconfiguration
<name>
[<string>]DriveIdentifier.
| proxmox-tape | drive scan | [OPTIONS] |     |     |     |
| ------------ | ---------- | --------- | --- | --- | --- |
Scanfordrives
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | drive update | <name> [OPTIONS] |     |     |     |
| ------------ | ------------ | ---------------- | --- | --- | --- |
Updateadriveconfiguration
<name>
[<string>]DriveIdentifier.
Optionalparameters:
--changer<string>
TapeChangerIdentifier.
| --changer-drivenum<integer> |     | (0 - 255) | (default=0) |     |     |
| --------------------------- | --- | --------- | ----------- | --- | --- |
Associatedchangerdrivenumber(requiresoptionchanger)
--deletechanger|changer-drivenum
| Listofpropertiestodelete. |     | Canbespecifiedmorethanonce. |     |     |     |
| ------------------------- | --- | --------------------------- | --- | --- | --- |
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
--path<string>
| ThepathtoaLTOSCSI-generictapedevice(i.e. |                 |     | ’/dev/sg0’) |     |     |
| ---------------------------------------- | --------------- | --- | ----------- | --- | --- |
| proxmox-tape                             | eject [OPTIONS] |     |             |     |     |
Eject/Unloaddrivemedia
Optionalparameters:
| 242 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape eod [OPTIONS]
Movetoendofmedia(MTEOM,usedtodebug)
Optionalparameters:
--drive<string>
DriveIdentifier.
proxmox-tape export-media <label-text> [OPTIONS]
Exportmediawithspecifiedlabel
<label-text>
[<string>]MediaLabel/Barcode.
Optionalparameters:
--drive<string>
DriveIdentifier.
proxmox-tape format [OPTIONS]
Formatmedia
Optionalparameters:
--drive<string>
DriveIdentifier.
--fast<boolean> (default=true)
Usefasterase.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-tape inventory [OPTIONS]
List(andupdate)medialabels(ChangerInventory)
Optionalparameters:
A.3. proxmox-tape 243

ProxmoxBackupDocumentation,Release4.2.8‐1
| --catalog<boolean> |     | (default=false) |     |     |     |
| ------------------ | --- | --------------- | --- | --- | --- |
Trytorestorecatalogsfromtapes.
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
| --read-all-labels<boolean> |     | (default=false) |     |     |     |
| -------------------------- | --- | --------------- | --- | --- | --- |
Loadalltapesandtryreadlabels(evenifalreadyinventoried)
| --read-labels<boolean> |     | (default=false) |     |     |     |
| ---------------------- | --- | --------------- | --- | --- | --- |
Loadunknowntapesandtryreadlabels
proxmox-tape key change-passphrase <fingerprint> --hint <string> [OPTIONS]
Changetheencryptionkey’spassword.
<fingerprint>
[<string>]Tapeencryptionkeyfingerprint(sha256).
--hint<string>
Passwordhint.
Optionalparameters:
| --force<boolean> | (default=false) |     |     |     |     |
| ---------------- | --------------- | --- | --- | --- | --- |
Resetthepassphraseforatapekey,withoutaskingfortheoldone.
| --kdfnone|scrypt|pbkdf2 |     | (default=scrypt) |     |     |     |
| ----------------------- | --- | ---------------- | --- | --- | --- |
Keyderivationfunctionforpasswordprotectedencryptionkeys.
| proxmox-tape | key create | --hint <string> | [OPTIONS] |     |     |
| ------------ | ---------- | --------------- | --------- | --- | --- |
Createkey(readpasswordfromstdin)
--hint<string>
Passwordrestorehint.
Optionalparameters:
| --kdfnone|scrypt|pbkdf2 |     | (default=scrypt) |     |     |     |
| ----------------------- | --- | ---------------- | --- | --- | --- |
Keyderivationfunctionforpasswordprotectedencryptionkeys.
| proxmox-tape | key list | [OPTIONS] |     |     |     |
| ------------ | -------- | --------- | --- | --- | --- |
Listkeys
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
| proxmox-tape | key paperkey | <fingerprint> | [OPTIONS] |     |     |
| ------------ | ------------ | ------------- | --------- | --- | --- |
Generateaprintable,humanreadabletextfilecontainingtheencryptionkey.
ThisalsoincludesascanableQRcodeforfastkeyrestore.
<fingerprint>
[<string>]Tapeencryptionkeyfingerprint(sha256).
Optionalparameters:
| 244 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
--output-formattext|html
Paperkeyoutputformat
--subject<string>
Includethespecifiedsubjectastitletext.
proxmox-tape key remove <fingerprint> [OPTIONS]
Removeaencryptionkeyfromthedatabase
Pleasenotethatyoucannolongeraccesstapesusingthiskey.
<fingerprint>
[<string>]Tapeencryptionkeyfingerprint(sha256).
Optionalparameters:
--digest<string>
PreventchangesifcurrentconfigurationfilehasdifferentSHA256digest. Thiscanbeusedto
preventconcurrentmodifications.
proxmox-tape key restore [OPTIONS]
Restoreencryptionkeyfromtapeorfromabackupfile/string(readspasswordfromstdin)
Optionalparameters:
--drive<string>
DriveIdentifier.
--key<string>
Importkeyfromjsonstringoranexportedpaperkey-format.
--key-file<string>
Importkeyfromafilewitheitherjsonorexportedpaperkey-format.
proxmox-tape key show <fingerprint> [OPTIONS]
Printtheencryptionkey’smetadata.
<fingerprint>
[<string>]Tapeencryptionkeyfingerprint(sha256).
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape label --label-text <string> [OPTIONS]
Labelmedia
--label-text<string>
MediaLabel/Barcode.
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
A.3. proxmox-tape 245

ProxmoxBackupDocumentation,Release4.2.8‐1
--pool<string>
Mediapoolname.
proxmox-tape load-media <label-text> [OPTIONS]
Loadmediawithspecifiedlabel
<label-text>
[<string>]MediaLabel/Barcode.
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape load-media-from-slot <source-slot> [OPTIONS]
Loadmediafromthespecifiedslot
<source-slot>
[<integer> (1 - N)]Sourceslotnumber.
Optionalparameters:
--drive<string>
DriveIdentifier.
proxmox-tape media content [OPTIONS]
Listmediacontent
Optionalparameters:
--backup-id<string>
BackupID.
--backup-typevm|ct|host
Backuptypes.
--label-text<string>
MediaLabel/Barcode.
--media<string>
MediaUuid.
--media-set<string>
MediaSetUuid(Weusetheall-zeroUuidtoreserveanemptymediaforaspecificpool).
--output-formattext|json|json-pretty
Outputformat.
--pool<string>
Mediapoolname.
proxmox-tape media destroy [<label-text>] [OPTIONS]
Destroymedia(completelyremovefromdatabase)
<label-text>
[<string>]MediaLabel/Barcode.
246 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
Optionalparameters:
--force<boolean>
Forceremoval(evenifmediaisusedinamediaset).
--uuid<string>
MediaUuid.
proxmox-tape media list [OPTIONS]
Listpoolmedia
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
--pool<string>
Mediapoolname.
--update-status<boolean> (default=true)
Trytoupdatetapelibrarystatus(checkwhattapesareonline).
--update-status-changer<string>
TapeChangerIdentifier.
proxmox-tape pool config <name> [OPTIONS]
Getmediapoolconfiguration
<name>
[<string>]Mediapoolname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape pool create <name> [OPTIONS]
Createanewmediapool
<name>
[<string>]Mediapoolname.
Optionalparameters:
--allocation<string>
Mediasetallocationpolicy(’continue’,’always’,oracalendarevent).
--comment<string>
Comment.
--encrypt<string>
Tapeencryptionkeyfingerprint(sha256).
--retention<string>
Mediaretentionpolicy(’overwrite’,’keep’,ortimespan).
--template<string>
Mediasetnamingtemplate(maycontainstrftime()timeformatspecifications).
A.3. proxmox-tape 247

ProxmoxBackupDocumentation,Release4.2.8‐1
proxmox-tape pool list [OPTIONS]
Listmediapool
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape pool remove <name>
Deleteamediapoolconfiguration
<name>
[<string>]Mediapoolname.
proxmox-tape pool update <name> [OPTIONS]
Updatemediapoolsettings
<name>
[<string>]Mediapoolname.
Optionalparameters:
--allocation<string>
Mediasetallocationpolicy(’continue’,’always’,oracalendarevent).
--comment<string>
Comment.
--deleteallocation|retention|template|encrypt|comment
Listofpropertiestodelete. Canbespecifiedmorethanonce.
--encrypt<string>
Tapeencryptionkeyfingerprint(sha256).
--retention<string>
Mediaretentionpolicy(’overwrite’,’keep’,ortimespan).
--template<string>
Mediasetnamingtemplate(maycontainstrftime()timeformatspecifications).
proxmox-tape read-label [OPTIONS]
Readmedialabel
Optionalparameters:
--drive<string>
DriveIdentifier.
--inventorize<boolean>
Inventorizemedia
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape restore <media-set> <store> [{<snapshots>}] [OPTIONS]
Restoredatafrommedia-set
248 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
<media-set>
[<string>]MediasetUUID.
<store>
[[(<source>=)?<target>, ...]] A list of Datastore mappings (or single datastore),
commaseparated. Forexample’a=b,e’mapsthesourcedatastore’a’totarget’bandallother
sourcestothedefault’e’. Ifnodefaultisgiven,onlythespecifiedsourcesaremapped.
<snapshots>
[store:[ns/namespace/...]type/id/time] List of snapshots. Can be specified more
thanonce.
Optionalparameters:
--drive<string>
DriveIdentifier.
--namespaces[store=<string> [,max-depth=<integer>] [,source=<string>]
[,target=<string>]]
Listofnamespacetorestore. Canbespecifiedmorethanonce.
--notify-user<string>
UserID
--output-formattext|json|json-pretty
Outputformat.
--owner<string>
AuthenticationID
proxmox-tape rewind [OPTIONS]
Rewindtape
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
proxmox-tape scan [OPTIONS]
Rewind,thenreadmediacontentsandprintdebuginfo
Note: ThisreadsunlessthedriverreturnsanIOError,sothismethodisexpectedtofailswhenwe
reachEOT.
Optionalparameters:
--drive<string>
DriveIdentifier.
proxmox-tape status [OPTIONS]
Getdrive/mediastatus
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
A.3. proxmox-tape 249

ProxmoxBackupDocumentation,Release4.2.8‐1
| proxmox-tape | unload [OPTIONS] |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
Unloadmediaviachanger
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
| --target-slot<integer> | (1 - | N)  |     |     |
| ---------------------- | ---- | --- | --- | --- |
Targetslotnumber. Ifomitted,defaultstotheslotthatthedrivewasloadedfrom.
| proxmox-tape | volume-statistics | [OPTIONS] |     |     |
| ------------ | ----------------- | --------- | --- | --- |
ReadVolumeStatistics(SCSIlogpage17h)
Optionalparameters:
--drive<string>
DriveIdentifier.
--output-formattext|json|json-pretty
Outputformat.
A.4 pmt
Allcommandssupportthefollowingparameterstospecifythetapedevice:
--device<path> PathtotheLinuxtapedevice
--drive<name> UsedrivefromProxmoxBackupServerconfiguration.
Commandswhichgenerateoutputsupportthe--output-formatparameter. Itacceptsthefol-
lowingvalues:
text
| Textformat(default). | Humanreadable. |     |     |     |
| -------------------- | -------------- | --- | --- | --- |
json
JSON(singleline).
json-pretty
JSON(multiplelines,nicelyformatted).
| pmt asf <count> |     |     |     |     |
| --------------- | --- | --- | --- | --- |
Positionthetapeatthebeginningofthecountfile(afterfilemarkcount)
<count>
| [<integer>      | (0 - 2147483647)]Filemarkposition(0isBOT). |     |     |     |
| --------------- | ------------------------------------------ | --- | --- | --- |
| pmt bsf <count> |                                            |     |     |     |
Backwardspacecountfiles(positionbeforefilemark).
Thetapeispositionedonthelastblockofthepreviousfile.
| 250 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
<count>
[<integer> (1 - 2147483647)]Filemarkcount.
pmt bsfm <count>
Backwardspacecountfiles,thenforwardspaceonerecord(positionafterfilemark).
Thisleavesthetapepositionedatthefirstblockofthefilethatiscount-1filesbeforethecurrent
file.
<count>
[<integer> (1 - 2147483647)]Filemarkcount.
pmt bsr <count>
Backwardspacerecords.
<count>
[<integer> (1 - 2147483647)]Recordcount.
pmt cartridge-memory
ReadCartridgeMemory
pmt eject
Ejectdrivemedia
pmt eod
Movetoendofmedia
pmt erase [OPTIONS]
Erasemedia(fromcurrentposition)
Optionalparameters:
--fast<boolean> (default=true)
Usefasterase.
pmt format [OPTIONS]
Formatmedia,singlepartition
Optionalparameters:
--fast<boolean> (default=true)
Usefasterase.
pmt fsf <count>
Forwardspacecountfiles(positionafterfilemark).
Thetapeispositionedonthefirstblockofthenextfile.
A.4. pmt 251

ProxmoxBackupDocumentation,Release4.2.8‐1
<count>
| [<integer> | (1 -    | 2147483647)]Filemarkcount. |     |     |
| ---------- | ------- | -------------------------- | --- | --- |
| pmt fsfm   | <count> |                            |     |     |
Forwardspacecountfiles,thenbackwardspaceonerecord(positionbeforefilemark).
Thisleavesthetapepositionedatthelastblockofthefilethatiscount-1filespastthecurrentfile.
<count>
| [<integer> | (1 -    | 2147483647)]Filemarkcount. |     |     |
| ---------- | ------- | -------------------------- | --- | --- |
| pmt fsr    | <count> |                            |     |     |
Forwardspacerecords.
<count>
| [<integer> | (1 -          | 2147483647)]Recordcount. |     |     |
| ---------- | ------------- | ------------------------ | --- | --- |
| pmt help   | [{<command>}] | [OPTIONS]                |     |     |
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
pmt load
Loadmedia
pmt lock
Lockthetapedrivedoor
| pmt options | [OPTIONS] |     |     |     |
| ----------- | --------- | --- | --- | --- |
Setvariosdriveoptions
Optionalparameters:
| --blocksize<integer> |     | (0 - 8388608) |     |     |
| -------------------- | --- | ------------- | --- | --- |
Settapedriveblock_length(0isvariablelength).
--buffer_mode<boolean>
Usedrivebuffer.
--compression<boolean>
Enable/disablecompression.
--defaults<boolean>
Setdefaultoptions
| 252 |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
pmt rewind
Rewindthetape
pmt scan
Scanforexistingtapechangerdevices
pmt status
DriveStatus
pmt tape-alert-flags
ReadTapeAlertFlags
pmt unlock
Unlockthetapedrivedoor
pmt volume-statistics
VolumeStatistics
pmt weof [<count>]
Writecount(default1)EOFmarksatcurrentposition.
<count>
[<integer> (1 - 2147483647)]Filemarkcount.
A.5 pmtx
pmtx help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
pmtx inquiry
Inquiry
pmtx inventory
A.5. pmtx 253

ProxmoxBackupDocumentation,Release4.2.8‐1
Inventory
pmtx load <slot> [OPTIONS]
Load
<slot>
[<integer>]Storageslotnumber(source).
Optionalparameters:
--drivenum<integer>
Targetdrivenumber(defaultstoDrive0)
pmtx scan
Scanforexistingtapechangerdevices
pmtx status
ChangerStatus
pmtx transfer <from> <to>
Transfer
<from>
[<integer>]Sourcestorageslotnumber.
<to>
[<integer>]Targetstorageslotnumber.
pmtx unload [OPTIONS]
Unload
Optionalparameters:
--drivenum<integer>
Targetdrivenumber(defaultstoDrive0)
--slot<integer>
Storageslotnumber(target). Ifomitted,defaultstotheslotthatthedrivewasloadedfrom.
A.6 pxar
pxar create <archive> <source> [OPTIONS]
Createanew.pxararchive.
<archive>
[<string>]Archivename.
<source>
[<string>]Sourcedirectory.
Optionalparameters:
--all-file-systems<boolean> (default=false)
Includemountedsudirs.
254 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--entries-max<integer> (0 - 9223372036854775807) (default=1048576)
Maxnumberofentriesloadedatonceintomemory
--exclude<string>
Listofpathsorpatternmatchingfilestoexclude. Canbespecifiedmorethanonce.
| --no-acls<boolean> | (default=false) |     |     |
| ------------------ | --------------- | --- | --- |
Ignoreaccesscontrollistentries.
| --no-device-nodes<boolean> |     | (default=false) |     |
| -------------------------- | --- | --------------- | --- |
Ignoredevicenodes.
| --no-fcaps<boolean> |     | (default=false) |     |
| ------------------- | --- | --------------- | --- |
Ignorefilecapabilities.
| --no-fifos<boolean> |     | (default=false) |     |
| ------------------- | --- | --------------- | --- |
Ignorefifos.
| --no-sockets<boolean> |     | (default=false) |     |
| --------------------- | --- | --------------- | --- |
Ignoresockets.
| --no-xattrs<boolean> |     | (default=false) |     |
| -------------------- | --- | --------------- | --- |
Ignoreextendedfileattributes.
--payload-output<string>
’ppxar’payloadoutputdatafiletocreatesplitarchive.
| pxar extract | <archive> | [<target>] | [OPTIONS] |
| ------------ | --------- | ---------- | --------- |
Extractanarchive.
<archive>
[<string>]Archivename.
<target>
[<string>]Targetdirectory
Optionalparameters:
| --allow-existing-dirs<boolean> |     |     | (default=false) |
| ------------------------------ | --- | --- | --------------- |
Allowsdirectoriestoalreadyexistonrestore.
--files-from<string>
Filecontainingmatchpatternforfilestorestore.
| --no-acls<boolean> | (default=false) |     |     |
| ------------------ | --------------- | --- | --- |
Ignoreaccesscontrollistentries.
| --no-device-nodes<boolean> |     | (default=false) |     |
| -------------------------- | --- | --------------- | --- |
Ignoredevicenodes.
| --no-fcaps<boolean> |     | (default=false) |     |
| ------------------- | --- | --------------- | --- |
Ignorefilecapabilities.
| --no-fifos<boolean> |     | (default=false) |     |
| ------------------- | --- | --------------- | --- |
Ignorefifos.
| --no-sockets<boolean> |     | (default=false) |     |
| --------------------- | --- | --------------- | --- |
Ignoresockets.
| --no-xattrs<boolean> |     | (default=false) |     |
| -------------------- | --- | --------------- | --- |
Ignoreextendedfileattributes.
| --overwrite<boolean> |     | (default=false) |     |
| -------------------- | --- | --------------- | --- |
overwritealreadyexistingfiles,symlinksandhardlinks
| --overwrite-files<boolean> |     | (default=false) |     |
| -------------------------- | --- | --------------- | --- |
overwritealreadyexistingfiles
A.6. pxar 255

ProxmoxBackupDocumentation,Release4.2.8‐1
| --overwrite-hardlinks<boolean> |     |     | (default=false) |     |     |
| ------------------------------ | --- | --- | --------------- | --- | --- |
overwritealreadyexistingentriesbyarchiveshardlink
| --overwrite-symlinks<boolean> |     | (default=false) |     |     |     |
| ----------------------------- | --- | --------------- | --- | --- | --- |
overwritealreadyexistingentriesbyarchivessymlink
--pattern<string>
Pathormatchpatterntolimitfilesthatgetrestored. Canbespecifiedmorethanonce.
--payload-input<string>
’ppxar’payloadinputdatafiletorestoresplitarchive.
--prelude-target<string>
Pathtorestorepxararchivepreludeto.
| --strict<boolean> |                                    | (default=false) |     |     |     |
| ----------------- | ---------------------------------- | --------------- | --- | --- | --- |
| Stoponerrors.     | Otherwisemosterrorswillsimplywarn. |                 |     |     |     |
| pxar help         | [{<command>}]                      | [OPTIONS]       |     |     |     |
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
| pxar list | <archive> | [OPTIONS] |     |     |     |
| --------- | --------- | --------- | --- | --- | --- |
Listthecontentsofanarchive.
<archive>
[<string>]Archivename.
Optionalparameters:
--payload-input<string>
’ppxar’payloadinputdatafileforsplitarchive.
| pxar mount | <archive> | <mountpoint> | [OPTIONS] |     |     |
| ---------- | --------- | ------------ | --------- | --- | --- |
MountthearchivetotheprovidedmountpointviaFUSE.
<archive>
[<string>]Archivename.
<mountpoint>
[<string>]Mountpointforthefilesystem.
Optionalparameters:
--payload-input<string>
’ppxar’payloadinputdatafiletorestoresplitarchive.
| --verbose<boolean> |     | (default=false) |     |     |     |
| ------------------ | --- | --------------- | --- | --- | --- |
Verboseoutput,runningintheforeground(fordebugging).
| 256 |     |     |     | AppendixA. | CommandSyntax |
| --- | --- | --- | --- | ---------- | ------------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
A.7 proxmox-file-restore
proxmox-file-restore extract <snapshot> <path> [<target>] [OPTIONS]
Restorefilesfromabackupsnapshot.
<snapshot>
[<string>]Group/Snapshotpath.
<path>
[<string>]Pathtorestore. Directorieswillberestoredasarchivefilesifextractedtostdout.
<target>
| [<string>]Targetdirectorypath. |     | Use’-’towritetostandardoutput. |     |
| ------------------------------ | --- | ------------------------------ | --- |
Optionalparameters:
--auth-id<string>
AuthenticationID
| --base64<boolean> | (default=false) |     |     |
| ----------------- | --------------- | --- | --- |
Ifset,’path’willbeinterpretedasbase64encoded.
| --crypt-modenone|encrypt|sign-only |     | (default=encrypt) |     |
| ---------------------------------- | --- | ----------------- | --- |
Defineswhetherdataisencrypted(usinganAEADcipher),onlysigned,orneither.
--datastore<string>
Datastorename.
--driverQemu
Theblockdrivertypetouse.
--formatplain|pxar|zip|tar
Thedesiredformatoftheresult.
| --ignore-missing-signature<boolean> |     | (default=false) |     |
| ----------------------------------- | --- | --------------- | --- |
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
| --keyfd<integer> | (0 - N) |     |     |
| ---------------- | ------- | --- | --- |
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
| Pathtoencryptionkey. | Alldatawillbeencryptedusingthiskey. |     |     |
| -------------------- | ----------------------------------- | --- | --- |
--ns<string>
Namespace.
| --port<integer>   | (1 - 65535) | (default=8007) |     |
| ----------------- | ----------- | -------------- | --- |
| Backupserverport. | Default:    | 8007           |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |                 |     | localhost |
| ------------------------------------------ | --------------- | --- | --------- |
| --verbose<boolean>                         | (default=false) |     |           |
Printverboseinformation
| --zstd<boolean> | (default=false) |     |     |
| --------------- | --------------- | --- | --- |
Iftrue,outputwillbezstdcompressed.
| proxmox-file-restore | help | [{<command>}] | [OPTIONS] |
| -------------------- | ---- | ------------- | --------- |
Gethelpaboutspecifiedcommand(orsub-command).
A.7. proxmox-file-restore 257

ProxmoxBackupDocumentation,Release4.2.8‐1
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
| proxmox-file-restore | list | <snapshot> | <path> [OPTIONS] |     |     |
| -------------------- | ---- | ---------- | ---------------- | --- | --- |
Listadirectoryfromabackupsnapshot.
<snapshot>
[<string>]Group/Snapshotpath.
<path>
[<string>](Sub-)Pathtolist.
Optionalparameters:
--auth-id<string>
AuthenticationID
| --base64<boolean> | (default=false) |     |     |     |     |
| ----------------- | --------------- | --- | --- | --- | --- |
Ifset,’path’willbeinterpretedasbase64encoded.
| --crypt-modenone|encrypt|sign-only |     |     | (default=encrypt) |     |     |
| ---------------------------------- | --- | --- | ----------------- | --- | --- |
Defineswhetherdataisencrypted(usinganAEADcipher),onlysigned,orneither.
--datastore<string>
Datastorename.
--driverQemu
Theblockdrivertypetouse.
| --ignore-missing-signature<boolean> |     |     | (default=false) |     |     |
| ----------------------------------- | --- | --- | --------------- | --- | --- |
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
| --keyfd<integer> | (0 - N) |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
| Pathtoencryptionkey. | Alldatawillbeencryptedusingthiskey. |     |     |     |     |
| -------------------- | ----------------------------------- | --- | --- | --- | --- |
--ns<string>
Namespace.
--output-formattext|json|json-pretty
Outputformat.
| --port<integer>   | (1 - 65535) | (default=8007) |     |     |     |
| ----------------- | ----------- | -------------- | --- | --- | --- |
| Backupserverport. | Default:    | 8007           |     |     |     |
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
| Backupserveraddress(hostnameorIP).Default: |         |     | localhost |     |     |
| ------------------------------------------ | ------- | --- | --------- | --- | --- |
| --timeout<integer>                         | (1 - N) |     |           |     |     |
Definesthemaximumtimethecallcanshouldtake.
| proxmox-file-restore | status | [OPTIONS] |     |            |               |
| -------------------- | ------ | --------- | --- | ---------- | ------------- |
| 258                  |        |           |     | AppendixA. | CommandSyntax |

ProxmoxBackupDocumentation,Release4.2.8‐1
Retrievestatusinformationaboutcurrentlyrunning/mappedrestoreimages
Optionalparameters:
--driverQemu
Theblockdrivertypetouse.
--output-formattext|json|json-pretty
Outputformat.
proxmox-file-restore stop <name>
Immediatelystop/unmapagivenimage. Nottypicallynecessary,asVMswillstopthemselvesafter
atimeranyway.
<name>
[<string>]ThenameoftheVMtostop.
A.8 proxmox-backup-debug
proxmox-backup-debug api create <api-path> [OPTIONS]
CallAPIon<api-path>
<api-path>
[<string>]APIpath.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug api delete <api-path> [OPTIONS]
CallAPIon<api-path>
<api-path>
[<string>]APIpath.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug api get <api-path> [OPTIONS]
CallAPIon<api-path>
<api-path>
[<string>]APIpath.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug api ls [<path>] [OPTIONS]
GetAPIusageinformationfor<path>
<path>
[<string>]APIpath.
A.8. proxmox-backup-debug 259

ProxmoxBackupDocumentation,Release4.2.8‐1
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug api set <api-path> [OPTIONS]
CallAPIon<api-path>
<api-path>
[<string>]APIpath.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug api usage <path> [OPTIONS]
GetAPIusageinformationfor<path>
<path>
[<string>]APIpath.
Optionalparameters:
--verbose<boolean> (default=false)
Verboseoutputformat.
proxmox-backup-debug diff archive <prev-snapshot> <snapshot> <archive-name>
[OPTIONS]
Diffanarchiveintwosnapshots. Thecommandwilloutputalistofadded,modifiedanddeleted
files. For modified files, the file metadata (e.g. mode, uid, gid, size, etc.) will be considered. For
detectingmodificationoffilecontent,onlymtimewillbeusedbydefault. Ifthe--compare-content
flagisprovided,mtimeisignoredandfilecontentwillbecompared.
<prev-snapshot>
[<string>]Pathforthefirstsnapshot.
<snapshot>
[<string>]Pathforthesecondsnapshot.
<archive-name>
[<string>]Backuparchivename.
Optionalparameters:
--auth-id<string>
AuthenticationID
--coloralways|auto|never (default=auto)
Coloroutputoptions
--compare-content<boolean> (default=false)
Comparefilecontentratherthansolelyrelyingonmtimefordetectingmodifiedfiles.
--datastore<string>
Datastorename.
--ignore-missing-signature<boolean> (default=false)
Readabackupwhosemanifesthasnosignatureeventhoughanencryptionkeyisconfigured.
Thebackup’sintegritycannotbeverifiedinthatcase.
260 AppendixA. CommandSyntax

ProxmoxBackupDocumentation,Release4.2.8‐1
--keyfd<integer> (0 - N)
Passanencryptionkeyviaanalreadyopenedfiledescriptor.
--keyfile<string>
Pathtoencryptionkey.
--ns<string>
Namespace.
--port<integer> (1 - 65535) (default=8007)
Backupserverport. Default: 8007
--repository<string>
RepositoryURL:[[auth-id@]server[:port]:]datastore
--server<string>
Backupserveraddress(hostnameorIP).Default: localhost
proxmox-backup-debug help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-backup-debug inspect chunk <chunk> [OPTIONS]
Inspectachunk
<chunk>
[<string>]Thechunkfile.
Optionalparameters:
--decode<string>
Pathtothefiletowhichthechunkshouldbedecoded,’-’->decodetostdout.
--digest<string>
Neededwhensearchingforreferences,ifset,itwillbeusedforverificationwhendecoding.
--keyfile<string>
Pathtothekeyfilewithwhichthechunkwasencrypted.
--output-formattext|json|json-pretty
Outputformat.
--reference-filter<string>
Pathtothedirectorythatshouldbesearchedforreferences.
--use-filename-as-digest<boolean> (default=true)
The filename should be used as digest for reference search and decode verification, if no
digestisspecified.
proxmox-backup-debug inspect device <device> [OPTIONS]
Inspectadeviceforpossibledatastoresonit
<device>
[<string>]Devicepath,usually/dev/...
A.8. proxmox-backup-debug 261

ProxmoxBackupDocumentation,Release4.2.8‐1
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug inspect file <file> [OPTIONS]
Inspectafile,forblobfilewithoutdecodeonlythesizeandencryptionmodeisprinted
<file>
[<string>]Pathtothefile.
Optionalparameters:
--decode<string>
Pathtothefiletowhichthefileshouldbedecoded,’-’->decodetostdout.
--keyfile<string>
Pathtothekeyfilewithwhichthefilewasencrypted.
--output-formattext|json|json-pretty
Outputformat.
proxmox-backup-debug recover index <file> <chunks> [OPTIONS]
Restore the data from an index file, given the directory of where chunks are saved, the index file
andakeyfile,ifneededfordecryption.
<file>
[<string>]Pathtotheindexfile,either.fidxor.didx.
<chunks>
[<string>]Pathtothedirectorythatcontainsthechunks,usually<datastore>/.chunks.
Optionalparameters:
--ignore-corrupt-chunks<boolean> (default=false)
Ifachunkiscorrupt,warnandwrite0-bytesinsteadtoattemptpartialrecovery.
--ignore-missing-chunks<boolean> (default=false)
Ifachunkismissing,warnandwrite0-bytesinsteadtoattemptpartialrecovery.
--keyfile<string>
Pathtoakeyfile,ifthedatawasencrypted,akeyfileisneededfordecryption.
--output-path<string>
Outputfilepath,defaultstofilewithoutextension,’-’meansSTDOUT.
--skip-crc<boolean> (default=false)
Skipthecrcverification,increasestherestorespeedbylot.
262 AppendixA. CommandSyntax

APPENDIX
B
CONFIGURATION FILES
AllProxmoxBackupServerconfigurationfilesresideinthedirectory/etc/proxmox-backup/.
B.1 acl.cfg
B.1.1 FileFormat
ThisfilecontainstheaccesscontrollistfortheProxmoxBackupServerAPI.
Eachlinestartswithacl:,followedby4additionalvaluesseparatedbycolon.
propagate
Propagatepermissionsdownthehierarchy
path
Theobjectpath
User/Token
Listofusersandtokens
Role
Listofassignedroles
Hereisanexamplelist:
acl:1:/:root@pam!test:Admin
acl:1:/datastore/store1:user1@pbs:DatastoreAdmin
Youcanusetheproxmox-backup-manager aclcommandtomanipulatethisfile.
B.1.2 Roles
Thefollowingrolesexist:
Admin
Administrator
Audit
Auditor
NoAccess
DisableAccess
DatastoreAdmin
DatastoreAdministrator
DatastoreReader
DatastoreReader(inspectdatastorecontentanddorestores)
DatastoreBackup
DatastoreBackup(backupandrestoreownedbackups)
263

ProxmoxBackupDocumentation,Release4.2.8‐1
DatastorePowerUser
DatastorePowerUser(backup,restoreandpruneownedbackup)
DatastoreAudit
DatastoreAuditor
RemoteAudit
RemoteAuditor
RemoteAdmin
RemoteAdministrator
RemoteSyncOperator
SynchronizationOperator
RemoteSyncPushOperator
SynchronisationOperator(pushdirection)
RemoteDatastorePowerUser
RemoteDatastorePrune
RemoteDatastoreAdmin
RemoteDatastoreAdmin
TapeAudit
TapeAuditor
TapeAdmin
TapeAdministrator
TapeOperator
TapeOperator
TapeReader
TapeReader
B.2 datastore.cfg
B.2.1 FileFormat
This file contains a list of datastore configuration sections. Each section starts with the header
datastore: <name>,followedbythedatastoreconfigurationoptions.
datastore: <name1>
path <path1>
<.o..ption1> <value1>
datastore: <name2>
p.a.t.h <path2>
Youcanusetheproxmox-backup-manager datastorecommandtomanipulatethisfile.
B.2.2 Options
Requiredproperties:
path
[<string>] Either the absolute path to the datastore directory, or a relative on-device path
forremovabledatastores.
Optionalproperties:
backend
[<backend-config>]Datastorebackendconfig
backing-device
[<string>]TheUUIDofthefilesystempartitionforremovabledatastores.
264 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
comment
[<string>]Comment.
counter-reset-schedule
[<calendar-event>]Resetnotificationthresholdrelatedcountersatspecifiedschedule.
gc-on-unmount
[<boolean>]Rungarbagecollectionbeforeunmountingaremovabledatastore.
gc-schedule
[<calendar-event>]Rungarbagecollectionjobatspecifiedschedule.
maintenance-mode
[[type=<enum> [,message=<string>]]] Maintenance mode, type is either ’offline’ or
’read-only’,messageshouldbeenclosedin”
type=read-only|offline|delete|unmount|s3-refresh
Maintenancetype.
message=<string>
Messagedescribingthereasonforthemaintenance.
notification-mode
[legacy-sendmail|notification-system (default=notification-system)] Con-
figure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
notification-thresholds
[[[s3-delete=<integer>] [,s3-download=<string>] [,s3-get=<integer>]
[,s3-head=<integer>] [,s3-post=<integer>] [,s3-put=<integer>] [,
s3-upload=<string>]]]Thresholdvaluesfornotifications
s3-delete=<integer>
ThresholdforDELETErequests.
s3-download=<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
s3-get=<integer>
ThresholdforGETrequests.
s3-head=<integer>
ThresholdforHEADrequests.
s3-post=<integer>
ThresholdforPOSTrequests.
s3-put=<integer>
ThresholdforPUTrequests.
s3-upload=<string>
Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
notify
[[[gc=<enum>] [,prune=<enum>] [,sync=<enum>] [,verify=<enum>]]] Datastore
notificationsetting,enumcanbeoneof’always’,’never’,or’error’.
gc=never|always|error
Whendowesendnotifications
prune=never|always|error
Whendowesendnotifications
sync=never|always|error
Whendowesendnotifications
B.2. datastore.cfg 265

ProxmoxBackupDocumentation,Release4.2.8‐1
verify=never|always|error
Whendowesendnotifications
notify-user
[<string>]UserID
prune-schedule
[<calendar-event>]Runprunejobatspecifiedschedule.
tuning
[[[chunk-order=<enum>] [,default-verification-readers=<integer>] [,
default-verification-workers=<integer>] [,gc-atime-cutoff=<integer>]
[,gc-atime-safety-check=<1|0>] [,gc-cache-capacity=<integer>] [,
sync-level=<enum>]]]Datastoretuningoptions
chunk-order=none|inode (default=inode)
Theordertosortchunksby
default-verification-readers=<integer> (1 - 32) (default=1)
Thenumberofthreadstouseforreadingchunksinverifyjob.
default-verification-workers=<integer> (1 - 32) (default=4)
Thenumberofthreadstouseforverifyingchunksinverifyjob.
gc-atime-cutoff=<integer> (1 - 2880) (default=1445)
Cutoff(inminutes)forchunkcleanupatimecheckingarbagecollectionphase2(default
24h5m)
gc-atime-safety-check=<boolean> (default=true)
Check filesystem atime updates are honored during store creation and garbage collec-
tion
gc-cache-capacity=<integer> (0 - 8388608) (default=1048576)
Garbagecollectionchunkdigestcachecapacity
sync-level=none|file|filesystem (default=filesystem)
Thelevelofsyncingthatisdonewhenwritingintoadatastore.
verify-new
[<boolean>]Ifenabled,allnewbackupswillbeverifiedrightaftercompletion.
keep-daily
[<integer> (1 - N)]Numberofdailybackupstokeep.
keep-hourly
[<integer> (1 - N)]Numberofhourlybackupstokeep.
keep-last
[<integer> (1 - N)]Numberofbackupstokeep.
keep-monthly
[<integer> (1 - N)]Numberofmonthlybackupstokeep.
keep-weekly
[<integer> (1 - N)]Numberofweeklybackupstokeep.
keep-yearly
[<integer> (1 - N)]Numberofyearlybackupstokeep.
B.3 domains.cfg
B.3.1 FileFormat
Thisfilecontainsthelistauthenticationrealms.
266 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
Eachuserconfigurationsectionstartswiththeheader<realm-type>: <name>,followedbythe
realm’sconfigurationoptions.
ForLDAPrealms,theLDAPbindpasswordisstoredinldap_passwords.json.
openid: master
client-id pbs
comment
issuer-url http://192.168.0.10:8080/realms/master
username-claim username
ldap: ldap-server
base-dn OU=People,DC=ldap-server,DC=example,DC=com
mode ldaps
server1 192.168.0.10
sync-attributes email=mail
sync-defaults-options enable-new=0,remove-vanished=acl;entry
user-attr uid
user-classes inetorgperson,posixaccount,person,user
You can use the proxmox-backup-manager openid, proxmox-backup-manager ldap and
proxmox-backup-manager adcommandstomanipulatethisfile.
B.3.2 Options
Sectiontype’ad’: ADrealmconfigurationproperties.
Requiredproperties:
server1
[<string>]ADserveraddress
Optionalproperties:
base-dn
[<string>]LDAPDomain
bind-dn
[<string>]LDAPDomain
capath
[<string>]CAcertificatetousefortheserver. Thepathcanpointtoeitherafile,oradirec-
tory. Ifitpointstoafile,thePEM-formattedX.509certificatestoredatthepathwillbeadded
as a trusted certificate. If the path points to a directory, the directory replaces the system’s
defaultcertificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrusted
certificate.
comment
[<string>]Comment.
default
[<boolean> (default=false)] True if you want this to be the default realm selected on
login.
filter
[<string>]CustomLDAPsearchfilterforusersync
mode
[ldap|ldap+starttls|ldaps (default=ldap)]LDAPconnectiontype
port
[<integer> (0 - 65535)]ADserverPort
server2
[<string>]FallbackADserveraddress
sync-attributes
[[[email=<string>] [,firstname=<string>] [,lastname=<string>]]] Comma-
separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhichPBSuser
field. Forexample,tomaptheLDAPattributemailtoPBS’semail,writeemail=mail.
B.3. domains.cfg 267

ProxmoxBackupDocumentation,Release4.2.8‐1
email=<string>
NameoftheLDAPattributecontainingtheuser’semailaddress
firstname=<string>
NameoftheLDAPattributecontainingtheuser’sfirstname
lastname=<string>
NameoftheLDAPattributecontainingtheuser’slastname
sync-defaults-options
[[[enable-new=<1|0>] [,remove-vanished=<string>]]]syncdefaultsoptions
enable-new=<boolean>
Enablenewusersaftersync
remove-vanished=[acl|entry|properties, ...]
A semicolon-separated list of things to remove when they or the user vanishes during
usersynchronization. Thefollowingvaluesarepossible: entryremovestheuserwhen
notreturnedfromthesync; propertiesremovesanypropertiesonexistinguserthat
donotappearinthesource. aclremovesACLswhentheuserisnotreturnedfromthe
sync.
user-classes
[[<string>, ...] (default=inetorgperson,posixaccount,person,user)]
Comma-separated list of allowed objectClass values for user synchronization. For in-
stance,if user-classesissettoperson,user,thenusersynchronizationwillconsiderall
LDAPentitieswhereobjectClass: personorobjectClass: user.
verify
[<boolean> (default=false)]Verifyservercertificate
Sectiontype’ldap’: LDAPconfigurationproperties.
Requiredproperties:
base-dn
[<string>]LDAPDomain
server1
[<string>]LDAPserveraddress
user-attr
[<string>]Usernameattribute. UsedtomapauseridtoLDAPtoanLDAPdn.
Optionalproperties:
bind-dn
[<string>]LDAPDomain
capath
[<string>]CAcertificatetousefortheserver. Thepathcanpointtoeitherafile,oradirec-
tory. Ifitpointstoafile,thePEM-formattedX.509certificatestoredatthepathwillbeadded
as a trusted certificate. If the path points to a directory, the directory replaces the system’s
defaultcertificatestoreat/etc/ssl/certs-Everyfileinthedirectorywillbeloadedasatrusted
certificate.
comment
[<string>]Comment.
default
[<boolean> (default=false)] True if you want this to be the default realm selected on
login.
filter
[<string>]CustomLDAPsearchfilterforusersync
mode
[ldap|ldap+starttls|ldaps (default=ldap)]LDAPconnectiontype
268 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
port
[<integer> (0 - 65535)]Port
server2
[<string>]FallbackLDAPserveraddress
sync-attributes
[[[email=<string>] [,firstname=<string>] [,lastname=<string>]]] Comma-
separatedlistofkey=valuepairsforspecifyingwhichLDAPattributesmaptowhichPBSuser
field. Forexample,tomaptheLDAPattributemailtoPBS’semail,writeemail=mail.
email=<string>
NameoftheLDAPattributecontainingtheuser’semailaddress
firstname=<string>
NameoftheLDAPattributecontainingtheuser’sfirstname
lastname=<string>
NameoftheLDAPattributecontainingtheuser’slastname
sync-defaults-options
[[[enable-new=<1|0>] [,remove-vanished=<string>]]]syncdefaultsoptions
enable-new=<boolean>
Enablenewusersaftersync
remove-vanished=[acl|entry|properties, ...]
A semicolon-separated list of things to remove when they or the user vanishes during
usersynchronization. Thefollowingvaluesarepossible: entryremovestheuserwhen
notreturnedfromthesync; propertiesremovesanypropertiesonexistinguserthat
donotappearinthesource. aclremovesACLswhentheuserisnotreturnedfromthe
sync.
user-classes
[[<string>, ...] (default=inetorgperson,posixaccount,person,user)]
Comma-separated list of allowed objectClass values for user synchronization. For in-
stance,if user-classesissettoperson,user,thenusersynchronizationwillconsiderall
LDAPentitieswhereobjectClass: personorobjectClass: user.
verify
[<boolean> (default=false)]Verifyservercertificate
Sectiontype’openid’: OpenIDconfigurationproperties.
Requiredproperties:
client-id
[<string>]OpenIDClientID
issuer-url
[<string>]OpenIDIssuerUrl
Optionalproperties:
acr-values
[[<string>, ...]]OpenIDACRList
audiences
[[<string>, ...]]OpenIDaudiencelist.
autocreate
[<boolean> (default=false)]Automaticallycreateusersiftheydonotexist.
client-key
[<string>]OpenIDClientKey
comment
[<string>]Comment.
B.3. domains.cfg 269

ProxmoxBackupDocumentation,Release4.2.8‐1
default
[<boolean> (default=false)] True if you want this to be the default realm selected on
login.
prompt
[<string>]OpenIDPrompt
scopes
[[<string>, ...] (default=email profile)]OpenIDScopeList
username-claim
[<string>]Usethevalueofthisattribute/claimasuniqueusername. Itisuptotheidentity
provider to guarantee the uniqueness. The OpenID specification only guarantees that Sub-
ject(’sub’)isunique. Alsomakesurethattheuserisnotallowedtochangethatattributeby
himself!
Sectiontype’pam’: Built-inPAMrealmconfigurationproperties.
Requiredproperties:
type
[pam|pbs|openid|ldap|ad]typeoftherealm
Optionalproperties:
comment
[<string>]Comment.
default
[<boolean> (default=false)] True if you want this to be the default realm selected on
login.
Sectiontype’pbs’: Built-inProxmoxBackupServerrealmconfigurationproperties.
Requiredproperties:
type
[pam|pbs|openid|ldap|ad]typeoftherealm
Optionalproperties:
comment
[<string>]Comment.
default
[<boolean> (default=false)] True if you want this to be the default realm selected on
login.
B.4 media-pool.cfg
B.4.1 FileFormat
Each entry starts with the header pool: <name>, followed by the media pool configuration op-
tions.
pool: company1
allocation always
retention overwrite
pool: ...
Youcanusetheproxmox-tape poolcommandtomanipulatethisfile.
270 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
B.4.2 Options
Optionalproperties:
allocation
[<string>]Mediasetallocationpolicy(’continue’,’always’,oracalendarevent).
comment
[<string>]Comment.
encrypt
[<string>]Tapeencryptionkeyfingerprint(sha256).
retention
[<string>]Mediaretentionpolicy(’overwrite’,’keep’,ortimespan).
template
[<string>]Mediasetnamingtemplate(maycontainstrftime()timeformatspecifications).
B.5 node.cfg
B.5.1 Options
Thefilecontainstheseoptions:
acme
TheACMEaccounttouseonthisnode.
acmedomain0
ACMEdomain.
acmedomain1
ACMEdomain.
acmedomain2
ACMEdomain.
acmedomain3
ACMEdomain.
acmedomain4
ACMEdomain.
http-proxy
Setproxyforaptandsubscriptionchecks.
email-from
Fallbackemailfromwhichnotificationswillbesent.
ciphers-tls-1.3
ListofTLSciphersforTLS1.3thatwillbeusedbytheproxy. Colon-separatedand
in descending priority (https://docs.openssl.org/master/man1/openssl-ciphers/).
(Proxyhastoberestartedforchangestotakeeffect.)
ciphers-tls-1.2
ListofTLSciphersforTLS<=1.2thatwillbeusedbytheproxy. Colon-separatedand
in descending priority (https://docs.openssl.org/master/man1/openssl-ciphers/).
(Proxyhastoberestartedforchangestotakeeffect.)
default-lang
DefaultlanguageusedintheGUI.
description
Nodedescription.
B.5. node.cfg 271

ProxmoxBackupDocumentation,Release4.2.8‐1
task-log-max-days
Maximumdaystokeeptasklogs.
Forexample:
acme: local
| acmedomain0: | first.domain.com   |     |     |     |
| ------------ | ------------------ | --- | --- | --- |
| acmedomain1: | second.domain.com  |     |     |     |
| acmedomain2: | third.domain.com   |     |     |     |
| acmedomain3: | fourth.domain.com  |     |     |     |
| acmedomain4: | fifth.domain.com   |     |     |     |
| http-proxy:  | internal.proxy.com |     |     |     |
| email-from:  | proxmox@mail.com   |     |     |     |
ciphers-tls-1.3: TLS_AES_128_GCM_SHA256:TLS_AES_128_CCM_8_SHA256:TLS_CHACHA20_POLY1305_SHA256
| ciphers-tls-1.2:   | RSA_WITH_AES_128_CCM:DHE_RSA_WITH_AES_128_CCM |              |     |     |
| ------------------ | --------------------------------------------- | ------------ | --- | --- |
| default-lang:      | en                                            |              |     |     |
| description:       | Primary                                       | PBS instance |     |     |
| task-log-max-days: | 30                                            |              |     |     |
Youcanusetheproxmox-backup-manager nodecommandtomanipulatethisfile.
B.6 notifications.cfg
B.6.1 FileFormat
Thisfilecontainsconfigurationfornotificationtargetsandnotificationmatchers.
B.6.2 Options
| Sectiontype’gotify’: |     | ConfigforGotifynotificationendpoints |     |     |
| -------------------- | --- | ------------------------------------ | --- | --- |
Requiredproperties:
server
[<string>]GotifyServerURL.
Optionalproperties:
comment
[<string>]Comment.
disable
[<boolean>]Disablethistarget.
filter
[<string>]Deprecated.
origin
[user-created|builtin|modified-builtin] The origin of a notification configuration
entry.
| Sectiontype’matcher’: |     | ConfigforSendmailnotificationendpoints |     |     |
| --------------------- | --- | -------------------------------------- | --- | --- |
Optionalproperties:
comment
[<string>]Comment.
disable
[<boolean>]Disablethismatcher.
invert-match
[<boolean>]Invertmatchofthewholefilter.
match-calendar
[<string>]Listofmatchedseveritylevels. Canbespecifiedmorethanonce.
match-field
[<string>]Listofmatchedmetadatafields. Canbespecifiedmorethanonce.
| 272 |     |     | AppendixB. | ConfigurationFiles |
| --- | --- | --- | ---------- | ------------------ |

ProxmoxBackupDocumentation,Release4.2.8‐1
match-severity
[<string>]Listofmatchedseveritylevels. Canbespecifiedmorethanonce.
mode
[all|any (default=all)]Themodeinwhichtheresultsofmatchesarecombined.
origin
[user-created|builtin|modified-builtin] The origin of a notification configuration
entry.
target
[<string>]Targetstonotify. Canbespecifiedmorethanonce.
Sectiontype’sendmail’: ConfigforSendmailnotificationendpoints
Optionalproperties:
author
[<string>]Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
comment
[<string>]Comment.
disable
[<boolean>]Disablethistarget.
filter
[<string>]Deprecated.
from-address
[<string>]FromaddressforsentE-Mails. Iftheparameterisnotset,thepluginwillfallback
totheemail-fromsettingfromnode.cfg(PBS).Ifthatisalsonotset,thepluginwilldefaultto
root@$hostname,where$hostnameisthehostnameofthenode.
mailto
[<string>]Mailaddresstosendamailto. Canbespecifiedmorethanonce.
mailto-user
[<string>] Users to send a mail to. The email address of the user will be looked up in
users.cfg. Canbespecifiedmorethanonce.
origin
[user-created|builtin|modified-builtin] The origin of a notification configuration
entry.
Sectiontype’smtp’: ConfigforSendmailnotificationendpoints
Requiredproperties:
from-address
[<string>]Fromaddressforthemail. SMTPrelaysmightrequirethatthisaddressisowned
by the user in order to avoid spoofing. The From header in the email will be set to $author
<$from-address>.
server
[<string>]HostnameorIPoftheSMTPrelay.
Optionalproperties:
author
[<string>]Authorofthemail. Defaultsto’ProxmoxBackupServer($hostname)’
comment
[<string>]Comment.
disable
[<boolean>]Disablethistarget.
B.6. notifications.cfg 273

ProxmoxBackupDocumentation,Release4.2.8‐1
mailto
[<string>]Mailaddresstosendamailto. Canbespecifiedmorethanonce.
mailto-user
[<string>] Users to send a mail to. The email address of the user will be looked up in
users.cfg. Canbespecifiedmorethanonce.
mode
[insecure|starttls|tls (default=tls)]Connectionsecurity
origin
[user-created|builtin|modified-builtin] The origin of a notification configuration
entry.
port
[<integer> (0 - 65535)] The port to connect to. If not set, the used port defaults to 25
(insecure),465(tls)or587(starttls),dependingonthevalueofmode
username
[<string>]Usernametouseduringauthentication. Ifnousernameisset,noauthentication
willbeperformed. ThePLAINandLOGINauthenticationmethodsaresupported
Sectiontype’webhook’: ConfigforWebhooknotificationendpoints
Requiredproperties:
method
[post|put|get (default=post)]HTTPMethodtouse.
url
[<string>]HTTP(s)urlwithoptionalport.
Optionalproperties:
body
[<string>]TheHTTPbodytosend. Supportstemplating.
comment
[<string>]Comment.
disable
[<boolean>]Disablethistarget.
header
[[name=<string> [,value=<string>]]]ArrayofHTTPheaders. Eachentryisaproperty
stringwithanameandavalue. Thevaluepropertycontainstheheaderinbase64encoding.
Supportstemplating. Canbespecifiedmorethanonce.
origin
[user-created|builtin|modified-builtin] The origin of a notification configuration
entry.
secret
[[name=<string> [,value=<string>]]]Arrayofsecrets. Eachentryisapropertystring
withanameandanoptionalvalue. Thevaluepropertycontainsthesecretinbase64encod-
ing. For any API endpoints returning the endpoint config, only the secret name but not the
valuewillbereturned. Whenupdatingtheconfig,alsosendallsecretsthatyouwanttokeep,
settingonlythenamebutnotthevalue. Canbeaccessedfromtemplates. Canbespecified
morethanonce.
B.7 notifications-priv.cfg
B.7.1 FileFormat
Thisfilecontainsprotectedcredentialsfornotificationtargets.
274 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
B.7.2 Options
Sectiontype ’gotify’: Privateconfigurationfor Gotifynotification endpoints. This config willbe
savedtoaseparateconfigurationfilewithstricterpermissions(root:root0600)
Requiredproperties:
token
[<string>]Authenticationtoken
Sectiontype’smtp’: PrivateconfigurationforSMTPnotificationendpoints. Thisconfigwillbesaved
toaseparateconfigurationfilewithstricterpermissions(root:root0600)
Optionalproperties:
password
[<string>]Thepasswordtouseduringauthentication.
Sectiontype’webhook’: PrivateconfigurationforWebhooknotificationendpoints. Thisconfigwill
besavedtoaseparateconfigurationfilewithstricterpermissions(root:root0600).
Optionalproperties:
secret
[[name=<string> [,value=<string>]]]Arrayofsecrets. Eachentryisapropertystring
withaname,andavalueproperty. Thevaluepropertycontainsthesecretinbase64encoding.
Canbeaccessedfromtemplates. Canbespecifiedmorethanonce.
B.8 prune.cfg
B.8.1 FileFormat
Eachentrystartswiththeheaderprune: <name>,followedbythejobconfigurationoptions.
prune: prune-store2
schedule mon..fri 10:30
store my-datastore
prune: ...
Youcanusetheproxmox-backup-manager prune-jobcommandtomanipulatethisfile.
B.8.2 Options
Requiredproperties:
schedule
[<calendar-event>]Runprunejobatspecifiedschedule.
store
[<string>]Datastorename.
Optionalproperties:
comment
[<string>]Comment.
disable
[<boolean> (default=false)]Disablethisjob.
max-depth
[<integer> (0 - 7)] How many levels of namespaces should be operated on (0 == no
recursion, empty == automatic full recursion, namespace depths reduce maximum allowed
value)
ns
[<string>]Namespace.
B.8. prune.cfg 275

ProxmoxBackupDocumentation,Release4.2.8‐1
keep-daily
[<integer> (1 - N)]Numberofdailybackupstokeep.
keep-hourly
[<integer> (1 - N)]Numberofhourlybackupstokeep.
keep-last
[<integer> (1 - N)]Numberofbackupstokeep.
keep-monthly
[<integer> (1 - N)]Numberofmonthlybackupstokeep.
keep-weekly
[<integer> (1 - N)]Numberofweeklybackupstokeep.
keep-yearly
[<integer> (1 - N)]Numberofyearlybackupstokeep.
B.9 tape.cfg
B.9.1 FileFormat
Each LTO drive configuration section starts with the header lto: <name>, followed by the drive
configurationoptions.
Tape changer configurations start with the header changer: <name>, followed by the changer
configurationoptions.
lto: hh8
changer sl3
path /dev/tape/by-id/scsi-10WT065325-nst
changer: sl3
export-slots 14,15,16
path /dev/tape/by-id/scsi-CJ0JBE0059
Youcanusetheproxmox-tape driveandproxmox-tape changercommandstomanipulate
thisfile.
(cid:174) Note
Thevirtual: drivetypeisexperimentalandshouldonlybeusedfordebugging.
B.9.2 Options
Sectiontype’changer’: SCSItapechanger
Requiredproperties:
path
[<string>]PathtoLinuxgenericSCSIdevice(e.g. ’/dev/sg4’)
Optionalproperties:
eject-before-unload
[<boolean> (default=false)]ifsettotrue,tapesareejectedmanuallybeforeunloading
export-slots
[[<integer>, ...]]Alistofslotnumbers,commaseparated. Thoseslotsarereservedfor
Import/Export,i.e. anymediainthoseslotsareconsideredtobe’offline’.
Sectiontype’lto’: LtoSCSItapedriver
Requiredproperties:
276 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
path
[<string>]ThepathtoaLTOSCSI-generictapedevice(i.e. ’/dev/sg0’)
Optionalproperties:
changer
[<string>]TapeChangerIdentifier.
changer-drivenum
[<integer> (0 - 255) (default=0)]Associatedchangerdrivenumber(requiresoption
changer)
Sectiontype’virtual’: Simulatetapedrives(onlyfortestanddebug)
Requiredproperties:
path
[<string>]Pathtodirectory
Optionalproperties:
max-size
[<integer> (0 - N)]Virtualtapesize
B.10 tape-job.cfg
B.10.1 FileFormat
Eachentrystartswiththeheaderbackup: <name>,followedbythejobconfigurationoptions.
backup: job1
drive hh8
pool p4
store store3
schedule daily
backup: ...
Youcanusetheproxmox-tape backup-jobcommandtomanipulatethisfile.
B.10.2 Options
Requiredproperties:
drive
[<string>]DriveIdentifier.
pool
[<string>]Mediapoolname.
store
[<string>]Datastorename.
Optionalproperties:
comment
[<string>]Comment.
schedule
[<calendar-event>]Runsyncjobatspecifiedschedule.
eject-media
[<boolean>]Ejectmediauponjobcompletion.
export-media-set
[<boolean>]Exportmediasetuponjobcompletion.
B.10. tape-job.cfg 277

ProxmoxBackupDocumentation,Release4.2.8‐1
group-filter
[[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>] List of
groupfilters. Canbespecifiedmorethanonce.
latest-only
[<boolean>]Backuplatestsnapshotsonly.
max-depth
[<integer> (0 - 7) (default=7)]Howmanylevelsofnamespacesshouldbeoperated
on(0==norecursion)
notification-mode
[legacy-sendmail|notification-system (default=notification-system)] Con-
figure how notifications for this datastore should be sent. legacy- sendmail sends email
notifications to the user configured in notify-user via the system’s sendmail executable.
notification-systememitsmatchablenotificationeventstothenotificationsystem.
notify-user
[<string>]UserID
ns
[<string>]Namespace.
worker-threads
[<integer> (1 - 32) (default=1)] The number of threads to use for the tape backup
job.
B.11 user.cfg
B.11.1 FileFormat
ThisfilecontainsthelistofAPIusersandAPItokens.
Eachuserconfigurationsectionstartswiththeheaderuser: <name>, followedbytheusercon-
figurationoptions.
APItokenconfigurationstartswiththeheadertoken: <userid!token_name>, followedbythe
token configuration. The data used to authenticate tokens is stored in a separate file (token.
shadow).
user: root@pam
comment Superuser
e.m.a.il test@example.local
token: root@pam!token1
comment API test token
enable true
expire 0
user: ...
Youcanusetheproxmox-backup-manager usercommandtomanipulatethisfile.
B.11.2 Options
Sectiontype’token’: ApiTokenproperties.
Optionalproperties:
comment
[<string>]Comment.
enable
[<boolean> (default=true)]Enabletheaccount(default). Youcansetthisto’0’todisable
theaccount.
278 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
expire
[<integer> (0 - N) (default=0)] Account expiration date (seconds since epoch). ’0’
meansnoexpirationdate.
Sectiontype’user’: Userproperties.
Optionalproperties:
comment
[<string>]Comment.
email
[<string>]E-MailAddress.
enable
[<boolean> (default=true)]Enabletheaccount(default). Youcansetthisto’0’todisable
theaccount.
expire
[<integer> (0 - N) (default=0)] Account expiration date (seconds since epoch). ’0’
meansnoexpirationdate.
firstname
[<string>]Firstname.
lastname
[<string>]Lastname.
B.12 remote.cfg
B.12.1 FileFormat
Thisfilecontainsinformationusedtoaccessremoteservers.
Eachentrystartswiththeheaderremote: <name>,followedbytheremoteconfigurationoptions.
remote: server1
host server1.local
a.u.t.h-id sync@pbs
remote: ...
Youcanusetheproxmox-backup-manager remotecommandtomanipulatethisfile.
B.12.2 Options
Requiredproperties:
password
[<string>]Passwordorauthtokenforremotehost(storedasbase64string).
auth-id
[<string>]AuthenticationID
host
[<string>]DNSnameorIPaddress.
Optionalproperties:
comment
[<string>]Comment.
fingerprint
[<string>]X509certificatefingerprint(sha256).
port
[<integer>]The(optional)port
B.12. remote.cfg 279

ProxmoxBackupDocumentation,Release4.2.8‐1
use-node-proxy
[<boolean> (default=false)] Use the http proxy configuration of the node for remote
connections.
B.13 sync.cfg
B.13.1 FileFormat
Eachentrystartswiththeheadersync: <name>,followedbythejobconfigurationoptions.
sync: job1
store store1
remote-store store1
remote lina
sync: ...
Youcanusetheproxmox-backup-manager sync-jobcommandtomanipulatethisfile.
B.13.2 Options
Requiredproperties:
remote-store
[<string>]Datastorename.
store
[<string>]Datastorename.
Optionalproperties:
active-encryption-key
[<string>]IDtouniquelyidentifyencryption/decriptionkey
associated-key
[<string>]Listofcryptographickeysassociatedwithsyncjob. Canbespecifiedmorethan
once.
comment
[<string>]Comment.
encrypted-only
[<boolean>]Onlysynchronizeencryptedbackupsnapshots,excludeothers.
group-filter
[[<exclude:|include:>]<type:<vm|ct|host>|group:GROUP|regex:RE>] List of
groupfilters. Canbespecifiedmorethanonce.
max-depth
[<integer> (0 - 7)] How many levels of namespaces should be operated on (0 == no
recursion, empty == automatic full recursion, namespace depths reduce maximum allowed
value)
ns
[<string>]Namespace.
owner
[<string>]AuthenticationID
remote
[<string>]RemoteID.
remote-ns
[<string>]Namespace.
280 AppendixB. ConfigurationFiles

ProxmoxBackupDocumentation,Release4.2.8‐1
remove-vanished
[<boolean> (default=false)] Delete vanished backups. This removes the local copy if
theremotebackupwasdeleted.
resync-corrupt
[<boolean>]Iftheverificationfailedforalocalsnapshot,trytopullitagain.
run-on-mount
[<boolean>]Runthisjobwhenarelevantdatastoreismounted.
schedule
[<calendar-event>]Runsyncjobatspecifiedschedule.
sync-direction
[pull|push (default=pull)]Directionofthesyncjob,pushorpull
transfer-last
[<integer> (1 - N)]LimittransfertolastNsnapshots(pergroup),skippingothers
unmount-on-done
[<boolean>] Unmount involved removable datastore after the sync job finishes. Requires
’run-on-mount’tobeenabled.
verified-only
[<boolean>]Onlysynchronizeverifiedbackupsnapshots,excludeothers.
worker-threads
[<integer> (1 - 32) (default=1)]Thenumberofworkerthreadstoprocessgroupsin
parallel.
burst-in
[<string>]Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
burst-out
[<string>]Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
rate-in
[<string>]Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
rate-out
[<string>]Bytesizewithoptionalunit(B,KB(base10),MB,GB,...,KiB(base2),MiB,Gib,...).
B.14 verification.cfg
B.14.1 FileFormat
Eachentrystartswiththeheaderverification: <name>,followedbythejobconfigurationop-
tions.
verification: verify-store2
ignore-verified true
outdated-after 7
schedule daily
store store2
verification: ...
Youcanusetheproxmox-backup-manager verify-jobcommandtomanipulatethisfile.
B.14.2 Options
Requiredproperties:
store
[<string>]Datastorename.
Optionalproperties:
B.14. verification.cfg 281

ProxmoxBackupDocumentation,Release4.2.8‐1
comment
[<string>]Comment.
ignore-verified
[<boolean> (default=true)]Donotverifybackupsthatarealreadyverifiediftheirverifi-
cationisnotoutdated.
max-depth
[<integer> (0 - 7) (default=7)]Howmanylevelsofnamespacesshouldbeoperated
on(0==norecursion)
ns
[<string>]Namespace.
outdated-after
[<integer> (0 - N)]Daysafterthataverificationbecomesoutdated. (0isdeprecated)’
read-threads
[<integer> (1 - 32) (default=1)]Thenumberofthreadstouseforreadingchunksin
verifyjob.
schedule
[<calendar-event>]Runverifyjobatspecifiedschedule.
verify-threads
[<integer> (1 - 32) (default=4)] The number of threads to use for verifying chunks
inverifyjob.
282 AppendixB. ConfigurationFiles

APPENDIX
C
FILE FORMATS
| C.1 Proxmox  | File Archive                                 | Format | (.pxar) |                    |
| ------------ | -------------------------------------------- | ------ | ------- | ------------------ |
| archive.pxar |                                              | ENTRY  |         | size: u64 = 64     |
|              | {XATTR}* extended attribute list             |        |         | type: u64 = ENTRY  |
|              | {ACL_USER}* USER ACL entries                 |        |         | feature_flags: u64 |
|              | {ACL_GROUP}* GROUP ACL entries               |        |         | mode: u64          |
|              | [ACL_GROUP_OBJ] the ACL_GROUP_OBJ            |        |         | flags: u64         |
|              | [ACL_DEFAULT] the various default ACL fields |        |         | uid: u64           |
|              | {ACL_DEFAULT_USER}* USER ACL entries         |        |         | gid: u64           |
|              | {ACL_DEFAULT_GROUP}* GROUP ACL entries       |        |         | mtime: u64         |
[FCAPS] file capability in Linux disk format
[QUOTA_PROJECT_ID] the ext4/xfs quota project ID
|             |                 |        | {DirectoryEntries}* | FILENAME       |
| ----------- | --------------- | ------ | ------------------- | -------------- |
|             | PAYLOAD SYMLINK | DEVICE |                     |                |
|             |                 |        | GOODBYE             | ENTRY HARDLINK |
| C.2 Proxmox | File Archive    | Format | ‐ Meta (.mpxar)     |                |
Pxar metadata archive with same structure as a regular pxar archive, with the exception of regu-
lar file payloads not being contained within the archive itself, but rather being stored as payload
referencestothecorrespondingpxarpayload(.ppxar)file.
Canbeusedtolookupallthearchiveentriesandmetadatawithoutthesizeoverheadintroduced
bythefilepayloads.
283

ProxmoxBackupDocumentation,Release4.2.8‐1
| archive.mpxar | FORMAT_VERSION |     |     |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
PRELUDE
|     | ENTRY                                        |     |     |     |     |     | size: u64 = 64     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- |
|     | {XATTR}* extended attribute list             |     |     |     |     |     | type: u64 = ENTRY  |     |
|     | {ACL_USER}* USER ACL entries                 |     |     |     |     |     | feature_flags: u64 |     |
|     | {ACL_GROUP}* GROUP ACL entries               |     |     |     |     |     | mode: u64          |     |
|     | [ACL_GROUP_OBJ] the ACL_GROUP_OBJ            |     |     |     |     |     | flags: u64         |     |
|     | [ACL_DEFAULT] the various default ACL fields |     |     |     |     |     | uid: u64           |     |
|     | {ACL_DEFAULT_USER}* USER ACL entries         |     |     |     |     |     | gid: u64           |     |
|     | {ACL_DEFAULT_GROUP}* GROUP ACL entries       |     |     |     |     |     | mtime: u64         |     |
[FCAPS] file capability in Linux disk format
|     | [QUOTA_PROJECT_ID] the ext4/xfs quota project ID |     |     |     |     |     | FILENAME |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- |
{DirectoryEntries}*
|     | PAYLOAD_REF |     | SYMLINK | DEVICE |     |     | ENTRY | HARDLINK |
| --- | ----------- | --- | ------- | ------ | --- | --- | ----- | -------- |
GOODBYE
offset: u64
size: u64
| C.3 Proxmox | File Archive |     | Format | ‐ Payload | (.ppxar) |     |     |     |
| ----------- | ------------ | --- | ------ | --------- | -------- | --- | --- | --- |
Pxarpayloadfilestoringregularfilepayloadstobereferencedandaccessedbythecorresponding
pxarmetadata(.mpxar)archive. Containsaconcatenationofregularfilepayloads,eachprefixed
byaPAYLOADheader. Further,theactualreferencedpayloadentriesmightbeseparatedbypadding
(full/partial payloads not referenced), introducedwhen reusingchunks of a previous backup run,
whenchunkboundariesdidnotalignedtopayloadentryoffsets.
Allheadersarestoredaslittle-endian.
PAYLOAD_START_MARKEhReaderof [u8; 16]consistingoftypehashandsize;marksstart
PAYLOAD header of [u8; 16] consisting of type hash and size; referenced by
metadataarchive
| Payload | rawregularfilepayload |     |     |     |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
Padding partial/full unreferenced payloads, caused by unaligned chunk bound-
ary
| ... | furtherconcatenationofpayloadheader,payloadandpadding |     |     |     |     |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
PAYLOAD_TAIL_MARKERheaderof [u8; 16]consistingoftypehashandsize;marksend
| C.4 Proxmox | Catalog | File | Format | (.pcat1) |     |     |     |     |
| ----------- | ------- | ---- | ------ | -------- | --- | --- | --- | --- |
Thecatalogfileusesthefollowingstructure:
| MAGIC: [u8;  | 8]  |     | [145, 253,             | 96, 249,   | 196, | 103,          | 88, 213]. |     |
| ------------ | --- | --- | ---------------------- | ---------- | ---- | ------------- | --------- | --- |
| CATALOG_DATA |     |     | Catalogdatatable.      | SeeCatalog |      | Datacontents. |           |     |
| ...          |     |     | Morecatalogdatatables. |            |      |               |           |     |
ROOT_START_OFFSET: Pointsatthestartofthe’/’catalogentry. Storedaslittle-endian.
u64
| 284 |     |     |     |     |     |     | AppendixC. | FileFormats |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
C.4.1 CatalogDataTables
Eachtablerepresentsthecontentsofasingledirectory.
TABLE_LENGTH: Totallengthofthecontentsinsidethistable.
u64*
ENTRY_COUNT: u64* Numberofentriespresentinthetable.
ENTRIES Concatenated ENTRY_COUNT ENTRY structures (see the ENTRY layout
.).
C.4.2 CatalogTableEntries
Eachentryconsistsofthelengthandvalueofitsname. Additionally,fileanddirectorytypeen-
triescontainaPAYLOADfield. Fordirectoryentries,theoffset_backpayloadstoresthebackward
bytedistancefromthestartoftheparentdirectorytabletothestartofthereferencedchilddirec-
torytable. Thestartoffsetofthechilddirectorytablecanbecomputedasparent_table_start
- offset_back.
ENTRY_TYPE: u8 Thetypeofentry(seeentrytypes).
NAME_LENGTH: u64* Lengthoffileordirectoryname. Storedasvari-
ablelengthencodedu64.
NAME: [u8] TherawUTF-8stringbytesofthename.
PAYLOAD BytesbasedonENTRY_TYPE
• Directory (’d’): offset_back: u64*
(Child-to-Parentoffsetdistance.)
• File (’f’): size: u64* followed by
mtime: i64*
C.4.3 EntryTypes:
d Directory
f File
l Symlink
h Hardlink
b Blockdevice
c Chardevice
p FIFO
s Socket
C.4.4 VariableLengthEncoding:
Theasterisknotationindicatesvariable-lengthintegers:
• u64*: Unsigned variable-length integer. Each encoded byte is 8 bits wide. Bit 7, the most
significant bit, is the continuation flag. Bits 0 through 6 carry value bits. The first encoded
byte stores the lowest order 7 value bits, the second encoded byte stores the next 7 value
bits,andsoon.
• i64*: Signedvariable-lengthinteger. Eachnonzeroencodedbyteis8bitswide. Bit7,themost
significantbit,isthecontinuationflag. Bits0through6carryvaluebits. Thefirstencodedbyte
storesthelowest-order7valuebits,thesecondencodedbytestoresthenext7valuebits,and
soon. Non-negativevaluesendwithabytewhosecontinuationflagisclear. Negativevalues
endwithanadditional0x00terminatorbyte.
C.4. ProxmoxCatalogFileFormat(.pcat1) 285

ProxmoxBackupDocumentation,Release4.2.8‐1
| C.5 | Data | Blob | Format |     | (.blob) |     |     |     |     |     |
| --- | ---- | ---- | ------ | --- | ------- | --- | --- | --- | --- | --- |
The data blob format is used to store small binary data. The magic number decides the exact
format:
[66, 171, 56, 7, 190, 131, 112, 161] unencrypted uncompressed
|     | [49,  | 185, | 88,  | 66,  | 111,     | 182, 163, | 127] | unencrypted | compressed   |     |
| --- | ----- | ---- | ---- | ---- | -------- | --------- | ---- | ----------- | ------------ | --- |
|     | [123, | 103, | 133, |      | 190, 34, | 45, 76,   | 240] | encrypted   | uncompressed |     |
|     | [230, | 89,  | 27,  | 191, | 11,      | 191, 216, | 11]  | encrypted   | compressed   |     |
Thecompressionalgorithmusediszstd. TheencryptioncipherisAES_256_GCM.
Unencryptedblobsusethefollowingformat:
|     |     |     |     |     |     | MAGIC:     | [u8; 8] |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | --- | --- |
|     |     |     |     |     |     | CRC32:     | [u8; 4] |     |     |     |
|     |     |     |     |     |     | Data: (max | 16MiB)  |     |     |     |
Encrypted blobs additionally contain a 16 byte initialization vector (IV), followed by a 16 byte au-
thenticatedencryption(AE)tag,followedbytheencrypteddata:
|     |       |       |     |        |         | MAGIC:     | [u8; 8] |     |     |     |
| --- | ----- | ----- | --- | ------ | ------- | ---------- | ------- | --- | --- | --- |
|     |       |       |     |        |         | CRC32:     | [u8; 4] |     |     |     |
|     |       |       |     |        |         | IV: [u8;   | 16]     |     |     |     |
|     |       |       |     |        |         | TAG: [u8;  | 16]     |     |     |     |
|     |       |       |     |        |         | Data: (max | 16MiB)  |     |     |     |
| C.6 | Fixed | Index |     | Format | (.fidx) |            |         |     |     |     |
Allnumbersarestoredaslittle-endian.
| MAGIC:      |      | [u8; 8] |     | [47,                                  | 127, | 65, 237, | 145, | 253, 15, | 205]     |         |
| ----------- | ---- | ------- | --- | ------------------------------------- | ---- | -------- | ---- | -------- | -------- | ------- |
| uuid:       | [u8; | 16],    |     | UniqueID                              |      |          |      |          |          |         |
| ctime:      |      | i64,    |     | CreationTime(epoch)                   |      |          |      |          |          |         |
| index_csum: |      | [u8;    |     | SHA-256                               |      | over     | the  | index    | (without | header) |
| 32],        |      |         |     | SHA256(digest1||digest2||...)         |      |          |      |          |          |         |
| size:       | u64, |         |     | Imagesize                             |      |          |      |          |          |         |
| chunk_size: |      | u64,    |     | Chunksize                             |      |          |      |          |          |         |
| reserved:   |      | [u8;    |     | Overallheadersizeisonepage(4096bytes) |      |          |      |          |          |         |
4016],
| digest1: |         | [u8; | 32]   | Firstchunkdigest   |     |         |     |     |     |     |
| -------- | ------- | ---- | ----- | ------------------ | --- | ------- | --- | --- | --- | --- |
| digest2: |         | [u8; | 32]   | Secondchunkdigest  |     |         |     |     |     |     |
| ...      |         |      |       | Nextchunkdigest... |     |         |     |     |     |     |
| C.7      | Dynamic |      | Index | Format             |     | (.didx) |     |     |     |     |
Allnumbersarestoredaslittle-endian.
| 286 |     |     |     |     |     |     |     |     | AppendixC. | FileFormats |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- |

ProxmoxBackupDocumentation,Release4.2.8‐1
| MAGIC: [u8; | 8] [28,                                         | 145, 78, | 165, 25, | 186, 179, | 205]     |         |
| ----------- | ----------------------------------------------- | -------- | -------- | --------- | -------- | ------- |
| uuid: [u8;  | 16], UniqueID                                   |          |          |           |          |         |
| ctime: i64, | CreationTime(epoch)                             |          |          |           |          |         |
| index_csum: | SHA-256                                         |          | over     | the index | (without | header) |
| [u8; 32],   | SHA256(offset1||digest1||offset2||digest2||...) |          |          |           |          |         |
| reserved:   | [u8; Overallheadersizeisonepage(4096bytes)      |          |          |           |          |         |
4032],
| offset1: | u64 Endoffirstchunk   |     |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- | --- |
| digest1: | [u8; Firstchunkdigest |     |     |     |     |     |
32]
| offset2: | u64 Endofsecondchunk   |     |     |     |     |     |
| -------- | ---------------------- | --- | --- | --- | --- | --- |
| digest2: | [u8; Secondchunkdigest |     |     |     |     |     |
32]
| ...                            | Nextchunkoffset/digest |     |     |     |     |     |
| ------------------------------ | ---------------------- | --- | --- | --- | --- | --- |
| C.7. DynamicIndexFormat(.didx) |                        |     |     |     |     | 287 |

ProxmoxBackupDocumentation,Release4.2.8‐1
| 288 | AppendixC. | FileFormats |
| --- | ---------- | ----------- |

APPENDIX
D
BACKUP PROTOCOL
ProxmoxBackupServerusesaREST-basedAPI.WhilethemanagementinterfaceusesnormalHTTP,
the actual backup and restore interface uses HTTP/2 for improved performance. Both HTTP and
HTTP/2arewellknownstandards,sothefollowingsectionassumesthatyouarefamiliarwithhow
tousethem.
D.1 Backup Protocol API
Tostartanewbackup,theAPIcallGET /api2/json/backupneedstobeupgradedtoaHTTP/2
connectionusingproxmox-backup-protocol-v1astheprotocolname:
GET /api2/json/backup HTTP/1.1
UPGRADE: proxmox-backup-protocol-v1
TheserverreplieswiththeHTTP 101 Switching Protocolstatuscode,andyoucanthenissue
RESTcommandsontheupdatedHTTP/2connection.
Thebackupprotocolallowsyoutouploadthreedifferentkindoffiles:
• Chunksandblobs(binarydata)
• Fixedindexes(Listofchunkswithfixedsize)
• Dynamicindexes(Listofchunkswithvariablesize)
Thefollowingsectionprovidesashortintroductiononhowtouploadsuchfiles. PleaseusetheAPI
ViewerfordetailsabouttheavailableRESTcommands.
D.1.1 UploadBlobs
BlobsareuploadedusingPOST /blob. TheHTTPbodycontainsthedataencodedasDataBlob.
Thefilenamemustendwith.blobandmustbeaddedtothebackupmanifest,whichisuploaded
asadedicatedindex.json.blobbeforethecalltoPOST /finish. Blobsnotuploadedaspart
ofthebackupprotocol,forexampleclientlogs,arenottrackedbythemanifest.
D.1.2 UploadChunks
Chunks belong to an index, so you first need to open an index (see below). After that, you can
uploadchunksusingPOST /fixed_chunkandPOST /dynamic_chunk. TheHTTPbodycontains
thechunkdataencodedasDataBlob).
D.1.3 UploadFixedIndexes
Fixed indexes are used to store VM image data. The VM image is split into equally sized chunks,
whichareuploadedindividually. Theindexfilesimplycontainsalistofchunkdigests.
289

ProxmoxBackupDocumentation,Release4.2.8‐1
You create a fixed index with POST /fixed_index. Then, upload chunks with POST /
fixed_chunk,andappendthemtotheindexwithPUT /fixed_index. Whenfinished,youneed
toclosetheindexusingPOST /fixed_close.
Thefilenameneedstoendwith.fidx,andmustbeaddedtothebackupmanifest,whichisup-
loadedasadedicatedindex.json.blobbeforethecalltoPOST /finish.
D.1.4 UploadDynamicIndexes
Dynamicindexesareusedtostorefilearchivedata. Thearchivedataissplitintodynamicallysized
chunks,whichareuploadedindividually. Theindexfilesimplycontainsalistofchunkdigestsand
offsets.
YoucancreateadynamicallysizedindexwithPOST /dynamic_index. Then,uploadchunkswith
POST /dynamic_chunk, and append them to the index with PUT /dynamic_index. When fin-
ished,youneedtoclosetheindexusingPOST /dynamic_close.
The filename needs to end with .didx, and must be added to the backup manifest, which is up-
loadedasadedicatedindex.json.blobbeforethecalltoPOST /finish.
D.1.5 FinishBackup
Onceyouhaveuploadedalldata,youneedtocallPOST /finish. Thiscommitsalldata,verifies
andpersiststhemanifestandendsthebackupprotocol.
D.2 Restore/Reader Protocol API
To start a new reader, the API call GET /api2/json/reader needs to be upgraded to a HTTP/2
connectionusingproxmox-backup-reader-protocol-v1asprotocolname:
GET /api2/json/reader HTTP/1.1
UPGRADE: proxmox-backup-reader-protocol-v1
TheserverreplieswiththeHTTP 101 Switching Protocolstatuscode,andyoucanthenissue
RESTcommandsonthatupdatedHTTP/2connection.
Thereaderprotocolallowsyoutodownloadthreedifferentkindsoffiles:
• Chunksandblobs(binarydata)
• Fixedindexes(listofchunkswithfixedsize)
• Dynamicindexes(listofchunkswithvariablesize)
Thefollowingsectionprovidesashortintroductiononhowtodownloadsuchfiles. Pleaseusethe
APIViewerfordetailsabouttheavailableRESTcommands.
D.2.1 DownloadBlobs
BlobsaredownloadedusingGET /download. TheHTTPbodycontainsthedataencodedasData
Blob.
D.2.2 DownloadChunks
Chunks are downloaded using GET /chunk. The HTTP body contains the data encoded as Data
Blob.
290 AppendixD. BackupProtocol

ProxmoxBackupDocumentation,Release4.2.8‐1
D.2.3 DownloadIndexFiles
IndexfilesaredownloadedusingGET /download. TheHTTPbodycontainsthedataencodedas
FixedIndexorDynamicIndex.
D.2. Restore/ReaderProtocolAPI 291

ProxmoxBackupDocumentation,Release4.2.8‐1
| 292 | AppendixD. | BackupProtocol |
| --- | ---------- | -------------- |

APPENDIX
E
CALENDAR EVENTS
| E.1 Introduction and | Format |     |
| -------------------- | ------ | --- |
Certaintasks,forexamplepruningandgarbagecollection,needtobeperformedonaregularbasis.
Proxmox Backup Server uses a format inspired by the systemd Time and Date Specification (see
systemd.timemanpage)calledcalendareventsforitsschedules.
Calendareventsareexpressionstospecifyoneormorepointsintime. Theyaremostlycompatible
withsystemd’scalendarevents.
Thegeneralformatisasfollows:
|     | Listing1: Calendarevent |     |
| --- | ----------------------- | --- |
[WEEKDAY] [[YEARS-]MONTHS-DAYS] [HOURS:MINUTES[:SECONDS]]
Notethatthereeitherhastobeatleastaweekday,dateortimepart. Iftheweekdayordatepartis
omitted,all(week)daysareincluded. Ifthetimepartisomitted,thetime00:00:00isimplied. (e.g.
’2020-01-01’refersto’2020-01-0100:00:00’)
WeekdaysarespecifiedwiththeabbreviatedEnglishversion: mon,tue,wed,thu,fri,sat,sun.
Eachfieldcancontainmultiplevaluesinthefollowingformats:
• comma-separated: e.g.,01,02,03
• asarange: e.g.,01..10
• asarepetition: e.g,05/10(meansstartingat5every10)
• andacombinationoftheabove: e.g.,01,05..10,12/02
• ora*foreverypossiblevalue: e.g.,*:00
Therearesomespecialvaluesthathaveaspecificmeaning:
| Value             |                 | Syntax                   |
| ----------------- | --------------- | ------------------------ |
| minutely          |                 | *-*-**:*:00              |
| hourly            |                 | *-*-**:00:00             |
| daily             |                 | *-*-*00:00:00            |
| weekly            |                 | mon*-*-*00:00:00         |
| monthly           |                 | *-*-0100:00:00           |
| yearly orannually |                 | *-01-0100:00:00          |
| quarterly         |                 | *-01,04,07,10-0100:00:00 |
| semiannually      | orsemi-annually | *-01,07-0100:00:00       |
Hereisatablewithsomeusefulexamples:
293

ProxmoxBackupDocumentation,Release4.2.8‐1
| Example                     | Alternative | Explanation                    |     |     |
| --------------------------- | ----------- | ------------------------------ | --- | --- |
| mon,tue,wed,thu,mfrion..fri |             | Everyworkingdayat00:00         |     |     |
| sat,sun                     | sat..sun    | Onlyonweekendsat00:00          |     |     |
| mon,wed,fri                 | --          | Monday,Wednesday,Fridayat00:00 |     |     |
| 12:05                       | --          | Everydayat12:05PM              |     |     |
| *:00/5                      | 0/1:0/5     | Everyfiveminutes               |     |     |
mon..wed mon,tue,wed Monday, Tuesday, Wednesday30, 40and50minutesafterev-
| *:30/10 | *:30/10 | eryfullhour |     |     |
| ------- | ------- | ----------- | --- | --- |
mon..fri -- Every working day every 15 minutes between 8 AM and 6 PM
| 8..17,22:0/15 |     | andbetween10PMand11PM |     |     |
| ------------- | --- | --------------------- | --- | --- |
fri12..13:5/20 fri12,13:5/20 Fridayat12:05,12:25,12:45,13:05,13:25and13:45
12,14,16,18,20,221:52/2:5 Everydaystartingat12:05until22:05,every2hours
| *:*        | 0/1:0/1 | Everyminute(minimuminterval)  |     |     |
| ---------- | ------- | ----------------------------- | --- | --- |
| *-05       | --      | Onthe5thdayofeveryMonth       |     |     |
| Sat *-1..7 | --      | FirstSaturdayeachMonthat15:00 |     |     |
15:00
| 2015-10-21      | --         | 21stOctober2015at00:00 |     |     |
| --------------- | ---------- | ---------------------- | --- | --- |
| E.2 Differences | to systemd |                        |     |     |
Notallfeaturesofsystemdcalendareventsareimplemented:
• no Unix timestamps (e.g. @12345): instead use date and time to specify a specific point in
time
| • notimezone: | allschedulesusethetimezoneoftheserver |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- |
• nosub-secondresolution
| • noreversedaysyntax(e.g.   |               | 2020-03~01) |     |     |
| --------------------------- | ------------- | ----------- | --- | --- |
| • norepetitionofranges(e.g. |               | 1..10/2)    |     |     |
| E.3 Notes                   | on Scheduling |             |     |     |
InProxmoxBackup,schedulingformosttasksisdoneintheproxmox-backup-proxy. Thisdaemon
checksalljobscheduleseveryminute,toseeifanyaredue. Thismeansthateventhoughcalendar
eventscancontainseconds,itwillonlybecheckedonceperminute.
Also,allscheduleswillbecheckedagainstthetimezonesetintheProxmoxBackupServer.
| 294 |     |     | AppendixE. | CalendarEvents |
| --- | --- | --- | ---------- | -------------- |

APPENDIX
F
MARKDOWN PRIMER
”Markdownisatext-to-HTMLconversiontoolforwebwriters. Markdownallowsyouto
writeusinganeasy-to-read,easy-to-writeplaintextformat,thenconvertittostructurally
validXHTML(orHTML).”
—JohnGruber,https://daringfireball.net/projects/markdown/
The”Notes”paneloftheProxmoxBackupServerweb-interfacesupportsrenderingMarkdowntext.
ProxmoxBackupServersupportsCommonMarkwithmostextensionsofGFM(GitHubFlavoured
Markdown),liketablesortask-lists.
F.1 Markdown Basics
Notethatweonlydescribethebasicshere. Pleasesearchthewebformoreextensiveresources,
forexampleonhttps://www.markdownguide.org/
F.1.1 Headings
# This is a Heading h1
## This is a Heading h2
##### This is a Heading h5
F.1.2 Emphasis
Use*text*or_text_foremphasis.
Use**text**or__text__forbold,heavy-weighttext.
Combinationsarealsopossible,forexample:
_You **can** combine them_
F.1.3 Links
You can use automatic detection of links. For example, https://forum.proxmox.com/ would
transformitintoaclickablelink.
Youcanalsocontrolthelinktext,forexample:
Now, [the part in brackets will be the link text](https://forum.proxmox.com/).
F.1.4 Lists
UnorderedLists
Use*or-forunorderedlists,forexample:
295

ProxmoxBackupDocumentation,Release4.2.8‐1
* Item 1
* Item 2
* Item 2a
* Item 2b
Youcancreatenestedlistsbyaddingindentation.
OrderedLists
1. Item 1
1. Item 2
1. Item 3
| 1. Item | 3a  |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
| 1. Item | 3b  |     |     |     |     |     |     |
NOTE:Theintegeroforderedlistsdoesnotneedtobecorrect,theywillbenumberedautomatically.
TaskLists
Tasklistsuseaemptybox[ ]forunfinishedtasksandaboxwithanX forfinishedtasks.
Forexample:
| - [X] First  | task already | done!       |     |     |     |     |     |
| ------------ | ------------ | ----------- | --- | --- | --- | --- | --- |
| - [X] Second | one too      |             |     |     |     |     |     |
| - [ ] This   | one is       | still to-do |     |     |     |     |     |
| - [ ] So     | is this one  |             |     |     |     |     |     |
F.1.5 Tables
Tablesusethepipesymbol|toseparatecolumns,and-toseparatethetableheaderfromthetable
body. Inthatseparation,youcanalsosetthetextalignment,makingonecolumnleft-,center-,or
right-aligned.
| Left columns | Right columns | Some | More | Cols.| Centering Works Too
| ------------- |--------------:|--------|------|------|:------------------:|
| | left | foo | | right foo | | First  | | Row | Here  | | >center< |     | |   |
| ------ | ----- | --------- | -------- | ------------- | ---------- | --- | --- |
| | left | bar | | right bar | | Second | | Row | Here  | | 12345    |     | |   |
| | left | baz | | right baz | | Third  | | Row | Here  | | Test     |     | |   |
| | left | zab | | right zab | | Fourth | | Row | Here  | | ☁☁☁      |     | |   |
| | left | rab | | right rab | | And    | | Last | Here | | The End  |     | |   |
Note that you do not need to align the columns nicely with white space, but that makes editing
tableseasier.
F.1.6 BlockQuotes
Youcanenterblockquotesbyprefixingalinewith>,similarasinplain-textemails.
> Markdown is a lightweight markup language with plain-text-formatting syntax,
| > created | in 2004 | by John Gruber | with Aaron | Swartz. |     |     |     |
| --------- | ------- | -------------- | ---------- | ------- | --- | --- | --- |
>
>> Markdown is often used to format readme files, for writing messages in online discussion␣
,→forums,
| >> and | to create rich | text using | a plain | text editor. |     |     |     |
| ------ | -------------- | ---------- | ------- | ------------ | --- | --- | --- |
F.1.7 CodeandSnippets
Youcanusebacktickstoavoidprocessingagroupofwordsorparagraphs. Thisisusefulforpre-
ventingacodeorconfigurationhunkfrombeingmistakenlyinterpretedasmarkdown.
InlineCode
Surroundingpartofalinewithsinglebackticksallowsyoutowritecodeinline,forexamples:
| This hosts | IP address | is `10.0.0.1`. |     |     |     |            |                |
| ---------- | ---------- | -------------- | --- | --- | --- | ---------- | -------------- |
| 296        |            |                |     |     |     | AppendixF. | MarkdownPrimer |

ProxmoxBackupDocumentation,Release4.2.8‐1
EntireBlocksofCode
Forcodeblocksspanningseverallines,youcanusetriple-backtickstostartandendsuchablock,
forexample:
```
| # This is | the network config | I want to remember | here |
| --------- | ------------------ | ------------------ | ---- |
auto vmbr2
| iface vmbr2       | inet static |     |     |
| ----------------- | ----------- | --- | --- |
| address           | 10.0.0.1/24 |     |     |
| bridge-ports      | ens20       |     |     |
| bridge-stp        | off         |     |     |
| bridge-fd         | 0           |     |     |
| bridge-vlan-aware |             | yes |     |
| bridge-vids       | 2-4094      |     |     |
```
F.1. MarkdownBasics 297

ProxmoxBackupDocumentation,Release4.2.8‐1
| 298 | AppendixF. | MarkdownPrimer |
| --- | ---------- | -------------- |

APPENDIX
G
GLOSSARY
Virtualmachine
Avirtualmachineisaprogramthatcanexecuteanentireoperatingsysteminsideanemulated
hardwareenvironment.
Container
A container is an isolated user space. Programs run directly on the host’s kernel, but with
limitedaccesstothehost’sresources.
Datastore
Aplacetostorebackups. Adirectorywhichcontainsthebackupdata. Thecurrentimplemen-
tationisfile-systembased.
Rust
Rustisanew,fastandmemory-efficientsystemprogramminglanguage. Ithasnoruntimeor
garbage collector. Rust’s rich type system and ownership model guarantee memory-safety
andthread-safety. Thiscaneliminatemanyclassesofbugsatcompile-time.
Sphinx
Isatoolthatmakesiteasytocreateintelligentandnicelyformatteddocumentation. Itwas
originallycreatedforthedocumentationofthePythonprogramminglanguage. Ithasexcel-
lentfacilitiesforthedocumentationofsoftwareprojectsinarangeoflanguages.
reStructuredText
Isaneasy-to-read,what-you-see-is-what-you-get,plaintextmarkupsyntaxandparsersystem.
FUSE
FilesysteminUserspace(FUSE)definesaninterfacewhichmakesitpossibletoimplementa
filesysteminuserspaceas opposedto implementingitin thekernel. Thefuse kerneldriver
handlesfilesystemrequestsandsendsthemtoauserspaceapplication.
Remote
A remote Proxmox Backup Server installation and credentials for a user on it. You can pull
datastoresfromaremotetoalocaldatastoreinordertohaveredundantbackups.
299

ProxmoxBackupDocumentation,Release4.2.8‐1
| 300 | AppendixG. | Glossary |
| --- | ---------- | -------- |

APPENDIX
H
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
301

ProxmoxBackupDocumentation,Release4.2.8‐1
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
302 AppendixH. GNUFreeDocumentationLicense

ProxmoxBackupDocumentation,Release4.2.8‐1
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
303

ProxmoxBackupDocumentation,Release4.2.8‐1
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
304 AppendixH. GNUFreeDocumentationLicense

ProxmoxBackupDocumentation,Release4.2.8‐1
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
305

ProxmoxBackupDocumentation,Release4.2.8‐1
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
306 AppendixH. GNUFreeDocumentationLicense

INDEX
C
Container,299
D
Datastore,299
F
FUSE,299
R
Remote,299
reStructuredText,299
Rust,299
S
Sphinx,299
V
Virtual machine,299
307