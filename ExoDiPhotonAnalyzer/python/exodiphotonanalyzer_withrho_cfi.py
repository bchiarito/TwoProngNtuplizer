import FWCore.ParameterSet.Config as cms

diphotonAnalyzer = cms.EDAnalyzer('ExoDiPhotonAnalyzer',
                                  photonCollection = cms.untracked.InputTag("photons"),
                                  ptMin = cms.untracked.double(10),
                                  hltResults = cms.untracked.InputTag("TriggerResults","","HLT"),
                                  L1Results = cms.untracked.InputTag("gtDigis"),
                                  rho25Correction = cms.InputTag("kt6PFJets25","rho"),
                                  pileupCorrection = cms.untracked.InputTag("addPileupInfo"),
                                  removeSpikes = cms.untracked.bool(False),
                                  requireTightPhotons = cms.untracked.bool(True),
                                  requireGenEventInfo = cms.untracked.bool(False),
                                  isMC = cms.untracked.bool(True),
                                  #If running on Data do not change. Only loaded as strings into the Analyzer and will have no effect. If on MC then change to the specific files you need lodaed for the MC   
                                  PUMCFileName = cms.untracked.string("PileUpMC.root"),
                                  PUDataFileName = cms.untracked.string("PileupDataAug10thHistogram.root"),
                                  PUMCHistName = cms.untracked.string("MCPileUpHistogram"),
                                  PUDataHistName = cms.untracked.string("pileup"),
                                  PFIDCategory = cms.untracked.string("Medium"),
                                  IDMethod = cms.untracked.string("Detector"),
                                  #Input taken from Ilya's code
                                  rho = cms.InputTag("fixedGridRhoFastjetAll"),
                                  # Objects specific to AOD format
                                  photons = cms.InputTag("gedPhotons"),
                                  genParticles = cms.InputTag("genParticles"),
                                  # Objects specific to MiniAOD format
                                  photonsMiniAOD = cms.InputTag("slimmedPhotons"),
                                  genParticlesMiniAOD = cms.InputTag("prunedGenParticles"),
                                  # ValueMap names from the producer upstream
                                  full5x5SigmaIEtaIEtaMap   = cms.InputTag("photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta"),
                                  phoChargedIsolation = cms.InputTag("photonIDValueMapProducer:phoChargedIsolation"),
                                  phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer:phoNeutralHadronIsolation"),
                                  phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),
                                  # Locations of files with the effective area constants.
                                  # The constants in these files below are derived for PHYS14 MC.
                                  effAreaChHadFile = cms.FileInPath
                                  ("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfChargedHadrons_V2.txt"),
                                  effAreaNeuHadFile= cms.FileInPath
                                  ("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfNeutralHadrons_V2.txt"),
                                  effAreaPhoFile   = cms.FileInPath
                                  ("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfPhotons_V2.txt"),
                                  # ID decisions (common to all formats)
                                  phoLooseIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-PHYS14-PU20bx25-V2-standalone-loose"),
                                  phoMediumIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-PHYS14-PU20bx25-V2-standalone-medium"),
                                  phoTightIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-PHYS14-PU20bx25-V2-standalone-tight"),
                                  # recHitsEB = cms.InputTag("reducedEcalRecHitsEB"),
                                  # recHitsEE = cms.InputTag("reducedEcalRecHitsEE"),
                                  # recHitsEBMiniAOD = cms.InputTag("reducedEgamma:reducedEBRecHits"),
                                  # recHitsEEMiniAOD = cms.InputTag("reducedEgamma:reducedEERecHits")
                                  )
