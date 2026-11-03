| OpenShift    |     | Data | Foundation |
| ------------ | --- | ---- | ---------- |
| Subscription |     |      | Guide      |
(2024/08)
| An overview     | of how | subscriptions | for OpenShift |
| --------------- | ------ | ------------- | ------------- |
| Data Foundation | work   |               |               |
LastUpdated:2024-08-19

Red Hat OpenShift Data Foundation Subscription Guide
LegalNotice
Copyright©2022RedHat,Inc.
ThetextandillustrationsinthisdocumentarelicensedbyRedHatunderaCreativeCommons
Attribution–ShareAlike3.0Unportedlicense("CC-BY-SA").AnexplanationofCC-BY-SAis
availableat
http://creativecommons.org/licenses/by-sa/3.0/
InaccordancewithCC-BY-SA,ifyoudistributethisdocumentoranadaptationofit,youmust
providetheURLfortheoriginalversion.
RedHat,asthelicensorofthisdocument,waivestherighttoenforce,andagreesnottoassert,
Section4dofCC-BY-SAtothefullestextentpermittedbyapplicablelaw.
RedHat,RedHatEnterpriseLinux,theShadowmanlogo,theRedHatlogo,JBoss,OpenShift,
Fedora,theInfinitylogo,andRHCEaretrademarksofRedHat,Inc.,registeredintheUnited
Statesandothercountries.
Linux®istheregisteredtrademarkofLinusTorvaldsintheUnitedStatesandothercountries.
Java®isaregisteredtrademarkofOracleand/oritsaffiliates.
XFS®isatrademarkofSiliconGraphicsInternationalCorp.oritssubsidiariesintheUnited
Statesand/orothercountries.
MySQL®isaregisteredtrademarkofMySQLABintheUnitedStates,theEuropeanUnionand
othercountries.
Node.js®isanofficialtrademarkofJoyent.RedHatisnotformallyrelatedtoorendorsedbythe
officialJoyentNode.jsopensourceorcommercialproject.
TheOpenStack®WordMarkandOpenStacklogoareeitherregisteredtrademarks/service
marksortrademarks/servicemarksoftheOpenStackFoundation,intheUnitedStatesand
othercountriesandareusedwiththeOpenStackFoundation'spermission.
Wearenotaffiliatedwith,endorsedorsponsoredbytheOpenStackFoundation,orthe
OpenStackcommunity.
Allothertrademarksarethepropertyoftheirrespectiveowners.
Abstract
ThisdocumentprovidesanoverviewonhowOpenShiftDataFoundationssubscriptionswork.
Page2

| Red Hat OpenShift                                  | Data Foundation | Subscription | Guide |     |
| -------------------------------------------------- | --------------- | ------------ | ----- | --- |
| WhatisRedHatOpenShiftDataFoundation?               |                 |              |       | 5   |
| WherecanRedHatOpenShiftDataFoundationbedeployed?   |                 |              |       | 5   |
| HowcanRedHatOpenShiftDataFoundationbedeployed?     |                 |              |       | 6   |
| InternalmodeOpenShiftDataFoundation                |                 |              |       | 6   |
| InternalmodedeployedonOpenShiftinfrastructurenodes |                 |              |       | 6   |
| ExternalmodeOpenShiftDataFoundation                |                 |              |       | 7   |
ExternalmodeOpenShiftDataFoundationwithmultipleOpenShiftclusters 8
| RedHatOpenShiftDataFoundationEditions          |            |     |     | 9   |
| ---------------------------------------------- | ---------- | --- | --- | --- |
| RedHatOpenShiftDataFoundationEssentialsEdition |            |     |     | 9   |
| RedHatOpenShiftDataFoundationAdvancedEdition   |            |     |     | 9   |
| Mixed workload                                 | definition |     |     | 9   |
FeaturecomparisonRedHatOpenShiftDataFoundationEssentialsvsAdvancedEdition
10
| RedHatOpenShiftPlatformPlus |     |     |     | 10  |
| --------------------------- | --- | --- | --- | --- |
RedHatOpenShiftPlatformPluswithRedHatOpenShiftDataFoundationAdvanced 11
| HowareOpenShiftDataFoundationsubscriptionscounted? |     |     |     | 12  |
| -------------------------------------------------- | --- | --- | --- | --- |
| Bare-metaldeployments                              |     |     |     | 12  |
| Socket-basedsubscriptions                          |     |     |     | 12  |
| Example1-InternalMode                              |     |     |     | 12  |
Example2-Externalmodewith1OpenShiftclusterand1OpenShiftDataFoundation
| cluster |     |     |     | 12  |
| ------- | --- | --- | --- | --- |
Example3-Externalmodewith3OpenShiftclustersand1OpenShiftDataFoundation
| cluster                                               |     |     |     | 13  |
| ----------------------------------------------------- | --- | --- | --- | --- |
| Virtualizeddeployments                                |     |     |     | 13  |
| CoresversusvCPUsandHyper-ThreadingTechnology          |     |     |     | 13  |
| Example1-InternalMode                                 |     |     |     | 13  |
| Example2-InternalModewithinfrastructurenodes          |     |     |     | 14  |
| OpenShiftDataFoundationdeploymentswithoutworker-nodes |     |     |     | 14  |
| OpenShiftDataFoundationCapacityboundaries             |     |     |     | 14  |
Example-OpenShiftclustersand1ExternalModeOpenShiftDataFoundationcluster
| with12PBrawcapacity                                |     |     |     | 15  |
| -------------------------------------------------- | --- | --- | --- | --- |
| SupportLevelofSubscriptions                        |     |     |     | 16  |
| DisasterRecoverydeploymentsandsubscriptioncoverage |     |     |     | 16  |
| HotDR                                              |     |     |     | 16  |
| WarmDR                                             |     |     |     | 16  |
| ColdDR                                             |     |     |     | 17  |
Page3

| Red Hat OpenShift | Data Foundation | Subscription | Guide |
| ----------------- | --------------- | ------------ | ----- |
Migrationandswingupgrades 17
Page4

Red Hat OpenShift Data Foundation Subscription Guide
What is Red Hat OpenShift Data Foundation ?
RedHatOpenShiftDataFoundation(OpenShiftDataFoundation)isasoftware-defined
persistentstoragesolutionforcontainerizedapplicationsrunningonOpenShiftandfor
OpenShiftinfrastructurecomponentsandserviceswhichrequirestoringdata.OpenShiftData
Foundationprovidespersistentfile,blockorobjectstorageservices.Storageservicescanbe
provisionedbyadministrators,byusersorAPI-driven.Asasoftware-definedstoragesolution,
OpenShiftDataFoundationprovidesthesoftwarecomponentstodeploy,virtualize,provision,
manageandmonitorallstoragerelatedservices.OpenShiftDataFoundationistypically
deployedassoftwarecontainersrunningonphysicalorvirtualservers.Theseserversmust
providephysicalorvirtualdiskstobeconsumedandvirtualizedbythestoragesoftware.
Where can Red Hat OpenShift Data Foundation be
deployed ?
RedHatOpenShiftDataFoundationcanbedeployedonmostplatformsthatRedHat
OpenShiftContainerPlatformcanbedeployedon,butitcanalsobedeployedasadedicated
standalonestoragecluster.Therearefundamentallytwodifferentdeploymentflavors:
● RedHatOpenShiftDataFoundationdeployedonphysicalservers
=>Bare-metalnodes
=>Socket-basedsubscriptionswillberequired
● RedHatOpenShiftDataFoundationdeployedonvirtualserversorinthepubliccloud
=>Virtualnodes
=>Core-basedsubscriptionswillberequired
Dependingonthedeploymentplatform,differentunitsofmeasurewillbeusedtocount
subscriptionsforRedHatOpenShiftDataFoundation.
Page5

| Red Hat  | OpenShift | Data Foundation |     | Subscription | Guide      |     |
| -------- | --------- | --------------- | --- | ------------ | ---------- | --- |
| How      | can Red   | Hat OpenShift   |     | Data         | Foundation | be  |
| deployed | ?         |                 |     |              |            |     |
RedHatOpenShiftDataFoundationcanbedeployedintwodifferentdeploymentmodes:
InternalmodeandExternalmode
| Internal | mode | OpenShift | Data | Foundation |     |     |
| -------- | ---- | --------- | ---- | ---------- | --- | --- |
InternalmodemeansthatallOpenShiftDataFoundationsoftwarecomponentsaredeployedas
containersdirectlyontheOpenShiftclusternodestogetherwithothercontainerized
applications.Ininternalmode,OpenShiftDataFoundationistypicallydeployedonOpenShift
workernodesorinfrastructurenodes.Thesenodesneedtoprovidephysicalorvirtualstorage
devicesandcapacitywhichcanbeconsumedbyRedHatOpenShiftDataFoundation.Ininternal
modethestorageserviceswhichOpenShiftDataFoundationprovidescanonlybeconsumedby
thesameOpenShiftclusterwhereOpenShiftDataFoundationisdeployed.
InternalmodeiscurrentlytheonlydeploymentmodelthatissupportedforOpenShift
deploymentsinthepubliccloudoronVMware.
Figure1:OpenShiftwithOpenShiftDataFoundationinInternalMode
| Internal | mode | deployed | on  | OpenShift | infrastructure | nodes |
| -------- | ---- | -------- | --- | --------- | -------------- | ----- |
Note:OpenShiftDataFoundationcanalsobedeployedonOpenShiftinfrastructurenodesbut
forsubscriptionsonlytheworkernodecoresorsocketsarecounted.BydeployingOpenShift
DataFoundationoninfrastructurenodes,customerscanpotentiallyreducetheamountofcores
neededontheworkernodeswhichcanhelptodecreasethesubscriptioncostasworkernode
cores/socketsisthemainmeasureforcountingsubscriptionsinOpenShift.
Page6

Red Hat OpenShift Data Foundation Subscription Guide
Figure2:OpenShiftwithOpenShiftDataFoundationinInternalModedeployedinOpenShiftInfrastructureNodes
External mode OpenShift Data Foundation
ExternalmodemeansthatOpenShiftDataFoundationisdeployedonadedicatedstorage
cluster,typicallyaseparateCephcluster,whichprovidesitsstorageservicestooneormultiple
OpenShiftclusters.Externalmodeisonlyavailableforon-premiseandbare-metal
deployments.Theintegrationandmanagementofthesestorageservicesisprovidedbythe
OpenShiftDataFoundationOperatorwhichneedstobedeployedoneachOpenShiftcluster
whichrequirespersistentstorage.AttachingaRedHatCephStorageclusterdirectlyto
OpenShiftwithouttheseintegrationcomponentsisnotsupported.
Pleasenote:TechnicallyanODFExternalModedeploymentconsistsofadedicatedRedHat
CephStorageclusterandtheODFintegrationbitsrunningonOpenShift.However,herewe
viewthisfromasubscriptionperspectiveonly.ODFAdvanced(partofOpenShiftPlatformPlus
withODFAdvanced)containsallsubscriptionsrequiredtodeployadedicatedCephstorage
clusterincludingRHEL.
Page7

| Red Hat | OpenShift | Data Foundation | Subscription | Guide |
| ------- | --------- | --------------- | ------------ | ----- |
Figure2:OpenShiftwithOpenShiftDataFoundationinExternalMode
| External  | mode     | OpenShift | Data Foundation | with multiple |
| --------- | -------- | --------- | --------------- | ------------- |
| OpenShift | clusters |           |                 |               |
InExternalMode,theOpenShiftDataFoundationstorageservicescanalsobeconsumedby
multipleOpenShiftclustersandalsoworkloadswhicharenotdeployedonOpenShift.
Note:Aproperscopingofworkloadrequirementsneedstobeconductedbeforemultiple
OpenShiftclustersareattachedtoonesingleOpenShiftDataFoundationStorageclusteras
performance,throughputandlatenciesarenotinfinite.WerecommendgettingRedHatGlobal
ProfessionalServicesoracertifiedRedHatOpenShiftPartnerinvolvedtoconductthescoping.
Figure3:MultipleOpenShiftclusterswithoneOpenShiftDataFoundationStoragecluster
Page8

| Red Hat | OpenShift | Data Foundation | Subscription | Guide    |     |
| ------- | --------- | --------------- | ------------ | -------- | --- |
| Red Hat | OpenShift | Data            | Foundation   | Editions |     |
TherearetwodifferentflavorsofOpenShiftDataFoundationavailable,OpenShiftData
FoundationEssentialsandOpenShiftDataFoundationAdvanced.
| Red Hat | OpenShift | Data Foundation |     | Essentials | Edition |
| ------- | --------- | --------------- | --- | ---------- | ------- |
providespersistentandhighlyavailablestorageforapplicationsrunningonOpenShiftand
OpenShiftinternalserviceslikelogging,metricsandregistry,etc.Therecommendedwaytoget
RedHatOpenShiftDataFoundationEssentialsisthroughgettingRedHatOpenShiftPlatform
PluswhichincludesOpenShiftDataFoundationEssentials.
| Red Hat | OpenShift | Data Foundation |     | Advanced | Edition |
| ------- | --------- | --------------- | --- | -------- | ------- |
comeswithadditionaldatasecurity,disasterrecoveryfeaturesandmoredeploymentoptions
thanOpenShiftDataFoundationEssentials.TherecommendedwaytoimplementOpenShift
DataFoundationAdvancedEditionisthroughgettingRedHatOpenShiftPlatformPluswith
OpenShiftDataFoundationAdvanced.Thisproductbundlecontainsallthenecessary
technologiesrequiredtoimplementacontainerplatformwithenhancedresilience,securityand
manageability.ODFAdvancedEditionalsosupportsmixedworkloads.
| Mixed | workload | definition |     |     |     |
| ----- | -------- | ---------- | --- | --- | --- |
MixedworkloadsforODFAdvancedaredefinedasODFcanprovideS3objectstoragefor
applicationsdeployedonOpenShiftandoutsideofOpenShifte.g.applicationsrunningonRHEL.
TheuseofCephRBDorCephFSdirectlyforexternalapplicationsorplatformsbeyondtheuseas
persistentstorageforOpenShiftthroughODFAdvancedisnotsupportedandnotcoveredby
thesubscription.MixedworkloadsareonlysupportedforODFAdvanceddeployedinexternal
mode.
Page9

| Red Hat OpenShift | Data Foundation | Subscription | Guide |     |
| ----------------- | --------------- | ------------ | ----- | --- |
Feature comparison Red Hat OpenShift Data Foundation Essentials vs
Advanced Edition
| ProductComponent |     |     | OPP | OPPwODFAdv |
| ---------------- | --- | --- | --- | ---------- |
|                  |     |     | ☑   | ☑          |
RedHatOpenShiftContainerPlatform
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
RedHatAdvancedClusterManagementforKubernetes
| RedHatAdvancedContainerSecurityforKubernetes |     |     | ☑   | ☑   |
| -------------------------------------------- | --- | --- | --- | --- |
|                                              |     |     | ☑   | ☑   |
RedHatQuay
OpenShiftDataFoundation
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
Block&File
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
Object
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
MultiCloudGateway
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
NodeandDiskresiliency
| StorageOperatorsbasedautomation |     |     | ☑   | ☑   |
| ------------------------------- | --- | --- | --- | --- |
|                                 |     |     | ☑   | ☑   |
Compression
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
DeduplicationforMultiCloudObjectGateway
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
LocalSnapshots&Clones
| BasicCluster-wideEncryption |     |     | ☑   | ☑   |
| --------------------------- | --- | --- | --- | --- |
|                             |     |     | ☑   | ☑   |
Cross-availabilityzoneHA(3zones)
|     |     |     | ☑   | ☑   |
| --- | --- | --- | --- | --- |
InternalDeploymentMode
StretchCluster
|     |     |     | ☐   | ☑   |
| --- | --- | --- | --- | --- |
(OCPandODFstretchedover2zones+arbiter)
|     |     |     | ☐   | ☑   |
| --- | --- | --- | --- | --- |
AdvancedEncryptionwithKMSsupport
| MetroDR(syncreplication)(1) |     |     | ☐   | ☑   |
| --------------------------- | --- | --- | --- | --- |
|                             |     |     | ☐   | ☑   |
RegionalDR(asyncreplication)(2)
|     |     |     | ☐   | ☑   |
| --- | --- | --- | --- | --- |
ExternalDeploymentMode
|     |     |     | ☐   | ☑   |
| --- | --- | --- | --- | --- |
Multi-ClusterSupport
| Mixed-WorkloadSupport(3) |     |     | ☐   | ☑   |
| ------------------------ | --- | --- | --- | --- |
|                          |     |     | ☐   | ☑   |
HostedControlPlaneSupport(4)
| RawCapacityincluded(5) |     |     | 256TB |     |
| ---------------------- | --- | --- | ----- | --- |
(1)RequiresStretchedStorageClusterandRHACM
(2)RequiresRHACM
(3)Mixedworkloadsdefinition:applicationsorclientsthatrequireS3objectstoragedeployedonOpenShiftorexternally.This
doesnotcoverusageofCephRBDorCephFSservicesbeyondOpenShiftandthroughODFAdvanced.
(4)Subscriptioncountisbasedonthehostedworkers.OPP+AdvancedshouldbeusedforthiscaseinsteadofOPP.
(5)ExpandablethroughCapacityExpansionPacks
Page10

Red Hat OpenShift Data Foundation Subscription Guide
Red Hat OpenShift Platform Plus
RedHatOpenShiftPlatformPluscontainsallcomponentsrequiredinamodernHybridCloud
Platformforstatefulapplications.Italsoincludespersistentstorageandhighavailability
featuresandcanbedeployedvirtualizedoronbare-metalservers.RedHatOpenShiftData
FoundationEssentialsispartofthissolution.Bydefinition,RedHatOpenShiftDataFoundation
EssentialsalwayshastobedeployedinInternalMode(directlyontheOpenShiftnodes).
RedHatOpenShiftPlatformPluscontains
- RedHatOpenShiftContainerPlatform
- RedHatOpenShiftDataFoundationEssentials
- RedHatAdvancedClusterManagement
- RedHatAdvancedContainerSecurity
- RedHatQuay
Red Hat OpenShift Platform Plus with Red Hat OpenShift Data
Foundation Advanced
InadditiontoallcomponentsandfeaturesofRedHatOpenShiftPlatformPlus,thissolution
alsocontainsRedHatOpenShiftDataFoundationAdvancedwhichbydefinitioncanalsobe
deployedasaseparateanddedicatedRedHatOpenShiftDataFoundationstoragecluster,
whichiscalledExternalMode.
RedHatOpenShiftPlatformPluswithRedHatOpenShiftDataFoundationAdvancedcontains
- RedHatOpenShiftContainerPlatform
- RedHatOpenShiftDataFoundationAdvanced
- RedHatAdvancedClusterManagement
- RedHatAdvancedContainerSecurity
- RedHatQuay
MoredetailedinformationonRedHatOpenShiftPlatformPlussizingandsubscriptionscanbe
foundhere:
https://www.redhat.com/en/resources/self-managed-openshift-sizing-subscription-guide
Page11

| Red Hat | OpenShift     | Data Foundation | Subscription    | Guide         |
| ------- | ------------- | --------------- | --------------- | ------------- |
| How     | are OpenShift |                 | Data Foundation | subscriptions |
| counted | ?             |                 |                 |               |
IngeneralRedHatOpenShiftDataFoundationsubscriptionsarecountedthesamewayasRed
HatOpenShiftarecounted:everyOpenShiftworkernodeneedsanactiveRedHat
subscription.SubscriptionswilldifferdependingonwhereOpenShift/OpenShiftData
Foundationisbeingdeployed.
| Bare-metal | deployments |     |     |     |
| ---------- | ----------- | --- | --- | --- |
WheneverOpenShift/OpenShiftDataFoundationisdeployedonbare-metalservers,
subscriptionsarebasedonCPUsockets.
| Socket-based | subscriptions |     |     |     |
| ------------ | ------------- | --- | --- | --- |
OneOpenShiftDataFoundationsocket-basedsubscriptionscanbeusedforphysicalservers
withupto2CPUsocketsorupto64cores(unlimitedcoresforNFVcases)intotalandcannot
beusedforvirtualizedOpenShiftdeployments.
| Example | 1 - Internal | Mode |     |     |
| ------- | ------------ | ---- | --- | --- |
OpenShiftisdeployedon3masternodesand6workernodes.OpenShiftDataFoundationIs
deployedinthesameenvironmentrunningonthe6workernodes.Eachofthesephysicalnodes
haveeither1or2CPUsockets.Youwouldrequire:
6xRedHatOpenShiftPlatformPlus(includesOpenShiftDataFoundationEssentials),
1-2socketsubscription
Example 2 - External mode with 1 OpenShift cluster and 1 OpenShift Data
| Foundation | cluster |     |     |     |
| ---------- | ------- | --- | --- | --- |
OpenShiftisdeployedon3mastersand2workernodes.OpenShiftDataFoundationis
deployedinExternalmodeon10storagenodes.Youwouldrequire:
2xRedHatOpenShiftPlatformPluswithRedHatOpenShiftDataFoundation
Advanced,1-2socketsubscription
Page12

Red Hat OpenShift Data Foundation Subscription Guide
Example 3 - External mode with 3 OpenShift clusters and 1 OpenShift Data
Foundation cluster
OpenShiftisdeployedon3clusterswith3mastersand4workernodes,each.OpenShiftData
FoundationisdeployedinExternalmodeon10storagenodes.Youwouldrequire:
3x4=12xRedHatOpenShiftPlatformPluswithRedHatOpenShiftDataFoundation
Advanced,1-2socketsubscription
Virtualized deployments
WheneverOpenShift/OpenShiftDataFoundationisdeployedonvirtualizedserverslikea
Hypervisorplatform,aprivatecloudorpubliccloudinfrastructure,subscriptionswillbebasedon
CPUcores.
Cores versus vCPUs and Hyper-Threading Technology
Makingadeterminationaboutwhetherornotaparticularsystemusesoneormorecoresis
currentlydependentonwhetherornotthatsystemhashyperthreadingavailable.Notethat
Hyper-ThreadingisafeatureonlyavailableonIntelCPUsbute.g.AMDCPUshaveasimilar
featurecalledSMT.ForsimplicitywewillrefertoHyper-Threadinggenericallyinthisdocument.
TodeterminewhetheraparticularsystemsupportsHyper-Threading,pleasevisit
https://access.redhat.com/solutions/7714.
ForsystemswhereHyper-ThreadingisenabledandwhereoneHyper-Threadequatestoone
visiblesystemcore,acalculationofcoresataratioof2cores=4vCPUsisused.
Inotherwords,a2-coresubscriptioncovers4vCPUsinaHyper-Threadedsystem.AlargeVM
mighthave8vCPUs,equatingto4subscriptioncores.Assubscriptionscomeinunitsof
2-cores,youwouldneedtwo2-coresubscriptionstocoverthese4coresor8vCPUs.
WhereHyper-Threadingisnotenabledandwhereeachvisiblesystemcorecorrelatesdirectlyto
anunderlyingphysicalcore,acalculationof2cores=2vCPUsisused.
Example 1 - Internal Mode
OpenShiftisdeployedon3masternodesand6workernodes.OpenShiftDataFoundationIs
deployedinthesameenvironmentrunningonthe6workernodes.Eachoftheworkernodesis
provisionedwith20cores/40vCPUs.Youwouldrequire:
Page13

Red Hat OpenShift Data Foundation Subscription Guide
6x20/2=60xRedHatOpenShiftPlatformPlus,2-coresubscription
Example 2 - Internal Mode with infrastructure nodes
OpenShiftisdeployedinthepubliccloudon3masternodes,2workernodesand5
infrastructurenodes.OpenShiftDataFoundationIsdeployedinthesameenvironmentrunning
onthe5infrastructurenodes.Eachoftheworkernodesisprovisionedwith20cores/40
vCPUs.Theinfrastructurenodesareprovisionedwith40cores/80vCPUs.Youwouldrequire:
2x20/2=20xRedHatOpenShiftPlatformPlus,2-coresubscription
OpenShift Data Foundation deployments without worker-nodes
HostedControlPlane
OpenShiftDataFoundationalignswithOpenShiftsubscriptionguidanceandwillbeusing1:1
RationwithOpenShiftonthemanagedhostedclusters,meaningOpenShiftPlatformPlus+
Advancedisrequiredhere.
ACMHubCluster
IfOpenShiftDataFoundationisusedtoprovidestorageforOpenShiftinternalinfrastructure
servicessuchasACM,ACSorQuaydeployedonadedicatedOpenShiftclusterwithoutany
workernodes,20xOpenShiftDataFoundationAdvancedsubscriptions(20x2-core)needto
beacquiredforthatinfrastructure.HoweverifODFissubscribedinthemanagedclusters
already,thenODFcanalsobedeployedforACMwithoutanyadditionalcost.
ThisrulealsoappliestoOpenShiftPlatformPlusdeploymentswherenoworkernodesare
subscribedbutOPPisusedtodeployACM,ACSorQuaywithACMdeploymentmodeof
active/backup.
OpenShift Data Foundation Capacity boundaries
EachRedHatOpenShiftContainerPlatformClusterwithRedHatOpenShiftDataFoundationis
entitledupto256TBofrawstoragecapacity.Additionalstoragecapacitycanbepurchased
throughRedHatOpenShiftDataFoundationCapacityExpansionPacks.CapacityExpansion
PackscannotbesharedacrossmultipleODFclustersbutthestoragecapacitiesofeach
OpenShiftcluster(256TB)addstothetotalcapacityofthecentralCephstorageclusterincase
ofanexternalmodedeployment.Alsoformixedworkloadslikee.g.anexternalapplicationwhich
requiresS3objectstorage,theadditionalcapacityrequiredforthisapplicationhastobeadded
tothetotalcapacityprovidedforOpenShift.ThefollowingOpenShiftDataFoundation
CapacityExpansionPacksareavailable:
Page14

Red Hat OpenShift Data Foundation Subscription Guide
256TB,512TB,1PB,2PB,3PB,4PB,5PBand10PB
Example - OpenShift clusters and 1 External Mode OpenShift Data
Foundation cluster with 12PB raw capacity
OpenShiftisdeployedon3bare-metalclusterswith3mastersand4workernodes,each.
OpenShiftDataFoundationisdeployedinExternalmodeon10storagenodeswithatotalraw
capacityof12PB.Youwouldrequire:
3x4=12xRedHatOpenShiftPlatformPluswithRedHatOpenShiftDataFoundation
Advanced,1-2socketsubscription
1xRedHatOpenShiftDataFoundationCapacityExpansionPack,10PBsubscription
1xRedHatOpenShiftDataFoundationCapacityExpansionPack,2PBsubscription
Page15

Red Hat OpenShift Data Foundation Subscription Guide
Support Level of Subscriptions
RedHatOpenShiftDataFoundationisavailableintwodifferentsupportlevels:
1. PremiumSupport:Coverageis24x7
2. StandardSupport:CoverageisStandardbusinesshours
Moredetailedinformationcanbefoundhere:
https://access.redhat.com/support/offerings/production/sla
Foranyseriousproductiondeploymentit’sstronglyadvisedtodefaulttoPremiumSupport.
Disaster Recovery deployments and subscription
coverage
RedHatdefinesthreetypesofdisasterrecovery(DR)environments—hot,warm,andcold.Paid
OpenShiftandOpenShiftDataFoundationAdvancedsubscriptionsfortheDR-siteareneeded
forhotDRonly.ForMetroDRorRegionalDRsolutions,RedHatOpenShiftDataFoundation
AdvancedandRedHatAdvancedClusterManagementforKubernetessubscriptionsare
requiredfortheprimarysiteandalsofortheDR-site. IncaseofanOpenShiftclusterwith
OpenshiftDataFoundationstretchedacrosstwositeswithdatavolumesbeingsynchronously
replicatedacrossthetwosites,itrequiresanOpenShiftDataFoundationAdvanced
subscription. ThebestwaytomeetalltechnicalrequirementsforDRistoinvolveRedHat
ConsultingandusetheRedHatOpenShiftPlatformPluswithRedHatOpenShiftData
FoundationAdvancedsolutionbundle.
Hot DR
HotDRsystemsaredefinedasfullyfunctionalandrunningconcurrentlytotheproduction
systems.WhenDataVolumesareactivelybeingreplicatedeithersynchronouslyor
asynchronouslybetweenclusterstheyareconsideredtobeHotDRsystems. HotDRsystems
arereadytoimmediatelyactivatetheirApplications,receiveclientIOtrafficandtakeoverinthe
eventofadisasterwithintheprimaryenvironment.
Warm DR
WarmDRsystemsaredefinedasalreadystockedwithhardwarerepresentingareasonable
facsimileofthatfoundintheprimarysite,butcontainingnocustomerdata.WarmDRsystems
shouldnotbeparticipatinginactivedatavolumereplicationeithersynchronouslyor
Page16

Red Hat OpenShift Data Foundation Subscription Guide
asynchronouslybetweenclusters.WarmDRrecoveryrequirescustomer’sdatahavingtobe
restoredontotheexistingclusterhardwarefromalastbackuplocatedoutsideofthecluster.
Cold DR
ColdDRsystemsaredefinedashavingtheinfrastructureinplace,butnotthefulltechnology
(hardware,software)neededtorestoreservice.
ForbothwarmDRandcoldDR,theRedHatOpenShiftsubscriptionscanbetransferredfrom
theprimaryenvironmenttotheDRenvironmentwhenthedisasteroccurstorestoreserviceand
maintaincompliancewithRedHat’ssubscriptionterms.
Migration and swing upgrades
RedHatOpenShift4providesin-placeupgradesbetweenminorversions.However,for
customerswhoareupgradingfromRedHatOpenShift3orneedtoperformaswingupgrade
duetomaintenancewindowsorotherconsiderations,yourRedHatOpenShiftsubscriptionwill
coverboththeoriginalanddestinationinfrastructureofaone-waymigrationuntilsuch
migrationiscomplete.ThisalsoappliestoRedHatOpenShiftDataFoundation.
Duringthemigration,RedHat’ssubscriptionmanagementtoolswillshowyourenvironmentas
beingout-of-compliancebasedonthenumberofOpenShiftorOpenShiftDataFoundation
subscriptionsyoupurchased.RedHatallowsthisformajorversionupgradesandwillnotrequire
thepurchaseofadditionalsubscriptionstogetbackintocomplianceduringthemigration.
Page17