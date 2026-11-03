| Proxmox | Offline | Mirror | Documentation |         |       |
| ------- | ------- | ------ | ------------- | ------- | ----- |
|         |         |        |               | Release | 0.8.0 |
|         |         |        | Proxmox       | Support | Team  |
Tuesday,20October2026

TABLE OF CONTENTS
1 Introduction 2
1.1 WhatisProxmoxOfflineMirror? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 TechnicalOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 GettingHelp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4.1 EnterpriseSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4.2 CommunitySupportForum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4.3 MailingLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4.4 BugTracker . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.5 License . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Installation 5
2.1 SystemRequirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 InstallationviaAPT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2.1 DebianPackageRepositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2.2 SecureApt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2.3 SetuptheRepositoryonnonProxmoxbasedsystems . . . . . . . . . . . . . . 6
3 OfflineSubscriptionKeys 8
3.1 MinimumVersionsforOfflineActivation . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 SetupOfflineMirrorKey . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.3 GatherServerIDs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.4 Register&RefreshKeys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.5 DeployKeys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4 OfflineRepositoryMirrors 10
4.1 SettingUpaMirror . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2 SyncingaMirror . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.3 VerifyMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.4 RequestTimeouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.5 LatestSnapshotSymlink . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.6 NamedSnapshots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.7 ReducingMirrorScope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.8 PruningSnapshots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.9 ComparingSnapshots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.10 SpaceManagement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.11 VerifyingPoolIntegrity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.12 GlobalOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.13 EnvironmentVariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
5 OfflineMedia 17
5.1 SettingUpaMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.2 SyncingaMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.3 UsingaMedium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.3.1 Example: LocalMountPoint. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
i

5.3.2 Example: LocalHTTPServer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
5.4 ActivatingaSubscriptionKey . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
A CommandSyntax 20
A.1 proxmox-offline-mirror . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
A.2 proxmox-offline-mirror-helper . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
B JSONCommandOutput 33
C ConfigurationFiles 38
C.1 proxmox-offline-mirror.cfg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
C.1.1 Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
D GNUFreeDocumentationLicense 40
ii

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Copyright(C)2022-2024,ProxmoxServerSolutionsGmbH
Version0.8.0--Tuesday,20October2026
Permissionisgrantedtocopy,distributeand/ormodifythisdocumentunderthetermsoftheGNU
FreeDocumentationLicense,Version1.3oranylaterversionpublishedbytheFreeSoftwareFoun-
dation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
licenseisincludedinthesectionentitled”GNUFreeDocumentationLicense”.
TABLEOFCONTENTS 1

CHAPTER
ONE
INTRODUCTION
1.1 What is Proxmox Offline Mirror?
With the Proxmox Offline Mirror tool, you can manage a local apt mirror for all package updates
forProxmoxandDebianprojects. Fromthislocalaptmirroryoucancreateanexternalmedium,
for example a USB flash drive or a local network share, to update systems which cannot access
thepackagerepositoriesdirectlyviatheinternet. Suchsystemsmightberestrictedbypoliciesto
accessthepublicinternetorarecompletelyair-gapped. Finally,youcanalsomanagesubscriptions
forsuchrestrictedhosts.
Thistoolconsistsoftwobinaries:
proxmox-offline-mirror
Themirrortooltocreateandmanagemirrorsandmediacontainingrepositories
proxmox-offline-mirror-helper
The helper to use the external medium on offline Proxmox VE, Proxmox Mail Gateway or
ProxmoxBackupServersystemsaswellasmanagingsubscriptionsonthesesystems.
1.2 Terminology
Therearethreebasicentitytypesavailableforconfiguration:
keys
Subscriptionkeysareeitherforthemirroringsystemitself,orfortheofflinesystems.
Theyareconfiguredwithproxmox-offline-mirror key ...
mirrors
A mirror consists of the metadata of an upstream repository and a local path where snap-
shotsoftheupstreamrepositoryarestored.
• configuredwithproxmox-offline-mirror config mirror ...
• usedwithproxmox-offline-mirror mirror ...
snapshots
Point-in-timeviewofamirror. Snapshotsconsistofhardlinksintotheunderlyingstoragepool
toreducethediskspacerequirements.
media
Amediumconsistingoflocalmirrorsandapathwherethemirrorsaresyncedto
• configuredwithproxmox-offline-mirror config media ...
• usedwithproxmox-offline-mirror medium ...
2

ProxmoxOfflineMirrorDocumentation,Release0.8.0
1.3 Technical Overview
Behindthescenes,oneormorepoolsconsistingof
• apooldirectorycontainingchecksumfiles(e.g.,sha256/3dc7bc5f82cdcc4ea0f69dd30d5f6bb19e0ccc36f4a79c865eed0e7a370cd5e4)
• alinkdirectorycontainingdirectoriesandhardlinkstothechecksumfilesinsidethepooldi-
rectory
are used to store the repository contents (”snapshots”) of repository mirrors in a space-efficient
way.
When adding a file, the following steps are done: first the checksum file(s) are added, then they
are linked under one or more paths. A garbage collect operation will iterate over all files in the
linkdirectoryandremovethose, whicharenot(ornolonger)ahardlinktoanychecksumfiles. It
will also remove any checksum files which have no hardlinks outside of the pool’s checksum file
directories.
Apooldirectorycanbesharedbymultiplemirrorsinordertodeduplicatestoredfilesacrossthe
mirror boundary. For example, it is recommended to have a single pool directory (mirror base
directory)forallmirrorsofProxmoxrepositories.
The default config path is /etc/proxmox-offline-mirror.cfg, but it can be overridden on a
per command basis (for example, to allow operation as a non-root user). Use the --config CLI
optionorthePROXMOX_OFFLINE_MIRROR_CONFIGenvironmentvariable.
1.4 Getting Help
1.4.1 EnterpriseSupport
UserswithaProxmoxOfflineMirror subscriptionhaveaccesstotheProxmoxCustomerPortalfor
offlinemirroring/keyhandlingrelatedissues,providedthecorrespondingofflinesystemhasavalid
subscriptionlevelhigherthanCommunity. Thecustomerportalprovidessupportwithguaranteed
responsetimesfromtheProxmoxdevelopers.
Formoreinformationorforvolumediscounts,pleasecontactsales@proxmox.com.
1.4.2 CommunitySupportForum
WealwaysencourageouruserstodiscussandsharetheirknowledgeusingtheProxmoxCommu-
nityForum. TheforumismoderatedbytheProxmoxsupportteam. Thelargeuserbaseisspread
outallovertheworld. Needlesstosaythatsuchalargeforumisagreatplacetogetinformation.
1.4.3 MailingLists
ProxmoxOfflineMirrorisfullyopen-sourceandcontributionsarewelcome! TheProxmoxVEde-
velopmentmailinglistactsastheprimarycommunicationchannelforofflinemirrordevelopers:
Mailinglistfordevelopers
PVEDevelopmentList
1.4.4 BugTracker
Proxmoxrunsapublicbugtrackerathttps://bugzilla.proxmox.com. Ifanissueappears, fileyour
reportthere. Anissuecanbeabug, aswellasarequestforanewfeatureorenhancement. The
bugtrackerhelpstokeeptrackoftheissueandwillsendanotificationonceithasbeensolved.
1.3. TechnicalOverview 3

ProxmoxOfflineMirrorDocumentation,Release0.8.0
1.5 License
Copyright(C)2022-2024,ProxmoxServerSolutionsGmbH
ThissoftwareiswrittenbyProxmoxServerSolutionsGmbH<support@proxmox.com>
ProxmoxOfflineMirrorisfreeandopensourcesoftware: youcanuseit,redistributeit,and/ormod-
ifyitunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedbytheFreeSoftware
Foundation,eitherversion3oftheLicense,or(atyouroption)anylaterversion.
Thisprogramisdistributedinthehopethatitwillbeuseful,butWITHOUT ANY WARRANTY;without
eventheimpliedwarrantyofMERCHANTABILITYorFITNESS FOR A PARTICULAR PURPOSE.See
theGNUAfferoGeneralPublicLicenseformoredetails.
YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicensealongwiththisprogram.
Ifnot,seeAGPL3.
1.5. License 4

CHAPTER
TWO
INSTALLATION
ProxmoxOfflineMirrorisreleasedasastandardDebianpackageandisavailableintheProxmox
VE,ProxmoxBackupServerandProxmoxMailGatewaypackagerepositories.
2.1 System Requirements
• CPU:64bit(x86-64orAMD64),ideally2+Cores
• Debianbasedsystem(physicalhost,VMorcontainer)
• Sufficientstoragespaceforthelocalmirrors. ForabasicDebianandProxmoxVEwerecom-
mendatleast150GiB
• Afilesystemsupportinghardlinksforboththelocalhostandtheexternalmedium. Notethat
mostLinuxderivedfilesystemssupporthardlinks,butWindowsderivedones(forexample,
*FAT)donotsupporthardlinks.
2.2 Installation via APT
If the host you want to install the proxmox-offline-mirror tools on, already has a package
repositoryfromaProxmoxsolutionconfigured,youcansimplyinstalltheofflinemirrortoolwith
apt:
# apt update
# apt install proxmox-offline-mirror
IfyoudonothaveanyProxmoxVE,ProxmoxBackupServerorProxmoxMailGatewayrepositories
setup,seeSecureAptandSetuptheRepositoryonnonProxmoxbasedsystemsforhowtodosobefore
usingthecommandsabove.
2.2.1 DebianPackageRepositories
AllDebianbasedsystemsuseAPTasapackagemanagementtool. Thelistsofrepositoriesarede-
finedin/etc/apt/sources.listandthe.listfilesfoundinthe/etc/apt/sources.list.
d/directory. Newersystemswillalsouse.sourcesfilesinthenewdeb822formatfoundatthe
samelocation. Updatescanbeinstalleddirectlywiththeaptcommandlinetool,orviatheGUI.
APTsources.listfileslistonepackagerepositoryperline,withthemostpreferredsourcelisted
first. Emptylinesareignored,anda#characteranywhereonalinemarkstheremainderofthatline
asacomment. Theinformationavailablefromtheconfiguredsourcesisacquiredbyapt update.
2.2.2 SecureApt
TheReleasefilesintherepositoriesaresignedwithGnuPG.APTisusingthesesignaturestoverify
thatallpackagesarefromatrustedsource.
5

ProxmoxOfflineMirrorDocumentation,Release0.8.0
(cid:98) Tip
If you install Proxmox Offline Mirror on an existing Proxmox VE, Proxmox Backup Server or
ProxmoxMailGateway,theverificationkeywillalreadybepresent.
IfyouinstallProxmoxOfflineMirrorontopofDebian13(Trixie),downloadandinstallthekeywith
thefollowingcommands:
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
Signed-By: linesinyourrepositorystanzasbelow.
2.2.3 SetuptheRepositoryonnonProxmoxbasedsystems
IfyoudonothaveaninternetfacinginstallationofaProxmoxsolution,orwanttosetupadedicated
systemforProxmoxOfflineMirror,youneedtoconfiguretherepositoryfirst.
ThisshouldworkonanyLinuxdistributionusingaptaspackagemanager,suchasDebian,Ubuntu
orderivativesthereof.
To configure the repository, you first need to set up the Proxmox release key. After that, add the
repositoryURLtotheAPTsourceslists.
Werecommendre-usingthepbs-clientrepositoryforinstallingtheProxmoxOfflineMirroron
nonProxmoxsystems.
(cid:98) Hint
WhileyoucouldalsouseaProxmoxVE,ProxmoxBackupServerorProxmoxMailGatewayrepos-
itory,thoseshipsomeupdatedpackagesfromDebiannativepackages,whichwouldgetpulled
in,evenifnotrequiredfortheofflinemirroring.
2.2. InstallationviaAPT 6

ProxmoxOfflineMirrorDocumentation,Release0.8.0
RepositoryforDebian13(Trixie)basedreleases
HerearetheactualstepsforagenericDebian13(Trixie)basedsystem.
Firsteditthefile/etc/apt/sources.list.d/pbs-client.sourcesandaddthefollowingsnip-
pet:
Listing 1: File: /etc/apt/sources.list.d/pbs-client.
sources
Types: deb
URIs: http://download.proxmox.com/debian/pbs-client
Suites: trixie
Components: main
Signed-by: /usr/share/keyrings/proxmox-archive-keyring.gpg
Nowyoushouldbeabletoinstalltheproxmox-offline-mirrorpackage,seeInstallationviaAPT.
RepositoryforDebian12(Bookworm)basedreleases
HerearetheactualstepsforagenericDebian12(Bookworm)basedsystem.
Firsteditthefile/etc/apt/sources.list.d/pbs-client.listandaddthefollowingsnippet:
Listing 2: File: /etc/apt/sources.list.d/pbs-client.
list
deb http://download.proxmox.com/debian/pbs-client bookworm main
Nowyoushouldbeabletoinstalltheproxmox-offline-mirrorpackage,seeInstallationviaAPT.
2.2. InstallationviaAPT 7

CHAPTER
THREE
|     |     |     | OFFLINE | SUBSCRIPTION | KEYS |
| --- | --- | --- | ------- | ------------ | ---- |
Theproxmox-offline-mirrortoolcanbeusedtomanagesubscriptionkeysforair-gappedsys-
temsorsystemsthatcannotaccessthepublicinternet. Tousethisfunctionality,youneedasub-
scriptionkeyforProxmoxOfflineMirroritself.
TheofflinemirrortoolwilltakecareofregisteringthesubscriptionkeysintheProxmoxshop. Ifthe
keyisvalid, itwillgetasigneddatablobinresponse. Thesignedresponsecanthenbeexported
toanofflinemediumtotransferandsetthesubscription keyinaProxmoxsolution, withoutany
needforaninternetconnectiononthehostitself.
| 3.1 Minimum | Versions | for Offline | Activation |     |     |
| ----------- | -------- | ----------- | ---------- | --- | --- |
OfflineactivationofsubscriptionkeysrequiressupportfromtherespectiveProxmoxsolution. The
followingtableshowsinwhichversionthissupporthasbeenadded.
|           | Solution            | Package               |     | MinimumVersion |     |
| --------- | ------------------- | --------------------- | --- | -------------- | --- |
|           | ProxmoxVE           | pve-manager           |     | 7.2-11         |     |
|           | ProxmoxBackupServer | proxmox-backup-server |     | 2.2.6-1        |     |
|           | ProxmoxMailGateway  | pmg-api               |     | 7.1-7          |     |
| 3.2 Setup | Offline Mirror      | Key                   |     |                |     |
First, add the pom-<keyid> mirror key using proxmox-offline-mirror key add-mirror-key
<key>. Thiscommandwillactivatethesubscriptionofthemirroringsystem.
(cid:174) Note
To purchase a subscription key for Proxmox Offline Mirror, please contact
<sales@proxmox.com>. IfyoualreadyhaveaStandardorPremiumsubscriptionforthemajor-
ity of your Proxmox VE, Proxmox Backup Server or Proxmox Mail Gateway hosts, you may be
eligibleforafreeOfflineMirrorsubscription. Inthatcase,pleaseemail<sales@proxmox.com>
togetmoredetails.
| 3.3 Gather | Server IDs |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
Next,gathertheserverIDsofthesystemsthatwillbesetupforofflinekeys. Youcanseetheserver
IDinthesubscriptionpanelofeachhost,orbyusingtheCLIwiththefollowingcommands:
| • pvesubscription | getforProxmoxVE |     |     |     |     |
| ----------------- | --------------- | --- | --- | --- | --- |
• proxmox-backup-manager subscription getforProxmoxBackupServer
8

ProxmoxOfflineMirrorDocumentation,Release0.8.0
| • pmgsubscription | getforProxmoxMailGateway |      |     |
| ----------------- | ------------------------ | ---- | --- |
| 3.4 Register      | & Refresh                | Keys |     |
(cid:174) Note
Tobeabletoaccessandmirroraproduct’senterpriserepository,proxmox-offline-mirror
requiresbothanactiveproductsubscriptionkeyandaProxmoxOfflineMirrorsubscription.
Register the hosts with their subscription keys and server IDs using proxmox-offline-mirror
| setuporproxmox-offline-mirror |     | key                | add,forexample: |
| ----------------------------- | --- | ------------------ | --------------- |
| proxmox-offline-mirror        | key | add pve2p-12345... | ABCDEF0123...   |
Bydefault,thiscommandwillfetchtheupdatedsubscriptioninformationfromtheProxmoxsub-
scriptionservers.
Youcanrefreshthesubscriptioninformationforasingle(--key XX)orallconfiguredkeysusing
| proxmox-offline-mirror |      | key refresh. |     |
| ---------------------- | ---- | ------------ | --- |
| 3.5 Deploy             | Keys |              |     |
Thesubscriptioninformationistransferredtoamedium(seeSyncingaMedium)andcanthenbe
activatedontheofflinesystemwitheitherproxmox-offline-mirror-helper offline-keyor
proxmox-offline-mirror-helper setup. Thisprocessmustberepeatedatleastonceayear
orbeforethenextduedateofthesubscriptionkeyisreached,whichevercomesfirst.
3.4. Register&RefreshKeys 9

CHAPTER
FOUR
|     |     |     | OFFLINE | REPOSITORY | MIRRORS |
| --- | --- | --- | ------- | ---------- | ------- |
OfflinerepositorymirrorsarepointingtoAPTrepositories,forexamplefromProxmoxVE,Proxmox
BackupServerorDebian. Aftertheinitialsetup, youcanmirroralltheavailablepackageslocally.
Theyareorganizedbycreatingpoint-in-timesnapshotsoftherepositories. Thosesnapshotscan
thenbeexportedtoaconfiguredmedium.
| 4.1 Setting Up | a Mirror |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
First, either run the setup wizard (proxmox-offline-mirror setup), or the config mirror
addcommand.
(cid:98) Tip
ThequickestwaytosetupallrelevantrepositoriesforaProxmoxsolutionistousethesetup
wizard. Choose the product when adding a mirror and confirm the question regarding auto-
addingtheDebianbaserepos.
(cid:174) Note
Tobeabletoaccessandmirroraproduct’senterpriserepository,proxmox-offline-mirror
requiresbothanactiveproductsubscriptionkeyandaProxmoxOfflineMirrorsubscription(see
SetupOfflineMirrorKey).
For example, to manually add a mirror entry for the Debian Bookworm security repository, the
followingcommandcanbeused:
| proxmox-offline-mirror        | config mirror | add \ |     |     |     |
| ----------------------------- | ------------- | ----- | --- | --- | --- |
| --id debian-bookworm-security | \             |       |     |     |     |
| --architectures amd64         | \             |       |     |     |     |
| --architectures all           | \             |       |     |     |     |
--repository 'deb http://deb.debian.org/debian-security bookworm-security main contrib non-
,→free' \
--key-path /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.gpg \
--sync true \
| --verify-mode size | \   |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
--base-dir /path/to/mirror/base-dir
(cid:174) Note
Thebase-dirdirectorycanbesharedbymirrorsforrepositoriesthathavecommoncontentsto
avoidstoringfilesmorethanonce. Forexample, havingasinglebasedirectoryforallmirrors
referencingProxmoxrepositoriesisrecommended.
10

ProxmoxOfflineMirrorDocumentation,Release0.8.0
(cid:174) Note
Theall architectureismeantforarchitectureindependentpackages,notforallpossiblearchi-
tectures. Itisalmostalwayssensibletoadditinadditiontothehost-specificarchitecture.
4.2 Syncing a Mirror
Tocreatethefirst(andsubsequent)snapshots,thefollowingcommandcanbeused:
proxmox-offline-mirror mirror snapshot create debian-bookworm-security
(cid:174) Note
Dependingontheparametersusedandthesizeoftheoriginalrepository,creatingasnapshot
cantakebothtimeandrequiresignificantdiskspace. Thisisespeciallytruefortheinitialsnap-
shot,assubsequentoneswillre-useunchangedpackagefilesandindices.
The --max-downloads option sets the number of concurrent binary package downloads. The
defaultis1,withamaximumof4tolimitloadonthesourcerepository. Increasingitcanspeedup
snapshotcreation, especiallythefirstrun. Sourcepackagesarealwaysdownloadedsequentially.
Forexample,toallowfourconcurrentbinarypackagedownloads:
proxmox-offline-mirror mirror snapshot create debian-bookworm-security --max-downloads 4
Onlyonesnapshotcreationpermirrorcanrunatatime. Asecondcreationwaitsuptofiveseconds
forthefirsttofinish. Ifthefirstisstillrunning,thesecondfails. Snapshotsofdifferentmirrorscan
becreatedinparallel,evenwhentheyshareabasedirectory.
Thesamelockprotectsotheroperationsthatchangeamirror’ssnapshotsorsymlinks: removing,
naming,unnaming,andpruningsnapshots;removingthemirror;andchangingitsbasedirectory
or latest-symlink settings. These operations also wait up to five seconds for the lock, then fail if
themirrorisstillbusy. Sincesnapshotcreationcantakehours,scheduleoperationsforthesame
mirrorsotheydonotoverlap.
4.3 Verify Mode
The --verify-mode option controls how snapshot creation checks files reused from the pool.
Newly downloaded files are always checked against the checksums provided by the repository.
Threemodesareavailable:
none
Onlycheckthatthefileexists. Thisisthefastestmode,butitdoesnotdetectdamagedfiles.
size
Alsocheckthatthefilesizematchestherepositoryindex. Thisdetectstruncatedfilesatneg-
ligiblecostandistherecommendedmode.
full
Readeveryreusedfileandverifyitschecksums. Thisisthemostthoroughmode,butitcan
read tens of gigabytes when creating a snapshot of a large repository, even if nothing has
changed.
Afilethatfailsverificationisdownloadedagaintorepairitsexistingpoolentry. Becausesnapshots
usehardlinkstopoolentries,thisalsorepairsthefileinoldersnapshotsthatreferencethesame
entry.
4.2. SyncingaMirror 11

ProxmoxOfflineMirrorDocumentation,Release0.8.0
The previous boolean option, verify, is still accepted as an alias: true means full and false
means none, so existing configurations keep their behavior. On the command line, the alias
requires an explicit value. Use --verify true or --verify-mode full instead of a bare
| --verify. | Toswitchanexistingmirrortosizemode: |     |
| --------- | ----------------------------------- | --- |
proxmox-offline-mirror config mirror update --id debian-bookworm-security \
| --verify-mode | size |     |
| ------------- | ---- | --- |
For on-demand full integrity checks without changing the configured mode, use the mirror
verifycommand(seebelow).
| 4.4 Request | Timeouts |     |
| ----------- | -------- | --- |
By default, each repository request has a total time limit of 15 minutes, plus the transfer time at
64 KiB/s when the expected file size is known. This bounds stalled requests while allowing large
packagestodownloadoverslowconnections. Therequest-timeoutoptionoverridesthiswitha
fixedlimitinseconds,upto604800(oneweek). Setitto0todisablethelimit:
proxmox-offline-mirror config mirror update --id debian-bookworm-security --request-timeout 0
Toreturntothedefaultlimit:
proxmox-offline-mirror config mirror update --id debian-bookworm-security \
| --delete   | request-timeout |         |
| ---------- | --------------- | ------- |
| 4.5 Latest | Snapshot        | Symlink |
By default, each mirror maintains a symlink called last that points to the most recently created
snapshot,sosystemscanusethelatestsnapshotwithoutknowingitstimestamp-basedname.
Thesymlinkisupdatedatomicallyaftereachsuccessfulsnapshotcreation. Whenthesnapshotit
pointstoisremoved,thesymlinkmovestothenextoldersnapshot,orisremovedifthereisnone.
The symlink exists only on the mirroring host. Offline media receive the snapshots themselves,
accessedthroughtheirtimestamp-baseddirectorynames.
Thefeaturecanbeconfiguredpermirror:
• --latest-symlinkcontrolswhetherthesymlinkismaintained(default: true)
• --latest-symlink-nameoverridesthesymlinkname(default: last)
Forexample,tochangethesymlinknametocurrent:
proxmox-offline-mirror config mirror update --id debian-bookworm-security \
| --latest-symlink-name |                                                  | current |
| --------------------- | ------------------------------------------------ | ------- |
| Use--delete           | latest-symlink-nametorestorethedefaultname,last. |         |
Todisablethefeatureforaspecificmirrorandremoveitssymlink:
proxmox-offline-mirror config mirror update --id debian-bookworm-security \
| --latest-symlink | false |     |
| ---------------- | ----- | --- |
mirror snapshot create and create-all also accept --latest-symlink false to leave
the symlink unchanged for a single run. This is useful for a test snapshot that clients should not
useyet. Ifthesnapshotcurrentlyservedbythesymlinkisremoved,thelinkfallsbacktoanolder
snapshotratherthanpromotingthenewertestsnapshot.
Thesymlink’snameandenabledstateareconfiguredpermirror. Asingleruncanskipupdatingit,
butcannotenableitorchooseadifferentname. Useanamedsnapshotwhenyouneedanalias
thatcontinuestopointtothesamesnapshot(seebelow).
| mirror snapshot | listshowswhichsnapshotthesymlinkpointsto. |     |
| --------------- | ----------------------------------------- | --- |
4.4. RequestTimeouts 12

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Renamingthesymlinkpreservesitscurrenttarget. Youcannotchangeitsnameandbase-dirin
thesamecommand,becausethesymlink’slocationdependsonwhetherthesnapshotdirectories
havealreadybeenmoved.
Thenewnamemustbeunusedinthemirrordirectory,sorenamingneveroverwritesanexisting
file,directory,orsymlink. Ifanamedsnapshotusesthedesiredname,removethataliasfirstwith
mirror snapshot unname.
4.6 Named Snapshots
Snapshotscanbegivenhuman-readablenames,whicharesymlinksnexttothetimestamp-based
directories. Unlikethelastsymlink,anamecontinuestopointtothesamesnapshot. Commands
thattakeasnapshotargumentstillrequireitstimestamp,notitsassignedname.
Tonameasnapshotatcreationtime:
proxmox-offline-mirror mirror snapshot create debian-bookworm-security --name stable
Tonameanexistingsnapshot:
proxmox-offline-mirror mirror snapshot name debian-bookworm-security 2025-03-05T14:30:45Z␣
,→stable
Toremoveanamewithoutremovingtheunderlyingsnapshot:
proxmox-offline-mirror mirror snapshot unname debian-bookworm-security stable
Themirror snapshot listcommandshowsnamesalongsidethetimestampstheypointto.
Removingasnapshotalsoremovesitsnames.
Likethelastsymlink,namesexistonlyonthemirroringhost: syncingtoanofflinemediumtrans-
fersthesnapshotsthemselves.
4.7 Reducing Mirror Scope
Therearedifferentmechanismsforreducingamirror’sscope(andcorrespondingly,theamountof
trafficanddiskspacerequiredtokeepitsynced):
• architecturefilters
• components(aspartoftherepository specification)
• packagenameandsectionfilters
Bydefault,onlypackagesforthearchitecturesall(seenoteabove)andamd64aremirrored.
Optionally, it’s possible to set up filters for downloaded binary or source packages via the --skip-
packagesand--skip-sectionsoptions. Thepackagefilterssupportglobbing,forexamplelinux-image-
* will skip all packages with a name starting with linux-image-. The section filters match the full
value,orthevalueprefixedwiththepackage’scomponent(forexample,gameswillmatchboththe
sectiongames,aswellasnon-free/gamesinapackagesindexofthenon-freecomponent).
Someexamplesforpackagesandsectionfilters:
• --skip-packages’linux-image-*’ -filterDebianlinuxkernelimagepackages
• --skip-sections’games’ -filtersectionscontaininggamepackages
• --skip-sections’debug’ -filtersectionscontainingdebuginformation
Ifyouwanttoskipalldebuggingrelatedpackages(whichmightnotalwaysbeinthedebugsection
mentionedintheexampleabove),thefollowingsetoffiltersshouldwork:
4.6. NamedSnapshots 13

ProxmoxOfflineMirrorDocumentation,Release0.8.0
| --skip-packages | '*-dbgsym' | \   |     |     |
| --------------- | ---------- | --- | --- | --- |
| --skip-packages | '*-dbg'    | \   |     |     |
| --skip-packages | '*-debug'  | \   |     |     |
| --skip-sections | debug      |     |     |     |
Please refer to https://packages.debian.org/bookworm/ for a list of Debian archive sections and
theircontents.
(cid:174)
Note
Proxmox releases based on Debian Bookworm and Trixie ship their debug symbol (-dbgsym)
packages in a dedicated repository, so the filters above do not apply to them. To have the
debug symbols offline, mirror that repository like any other Proxmox repository: component
<product>-dbgsym at https://dbgsym.proxmox.com/debian/<product>, for example
pve-dbgsymathttps://dbgsym.proxmox.com/debian/pve.
| 4.8 Pruning | Snapshots |     |     |     |
| ----------- | --------- | --- | --- | --- |
Over time, many snapshots accumulate. The prune command removes old snapshots based on
configurableretentionrules,similartoProxmoxBackupServer:
proxmox-offline-mirror mirror snapshot prune debian-bookworm-security \
| --keep-last | 3 --keep-daily | 7 --keep-weekly | 4 --keep-monthly | 6   |
| ----------- | -------------- | --------------- | ---------------- | --- |
Theavailableretentionoptionsare:
| --keep-last | N   |     |     |     |
| ----------- | --- | --- | --- | --- |
KeeptheNmostrecentsnapshotsregardlessofage.
| --keep-hourly | N   |     |     |     |
| ------------- | --- | --- | --- | --- |
KeepsnapshotsforthelastNdifferenthours. Ifthereismorethanonesnapshotforasingle
hour,onlythelatestiskept.
| --keep-daily | N   |     |     |     |
| ------------ | --- | --- | --- | --- |
KeepsnapshotsforthelastNdifferentdays. Ifthereismorethanonesnapshotforasingle
day,onlythelatestiskept.
| --keep-weekly | N   |     |     |     |
| ------------- | --- | --- | --- | --- |
KeepsnapshotsforthelastNdifferentISOweeks. Ifthereismorethanonesnapshotfora
singleweek,onlythelatestiskept.
| --keep-monthly | N   |     |     |     |
| -------------- | --- | --- | --- | --- |
Keep snapshots for the last N different months. If there is more than one snapshot for a
singlemonth,onlythelatestiskept.
| --keep-yearly | N   |     |     |     |
| ------------- | --- | --- | --- | --- |
KeepsnapshotsforthelastNdifferentyears. Ifthereismorethanonesnapshotforasingle
year,onlythelatestiskept.
At least one --keep-* option must be set. Rules are applied in the order listed above. Each
time-based rule skips periods in which an earlier rule already kept a snapshot. For example,
--keep-last 1 --keep-daily 1keepsthenewestsnapshotandthelatestsnapshotfromthe
mostrecentearlierdaythatcontainsone.
Onlyperiodscontainingsnapshotscounttowardthelimits. Iftheonlysnapshotisthreeyearsold,
--keep-hourly 1 still keeps it. Period boundaries use UTC, like the snapshot timestamps, and
maythereforedifferfromlocalcalendarboundaries.
Named snapshots are protected by default and do not count toward the retention limits. Use
--ignore-namestoapplytheretentionrulestothemaswell. Thelatest-snapshotsymlink’starget
isalwaysprotected,evenifnewersnapshotswerecreatedwith--latest-symlink false. These
protectionsandthecombinationofrulescanretainmorethanonesnapshotfromaperiod.
4.8. PruningSnapshots 14

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Use--dry-runtopreviewwhatwouldbekeptorremoved:
proxmox-offline-mirror mirror snapshot prune debian-bookworm-security \
--keep-daily 7 --dry-run
Use--gctoautomaticallyrungarbagecollectionafterpruning:
proxmox-offline-mirror mirror snapshot prune debian-bookworm-security \
--keep-last 5 --gc
Topruneallconfiguredmirrorsatonce:
proxmox-offline-mirror mirror snapshot prune-all --keep-daily 7 --keep-weekly 4
Pruningusestheper-mirrorlockdescribedaboveandfailsifitcannotacquirethelockwithinfive
seconds. prune-allskipsabusymirror,continueswiththeothers,andexitswithanerror. Adry
rundoesnotacquirethelock.
4.9 Comparing Snapshots
Themirror snapshot diffcommandshowswhatchangedbetweentwosnapshots. Bydefault
itliststhestoredfilesthatwereadded,removed,orchanged:
proxmox-offline-mirror mirror snapshot diff debian-bookworm-security <older> <newer>
Replace <older> and <newer> with the snapshot timestamps shown by mirror snapshot
list. Pass --packages to compare the package indices instead. This lists binary and source
packagesthatwereaddedorremoved,orwhoseversionschanged:
proxmox-offline-mirror mirror snapshot diff debian-bookworm-security <older> <newer> --
,→packages
Binarypackagesarereportedas<name>:<architecture>;apackagethatappearswithadiffer-
entversioninthenewersnapshotisreportedaschanged,showingbothversions.
Bothdiffvariantssupport--output-format jsonforuseinscripts. Thesameoptionisavailable
formirror snapshot list,remove,prune,prune-all,mirror gc,andmirror verify. See
JSONCommandOutputfortheoutputformats.
4.10 Space Management
Removingsnapshots,withmirror snapshot removeorbypruningwithout--gc,doesnotfree
diskspacebyitself. Runmirror gctodeletethepoolfilesthatnosnapshotusesanymore.
A failed or interrupted snapshot creation can leave a temporary directory named <snapshot>.
tmp. Itshardlinksprotectfilesalreadyaddedtothepoolfromgarbagecollection,allowingaretry
to reuse them. The next successful snapshot creation for that mirror removes these temporary
directories. Mediumsynchronizationdoesnotcopythem.
Package downloads are staged in a hidden .downloads directory next to the snapshots before
beingaddedtothepool. Unlikefilesalreadystoredinthepool,partialdownloadscannotbereused.
Thenextsnapshotcreationforthemirrorremovespartialdownloadsleftbyacrashedrun.
Snapshotremovalfirstrenamesthedirectoryto.<snapshot>.removingbeforedeletingitsfiles.
Thispreventsapartiallydeletedsnapshotfromappearinginlistingsorbeingcopiedtoamedium.
Ifdeletionfails,forexamplebecauseofapermissionerror,thecommandreportsthecleanuperror
andexitswithanonzerostatus. Garbagecollectionretriesdeletionoftheremainingfiles.
4.9. ComparingSnapshots 15

ProxmoxOfflineMirrorDocumentation,Release0.8.0
4.11 Verifying Pool Integrity
Themirror verifycommandcheckspoolfilesfordamageindependentlyoftheverify-mode
usedduringsnapshotcreation. Itreportsdamagewithoutrepairingfilesandexitswithanonzero
statusifverificationfails. Creatingasnapshotinfullverifymoderepairsdamagedfilesthatare
stillneededbythatsnapshotandavailablefromtherepository.
By default, the command reads each pool file and verifies its checksums. This can read tens of
gigabytesforalargemirror,soconsiderschedulingit. Forafastercheck,use--mode size. This
detectsfilestruncatedtozerobytes,butnotothersizechanges,becausethepooldoesnotstore
expected sizes. Files whose checksums identify empty content are accepted in either mode. For
example:
proxmox-offline-mirror mirror verify debian-bookworm-security
proxmox-offline-mirror mirror verify debian-bookworm-security --mode size
Withoutanidargument,allconfiguredmirrorsareverified(poolssharedbymultiplemirrorsare
onlyverifiedonce):
proxmox-offline-mirror mirror verify
(cid:174) Note
mirror verify and mirror gc act on all mirrors if no id is given. mirror snapshot
createandmirror snapshot prunerequireanidinstead,andhaveseparatecreate-all
andprune-allvariants.
4.12 Global Options
--config <path>
Path to the mirroring config file. Can be placed anywhere on the command line (before or
after the subcommand). If omitted, the PROXMOX_OFFLINE_MIRROR_CONFIG environment
variableisused,fallingbackto/etc/proxmox-offline-mirror.cfg.
4.13 Environment Variables
PROXMOX_OFFLINE_MIRROR_CONFIG
Path to the mirroring config file, if --config is not given. Defaults to /etc/
proxmox-offline-mirror.cfg.
ALL_PROXY
Whenset,proxmox-offline-mirrorusesthespecifiedHTTPproxyforallHTTP(s)connections.
Currently only HTTP proxies are supported. Valid proxy configurations have the following
format: [http://][user:password@]<host>[:port]. Defaultportis1080,ifnototherwisespecified.
(cid:174) Note
TheproxyservermustallowHTTP CONNECTforallportsthatareusedtoconnecttomirrors(e.g.
port80forHTTPmirrors). ForSquid,theappropriateconfigurationparameterishttp_access
allow CONNECT <acl> (http://www.squid-cache.org/Doc/config/http_access/). By default,
SquidonlyallowsHTTP CONNECTforport443.
4.11. VerifyingPoolIntegrity 16

CHAPTER
FIVE
OFFLINE MEDIA
A medium stores mirrored repositories and subscription information for use by offline Proxmox
systems. Itcanbeanexternalstoragedevice,suchasaUSBflashdrive,oralocalnetworkshare.
| 5.1 Setting Up | a Medium |     |
| -------------- | -------- | --- |
Either run the setup wizard again, or use the config media add command. For example, to
defineanewmediumcontainingtheproxmox-ve-bookworm-no-subscriptionanddebian-bookworm
mirrors,runthefollowingcommand:
| proxmox-offline-mirror | config media | add \ |
| ---------------------- | ------------ | ----- |
| --id pve-bookworm      | \            |       |
--mirrors proxmox-ve-bookworm-no-subscription \
| --mirrors debian-bookworm | \   |     |
| ------------------------- | --- | --- |
--sync true \
| --verify-mode size | \   |     |
| ------------------ | --- | --- |
--mountpoint /path/where/medium/is/mounted
| 5.2 Syncing a | Medium |     |
| ------------- | ------ | --- |
Tosyncthelocalmirrorstoamedium,thefollowingcommandcanbeused:
| proxmox-offline-mirror | medium sync | pve-bookworm |
| ---------------------- | ----------- | ------------ |
This command will sync all mirrors linked with this medium to the medium’s mount point. Addi-
tionally,itwillsyncallofflinekeysforfurtherprocessingbyproxmox-offline-mirror-helper
onthetargetsystem.
The medium’s verify-mode controls checks of files already stored on it. none checks only that
theyexist,sizecomparestheirsizeswiththecorrespondingsourcefilesinthemirror,andfull
verifies their checksums. A file that fails the selected check is copied again. In size and full
mode,checksumsarealsoverifiedduringcopying. Ifasourcefilefailsthischeck,synchronization
failsratherthancopyingdamagedcontentintothemedium’spool.
Whilecopyingamirror,synchronizationholdsthesameper-mirrorlockassnapshotcreation. This
prevents the snapshots from changing during the copy. If another operation holds the lock, syn-
chronizationwaitsuptofiveseconds,thenfailsifthemirrorisstillbusy. Retryoncetheconflicting
operationhasfinished.
| 5.3 Using a Medium |     |     |
| ------------------ | --- | --- |
Aftersyncingamediumyoucanmakeitaccessibleonthe(offline)targetsystembyeither:
• unmountingitfromthemirrorhost,pluggingitintothetargetandmountingitthere
• exposingiteitherdirectly(fromthemirrorhost)orindirectly(fromanotherhost)viathelocal
network(NFS,CIFS/SMBorHTTP)
17

ProxmoxOfflineMirrorDocumentation,Release0.8.0
After that you can upgrade the host as usual, either using the console or the web interface, as
describedintherespectiveproject’sdocumentation.
Onceanupgradeisdoneyoushoulddisable,orremove,thesnippettoavoidapterrorsfromau-
tomaticrefresh. Notethatyoucandisableandre-enablerepositoriessimplyviathewebinterface
ofProxmoxVE,ProxmoxBackupServerorProxmoxMailGateway.
5.3.1 Example: LocalMountPoint
Eitheroptionbelowassumesthatyoualreadymountedthemediumonthetargethost.
GuidedSetup
Foraguidedsetuprunproxmox-offline-mirror-helper setup. Itwillletyouselectthemir-
rorsandsnapshotsandcanthengenerateasources.list.dsnippet. Thissnippetcanbesavedtothe
/etc/apt/sources.list.ddirectory. Thedefaultfilenameisoffline-mirror.list.
ManualSetup
To use a snapshot directly with APT, create a repository entry in a .list file under /etc/apt/
sources.list.d/. Forexample:
deb [check-valid-until=false] file:///mnt/mirror-path/<mirror-name>/<snapshot-timestamp>
,→<suite> <components>
Replace <suite> with the suite from the mirror’s repository line, such as bookworm or
bookworm-security. Replace<components>withoneormoreofthatrepository’scomponents,
suchasmain,pve-enterprise,orpbstest. Usethemirrornameandsnapshottimestampfor
<mirror-name>and<snapshot-timestamp>.
Youcanthenupgradethesystemasusual. Afterupgrading,disabletherepositoryentryuntilthe
mediumisneededagain.
5.3.2 Example: LocalHTTPServer
YoucanalsoconfigureanHTTPservertoprovidethesnapshotsinyourinternalnetwork. Aminimal
sampleconfigurationfornginx:
# with the correct dns setup and path this corresponds to a sources.lists entry
# deb [ check-valid-until=false ] http://proxmox-offline-mirror.domain.example/
,→<mirror-name>/<snapshot-timestamp> <codename> <suite>
server {
listen 80 default_server;
listen [::]:80 default_server;
server_name proxmox-offline-mirror.domain.example;
root /path/to/medium;
disable_symlinks off;
autoindex on;
error_log /var/log/nginx/proxmox-offline-mirror.error.log;
access_log /var/log/nginx/proxmox-offline-mirror.access.log;
location / {
try_files $uri $uri/ =404;
}
}
Create a .list file under /etc/apt/sources.list.d/ with a repository entry pointing to the
HTTPserver:
deb [ check-valid-until=false ] http://proxmox-offline-mirror.domain.example/<mirror-name>/
,→<snapshot-timestamp> <suite> <components>
Replace the placeholders as described in Manual Setup above. You can then upgrade the system
asusual. Afterupgrading,disabletherepositoryentryuntilthemirrorisneededagain.
5.3. UsingaMedium 18

ProxmoxOfflineMirrorDocumentation,Release0.8.0
5.4 Activating a Subscription Key
To activate or update a subscription key offline, either use proxmox-offline-mirror-helper
offline-key directly or follow the respective step when doing the guided setup via the
proxmox-offline-mirror-helper setupcommand.
The offline-key command supports both local mountpoints and HTTP URLs. When using an
HTTPserver(asdescribedintheExample: LocalHTTPServersection),youcanactivatesubscription
keysdirectlyfromtheHTTPURLwithoutneedingtomountthemediumlocally:
proxmox-offline-mirror-helper offline-key --source http://proxmox-offline-mirror.domain.
,→example/
ThisisparticularlyusefulwhenthemirrorisservedoverHTTPandyouonlyneedtoactivatesub-
scription keys. Other operations like the status command and repository configuration still re-
quirealocalmountpoint.
5.4. ActivatingaSubscriptionKey 19

APPENDIX
A
COMMAND SYNTAX
A.1 proxmox-offline-mirror
ForsupportedenvironmentvariablespleaserefertoEnvironmentVariables.
Optionsavailableforcommandgroupproxmox-offline-mirror:
--config<string>
Pathtomirroringconfigfile.
proxmox-offline-mirror config media add --id <string> --mirrors <string>
--mountpoint <string> --sync <boolean> --verify-mode <string> [OPTIONS]
Createnewmediumconfigentry.
--id<string>
Mediumname.
--mirrors<string>
IDsofthemirrorstosynctothemedium. Canbespecifiedmorethanonce.
--mountpoint<string>
Mountpointwheremediumisavailableonmirroringsystem.
--sync<boolean>
WhethertowritenewfilesusingFSYNC.
--verify-mode<string>
Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoacceptstrue(full)
andfalse(none)forcompatibility.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config media list [OPTIONS]
Listconfiguredmedia.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
20

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Inheritedgroupparameters:
--config
proxmox-offline-mirror config media remove --id <string> --remove-data
<boolean> [OPTIONS]
Removemediumconfigentry.
--id<string>
Mediumname.
--remove-data<boolean>
RemoveALLDATAonmediumaswell.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config media show --id <string> [OPTIONS]
Showfullmediumconfigentry.
--id<string>
Mediumname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config media update --id <string> [OPTIONS]
Updatemediumconfigentry.
--id<string>
Mediumname.
Optionalparameters:
--mirrors<string>
IDsofthemirrorstosynctothemedium. Canbespecifiedmorethanonce.
--mountpoint<string>
Mountpointwheremediumisavailableonmirroringsystem.
--sync<boolean>
WhethertowritenewfilesusingFSYNC.
--verify-mode<string>
Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoacceptstrue(full)
andfalse(none)forcompatibility.
A.1. proxmox-offline-mirror 21

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Inheritedgroupparameters:
--config
proxmox-offline-mirror config mirror add --architectures <string>
--base-dir <string> --id <string> --key-path <string> --repository <string>
--sync <boolean> --verify-mode <string> [OPTIONS]
Createnewmirrorconfigentry.
--architectures<string>
Listofarchitecturesthatshouldbemirrored. Canbespecifiedmorethanonce.
--base-dir<string>
Pathtodirectorycontainingmirroredrepositorypool. Canbesharedbymultiplemirrors.
--id<string>
Mirrorname.
--key-path<string>
Pathtopublickeyfileforverifyingrepositoryintegrity.
--repository<string>
Singlerepositorydefinitioninsources.listformat.
--sync<boolean>
WhethertowritenewfilesusingFSYNC.
--verify-mode<string>
Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoacceptstrue(full)
andfalse(none)forcompatibility.
Optionalparameters:
--ignore-errors<boolean> (default=false)
Whethertodowngradedownloaderrorstowarnings.
--latest-symlink<boolean> (default=true)
Whethertomaintainasymlinkpointingtothelastsuccessfulsnapshot.
--latest-symlink-name<string> (default=last)
Nameofthelatest-snapshotsymlink.
--output-formattext|json|json-pretty
Outputformat.
--request-timeout<integer> (0 - 604800)
Maximumdurationofarepositoryrequestinseconds,or0fornolimit. Bydefault,allow15
minutesplusthetransfertimeat64KiB/swhentheexpectedfilesizeisknown.
--skip-packages<string>
Packagenamestoskip. Supportsglobpatterns. Canbespecifiedmorethanonce.
--skip-sections<string>
Sectionswhichshouldbeskipped. Canbespecifiedmorethanonce.
--use-subscriptionpve|pbs|pmg|pom
Accesstherepositorywiththeactivesubscriptionkeyofthisproduct(requiredforProxmox
enterpriserepositories).
--weak-crypto[[allow-sha1=<1|0>] [,min-dsa-key-size=<integer>]
[,min-rsa-key-size=<integer>]]
Whethertoallowusingweakcryptographyalgorithmsorparameters,deviatingfromthede-
faultpolicy.
A.1. proxmox-offline-mirror 22

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Inheritedgroupparameters:
--config
proxmox-offline-mirror config mirror list [OPTIONS]
Listconfiguredmirrors
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config mirror remove --id <string> --remove-data
<boolean> [OPTIONS]
Removemirrorconfigentry.
--id<string>
Mirrorname.
--remove-data<boolean>
Removemirrordataaswell.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config mirror show --id <string> [OPTIONS]
Showfullmirrorconfig
--id<string>
Mirrorname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror config mirror update --id <string> [OPTIONS]
Updatemirrorconfigentry.
--id<string>
Mirrorname.
Optionalparameters:
--architectures<string>
Listofarchitecturesthatshouldbemirrored. Canbespecifiedmorethanonce.
A.1. proxmox-offline-mirror 23

ProxmoxOfflineMirrorDocumentation,Release0.8.0
--base-dir<string>
Pathtodirectorycontainingmirroredrepositorypool. Canbesharedbymultiplemirrors.
--delete
use-subscription|ignore-errors|skip-packages|skip-sections|weak-crypto|latest-symlink|latest-symlink-name|request-timeout
Propertiestoresettotheirdefault. Canbespecifiedmorethanonce.
--ignore-errors<boolean> (default=false)
Whethertodowngradedownloaderrorstowarnings.
--key-path<string>
Pathtopublickeyfileforverifyingrepositoryintegrity.
--latest-symlink<boolean> (default=true)
Whethertomaintainasymlinkpointingtothelastsuccessfulsnapshot.
--latest-symlink-name<string> (default=last)
Nameofthelatest-snapshotsymlink.
--repository<string>
Singlerepositorydefinitioninsources.listformat.
--request-timeout<integer> (0 - 604800)
Maximumdurationofarepositoryrequestinseconds,or0fornolimit. Bydefault,allow15
minutesplusthetransfertimeat64KiB/swhentheexpectedfilesizeisknown.
--skip-packages<string>
Packagenamestoskip. Supportsglobpatterns. Canbespecifiedmorethanonce.
--skip-sections<string>
Sectionswhichshouldbeskipped. Canbespecifiedmorethanonce.
--sync<boolean>
WhethertowritenewfilesusingFSYNC.
--use-subscriptionpve|pbs|pmg|pom
Accesstherepositorywiththeactivesubscriptionkeyofthisproduct(requiredforProxmox
enterpriserepositories).
--verify-mode<string>
Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoacceptstrue(full)
andfalse(none)forcompatibility.
--weak-crypto[[allow-sha1=<1|0>] [,min-dsa-key-size=<integer>]
[,min-rsa-key-size=<integer>]]
Whethertoallowusingweakcryptographyalgorithmsorparameters,deviatingfromthede-
faultpolicy.
Inheritedgroupparameters:
--config
proxmox-offline-mirror help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
A.1. proxmox-offline-mirror 24

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Inheritedgroupparameters:
--config
proxmox-offline-mirror key add <key> <server-id> [OPTIONS]
Listsubscriptionkeysandtheirstatus
<key>
[<string>]Subscriptionkey.
<server-id>
[<string>]ServerID.
Optionalparameters:
--description<string>
Description,e.g. whichsystemthiskeyisdeployedon
--info<string>
base64encodedsubscriptioninfo-updatewith’refresh’command.
--refresh<boolean> (default=true)
Whethertorefreshthesubscriptioninfouponadding.
Inheritedgroupparameters:
--config
proxmox-offline-mirror key add-mirror-key <key>
Addofflinemirrorkey
<key>
[<string>]Subscriptionkey.
Inheritedgroupparameters:
--config
proxmox-offline-mirror key list [OPTIONS]
Listsubscriptionkeysandtheirstatus
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror key refresh [OPTIONS]
Refreshsubscriptionkeystatus.
Optionalparameters:
--key<string>
Subscriptionkey.
A.1. proxmox-offline-mirror 25

ProxmoxOfflineMirrorDocumentation,Release0.8.0
Inheritedgroupparameters:
--config
proxmox-offline-mirror key remove <key> [OPTIONS]
Removesubscriptionkeyconfigentry.
<key>
[<string>]Subscriptionkey.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror key show <key> [OPTIONS]
Show(decoded)subscriptionconfigentry.
<key>
[<string>]Subscriptionkey.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror key update <key> [OPTIONS]
Updatesubscriptionconfigentry.
<key>
[<string>]Subscriptionkey.
Optionalparameters:
--description<string>
Description,e.g. whichsystemthiskeyisdeployedon
--server-id<string>
ServerID.
Inheritedgroupparameters:
--config
proxmox-offline-mirror medium diff <id> [OPTIONS]
Diffamedium
<id>
[<string>]Mediumname.
Optionalparameters:
A.1. proxmox-offline-mirror 26

ProxmoxOfflineMirrorDocumentation,Release0.8.0
--verbose<boolean> (default=false)
Verboseoutput(printpathsinadditiontosummary).
Inheritedgroupparameters:
--config
proxmox-offline-mirror medium gc <id> [OPTIONS]
Garbagecollectallmirrorsonamedium.
<id>
[<string>]Mediumname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror medium status <id> [OPTIONS]
Printstatusofamedium
<id>
[<string>]Mediumname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror medium sync <id> [OPTIONS]
Syncamedium
<id>
[<string>]Mediumname.
Optionalparameters:
--keys-only<boolean> (default=false)
Onlysyncofflinesubscriptionkeys,skiprepositorycontents
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror gc [<id>] [OPTIONS]
Rungarbagecollectiononamirror’spool,oronthepoolsofallmirrorsifnoIDisgiven.
<id>
[<string>]Mirrorname.
Optionalparameters:
A.1. proxmox-offline-mirror 27

ProxmoxOfflineMirrorDocumentation,Release0.8.0
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot create <id> [OPTIONS]
Createarepositorysnapshot,downloadinganyrequiredfilesmissingfromthepool.
<id>
[<string>]Mirrorname.
Optionalparameters:
--dry-run<boolean> (default=false)
Onlyfetchtheindicesandprintasummaryofthemissingpackagefiles,withoutdownloading
themorcreatingasnapshot.
--latest-symlink<boolean>
Settofalsetoleavethelatest-snapshotsymlinkunchangedinthisrun. Itcanonlybeenabled
inthemirrorconfiguration.
--max-downloads<integer> (1 - 4) (default=1)
Maximum number of concurrent binary package downloads, kept low to spare the source
repository.
--name<string>
Snapshotname.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot create-all [OPTIONS]
Createasnapshotofeachconfiguredmirror,downloadingrequiredfilesmissingfromthepool.
Optionalparameters:
--dry-run<boolean> (default=false)
Onlyfetchtheindicesandprintasummaryofthemissingpackagefiles,withoutdownloading
themorcreatingasnapshot.
--latest-symlink<boolean>
Settofalsetoleavethelatest-snapshotsymlinkunchangedinthisrun. Itcanonlybeenabled
inthemirrorconfiguration.
--max-downloads<integer> (1 - 4) (default=1)
Maximum number of concurrent binary package downloads, kept low to spare the source
repository.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot diff <id> <snapshot>
<other_snapshot> [OPTIONS]
Printdifferencesbetweentwosnapshots.
<id>
[<string>]Mirrorname.
A.1. proxmox-offline-mirror 28

ProxmoxOfflineMirrorDocumentation,Release0.8.0
<snapshot>
[<string>]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
<other_snapshot>
[<string>]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
--packages<boolean> (default=false)
Listdifferencesperbinaryandsourcepackageinsteadofperstoredfile.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot list [<id>] [OPTIONS]
Listexistingrepositorysnapshots.
<id>
[<string>]Mirrorname.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot name <id> <snapshot> <name>
Assignanametoasnapshot.
<id>
[<string>]Mirrorname.
<snapshot>
[<string>]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
<name>
[<string>]Snapshotname.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot prune <id> [OPTIONS]
Prunesnapshotsaccordingtoretentionoptions.
<id>
[<string>]Mirrorname.
Optionalparameters:
--dry-run<boolean> (default=false)
Onlyshowwhatwouldberemoved.
--gc<boolean> (default=false)
Rungarbagecollectionafterpruning.
A.1. proxmox-offline-mirror 29

ProxmoxOfflineMirrorDocumentation,Release0.8.0
| --ignore-names<boolean> | (default=false) |     |     |
| ----------------------- | --------------- | --- | --- |
Don’tprotectnamedsnapshotsfrompruning.
| --keep-daily<integer> | (1 - N) |     |     |
| --------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentdays.
| --keep-hourly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differenthours.
| --keep-last<integer> | (1 - N) |     |     |
| -------------------- | ------- | --- | --- |
Keepthelast<N>snapshots.
| --keep-monthly<integer> | (1 - N) |     |     |
| ----------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentmonths.
| --keep-weekly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentweeks.
| --keep-yearly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentyears.
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
| proxmox-offline-mirror | mirror snapshot | prune-all | [OPTIONS] |
| ---------------------- | --------------- | --------- | --------- |
Prunesnapshotsforallconfiguredmirrors.
Optionalparameters:
| --dry-run<boolean> (default=false) |     |     |     |
| ---------------------------------- | --- | --- | --- |
Onlyshowwhatwouldberemoved.
--gc<boolean> (default=false)
Rungarbagecollectionafterpruning.
| --ignore-names<boolean> | (default=false) |     |     |
| ----------------------- | --------------- | --- | --- |
Don’tprotectnamedsnapshotsfrompruning.
| --keep-daily<integer> | (1 - N) |     |     |
| --------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentdays.
| --keep-hourly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differenthours.
| --keep-last<integer> | (1 - N) |     |     |
| -------------------- | ------- | --- | --- |
Keepthelast<N>snapshots.
| --keep-monthly<integer> | (1 - N) |     |     |
| ----------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentmonths.
| --keep-weekly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentweeks.
| --keep-yearly<integer> | (1 - N) |     |     |
| ---------------------- | ------- | --- | --- |
Keepsnapshotsforthelast<N>differentyears.
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
A.1. proxmox-offline-mirror 30

ProxmoxOfflineMirrorDocumentation,Release0.8.0
proxmox-offline-mirror mirror snapshot remove <id> <snapshot> [OPTIONS]
Removeasnapshotfromamirror. Itsdataisonlyfreedbyagarbagecollection.
<id>
[<string>]Mirrorname.
<snapshot>
[<string>]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror snapshot unname <id> <name>
Removeasnapshotname(doesnotremovethesnapshotdata).
<id>
[<string>]Mirrorname.
<name>
[<string>]Snapshotname.
Inheritedgroupparameters:
--config
proxmox-offline-mirror mirror verify [<id>] [OPTIONS]
Checkpoolintegritywithoutrepairingfiles.
<id>
[<string>]Mirrorname.
Optionalparameters:
--modefull|size (default=full)
Use’full’forchecksumverificationor’size’todetectunexpectedlyemptyfiles.
--output-formattext|json|json-pretty
Outputformat.
Inheritedgroupparameters:
--config
proxmox-offline-mirror setup
Interactivesetupwizard.
Inheritedgroupparameters:
--config
A.1. proxmox-offline-mirror 31

ProxmoxOfflineMirrorDocumentation,Release0.8.0
A.2 proxmox-offline-mirror-helper
proxmox-offline-mirror-helper help [{<command>}] [OPTIONS]
Gethelpaboutspecifiedcommand(orsub-command).
<command>
[<string>]Command. Thismaybealistinordertospecifynestedsub-commands. Canbe
specifiedmorethanonce.
Optionalparameters:
--verbose<boolean>
Verbosehelp.
proxmox-offline-mirror-helper offline-key --source <string> [OPTIONS]
Configuresanofflinesubscriptionkey
--source<string>
PathtomediummountpointorURLforkeyactivation
Optionalparameters:
--productpve|pbs|pmg|pom
Onlyactivatethesubscriptionkeyofthisproduct,insteadofthoseofallproducts.
proxmox-offline-mirror-helper setup
Interactivesetupwizard.
proxmox-offline-mirror-helper status --mountpoint <string> [OPTIONS]
Printsstatusofmedium
--mountpoint<string>
Pathtomediummountpoint
Optionalparameters:
--output-formattext|json|json-pretty
Outputformat.
A.2. proxmox-offline-mirror-helper 32

APPENDIX
B
JSON COMMAND OUTPUT
Thecommandslistedbelowsupportmachine-readableoutputonstdout. Pass--output-format
json for a compact, single-line result or --output-format json-pretty for indented output.
Diagnosticmessagesandprogressgotostderr,sostdoutcanbepipeddirectlyintotoolssuchas
jq.
Acommandcanprintaresultandstillexitwithanonzerostatus, forexampleifsomesnapshots
couldnotberemovedorsomefilesfailedverification. Checktheexitstatusaswellastheresult.
When piping output in Bash, use set -o pipefail so the pipeline also reports a failure of the
mirrorcommand. Acommandthatfailsbeforeithasaresultleavesstdoutempty.
config mirror list, config mirror show, and the corresponding config media com-
mands also support --output-format. They print configuration entries whose properties are
describedintheconfigurationfilereference.
mirror snapshot list
Snapshotlisting.
mirrors
[array of object]Per-mirrorsnapshotlistings,sortedbymirrorid.
mirror snapshot list: entriesofmirrors
Snapshotsofonemirror.
id
[string]Mirrorname.
latest-symlink
[object, optional] The latest-snapshot symlink, if the mirror maintains one that points at a
snapshot.
names
[array of object]Assignednames,sortedbyname.
snapshots
[array of string]Snapshots,oldestfirst.
mirror snapshot list: entriesofnames
Anamepinnedtoasnapshot.
name
[string]Snapshotname.
snapshot
[string]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
33

ProxmoxOfflineMirrorDocumentation,Release0.8.0
mirror snapshot list: latest-symlink
Thelatest-snapshotsymlink,ifthemirrormaintainsonethatpointsatasnapshot.
name
[string]Nameofthelatest-snapshotsymlink.
snapshot
[string]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
mirror snapshot remove
Summaryofasnapshotremoval.
cleanup-errors
[array of string, optional] Cleanup errors for a removed snapshot, such as failures to
updatethelatestsymlinkordeleteremainingfiles. Omittedifcleanupsucceeded.
latest-symlink
[string,optional]Newtargetofthelatestsymlink,iftheremovalmovedit.
latest-symlink-removed
[boolean,optional]Whetherthelatestsymlinkwasremovedbecausenooldersnapshotre-
mains.
removed-names
[array of string]Snapshotnames(pinnedsymlinks)removedtogetherwiththeirtarget
snapshot.
snapshot
[string]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
mirror snapshot pruneandprune-all
Prunesummary. Whengarbagecollectionisrequested,gcreportsitsoutcome,includingfailures.
Dryrunsomitgc.
dry-run
[boolean]Whetherthiswasadryrun,inwhichcasenothingwasremoved.
errors
[integer]Numberoffailedsnapshotremovalsandfailedcleanupsteps,plusoneforevery
mirrorthatcouldnotbeprunedatall. Garbagecollectionfailuresarecountedingc.errors.
gc
[object,optional]Garbagecollectionsummary.
kept
[integer]Totalnumberofsnapshotsselectedforretention.
mirrors
[array of object]Per-mirrorprunesummaries,sortedbymirrorid.
removed
[integer]Totalnumberofremovedsnapshots,orsnapshotsadryrunwouldremove.
mirror snapshot prune: entriesofmirrors
Prunesummaryofonemirror.
id
[string]Mirrorname.
kept
[integer]Numberofsnapshotsselectedforretention.
34

ProxmoxOfflineMirrorDocumentation,Release0.8.0
removed
[integer]Numberofremovedsnapshots,orsnapshotsadryrunwouldremove. Removals
withcleanuperrorsstillcounttowardthistotal;seecleanup-errors.
snapshots
[array of object]Per-snapshotprunedecisions,newestfirst.
mirror snapshot prune: entriesofsnapshots
Whatpruningdecidedforasinglesnapshot.
cleanup-errors
[array of string, optional] Cleanup errors for a removed snapshot, such as failures to
updatethelatestsymlinkordeleteremainingfiles. Omittedifcleanupsucceeded.
error
[string,optional]Whyasnapshotselectedforremovalcouldnotberemoved.
keep
[boolean]Whetherthesnapshotwasselectedforretentionratherthanremoval.
names
[array of string]Namespinnedtothesnapshot,sorted.
reason
[string,optional]Reasonforretainingthesnapshot: named,latest-symlink,keep-last,keep-
hourly, keep-daily, keep-weekly, keep-monthly, or keep-yearly. Omitted if the snapshot was
selectedforremoval.
snapshot
[string]MirrorsnapshottimestampinUTC,like2025-03-05T14:30:45Z.
mirror gc
Garbagecollectionsummary.
errors
[integer]Numberofpoolswhosegarbagecollectionfailed.
mirrors
[array of object] Per-mirror summaries; a pool shared by multiple mirrors is collected
andlistedonce.
removed-bytes
[integer]Totalsizeoftheremovedpoolfilesinbytes.
removed-files
[integer]Totalnumberofremovedpoolfiles.
mirror gc: entriesofmirrors
Garbagecollectionsummaryofonemirror’spool.
id
[string]Mirrorname.
removed-bytes
[integer]Totalsizeoftheremovedpoolfilesinbytes.
removed-files
[integer]Numberofremovedpoolfiles.
35

ProxmoxOfflineMirrorDocumentation,Release0.8.0
mirror verify
Poolverificationsummary.
bytes
[integer]Totalsizeofthecheckedpoolfilesinbytes.
errors
[integer]Numberofpoolsthatcouldnotbeverified.
failed
[integer]Totalnumberofpoolfilesthatfailedverification.
pools
[array of object] Per-pool summaries; a pool shared by multiple mirrors is verified and
listedonce.
verified
[integer]Totalnumberofpoolfilesthatpassedverification.
mirror verify: entriesofpools
Verificationsummaryofonemirror’spool.
base-dir
[string]Basedirectoryoftheverifiedpool.
bytes
[integer]Totalsizeofthecheckedpoolfilesinbytes.
failed
[integer]Numberofpoolfilesthatfailedverification.
id
[string]Mirrorname.
verified
[integer]Numberofpoolfilesthatpassedverification.
mirror snapshot diff
File-leveldifferencesbetweentwosnapshots.
added
[array of object]Filesonlypresentinthenewersnapshot,sortedbypath.
changed
[array of object]Filesinbothsnapshotswhosecontentdiffers,sortedbypath.
removed
[array of object]Filesonlypresentintheoldersnapshot,sortedbypath.
mirror snapshot diff: entriesofaddedandremoved
Astoredfilepresentinonlyoneoftwosnapshots.
path
[string]Pathrelativetothesnapshotdirectory.
size
[integer]Filesizeinbytes.
36

ProxmoxOfflineMirrorDocumentation,Release0.8.0
mirror snapshot diff: entriesofchanged
Astoredfilepresentinbothsnapshots,butwithdifferingcontent.
Only the size difference is reported: the diff compares stored files by inode, so a changed file of
thesamesize,likeare-signedReleasefile,reportsadifferenceofzero.
path
[string]Pathrelativetothesnapshotdirectory.
size-difference
[integer]Absolutedifferencebetweenthetwofilesizes,inbytes.
mirror snapshot diff --packages
Package-leveldifferencesbetweentwosnapshots,bypackagekind.
binary
[object]Package-leveldifferencesbetweentwosnapshots,eachlistsortedbyname.
source
[object]Package-leveldifferencesbetweentwosnapshots,eachlistsortedbyname.
mirror snapshot diff --packages: binaryandsource
Package-leveldifferencesbetweentwosnapshots,eachlistsortedbyname.
added
[array of object]Packagesonlypresentinthenewersnapshot,sortedbyname.
changed
[array of object] Packages present in both snapshots with different versions, sorted by
name.
removed
[array of object]Packagesonlypresentintheoldersnapshot,sortedbyname.
mirror snapshot diff --packages: packagelistentries
Asinglepackage(binaryorsource)thatdiffersbetweentwosnapshots.
name
[string]Packageidentity: <name>:<arch>forbinarypackages,theplainnameforsource
packages.
new-versions
[array of string]Versionsinthenewersnapshot. Emptyifthepackagewasremoved.
old-versions
[array of string]Versionsintheoldersnapshot. Emptyifthepackagewasadded.
37

APPENDIX
C
CONFIGURATION FILES
The Proxmox Offline Mirror configuration file is stored at /etc/proxmox-offline-mirror.
cfg by default. To use another file, pass --config <file> or set the
PROXMOX_OFFLINE_MIRROR_CONFIG environment variable. The command-line option takes
precedenceandcanappearbeforeorafterthesubcommand.
C.1 proxmox-offline-mirror.cfg
C.1.1 Options
Sectiontype’medium’: Configurationentryforanexternalmedium.
Requiredproperties:
mirrors
[<string>]IDsofthemirrorstosynctothemedium. Canbespecifiedmorethanonce.
mountpoint
[<string>]Mountpointwheremediumisavailableonmirroringsystem.
sync
[<boolean>]WhethertowritenewfilesusingFSYNC.
verify-mode
[<string>]Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoaccepts
true(full)andfalse(none)forcompatibility.
Sectiontype’mirror’: Configurationentryforamirroredrepository.
Requiredproperties:
architectures
[<string>]Listofarchitecturesthatshouldbemirrored. Canbespecifiedmorethanonce.
base-dir
[<string>]Pathtodirectorycontainingmirroredrepositorypool. Canbesharedbymultiple
mirrors.
key-path
[<string>]Pathtopublickeyfileforverifyingrepositoryintegrity.
repository
[<string>]Singlerepositorydefinitioninsources.listformat.
sync
[<boolean>]WhethertowritenewfilesusingFSYNC.
verify-mode
[<string>]Howtocheckfilesalreadyinthepool: none,size,orfull(checksum). Alsoaccepts
true(full)andfalse(none)forcompatibility.
Optionalproperties:
38

ProxmoxOfflineMirrorDocumentation,Release0.8.0
ignore-errors
[<boolean> (default=false)]Whethertodowngradedownloaderrorstowarnings.
latest-symlink
[<boolean> (default=true)]Whethertomaintainasymlinkpointingtothelastsuccess-
fulsnapshot.
latest-symlink-name
[<string> (default=last)]Nameofthelatest-snapshotsymlink.
request-timeout
[<integer> (0 - 604800)]Maximumdurationofarepositoryrequestinseconds,or0for
no limit. By default, allow 15 minutes plus the transfer time at 64 KiB/s when the expected
filesizeisknown.
use-subscription
[pve|pbs|pmg|pom] Access the repository with the active subscription key of this product
(requiredforProxmoxenterpriserepositories).
weak-crypto
[[[allow-sha1=<1|0>] [,min-dsa-key-size=<integer>] [,
min-rsa-key-size=<integer>]]]Whethertoallowusingweakcryptographyalgorithms
orparameters,deviatingfromthedefaultpolicy.
allow-sha1=<boolean> (default=false)
WhethertoallowSHA-1basedsignatures
min-dsa-key-size=<integer>
WhethertolowerthekeysizecutoffforDSA-basedsignatures
min-rsa-key-size=<integer>
WhethertolowerthekeysizecutoffforRSA-basedsignatures
skip-packages
[<string>] Package names to skip. Supports glob patterns. Can be specified more than
once.
skip-sections
[<string>]Sectionswhichshouldbeskipped. Canbespecifiedmorethanonce.
Sectiontype’subscription’: Subscriptionkeyusedforaccessingenterpriserepositoriesandfor
offlinesubscriptionactivation/renewal.
Requiredproperties:
server-id
[<string>]ServerID.
Optionalproperties:
description
[<string>]Description,e.g. whichsystemthiskeyisdeployedon
info
[<string>]base64encodedsubscriptioninfo-updatewith’refresh’command.
C.1. proxmox-offline-mirror.cfg 39

APPENDIX
D
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
40

ProxmoxOfflineMirrorDocumentation,Release0.8.0
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
41

ProxmoxOfflineMirrorDocumentation,Release0.8.0
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
42

ProxmoxOfflineMirrorDocumentation,Release0.8.0
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
43

ProxmoxOfflineMirrorDocumentation,Release0.8.0
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
44

ProxmoxOfflineMirrorDocumentation,Release0.8.0
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
45