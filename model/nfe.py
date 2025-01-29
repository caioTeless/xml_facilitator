from base import Base
class NFe(Base):
    def __init__(self, file):
        super().__init__(file)
        self.tags = {
            "nfe_key": ('.//infProt', 'chNFe'),
            "nfe_number": ('.//ide', 'nNF'),
            "nfe_series": ('.//ide', 'serie'),
            "nfe_doc_emit": ('.//emit', ('CNPJ', 'CPF')),
            "nfe_emit_name": ('.//emit', 'xNome'),
            "nfe_doc_dest": ('.//dest', ('CNPJ', 'CPF')),
            "nfe_dest_name": ('.//dest', 'xNome')
        }

    def populate_class(self):
        for key, (parent, tag) in self.tags.items():
            print(self.read_tags(parent, tag))

    
test = NFe('D:\\Downloads\\35241229808206000124550050000759821862814639.xml')

test.populate_class()

#print(test.data['nfe_key'])

#ET.parse('file')