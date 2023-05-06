import pandas as pd
from members.models import (
    Company,
    Profession,
    FieldPosition,
    Club,
    Player,
    MemberList,
    Expertise,
    Foot,
)

EXCEL_PATH = "members/members.xlsx"

def runMember():
    xlCompany = pd.read_excel(EXCEL_PATH, "Company")
    xlFieldPosition = pd.read_excel(EXCEL_PATH, "Fieldposition")
    xlExpertise = pd.read_excel(EXCEL_PATH, "Expertise")
    xlMemberlist = pd.read_excel(EXCEL_PATH, "Memberlist")
    xlProfession = pd.read_excel(EXCEL_PATH, "Profession")
    xlProfessionalClubNames = pd.read_excel(EXCEL_PATH, "ProfessionalClubNames")
    xlProfessionalPlayerNames = pd.read_excel(EXCEL_PATH, "ProfessionalPlayerNames")
    xlFoot = pd.read_excel(EXCEL_PATH, "Foot")

    listCompany = xlCompany.iloc[:, 0].tolist()
    listFoot = xlFoot.iloc[:, 0].tolist()
    listExpertise = xlExpertise.iloc[:, 0].tolist()
    listProfession = xlProfession.iloc[:, 0].tolist()
    listFieldPosition = xlFieldPosition.iloc[:, 0].tolist()
    listProfessionalClubNames = xlProfessionalClubNames.iloc[:, 0].tolist()
    listProfessionalPlayerNames = xlProfessionalPlayerNames.iloc[:, 0].tolist()

    for itemCompany in listCompany:
        objCompany, status = Company.objects.get_or_create(name=itemCompany)

    for itemFoot in listFoot:
        objFoot, status = Foot.objects.get_or_create(name=itemFoot)

    for itemExpertise in listExpertise:
        objExpertise, status = Expertise.objects.get_or_create(name=itemExpertise)

    for itemProfession in listProfession:
        objProfession, status = Profession.objects.get_or_create(name=itemProfession)

    for itemExpertise in listExpertise:
        objExpertise, status = Expertise.objects.get_or_create(name=itemExpertise)

    for itemFieldPosition in listFieldPosition:
        objFieldPosition, status = FieldPosition.objects.get_or_create(
            name=itemFieldPosition
        )

    for itemClub in listProfessionalClubNames:
        objClub, status = Club.objects.get_or_create(name=itemClub)

    for itemPlayer in listProfessionalPlayerNames:
        objPlayer, status = Player.objects.get_or_create(name=itemPlayer)

    xlMemberlist["phone"] = xlMemberlist["phone"].astype("str")
    xlMemberlist["phone"] = xlMemberlist["phone"].map(lambda phone: f"+{phone}")

    for number in range(len(xlMemberlist)):
        (
            name,
            image,
            preferred_foot,
            phone,
            pune_address,
            kolhapur_address,
            birthdate,
            area_of_expertise,
            preferred_field_position,
            secondary_field_position,
            profession,
            current_company,
            favorite_club,
            favorite_player,
        ) = xlMemberlist.loc[number].tolist()

        objCompany, status = Company.objects.get_or_create(name=current_company)
        objFoot, status = Foot.objects.get_or_create(name=preferred_foot)
        objProfession, status = Profession.objects.get_or_create(name=profession)
        objExpertise, status = Expertise.objects.get_or_create(name=area_of_expertise)
        objPrimaryFieldPosition, status = FieldPosition.objects.get_or_create(
            name=preferred_field_position
        )
        objSecondaryFieldPosition, status = FieldPosition.objects.get_or_create(
            name=secondary_field_position
        )
        objClub, status = Club.objects.get_or_create(name=favorite_club)
        objPlayer, status = Player.objects.get_or_create(name=favorite_player)

        objMember, status = MemberList.objects.get_or_create(
            name=name,
            image=image,
            preferred_foot=objFoot,
            phone=phone,
            pune_address=pune_address,
            kolhapur_address=kolhapur_address,
            birthdate=birthdate,
            area_of_expertise=objExpertise,
            preferred_field_position=objPrimaryFieldPosition,
            secondary_field_position=objSecondaryFieldPosition,
            profession=objProfession,
            current_company=objCompany,
            favorite_club=objClub,
            favorite_player=objPlayer,
        )