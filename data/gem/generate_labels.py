import csv
import json

class_labels = set()
entity_labels = set()

for filename in ['train.tsv', 'test.tsv', 'dev.tsv']:
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t", quotechar=None)
        lines = []
        for line in reader:
            class_labels.add(line[0])

            if line[2]:
                entities = line[2].split('|')

                for e in entities:
                    fields = e.split(':')
                    entity_labels.add(fields[2])

all_labels = []

label_list = list(class_labels)
label_list.sort()

all_labels = all_labels + label_list

with open('class_labels.txt', mode='w', encoding='utf-8') as f:
    f.write('\n'.join(label_list))

label_list = list(entity_labels)
label_list.sort()

with open('entity_labels.txt', mode='w', encoding='utf-8') as f:
    f.write('O' + '\n')
    all_labels.append('O')
    for name in label_list:
        all_labels.append('B_' + name)
        all_labels.append('I_' + name)
        f.write('B_' + name + '\n')
        f.write('I_' + name + '\n')

with open('all_labels.txt', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(all_labels, ensure_ascii=False))