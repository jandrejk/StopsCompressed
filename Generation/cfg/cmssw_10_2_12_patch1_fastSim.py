import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')
options.register('ctau',  0.001,  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.float,  "value for ctau")
options.register('mStop',  250,  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int,  "stop mass")
options.register('dm',  20.,  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.float,  "mass gap")
options.maxEvents=1000 # maxEvents is a registered option by default. 

if not 'ipython' in VarParsing.sys.argv[0]: options.parseArguments()
else: print "No parsing of arguments!"

# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIIAutumn18FSPremix-00052-fragment.py --fileout file:SUS-RunIIAutumn18FSPremix-00052.root --pileup_input dbs:/Neutrino_E-10_gun/RunIIFall17FSPrePremix-PUMoriond18_102X_upgrade2018_realistic_v15-v2/GEN-SIM-DIGI-RAW --mc --eventcontent AODSIM --fast --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200) --step GEN,SIM,RECOBEFMIX,DIGI,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --procModifiers premix_stage2 --nThreads 2 --datamix PreMix --era Run2_2018_FastSim --python_filename SUS-RunIIAutumn18FSPremix-00052_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('RECO',eras.Run2_2018_FastSim,eras.fastSim,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIIAutumn18FSPremix-00052-fragment.py nevts:%i'%options.maxEvents),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:SUS-RunIIAutumn18FSPremix-00052.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

process.genHTFilter = cms.EDFilter("GenHTFilter",
    genHTcut = cms.double(0.0),
    jetEtaCut = cms.double(5.0),
    jetPtCut = cms.double(30.0),
    src = cms.InputTag("tmpAk4GenJetsNoNu")
)


process.tmpGenParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    excludeResonances = cms.bool(False),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39, 12, 14, 16
    ),
    partonicFinalState = cms.bool(False),
    src = cms.InputTag("tmpGenParticles"),
    tausAsJets = cms.bool(False)
)


process.tmpAk4GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.tmpGenMetTrue = cms.EDProducer("GenMETProducer",
    applyFiducialThresholdForFractions = cms.bool(False),
    globalThreshold = cms.double(0.0),
    onlyFiducialParticles = cms.bool(False),
    src = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    usePt = cms.bool(True)
)

# 
stop_width = 197*10**-3*10**-15/(options.ctau)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    RandomizedParameters = cms.VPSet(cms.PSet(
        ConfigDescription = cms.string('T2tt_dM-10to80_genHT-160_genMET-80_250_230'),
        ConfigWeight = cms.double(1231.0),
        GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-StopStop/v1/SMS-StopStop_mStop-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'%options.mStop),
        PythiaParameters = cms.PSet(
            JetMatchingParameters = cms.vstring(
                'JetMatching:setMad = off', 
                'JetMatching:scheme = 1', 
                'JetMatching:merge = on', 
                'JetMatching:jetAlgorithm = 2', 
                'JetMatching:etaJetMax = 5.', 
                'JetMatching:coneRadius = 1.', 
                'JetMatching:slowJetPower = 1', 
                'JetMatching:qCut = 62', 
                'JetMatching:nQmatch = 5', 
                'JetMatching:nJetMax = 2', 
                'JetMatching:doShowerKt = off', 
                '6:m0 = 172.5', 
                '24:mMin = 0.1', 
                'Check:abortIfVeto = on'
            ),
            parameterSets = cms.vstring(
                'pythia8CommonSettings', 
                'pythia8CP2Settings', 
                'JetMatchingParameters', 
                'processParameters'
            ),
            processParameters = cms.vstring('LesHouches:setLifetime = 2'),
            pythia8CP2Settings = cms.vstring(
                'Tune:pp 14', 
                'Tune:ee 7', 
                'MultipartonInteractions:ecmPow=0.1391', 
                'PDF:pSet=17', 
                'MultipartonInteractions:bProfile=2', 
                'MultipartonInteractions:pT0Ref=2.306', 
                'MultipartonInteractions:coreRadius=0.3755', 
                'MultipartonInteractions:coreFraction=0.3269', 
                'ColourReconnection:range=2.323', 
                'SigmaTotal:zeroAXB=off', 
                'SpaceShower:rapidityOrder=off', 
                'SpaceShower:alphaSvalue=0.13', 
                'TimeShower:alphaSvalue=0.13'
            ),
            pythia8CommonSettings = cms.vstring(
                'Tune:preferLHAPDF = 2', 
                'Main:timesAllowErrors = 10000', 
                'Check:epTolErr = 0.01', 
                'Beams:setProductionScalesFromLHEF = off', 
                'SLHA:keepSM = on', 
                'SLHA:minMassSM = 1000.', 
                'ParticleDecays:limitTau0 = on', 
                'ParticleDecays:tau0Max = 10', 
                'ParticleDecays:allowPhotonRadiation = on'
            )
        ),
        SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     {mStop}          # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.00000000E+05    # ~g\n   1000022     {mneu}           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     {stop_width}   # stop1 decays\n    0.00000000E+00    4    1000022      5     -1    2  # dummy allowed decay, in order to turn on off-shell decays\n    1.00000000E+00    3    1000022      5   24\nDECAY   2000006     0.00000000E+00   # stop2 decays\n\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\nDECAY   1000021     0.00000000E+00   # gluino decays\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n'.format(stop_width=stop_width, mStop = options.mStop, mneu = options.mStop-options.dm))
    )),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.tmpGenParticles = cms.EDProducer("GenParticleProducer",
    abortOnUnknownPDGCode = cms.untracked.bool(False),
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator","unsmeared")
)


process.genMETfilter1 = cms.EDFilter("CandViewSelector",
    cut = cms.string('pt >= 0'),
    src = cms.InputTag("tmpGenMetTrue")
)


process.genMETfilter2 = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("genMETfilter1")
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.tmpGenParticles+process.tmpGenParticlesForJetsNoNu+process.tmpAk4GenJetsNoNu+process.genHTFilter+process.tmpGenMetTrue+process.genMETfilter1+process.genMETfilter2)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion