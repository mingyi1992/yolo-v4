#---------------------------------------------#
#   运行前一定要修改classes
#   如果生成的2007_train.txt里面没有目标信息
#   那么就是因为classes没有设定正确
#---------------------------------------------#
import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#-----------------------------------------------------#
#   这里设定的classes顺序要和model_data里的txt一样
#-----------------------------------------------------#

classes = ["bean_sprout","dried_tofu","cabbage","Fried_pork_ribs","Fried_chicken_legs","Baby_corn","peanut",\
            "Scrambled_Eggs_with_Carrots","Fried_eggplant","sausage","kelp","mixed_vegetables","orange_tofu",\
            "Green_bean","scrambled_eggs_with_corn","sweet_potato_leaves","Bell_pepper","Cooked_Bunashimeji",\
            "tomato","poached_egg","soy_sauce_braised_egg","anttree","Tomato_scrambled_eggs","Boiled_potatoes",\
            "Chinese_cabbage","green_pepper","fungus","Cucumber_salad","dried_radish","tofu_skin","Bok_Coy",\
            "A-choy","Fried_chicken_chop","fried_tofu","stew_radish","Fried_chicken_nuggets","Boiled_Daikon",\
            "Boiled_cabbage","Boiled_bean_sprouts","Barbecued_pork","bamboo_shoot","Gourd","Boiled_pumpkin",\
            "water_spinach","Sauerkraut","soy_chicken_leg","soy-stewed_pork","Boiled_carrots","Boiled_egg",\
            "Broccoli","chickenbreast","Cooked_purplerice","Poached_chickenbreast","Salmon","steak","Boiled_corn",\
            "Bunashimeji","eringi","Snow_peas","Cooked_tofu","tofu","Roasted_tofu","Boiled_okra","louver","Pork_Loin",\
            "Roasted_chicken_leg","spinach","Brassica_chinensis","Braised_Chicken_Chop","celery","Braised_Pork_Ribs",\
            "cauliflower","Kale","Steamed_egg","Black_beans","black_wood_ear","Minced_meat","Bean_wheel","Kelp_Bud",\
            "fried_tempura","Brassica_napus","fried_ham_with_corn","Stir-fried_Pork_with_Black_Pepper","Scallion_Egg_Fry",\
            "pickled_potherb_mustard","Diced_ham","Vegetable_fried_rolls","Vegetarian_ham","pea","white_gourd"]

def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id), encoding='utf-8')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0 
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()
