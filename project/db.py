### crud.py ###

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Date


Base = declarative_base()
database_name = 'compounds.db'
DATABASE_URI = 'sqlite:///' + database_name
engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class Compound(Base):
    __tablename__ = 'compounds'
    id = Column(Integer, primary_key=True)
    compound = Column(String)
    name = Column(String)
    formula = Column(String)
    inchi = Column(String)
    inchi_key = Column(String)
    smiles = Column(String)
    cross_links_count = Column(Integer)

    def __init__(self, compound, name, formula, inchi, inchi_key, smiles, cross_links_count):
        self.compound  = compound
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = cross_links_count
    
    def __repr__(self):
        return "<Compound(compound='{}', name='{}', formula='{}', inchi='{}', " \
               "inchi_key='{}', smiles='{}', л={})>"\
                .format(self.conpound, self.name, self.formula, self.inchi, self.inchi, self.inchi_key, self.smiles, self.cross_links_count)
