import xml.etree.ElementTree as ET

def remove_namespace(xml):
    for elem in xml.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

tree = ET.parse('D:\\Downloads\\35241229808206000124550050000759821862814639.xml')
root = tree.getroot()

remove_namespace(root)

cnpj_cpf_condition = lambda x: x == 'CNPJ' or x == 'CPF'

nfe_key = [data.text.strip() for data in root.find('.//infProt') if data.tag == 'chNFe'][0]
nfe_number = [data.text.strip() for data in root.find('.//ide') if data.tag == 'nNF'][0]
cnpj_emit = [data.text.strip() for data in root.find('.//emit') if cnpj_cpf_condition(data.tag)][0]
cnpj_cpf_dest = [data.text.strip() for data in root.find('.//dest') if cnpj_cpf_condition(data.tag)][0]

print(f'CPF ou CNPJ Emitente: {cnpj_emit}')
print(f'CPF ou CNPJ Destinatário: {cnpj_cpf_dest}')
print(f'Número da nota - {nfe_number}')
print(f'Chave da nota - {nfe_key}')
# for data in emit:
#     cnpj_emit = data.text[0]
#     name_emit = data.text[1]
    
# for data in dest:
#     cnpj_dest = data.text[0]
#     name_dest = data.text[1]


