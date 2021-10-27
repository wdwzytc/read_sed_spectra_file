# read_sed_spectra_file
find and deal with the spectral files (.sed) generated by 'SR-3500 Spectroradiometer/SM-3500 Spectrometer'. Extract reflectance and output as .csv

The code is written in python3.9


# This code is used to deal with the spectral files generated by 'SR-3500 Spectroradiometer/SM-3500 Spectrometer'.
# The spectral file has a suffix of .sed.
#
# To use this code, just give it a root directory, and it will check all the directories contained. If there are .sed
# files in one directory, the code will extract the reflectance data, and generate a .csv file as output in that
# directory.
#
# Because I stored the spectral files of different dates in different folders, I want to deal with them separately in
# each folder. That is why I make a .csv file for each folder.
