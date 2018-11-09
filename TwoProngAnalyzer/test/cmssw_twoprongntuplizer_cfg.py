import sys
# Command line options
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ("python")
# required
options.register("sample", "", VarParsing.multiplicity.singleton, VarParsing.varType.string, "which sample we want to run over")
options.register("globalTag", "", VarParsing.multiplicity.singleton, VarParsing.varType.string, "global tag to use when running")
# usually required
options.register("isSignal", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Specify singal MC for looking for Phi and omega gen particles")
options.register("isTauTau", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Specify Z->ll MC")
options.register("mcInfo", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "include mc weight in Ttree")
# other
options.register("mcXS", 1.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "mc cross section, if desired to be filled in trees")
options.register("mcN", 1.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "mc number generated, if desired to be filled in trees")
options.register("out", "", VarParsing.multiplicity.singleton, VarParsing.varType.string, "output file name")
options.register("debug", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "True includes all output, False removes most of the per event output")
options.register("doLumis", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "use a JSON file to specify lumis")
options.register("originalGeometry", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "use the original loads for geometry, taken from original diphoton ntuplizer")
# filters
options.register("filterOnPhoton", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "filter on >=1 Photon")
options.register("filterOnTwoProng", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "filter on >=1 TwoProng")
options.register("DYsignal", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("DYbkg", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("tauPreselection", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
# two-prong object definition
options.register("standardTwoProng", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("tauModifiedTwoProng", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("commandLineTwoProng", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
# two-prong object definition detailed
options.register("optionalExtraTrack", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("trackDR", 0.05, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("minPt", 20.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("maxEta", 2.5, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("constituentMinPt", 3.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("trackMinPt", 3.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("photonMinPt", 3.0, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("trackAsym", 0.2, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("photonAsym", 0.15, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("photonBoxPhi", 0.2, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("photonBoxEta", 0.05, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("chargedIsoCut", 0.1, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("neutralIsoCut", 0.1, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
options.register("egammaIsoCut", 0.1, VarParsing.multiplicity.singleton, VarParsing.varType.float, "")
# photon definition
options.register("addConeHE", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Add cut to high-pt-photon-id: Cone based HE < 0.05")
# output specification
options.register("ntuples", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Add ntuples (Ttrees) to output")
options.register("includeCands", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Include all cand twoprongs in ntuple")
options.register("includeLoose", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Include Loose twoprongs in ntuple")
options.register("fakeRateHistos", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("triggerEffHistos", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("twoprongYieldHistos", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.register("stackedDalitzHistos", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "")
options.setDefault("maxEvents", 10)
options.parseArguments()

# shortcut settings
if options.sample == 'eta125':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi125_Eta/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185319/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'eta125'
if options.sample == 'eta300':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi300_Eta/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185421/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'eta300'
if options.sample == 'eta500':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi500_Eta/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185444/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'eta500'
if options.sample == 'eta750':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi750_Eta/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185603/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'eta750'
if options.sample == 'eta1000':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi1000_Eta/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185641/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'eta1000'
if options.sample == 'etaprime125':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi125_Etaprime/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_190054/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'etaprime125'
if options.sample == 'etaprime300':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi300_Etaprime/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185936/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'etaprime300'
if options.sample == 'etaprime500':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi500_Etaprime/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185904/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'etaprime500'
if options.sample == 'etaprime750':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi750_Etaprime/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185807/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'etaprime750'
if options.sample == 'etaprime1000':
  options.sample = 'file:/cms/jrj90/eos/twoprong_generation/etaetaprime_run/july132018/Phi1000_Etaprime/76X_mcRun2_asymptotic_v12_Run2_25ns_MINIAOD/180713_185720/0000/MINIAOD_1.root'
  options.globalTag = 'mc2016'
  options.isSignal = True
  options.out = 'etaprime1000'

# Begin configuration
import FWCore.ParameterSet.Config as cms
process = cms.Process("TwoProngAnalysis")

# Log messages
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(options.debug) )

# Source
readFiles = []
readFiles.extend( [ options.sample ] )
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring( readFiles ))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( options.maxEvents ) )

# Output files
if options.out == "":
  pre = 'TwoProngNtuplizer'
else:
  pre = 'TwoProngNtuplizer_'
post = '.root'
process.TFileService = cms.Service( "TFileService", fileName = cms.string( pre + options.out + post ) )

# Global Tag
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
if options.globalTag == 'mc2016':
  process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v6'
elif options.globalTag == 'mc2015':
  process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v12'
elif options.globalTag == 'data2015':
  process.GlobalTag.globaltag = '74X_dataRun2_HLT_v3'
elif options.globalTag == 'data2016':
  process.GlobalTag.globaltag = '80X_dataRun2_2016SeptRepro_v7'
else:
  process.GlobalTag.globaltag = options.globalTag
if process.GlobalTag.globaltag == "":
  print "Must choose a GlobalTag, GlobalTag left blank... exiting"
  sys.exit()
print "Using GlobalTag: ", process.GlobalTag.globaltag

# Allow unscheduled
process.options.allowUnscheduled = cms.untracked.bool(True)

# Geometry for photon saturation 
if not options.originalGeometry:
  process.load("Configuration.Geometry.GeometryECALHCAL_cff") # default
else:
  process.load("Configuration.StandardSequences.GeometryDB_cff")

# filter on vertices
vtxCollName = 'offlineSlimmedPrimaryVertices'
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag(vtxCollName),
                                           minimumNDOF = cms.uint32(4),
                                           maxAbsZ = cms.double(24),	
                                           maxd0 = cms.double(2)	
)

# adds computation of more Photon ID decisions, this block comes from high-pt-id code, but these ids are not currently being use in high-pt-id
# included for reference and for agreement with high-pt-id framework
# Setup VID for EGM ID
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
switchOnVIDPhotonIdProducer(process, DataFormat.MiniAOD)
my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring15_25ns_V1_cff']
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)

# JSON file to choose what lumis to process
if not options.doLumis=="":
    import FWCore.PythonUtilities.LumiList as LumiList
    goodlumis = options.doLumis
    process.source.lumisToProcess = LumiList.LumiList(filename = goodlumis).getVLuminosityBlockRange()

# the ntuplizer
if options.tauModifiedTwoProng:
  process.load('TwoProngAnalysis.TwoProngAnalyzer.cmssw_twoprongntuplizer_taumodified_cfi')
elif options.commandLineTwoProng or options.standardTwoProng:
  process.load('TwoProngAnalysis.TwoProngAnalyzer.cmssw_twoprongntuplizer_standard_cfi')
else:
  print "must select one twoprong version"
# override if using command line
if options.commandLineTwoProng:
    process.twoprongNtuplizer.candidateMinPt = options.minPt
    process.twoprongNtuplizer.candidateAbsMaxEta = options.maxEta
    process.twoprongNtuplizer.candidateTrackAsymmetryCut = options.trackAsym
    process.twoprongNtuplizer.candidatePhotonAsymmetryCut = options.photonAsym
    process.twoprongNtuplizer.candidateOptionalExtraTrack = options.optionalExtraTrack
    process.twoprongNtuplizer.chargedHadronPairMinDR = options.trackDR
    process.twoprongNtuplizer.chargedHadronMinPt = options.constituentMinPt
    process.twoprongNtuplizer.photonPtCut = options.constituentMinPt
    process.twoprongNtuplizer.photonPhiBoxSize = options.photonBoxPhi
    process.twoprongNtuplizer.photonEtaBoxSize = options.photonBoxEta
    process.twoprongNtuplizer.chargedIsoCut = options.chargedIsoCut
    process.twoprongNtuplizer.neutralIsoCut = options.neutralIsoCut
    process.twoprongNtuplizer.egammaIsoCut = options.egammaIsoCut
# settings always overwritten by command line
process.twoprongNtuplizer.includeSignalGenParticles = options.isSignal
process.twoprongNtuplizer.runningOnTauTauMC = options.isTauTau
process.twoprongNtuplizer.mcXS = options.mcXS
process.twoprongNtuplizer.mcN = options.mcN
process.twoprongNtuplizer.includeMCInfo = options.mcInfo
process.twoprongNtuplizer.debug = options.debug
# filters
process.twoprongNtuplizer.filterOnPhoton = options.filterOnPhoton;
process.twoprongNtuplizer.filterOnTwoProng = options.filterOnTwoProng;
# Cone HE Photon
process.twoprongNtuplizer.addPhotonCutDrConeHE = options.addConeHE;
# object includes
process.twoprongNtuplizer.includeAllCandObjects = options.includeCands;
process.twoprongNtuplizer.includeAllLooseObjects = options.includeLoose;
# histo includes
process.twoprongNtuplizer.fakeRateHistos = options.fakeRateHistos;
process.twoprongNtuplizer.triggerEffHistos = options.triggerEffHistos;
process.twoprongNtuplizer.twoprongYieldHistos = options.twoprongYieldHistos;
process.twoprongNtuplizer.stackedDalitzHistos = options.stackedDalitzHistos;

# options filters
process.tauFilters = cms.Sequence()
if options.DYsignal:
  process.genDYsignalFilt = cms.EDFilter('ZtoTauHadTruthSelector',
    filterByTruthDecayType = cms.untracked.vdouble(5.1,5.2,5.3,5.4),
  )
  process.tauFilters *= process.genDYsignalFilt
if options.DYsignal:
  process.genDYbkgFilt = cms.EDFilter('ZtoTauHadTruthSelector',
    filterByTruthDecayType = cms.untracked.vdouble(1,2,3,4,6,7,8,9,0,10,-1),
  )
  process.tauFilters *= process.genDYbkgFilt
if options.tauPreselection:
  process.preselection = cms.EDFilter('ZtoTauHadRecoSelector',
    dumpCutflow = cms.untracked.bool(options.DYsignal or options.DYbkg)
  )
  process.tauFilters *= process.preselection

process.path = cms.Path(process.tauFilters * process.egmPhotonIDSequence * process.twoprongNtuplizer)