import csv
import codecs

#Relationship Table: https://www.doumori.com/guide/type.html

def main():
    #Parse data
    names = {}
    properties = {}
    prop_pair = {'Lazy': 0, 'Jock': 1, 'Cranky': 2, 'Smug': 3, 'Normal': 4, 'Peppy': 5, 'Snooty': 6, 'Sisterly': 7}
    prop_lookup = [ [2,1,5,2,1,2,2,5],
                    [1,5,2,2,2,5,1,2],
                    [5,2,2,1,2,1,5,2],
                    [2,2,1,5,5,2,2,1],
                    [1,2,2,5,5,1,2,2],
                    [2,5,1,2,1,5,2,2],
                    [2,1,5,2,2,2,5,1],
                    [5,2,2,1,2,2,1,5]]

    cons_pair = {'fire': 0, 'ground': 1, 'wind': 2, 'water': 3}
    cons_lookup = [ [5, 2, 2, 1],
                    [2, 5, 1, 1],
                    [2, 1, 5, 2],
                    [1, 2, 1, 5]]

    with codecs.open('npcname.csv', 'rb', 'utf-8-sig') as csvfile:
        namereader = csv.reader(csvfile)
        for row in namereader:
            names[row[0]] = row[1]
    
    with codecs.open('npcprop.csv', 'rb', 'utf-8-sig') as csvfile:
        propreader = csv.reader(csvfile)
        for row in propreader:
            # 'Agnes': ['Female', 'Sisterly', 'ground']
            properties[row[0]] = [row[2],row[3],constellation(row[4])]  
    
    x = input('Enter villager name:')
    if x in names:
        friends = []
        #my_gend = properties[names[x]][0]
        my_prop = prop_pair[properties[names[x]][1]]
        my_cons = cons_pair[properties[names[x]][2]]

        for k, v in properties.items():
            friend_prop = prop_pair[v[1]]
            friend_cons = cons_pair[v[2]]
            if prop_lookup[my_prop][friend_prop] + cons_lookup[my_cons][friend_cons] == 10 and k != names[x]:
                friends.append(list(names.keys())[list(names.values()).index(k)])
                
        
        print(friends)
            

#极其恶臭
#火：   3/21-4/19，     7/23-8/22，     11/23-12/21
#地：   4/20-5/20，     8/23-9/22，     12/22-1/19
#风：   5/21-6/21，     9/23-10/23，    1/20-2/18
#水：   6/22-7/22，     10/24-11/22，   2/19-3/20
def constellation(date):
    zodiacs = [(119, 'ground'), (218, 'wind'), (320, 'water'), (419, 'fire'), (520, 'ground'),
           (621, 'wind'), (722, 'water'), (822, 'fire'), (922, 'ground'), (1023, 'wind'),
           (1122, 'water'), (1221, 'fire'), (1231, 'ground')]
    month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    datelist = date.split()
    time = month_to_num[datelist[0]] * 100 + int(datelist[1])
    for z in zodiacs:
        if time <= z[0]:
            return z[1]

if __name__ == "__main__":
    main()