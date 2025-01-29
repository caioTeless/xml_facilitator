
cnpj_cpf_condition = lambda x: x == 'CNPJ' or x == 'CPF'

nfe_key = [data.text.strip() for data in root.find('.//infProt') if data.tag == 'chNFe'][0]
nfe_number = [data.text.strip() for data in root.find('.//ide') if data.tag == 'nNF'][0]
cnpj_emit = [data.text.strip() for data in root.find('.//emit') if cnpj_cpf_condition(data.tag)][0]
cnpj_cpf_dest = [data.text.strip() for data in root.find('.//dest') if cnpj_cpf_condition(data.tag)][0]

print(f'CPF ou CNPJ Emitente: {cnpj_emit}')
print(f'CPF ou CNPJ Destinatário: {cnpj_cpf_dest}')
print(f'Número da nota - {nfe_number}')
print(f'Chave da nota - {nfe_key}')

