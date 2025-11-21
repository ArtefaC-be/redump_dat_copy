from .system import System
from .systemcategory import SystemCategory
from enum import Enum

class RedumpSystem(Enum):
    # BIOS
    MicrosoftXboxBIOS = System(LongName = "Microsoft Xbox (BIOS)", ShortName = "xbox-bios", HasDat = True)
    NintendoGameCubeBIOS = System(LongName = "Nintendo GameCube (BIOS)", ShortName = "gc-bios", HasDat = True)
    SonyPlayStationBIOS = System(LongName = "Sony PlayStation (BIOS)", ShortName = "psx-bios", HasDat = True)
    SonyPlayStation2BIOS = System(LongName = "Sony PlayStation 2 (BIOS)", ShortName = "ps2-bios", HasDat = True)

    AtariJaguarCDInteractiveMultimediaSystem = System(Category = SystemCategory.DiscBasedConsole, LongName = "Atari Jaguar CD Interactive Multimedia System", ShortName = "ajcd", HasCues = True, HasDat = True)
    BandaiPlaydiaQuickInteractiveSystem = System(Category = SystemCategory.DiscBasedConsole, LongName = "Bandai Playdia Quick Interactive System", ShortName = "qis", HasCues = True, HasDat = True)
    BandaiPippin = System(Category = SystemCategory.DiscBasedConsole, LongName = "Bandai Pippin", ShortName = "pippin", HasCues = True, HasDat = True)
    CommodoreAmigaCD32 = System(Category = SystemCategory.DiscBasedConsole, LongName = "Commodore Amiga CD32", ShortName = "cd32", HasCues = True, HasDat = True)
    CommodoreAmigaCDTV = System(Category = SystemCategory.DiscBasedConsole, LongName = "Commodore Amiga CDTV", ShortName = "cdtv", HasCues = True, HasDat = True)
    EnvizionsEVOSmartConsole = System(Category = SystemCategory.DiscBasedConsole, Available = False, LongName = "Envizions EVO Smart Console")


    # IA GEN
    FujitsuFMTownsMarty = System(Category=SystemCategory.DiscBasedConsole, LongName="Fujitsu FM Towns Marty", HasDat=False)
    HasbroiONEducationalGamingSystem = System(Category=SystemCategory.DiscBasedConsole, LongName="Hasbro iON Educational Gaming System", HasDat=False)
    HasbroVideoNow = System(Category=SystemCategory.DiscBasedConsole, LongName="Hasbro VideoNow", ShortName="hvn", IsBanned=True, HasCues=True, HasDat=True)
    HasbroVideoNowColor = System(Category=SystemCategory.DiscBasedConsole, LongName="Hasbro VideoNow Color", ShortName="hvnc", IsBanned=True, HasCues=True, HasDat=True)
    HasbroVideoNowJr = System(Category=SystemCategory.DiscBasedConsole, LongName="Hasbro VideoNow Jr.", ShortName="hvnjr", IsBanned=True, HasCues=True, HasDat=True)
    HasbroVideoNowXP = System(Category=SystemCategory.DiscBasedConsole, LongName="Hasbro VideoNow XP", ShortName="hvnxp", IsBanned=True, HasCues=True, HasDat=True)
    MattelFisherPriceiXL = System(Category=SystemCategory.DiscBasedConsole, LongName="Mattel Fisher-Price iXL", ShortName="ixl", HasCues=True, HasDat=True)
    MattelHyperScan = System(Category=SystemCategory.DiscBasedConsole, LongName="Mattel HyperScan", ShortName="hs", HasCues=True, HasDat=True)
    MemorexVisualInformationSystem = System(Category=SystemCategory.DiscBasedConsole, LongName="Memorex Visual Information System", ShortName="vis", HasCues=True, HasDat=True)
    MicrosoftXbox = System(Category=SystemCategory.DiscBasedConsole, LongName="Microsoft Xbox", ShortName="xbox", HasCues=True, HasDat=True)
    MicrosoftXbox360 = System(Category=SystemCategory.DiscBasedConsole, LongName="Microsoft Xbox 360", ShortName="xbox360", HasCues=True, HasDat=True)
    MicrosoftXboxOne = System(Category=SystemCategory.DiscBasedConsole, LongName="Microsoft Xbox One", ShortName="xboxone", IsBanned=True, HasDat=True)
    MicrosoftXboxSeriesXS = System(Category=SystemCategory.DiscBasedConsole, LongName="Microsoft Xbox Series X", ShortName="xboxsx", IsBanned=True, HasDat=True)
    NECPCEngineCDTurboGrafxCD = System(Category=SystemCategory.DiscBasedConsole, LongName="NEC PC Engine CD & TurboGrafx CD", ShortName="pce", HasCues=True, HasDat=True)
    NECPCFXPCFXGA = System(Category=SystemCategory.DiscBasedConsole, LongName="NEC PC-FX & PC-FXGA", ShortName="pc-fx", HasCues=True, HasDat=True)
    NintendoGameCube = System(Category=SystemCategory.DiscBasedConsole, LongName="Nintendo GameCube", ShortName="gc", HasDat=True)
    NintendoSonySuperNESCDROMSystem = System(Category=SystemCategory.DiscBasedConsole, LongName="Nintendo-Sony Super NES CD-ROM System", HasDat=False)
    NintendoWii = System(Category=SystemCategory.DiscBasedConsole, LongName="Nintendo Wii", ShortName="wii", HasDat=True)
    NintendoWiiU = System(Category=SystemCategory.DiscBasedConsole, LongName="Nintendo Wii U", ShortName="wiiu", IsBanned=True, HasDat=True, HasKeys=True)
    Panasonic3DOInteractiveMultiplayer = System(Category=SystemCategory.DiscBasedConsole, LongName="Panasonic 3DO Interactive Multiplayer", ShortName="3do", HasCues=True, HasDat=True)
    PhilipsCDi = System(Category=SystemCategory.DiscBasedConsole, LongName="Philips CD-i", ShortName="cdi", HasCues=True, HasDat=True)
    PlaymajiPolymega = System(Category=SystemCategory.DiscBasedConsole, LongName="Playmaji Polymega", HasDat=False)
    PioneerLaserActive = System(Category=SystemCategory.DiscBasedConsole, LongName="Pioneer LaserActive", HasDat=False)
    SegaDreamcast = System(Category=SystemCategory.DiscBasedConsole, LongName="Sega Dreamcast", ShortName="dc", HasCues=True, HasDat=True, HasGdi=True)
    SegaMegaCDSegaCD = System(Category=SystemCategory.DiscBasedConsole, LongName="Sega Mega CD & Sega CD", ShortName="mcd", HasCues=True, HasDat=True)
    SegaSaturn = System(Category=SystemCategory.DiscBasedConsole, LongName="Sega Saturn", ShortName="ss", HasCues=True, HasDat=True)
    SNKNeoGeoCD = System(Category=SystemCategory.DiscBasedConsole, LongName="Neo Geo CD", ShortName="ngcd", HasCues=True, HasDat=True)
    SonyPlayStation = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation", ShortName="psx", HasCues=True, HasDat=True, HasLsd=True, HasSbi=True)
    SonyPlayStation2 = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation 2", ShortName="ps2", HasCues=True, HasDat=True)
    SonyPlayStation3 = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation 3", ShortName="ps3", HasCues=True, HasDat=True, HasDkeys=True, HasKeys=True)
    SonyPlayStation4 = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation 4", ShortName="ps4", IsBanned=True, HasDat=True)
    SonyPlayStation5 = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation 5", ShortName="ps5", IsBanned=True, HasDat=True)
    SonyPlayStationPortable = System(Category=SystemCategory.DiscBasedConsole, LongName="Sony PlayStation Portable", ShortName="psp", HasDat=True)
    VMLabsNUON = System(Category=SystemCategory.DiscBasedConsole, LongName="VM Labs NUON", ShortName="nuon", HasDat=True)
    VTechVFlashVSmilePro = System(Category=SystemCategory.DiscBasedConsole, LongName="VTech V.Flash & V.Smile Pro", ShortName="vflash", HasCues=True, HasDat=True)
    ZAPiTGamesGameWaveFamilyEntertainmentSystem = System(Category=SystemCategory.DiscBasedConsole, LongName="ZAPiT Games Game Wave Family Entertainment System", ShortName="gamewave", HasDat=True)


