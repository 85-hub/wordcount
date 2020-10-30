'''
get the stop-word-list
'''



with open("stop-word-list.txt","r") as f:
    data = f.readlines()
    print(data)

res = ""
lis = []
a = ['a\n', 'about\n', 'above\n', 'across\n', 'after\n', 'afterwards\n', 'again\n', 'against\n', 'all\n', 'almost\n', 'alone\n', 'along\n', 'already\n', 'also\n', 'although\n', 'always\n', 'am\n', 'among\n', 'amongst\n', 'amoungst\n', 'amount\n', 'an\n', 'and\n', 'another\n', 'any\n', 'anyhow\n', 'anyone\n', 'anything\n', 'anyway\n', 'anywhere\n', 'are\n', 'around\n', 'as\n', 'at\n', 'back\n', 'be\n', 'became\n', 'because\n', 'become\n', 'becomes\n', 'becoming\n', 'been\n', 'before\n', 'beforehand\n', 'behind\n', 'being\n', 'below\n', 'beside\n', 'besides\n', 'between\n', 'beyond\n', 'bill\n', 'both\n', 'bottom\n', 'but\n', 'by\n', 'call\n', 'can\n', 'cannot\n', 'cant\n', 'co\n', 'computer\n', 'con\n', 'could\n', 'couldnt\n', 'cry\n', 'de\n', 'describe\n', 'detail\n', 'do\n', 'done\n', 'down\n', 'due\n', 'during\n', 'each\n', 'eg\n', 'eight\n', 'either\n', 'eleven\n', 'else\n', 'elsewhere\n', 'empty\n', 'enough\n', 'etc\n', 'even\n', 'ever\n', 'every\n', 'everyone\n', 'everything\n', 'everywhere\n', 'except\n', 'few\n', 'fifteen\n', 'fify\n', 'fill\n', 'find\n', 'fire\n', 'first\n', 'five\n', 'for\n', 'former\n', 'formerly\n', 'forty\n', 'found\n', 'four\n', 'from\n', 'front\n', 'full\n', 'further\n', 'get\n', 'give\n', 'go\n', 'had\n', 'has\n', 'hasnt\n', 'have\n', 'he\n', 'hence\n', 'her\n', 'here\n', 'hereafter\n', 'hereby\n', 'herein\n', 'hereupon\n', 'hers\n', 'herse"\n', 'him\n', 'himse"\n', 'his\n', 'how\n', 'however\n', 'hundred\n', 'i\n', 'ie\n', 'if\n', 'in\n', 'inc\n', 'indeed\n', 'interest\n', 'into\n', 'is\n', 'it\n', 'its\n', 'itse"\n', 'keep\n', 'last\n', 'latter\n', 'latterly\n', 'least\n', 'less\n', 'ltd\n', 'made\n', 'many\n', 'may\n', 'me\n', 'meanwhile\n', 'might\n', 'mill\n', 'mine\n', 'more\n', 'moreover\n', 'most\n', 'mostly\n', 'move\n', 'much\n', 'must\n', 'my\n', 'myse"\n', 'name\n', 'namely\n', 'neither\n', 'never\n', 'nevertheless\n', 'next\n', 'nine\n', 'no\n', 'nobody\n', 'none\n', 'noone\n', 'nor\n', 'not\n', 'nothing\n', 'now\n', 'nowhere\n', 'of\n', 'off\n', 'often\n', 'on\n', 'once\n', 'one\n', 'only\n', 'onto\n', 'or\n', 'other\n', 'others\n', 'otherwise\n', 'our\n', 'ours\n', 'ourselves\n', 'out\n', 'over\n', 'own\n', 'part\n', 'per\n', 'perhaps\n', 'please\n', 'put\n', 'rather\n', 're\n', 'same\n', 'see\n', 'seem\n', 'seemed\n', 'seeming\n', 'seems\n', 'serious\n', 'several\n', 'she\n', 'should\n', 'show\n', 'side\n', 'since\n', 'sincere\n', 'six\n', 'sixty\n', 'so\n', 'some\n', 'somehow\n', 'someone\n', 'something\n', 'sometime\n', 'sometimes\n', 'somewhere\n', 'still\n', 'such\n', 'system\n', 'take\n', 'ten\n', 'than\n', 'that\n', 'the\n', 'their\n', 'them\n', 'themselves\n', 'then\n', 'thence\n', 'there\n', 'thereafter\n', 'thereby\n', 'therefore\n', 'therein\n', 'thereupon\n', 'these\n', 'they\n', 'thick\n', 'thin\n', 'third\n', 'this\n', 'those\n', 'though\n', 'three\n', 'through\n', 'throughout\n', 'thru\n', 'thus\n', 'to\n', 'together\n', 'too\n', 'top\n', 'toward\n', 'towards\n', 'twelve\n', 'twenty\n', 'two\n', 'un\n', 'under\n', 'until\n', 'up\n', 'upon\n', 'us\n', 'very\n', 'via\n', 'was\n', 'we\n', 'well\n', 'were\n', 'what\n', 'whatever\n', 'when\n', 'whence\n', 'whenever\n', 'where\n', 'whereafter\n', 'whereas\n', 'whereby\n', 'wherein\n', 'whereupon\n', 'wherever\n', 'whether\n', 'which\n', 'while\n', 'whither\n', 'who\n', 'whoever\n', 'whole\n', 'whom\n', 'whose\n', 'why\n', 'will\n', 'with\n', 'within\n', 'without\n', 'would\n', 'yet\n', 'you\n', 'your\n', 'yours\n', 'yourself\n', 'yourselves']
for i in range(len(a)):
    # print(a[i][:-1])
    res+=a[i][:-1]
    lis.append(a[i][:-1]+" ")

print(lis)





