from django.shortcuts import render
import csv

# Create your views here. Outline of functions we will need are listed below


def start_page(request):
    return render(request, 'index.html')

def list_cities_countries(request): #Anushka
    arr = []
    with open("../CityCountries.csv") as the_file:
        csv_read = csv.reader(the_file, delimiter,',')
        for row in csv_read:
            arr.append(row[0], ", ", row[1])
    return arr

def list_industries(request): #Kyra
    industry_arr = []
    # print("industries test")
    with open("../Industries.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                # print(row[0])
                industry_arr.append(row[0])
            line_count += 1
    #Gets the list of all industries

def investor_signup(request): #Nitya
    
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"

    data = json.loads(request.body)
    infos = data
    if request.method == "POST":
        if objective == "Sign Up":
            list_display = ('id', 'name', 'email', 'password', 'keycodes', 'blurb', 'companies', 'social_media', 'profile_photo')

            
            name, email, password, keycodes, blurb, companies, social_media, profile_photos = infos["name"], infos["email"], infos["password"], infos["second_password"], infos["keycodes"], infos["blurb"], infos["companies"], infos["social_media"], infos["profile_photo"]
            try:
                investor = Investor.objects.get(email=email)
                responses["message"] = False
                return JsonResponse(responses, status=404)
            except Exception as e:
                print(e)
                serializer = InvestorSerializer(data=infos) #If not, make a new investor
                if serializer.is_valid():
                    serializer.save()
                    responses['message'] = True
                    return JsonResponse(responses, status=404, safe=False) #Makes user if no object exists
                responses['message'] = False
                return JsonResponse(responses, status=404)
    return render(request, 'index.html') #Add context

    #return render(request, 'investor_signup.html')
    #Creates a new investor model based on information in request
    #Encode password before storing into database
    
    
def company_signup(request):

    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"

    infos = json.loads(request.body)
    if request.method == "POST":
        if objective == "Sign Up":
            name, company_blurb, email, password, second_password, industry, investors, business_model, social_media, tag, timeline, external, logo = infos["name"], infos["company_blurb"], infos["email"], infos["password"], infos["second_password"], infos["industry"], infos["investors"], infos["business_model"], infos["social_media"], infos["tag"], infos["timeline"], infos["external"], infos["logo"]
            try:
                company = Company.objects.get(email=email) 
                responses["message"] = False
                return JsonResponse(responses, status=404)
                
                for key, value in infos.items():
                    setattr(user, key, value)
                    user.save()
                # other_user = User.objects.get(username=username, email=email, password=password, second_password=second_password)
                # information = UserSerializer(instance=other_user).data
                # print(information)
                
                responses["user"] = json.dumps(information)
                print(responses["user"])
                responses["message"] = True
                return JsonResponse(responses, status=201)
            except Exception as e:
                print(e)
                serializer = UserSerializer(data=infos)
                if serializer.is_valid():
                    serializer.save()
                    responses['message'] = False
                    return JsonResponse(responses, status=404, safe=False) #Prevents user from signing up with current email and password
                responses['message'] = False
                return JsonResponse(responses, status=404)
    return render(request, 'company_dashboard.html')
    #Renders page for company sign up as well as completes company sign up

# kyra
def investor_portfolio(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"
    
    infos = json.loads(request.body)
    investor_id = infos["investor_id"]
    
    investor = Investor.objects.get(id = investor_id)
    information = InvestorSerializer(instance=investor).data
    responses["investor"] = json.dumps(information)
    return JsonResponse(responses, status=404)
    #return render(request, 'investor_dashboard.html')
    #Render page for investor portfolio


def company_portfolio(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"
    
    infos = json.loads(request.body)
    company_id = infos["company_id"]
    
    company = Company.objects.get(id = company_id)
    information = CompanySerializer(instance = company).data
    responses["company"] = json.dumps(information)
    return JsonResponse(responses, status=404)
    
    # return render(request, 'company_dashboard.html')
    #Renders page for company portfolio and gets company portfolio

def member_login(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
  ses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"

    infos = json.loads(request.body)
    email, password = infos["email"], infos["password"]
    try:
        company = Company.objects.get(email=email, password=password)
        new_company = CompanySerializer(instance=company).data
        responses['message'] = True
        responses['company_info'] = json.dumps(new_company)
        return JsonResponse(responses, status=201)
    except Exception as e:
        try:
            investor = Investor.objects.get(email = email, password = password)
            new_investor = InvestorSerializer(instance=investor).data
            responses['message'] = True
            responses['investor_info'] = json.dumps(new_investor)
            return JsonResponse(responses, status=201)
        except:
            print(e)
            responses['message'] = False
            return JsonResponse(responses, status=404)
            
    return render(request, 'member_login')  #Renders page for company login and completes company login



def get_investors(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"
    #No filters
    infos = json.loads(request.body)
    filter_option = infos["filter_option"]
    if filter_option == False:
        investors = Investor.objects.get()
        for investor in investors:
            new_investor = InvestorSerializer(instance=investor).data
            responses["investor" + investor.id] = new_investor
        return JsonResponse(responses, status=201)
    else: #Filters
        keycodes = request["keycodes"] #Keycodes selected by user
        investors = Investor.objects.get()

        score_dict = {}
        for investor in investors:
            score = 0.0
            for keyword in keywords:
                if(keyword == investor.keycodes):
                    len_keycodes = len(investor.keycodes)
                    score += 1
            score[investor.id] = socre/len_keycodes
        
        #Sort score dictionary
        #Return top in array
        #Iterate through investors and find keycodes
        
        
    return render(request, 'investor_marketplace.html')
    #Retrieves all investors that are currently in the database

def get_companies(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"
    
    infos = json.loads(request.body)
    filter_option = infos["filter_option"]
    companies = Company.objects.get()
    if filter_option == False:
        for company in companies:
            new_company = CompanySerializer(instance = company).data
            responses["company" + company.id] = new_company
        return JsonResponse(responses, status = 201)
    else:
        keywords = infos["keycodes"] #next important
        business_model = infos["business_model"] #least important
        industry = infos["industry"] #most important
        for company in companies:
            score = 0.0
            if industry != null:
                if industry == company.industry:
                    score+=1.5
            if keywords != null:
                total_keywords = len(company.keycodes)
                compatible_keywords = 0
                for keyword in company.keycodes:
                    #increase compatible_keywords by 1 if keywords contains this.
                score+=(compatible_keywords/total_keywords)
            if business_model != null:
                total_models = len(company.business_model)
                matched_models = 0
                for biz_model in company.business_model:
                    #increase matched_models by 1 if business_model contains this
                score+=((0.5)*(matched_models/total_models))
                
        companies = Company.objects.filter(keycode )
    
    return render(request, 'company_marketplace.html')


def company_rankings(request):
    return render(request, 'company_rankings.html')
    #Retrieves all companies that are currently in the database
    #Completes PCA/Clustering for types of companies that the investors like based on skips and likes

def about_us(request):
    return render(request, 'about_us.html')


def compare_companies(request):
    responses = {}
    responses['Access-Control-Allow-Origin'] = "*"
    responses['Access-Control-Request-Methods'] = "GET, PUT, POST, OPTIONS, DELETE"
    infos = json.loads(request.body)

    first_id = infos['company1']
    second_id = infos['company2'] 
    company1 = Company.objects.get(id = first_id)
    company2 = Company.objects.get(id = second_id)
    
    revenue_approximation = company1.revenue_approximation
    keycode = company1.keycode #Compair
    business_model = company1.business_model
    investor = company1.investor


    #Revenue Approximation 
    #Keycodes
    #Business Model
    #Number of investors --> Get this through accessing each company model and getting the investors they have and counting them
    
    return render(request, 'company_compare.html') 
    #Conducts comparison between similarities/differences of companies and ranks numerically

def search_companies(request):

    #Searches through list of companies to find those with similar characteristics as current company
    #Get current company from request
    
    response = {}
    

