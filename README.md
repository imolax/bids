# bids
BIDS Formatting

NOTE: this asussmes you have already built the dcm2bids config file for your study. If not, see: https://unfmontreal.github.io/Dcm2Bids/3.2.0/

1. Log in to the BIC portal: download.bic.theroyal.ca
2. Choose the relevant files, then "build" your download (zip the files)
   -In a perfect world, with no do-overs/restarts, you would select all files, but you may want only the 2nd MEMPRAGE and MEMPRAGE RMS as the first one is not filtered and you may have had to repeat a sequence.
3. Download the resulting zip file and extract on your local computer
4. Open your dcm2bids script location in the terminal
5. Activate the bids environment (type bidsgo if on barracuda)
6. Update your dcm2bids script ith relevant participant numbers 
7. Run the dcm2bids script
8. Check your outputs to make sure everything is present and properly labelled
