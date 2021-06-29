OutputFile = open("DatasetMerged.csv", "w")
OutputFile.write("Date,Time,Latitude,Longitude,Depth,Magnitude\n")

File2MergeTitle = "Data2Merge"
for i in range(3):
    File2Merge = open(File2MergeTitle+str(i+1)+".csv", encoding="utf-8")
    for Line in File2Merge:
        Segments = Line.split(',')
        DateTime = Segments[0].split('T')
        print(DateTime[0] + "," + DateTime[-1].split('.')[0] + "," + str(Segments[1]) + "," + str(Segments[2]) + "," + str(Segments[3]) + "," + str(Segments[4]))
        OutputFile.write(DateTime[0] + "," + DateTime[-1].split('.')[0] + "," + str(Segments[1]) + "," + str(Segments[2]) + "," + str(Segments[3]) + "," + str(Segments[4]) + "\n")

print("DONE")
