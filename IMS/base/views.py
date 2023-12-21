from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import*
from .serializer import*
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token# yesle chai every single user ko token create garxa


# Create your views here.
@api_view(['POST'])# yo chai apiview ho so login gardah feri userle username ra password pathauxa hamile chai email ra password patha xau so email ra password post garxau so pathau dah feri tw post method garxau ni tw post method le matra body ko data pathau xa so post method chai allow garnu paryo api view ko under ma
def login(request):
   email= request.data.get('email') #( email ma k value aako xa tyo nikalo ) user le kasari request pathau xa vani hamro bodyma aauxa  email: ..... ani password=.... json format  pathauxa froned le  ani hamile chai every single key chai lina milxa data ma email key ko value lai lini  get garera
   password= request.data.get('password')#( password ma k value aako xa tyo nikalo )
   user = authenticate(username=email, password=password)# (yesle chai k garxa vani database ma vako jati pni authenticate user xa ni jasko  email ra password match garxa data ma jun chai user le pathako ho teslai chai retuen garxa vetyo vani return garxa ani vetena vani none data  return garxa)hamro django ko kam username bata nai hunxa tei vayera username field ma email rakheko
   if user == None:
      return Response('user not found')# yesko lagi user banau ni
   else:
      token,_=Token.objects.get_or_create(user=user)#token,_ yo chai variable ho jun le chai boolean value linxa ani kin avani token model ko object haru ma get or create quesy  gardae xau get or create query vaneko chai yedi yuser field ma yo token vako already xa va vanitelai get garni xaina vani create garni ani token aayo ani key huxna  ani fronted le linxa 
      return Response(token.key)
   
   # yedi user xa vani login successfull garnu paryo arko kura chai hamile login ko token create  garna lako ki user ho vanera database xa vanera ani yo token liyera chai api ma request gara hai vannu parxa ani tesko lagi chai from rest_framework.authtoken.models import Token jun chai installed app ma xa yo model le chai k garxa vani every single user lai chai token create garxa
   # hamile postman ma post garnu parxa login ko lagi kina vani hamilai body send garnu xa   
class CompanyInfoApiView(GenericAPIView):
    queryset=CompanyInfo.objects.all()# yo queryset kin agareko vani GenericAPIView ko requirement ho yo view ma chai kun queryset hunxa  tei define garni ho
    serializer_class=ComapanyInfoSerializer # yo chai template error naaus ani sreliazer ko class define gareko kun serializer ho vanera
    permission_classes =[IsAuthenticated]#(yesle chai authentication magxa) yini haru tin chai generic api view ko jun paye tei variable hoina yo chai same hunu parxa variable
# sabai object dekhauni get method nai ho but euta single object matra pni dekhaunu get method nai tesko lagi chai hamile fronted bata id magera tyo id bata tyo object lai locate garera hami return garxau ani hamile update ra delete ko lagi pni garxau aba hamile single object get garnu xa ani ya update dete garnu xa hamile id magnu parxa tyo id  same company info url ma magera hudae na kina vani  api vitra id lini view haru hunna  get post le id lidae na tesko lagi hamile xuttai api view banau ni jasle chai id anusar kam garxa
    def get(self, request):# yo vayo all retrip jasle chai id magdae na
        company_info_objects= self.get_queryset()# yesle chai mathi ko queryset lai call gagarxa
        serializer= ComapanyInfoSerializer(company_info_objects, many=True)# yaha chai object lai pass gari raxau so hamile data=request.data garnu pardae na ani many=true kina gareko vani  default ma chai serializer le euta matra object lai json ma lagi ra hunxa but yesma dherae ota object liraxau so many=true
        return Response(serializer.data) # response pathaunu paryo request ko lagi so serializer le multiple data ko list hunxa so tyo data lai chai yaha pathaidini
    
    # get request gardah feri hamile  body ma k he pathaunu pardaena because hamile fronted bata data magi raxau backend le  ani postman ma send garu vani chai  tya body ko preety ma chai response aauxa
    # Post gardah feri chai backend le chai data pathauxa fronted lai jun data create garni ho tyo data pathauni tes paxi body ma gayera raw ma gayera type chai json garera json format ma chai jun data create gareko ho pathauna ko lagi tyo data rakhni key ra value json format ma string ra data ya charfield pathako xa vani double quattaion hunu parxa but integer lai chai quatation ma chai pardae na jati pni model ko table ko field xa teslai chai key ma rakhni field anusar rakhni value ani requred field pathayo vani kam garxa required field pathayena vani error dinxa
     
    def post(self, request): # yesma chai query garnu pardae na kina ki post ma data haru pathauni hoina data liyera save garni ho
        serializer=ComapanyInfoSerializer(data=request.data) # yo chai fronted le json format ma url ma pathako hunxa yo yeslai object ma convert gareko and data=request.data (yo garyo vani cahi serialzer le json lai object data ma lagdinxa )yo chai code ho yesle chai serrializer = data=request.data  yo gari raxau ni yo chai jun data aairaxa pass garxa  request ma aako data vaneko json data ho json data liyera data= vanera pass gari raxau
        if serializer.is_valid():# yo chai company info model  chaivalid xa ki nai vanera check gareko
            serializer.save()# yo chai database ma save hunxa ani data chai create hunxa 
            return Response('Data Created') # valid xa vani true return garxa ani yo response deko
        else:
            return Response(serializer.errors)# serializer.error le chai k error xa vanera dekhauxa
        # jati pni field xa company info ma json format rakhni body ma  double quatation ma ani json ma integer xa vani quatation ma pardae na
        # postman ko body chai yestoh part ho jaha chai request gardah feri data pathauxau so body ma chai data json ko banau xau jun chai request gardah feri jawos vanera ani jati ota url xa teti otai request banau nu parxa postman ma hamile jun method banayo view ma tei method matra run hunxa 
        # Post request gardah feri matra data janxa natra jadaina yesko nature chai yo method le request gardah feri chai user le chai data pathaunu parxa hai vanera yesko nature data create garni tei vayera datacreate gareko
    
# sabai object dekhauni get method nai ho but euta single object matra pni dekhaunu get method nai tesko lagi chai hamile fronted bata id magera tyo id bata tyo object lai locate garera hami return garxau ani hamile update ra delete ko lagi pni garxau aba hamile single object get garnu xa ani ya update delte garnu xa hamile id magnu parxa tyo id  same company info url ma magera hudae na kina vani  api vitra id lini view haru hunna  get post le id lidae na tesko lagi hamile xuttai api view banau ni jasle chai id anusar kam garxa
# single object dekhauna ko lgai single object lai response,delete ,update garnu xa vani arkai api banau ni ani get method use garni
class CompanyInfoIdApiView(GenericAPIView):# generic view ma chai queryset chai define garnai parxa
    queryset=CompanyInfo.objects.all()
    serializer_class=ComapanyInfoSerializer
    permission_classes =[IsAuthenticated]
    
    # hamile company info ma id nachaheni euta view banayem aba id chaheni arko view banau xau fronted bata id magaera kam garni method ko lagi aba view banau xau
    def get(self, request,pk): #fronted lai id mageko#(yo chai single retrip- euta single id le euta single object lai get garni) yesko duita method xa euta all request ko lagi sabai object lai tanni method ani arko euta single id le euta single object lai get garni wali method retrip ma two part hunxa euta all ritrib ani ani arko single ritrip 
        try:
          company_info_objects= CompanyInfo.objects.get(id=pk)# id chai table ko field vayo id chai autogenerated field ho define garnu parrdae na pk ma jun id aaunxa 123etc aba comapny table ko object 1 xa teslai chai get garera lerauxa aba yeslai chai serializer ma pass garnu paryo kina kijson ma convert garnu paryo
        except:
          return Response('Data not found !')
        serializer= ComapanyInfoSerializer(company_info_objects)
        return Response(serializer.data)
    # aba postman ma gayera ip address halera id halni( http://127.0.0.1:8000/company_info/1/)
# aba hamile  yo id bahek aru  id navako rakheu vani error dekhai rahunxa so hamile exception handling garni try ra except   def 
    def put(self, request, pk):#(existing data lai change garnu gho) yesle chai data lai update garxa single object lai update garxa ani yeslai pni id linxa kunchai object lai update garni vanera put method garesi chai user le put request garna milxa
        try:
          company_info_objects= CompanyInfo.objects.get(id=pk)
        except:
          return Response('Data not found !')
        serializer=ComapanyInfoSerializer(company_info_objects,data=request.data)#(request.data vaneko chai user le gareko request ho) aba hamile naya object haru lai update garna lakoxau tesko lagi first tyo object lai pass garnu parxa serializer ma ani data = request.data garera request ma naya data ai raxa teslai pass garnu parxa
        if serializer.is_valid():#check garni object valid xa ki nai j paye tei pathau na mildaena
           serializer.save()# object lai save garni 
           return Response('Data updates successfully')
        else:
           return Response(serializer.errors)
        
    # yo put ko lagi chai hamile data pathaunu paryo response garnu paryo so body ma gayera raw ma gayera json a jani kun value le update garna lako tyo pathauni honi tw sabai required field ma value janu parxa put method gardah feri  data chai field value pathau dah feri field  value chai required field ma passgarnai paryo jun change  gareko tyo pni pass garnai paryo 
    def delete(self,request,pk):
       try:
          company_info_objects= CompanyInfo.objects.get(id=pk)
       except:
          return Response('Data not found !')
       company_info_objects.delete()
       return Response('Data Deleted Successfully')
     # singleretrip update delete ko chai nature same xa fronted bata id magxau tyo id magera tyo id anusar garxau  so hamile mathi ko all object get wala ra post ma milena thapna so arko vview banayem
    # single object ko lagi get method nai banaun ani pk rakhni user le jun object get garna lako hunxa ni sabai object madheye pahila all wala object dekhauxa fronted le   all object madheye euta single object ma click garxa user le tyo object ko barema dekhauxatyo object ko id chai  fronted le pathauxa  fronted le api throgh pathauxa hamile method lai linu paryo ani method ma chai tyo id liyepaxi hamile query  companyinfo object maddhye ma  get query garnu paryo  jun chai single object matra liyera auxa jasle yo id meet garxa ani get garxa 

# Authentication ko part aba yo user based system ho  api based ho aba login ra logout chai fronted le ra backend le token through garxa  login gardah fronted mai interact huni ho client ani usle user name ra password halxa ani hamile tyo username ra password halera hamro data base ma herni data ma username ra password xa ki nai vanera yedi xa vani hamile euta token generate agarera pathauxau fronted lai  ani fronted le chai tyo tpken liyera hamro api ma request garnu parxa  tyo token le hamro user tha pauxa  ani login ko kura tei ho user thapauni ho backend ma kun  user le k gari raxa  vanera track garna ko lagi tyo token liyera every single api ma chai request garxa ani hamro system ko user ho  vanera tha pauxa ani kun user hi vanera tha hunxa
# token ko lagi hamile setting ma gayera rest_framework.authtoken rakhxau installed apps ma  kin rakheko vani token kam garnu pardah migration ko kam garnu parxa tyo migration chai rest_framework ko auth module le herxa kina migration garni yo user ko yo token hunu parxa tyo database mai hunxa tyo migration garba database ma hunxa tyo token ani 
# how to implement token authentication jani ani tya token authentication ko lagi dinxa ani copy garni ani setting ma paste garni
# makemigraions garxau ani migrate garxau tespaxi admin panael ma jana ipaddress ra admin rakhxau login garxau ani tya auth token dekhxau jaha chai user ko token create hunxa ani tei token liyera every single api ma request garxa fronted le
# aba api haru lai pni secure garnu paryo tesko lagi from  rest_framework.authentication import TokenAuthentication rakhni ani from  rest_framework.permissions import IsAuthenticated views ko top ma ani   class  ko serializer_class tala permission_classes =[IsAuthentication] ani authentication chai kasari garxa vani  request garni tw fronted side ho  ani uni haru le token pathau nu parxa token j paye tei hunna aso login ko function banau nu parxa
# from django.contrib.auth import authenticate hamile euta function lai cahi import garnu parxa django ma jun user le email ra password pathako xa ni tyo email ra password backend bata liyera database ma check garnu parxa tyo email ra password vako user ko ho ani tyo check garnu ko lagi hamile  aafai le operation haru garna milxa  but euta kura mildae na database ma hamro password chai encrypted hunxa every single user ko database ma password chai (user ko password vanni kura hamile pni herna mildae na)privacy hotyo encrypted password lai decrypted garera password check garnu paryo kina vani user pathako password tw encrypted password hunna user le pathako password tw real password hunxa tyo user le pathako password ra encrypted password lai check garna ko lagi chai hamilae garo hunxa so hamile authencticate vanni funtion use garera chai 
