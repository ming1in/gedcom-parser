'''
Created on 10/08/20
@author: Ming Lin
'''

tags = {
    'INDI': 'uid',
    'NAME': 'name',
    'SEX': 'sex',
    'BIRT': 'birth',
    'DEAT': 'death',
    'FAMC': 'isChildToFamId',
    'FAMS': 'isSpouseToFamId',
    'FAM': 'uid',
    'MARR': 'marriage',
    'HUSB': 'husband',
    'WIFE': 'wife',
    'CHIL': 'child',
    'DIV': 'divorce'
}


class Record:
    def __init__(self, level, tag, argument):
        self.level = level
        self.tag = tag
        self.argument = argument


class Family:
    def __init__(self, uid, husband, wife, child, marriage, divorce):
        self.uid = uid
        self.husband = husband
        self.wife = wife
        self.child = child
        self.marriage = marriage
        self.divorce = divorce


class Individual:
    def __init__(self, uid, name, sex, birth, death, isChildToFamId, isSpouseToFamId):
        self.uid = uid
        self.name = name
        self.sex = sex
        self.birth = birth
        self.death = death
        self.isChildToFamId = isChildToFamId
        self.isSpouseToFamId = isSpouseToFamId


class Gedcom:

    def __init__(self, gedcomFile):
        self.gedcomFile = gedcomFile
        self.gedcomArray = []
        self.families = []
        self.individuals = []
        self.createGedcomArray()
        self.parseGedcomArray()

    # method that maps lines within gedcom file into Record objects
    def createGedcomArray(self):
        # open gedcom file
        gedcomFile = open(self.gedcomFile, "r")
        # temp var to hold instance of nested record array
        record = [] 

        for line in gedcomFile:
            # construct line into array and clean up miscellaneous symbols
            recordArray = str(line).replace('\n', '').replace(
                '@', '').replace('/', '').replace('_MARNM', 'MARR').split(' ')

            # check for level 0 line which marks start of new individual or family
            if (recordArray[0] == '0'):
                # check if there was a previous record being built
                if (len(record) > 0):
                    #adds previous record to gedcomArray and reset record for new records
                    self.gedcomArray.append(record)
                    record = []
                
                # check for useless level 0 line
                if (recordArray[1] not in {'HEAD', 'TRLR', 'NOTE'}):
                    #adds individual/family to record, so they can be built up
                    record.append(Record('0', recordArray[2], recordArray[1]))

            # checks for level 1/2 lines and if record is available to be built up, based on
            # precedent that lines after level 0 are properties of that individual/family
            if ((recordArray[0] == '1' or recordArray[0] == '2') and len(record) > 0):
                record.append(
                    Record(recordArray[0], recordArray[1], ' '.join(recordArray[2:])))

    # method that maps Records within gedcomArray to Family/Individual objects
    def parseGedcomArray(self):
        # iterate through nested array of Records
        for records in self.gedcomArray:
            # checks if nested Records is for an individual
            if (records[0].tag == 'INDI'):
                # temp variable to hold properties of a individual
                individual = {
                    'uid': '',
                    'name': '',
                    'sex': '',
                    'birth': '',
                    'death': '',
                    'isChildToFamId': '',
                    'isSpouseToFamId': ''
                }
                # iterate through array of Records for the individual's properties
                for idx, record in enumerate(records):
                    # checks if tag is valid against tags dictionary
                    if (record.tag in tags):
                        # checks if tag is a date type, in that case the argument is in the next Record
                        if (record.tag in {'BIRT', 'DEAT'}):
                            individual[tags[record.tag]] = records[idx + 1].argument
                        else:
                            # store properties of the individual in temp variable individual
                            individual[tags[record.tag]] = record.argument

                # store individual along with properties in the Gedcom object's individuals property
                self.individuals.append(Individual(individual['uid'], individual['name'],
                                                   individual['sex'], individual['birth'],
                                                   individual['death'], individual['isChildToFamId'],
                                                   individual['isSpouseToFamId']))

                self.individuals.sort(key=lambda individual: individual.uid)

            # checks if nested Records is for an family
            if (records[0].tag == 'FAM'):
                # temp variable to hold properties of a family
                family = {
                    'uid': '',
                    'husband': '',
                    'wife': '',
                    'child': [],
                    'marriage': '',
                    'divorce': ''
                }

                # iterate through array of Records for the family's properties
                for idx, record in enumerate(records):
                    # checks if tag is valid against tags dictionary
                    if (record.tag in tags):
                        # checks if tag is a date type, in that case the argument is in the next Record
                        if (record.tag in {'MARR', 'DIV'}):
                            if(records[idx + 1].tag == 'DATE'):
                                family[tags[record.tag]] = records[idx + 1].argument
                        # checks if Record is a child to the family
                        elif (record.tag == 'CHIL'):
                            family['child'].append(record.argument)
                        else:
                            # store properties of the individual in temp variable family
                            family[tags[record.tag]] = record.argument

                # store family along with properties in the Gedcom object's families property
                self.families.append(Family(family['uid'], family['husband'], family['wife'],
                                            family['child'], family['marriage'], family['divorce']))

                self.families.sort(key=lambda family: family.uid)

    # method that prints out every necessary line in the gedcom file
    def printGedcom(self):
        for records in self.gedcomArray:
            print('----------------------------------------------------------------------')
            for record in records:
                print(record.level + ' | ' +
                      record.tag + ' | ' + record.argument)

        return

    # method that prints out every individual in Gedcom
    def printIndividuals(self):
        for individual in self.individuals:
            print('----------------------------------------------------------------------')
            print(individual.uid + ' | ' + individual.name + ' | ' + individual.sex + ' | ' + individual.birth)

        return

    # method that prints out every family in Gedcom and 
    def printFamilies(self):
        for family in self.families:
            print('----------------------------------------------------------------------')
            print(family.uid + ' | ' + family.husband + ' | ' + family.wife + ' | ' + family.marriage)

        return
    def deleteFamily(self, deleteFamily: Family):
        self.families = list(filter(lambda family: family.uid != deleteFamily.uid, self.families))
        
        return        
