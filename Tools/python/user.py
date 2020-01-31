import os

if os.environ['USER'] in ['phussain']:
    cache_directory                     = "/afs/hephy.at/data/cms05/StopsCompressed/"
    results_directory                   = "/afs/hephy.at/data/cms05/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms05/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/p/phussain/www/stopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
    
if os.environ['USER'] in ['prhussai']:
    results_directory                   = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed"
    postProcessing_output_directory     = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed/nanoTuples/"
    plot_directory                      = "/eos/user/p/prhussai/www/"
    private_results_directory           = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed/results"

if os.environ['USER'] in ['rschoefbeck']:
    results_directory                   = "/afs/hephy.at/data/cms02/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms02/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/r/rschoefbeck/www/StopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
