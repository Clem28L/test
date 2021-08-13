from FormattedData import FormatData

NewData = [FormatData("Georges", 65, True),
           FormatData("Sophie", 47, False),
           FormatData("Pierre", 52, True)]

FormatData.SaveData("TestFile.csv", NewData)
