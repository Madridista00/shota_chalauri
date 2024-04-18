from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Engine_ის შექმნა
engine = create_engine('mysql+mysqlconnector://shchala:1234@localhost/it_step34_1', echo=True)

Base = declarative_base()

# User კლასის შექმნა
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    profile = relationship("Profile", uselist=False, back_populates="user")

# Profile კლასის შექმნა
class Profile(Base):
    __tablename__ = 'Profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), unique=True, nullable=False)
    bio = Column(Text)
    profile_picture = Column(String(255))
    
    user = relationship("User", back_populates="profile")

# ცხრილების შექმნა
Base.metadata.create_all(engine)

# სესიების შექმნა
Session = sessionmaker(bind=engine)
session = Session()

# მონაცემების შეტანა ცხრილებში
user1 = User(username='IvaneKrtvelishvili', email='Ivane@gmail.com')
user2 = User(username='AnaAkhmeteli', email='Ana@gmail.com')
user3 = User(username='DavitAbuladze', email='Abu@gmail.com')
user4 = User(username='NataDidia', email='Didia_N@gmail.com')
user5 = User(username='PetreKanchaveli', email='Kancha@gmail.com')

profile1 = Profile(user=user1, bio='Software Engineer', profile_picture='Ivane_profile.jpg')
profile2 = Profile(user=user2, bio='Marketing Specialist', profile_picture='Ana_profile.jpg')
profile1 = Profile(user=user3, bio='Footballer', profile_picture='Davit_profile.jpg')
profile2 = Profile(user=user4, bio='CTO', profile_picture='Nata_profile.jpg')
profile2 = Profile(user=user5, bio='Programmer', profile_picture='Petre_profile.jpg')

session.add_all([user1, user2, user3, user4, user5])
session.commit()