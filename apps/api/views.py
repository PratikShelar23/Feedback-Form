from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from apps.utils import *
import os, sys

#--------------------------FEEDBACK MASTER-------------------POST AND GET------------------------
# Create your views here.
#POST operation
class FeedbackCRUD(APIView):
    def post(self, request):
        try:
            request_data = request.data
            clientname = request_data['clientname'] #notnull
            clientcompanyname = request_data['clientcompanyname'] #notnull
            address = request_data.get('address', None)
            personemail = request_data['personemail'] #notnull
            phoneno = request_data['phoneno'] #notnull
            agentrecno = request_data['agentrecno' ] #notnull
            date = getToday() # UN-UNSIGNED not goes in negative
            time = getlocaltime() # UN-UNSIGNED not goes in negative
            interested = request_data.get('interested',None)
            rating = request_data.get('rating',None)
            remark = request_data.get('remark',None)
            productsrecno = request_data['productsrecno'] #notnull
            nextmeetingdate = request_data.get('nextmeetingdate',None)
            suggestions = request_data.get('suggestions',None)
            latitude = request_data.get('latitude',None)
            longitude = request_data.get('longitude',None)

            # //insert query
            add = '''
                INSERT INTO feedbackmaster (
                    clientname, clientcompanyname, address, personemail, phoneno, agentrecno, date, time,
                    interested, rating, remark, productsrecno, nextmeetingdate, suggestions,
                    latitude, longitude
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                
            '''

            with connection.cursor() as c:
                    c.execute(add, [clientname,clientcompanyname,address,personemail,phoneno,agentrecno,date,time,interested,rating,remark,productsrecno,nextmeetingdate,suggestions,latitude, longitude])

            #select query
            # get = 'SELECT * FROM feedbackmaster ORDER BY recno DESC LIMIT 1'
            # with connection.cursor() as c:
            #         c.execute(get)
            #         row = dictfetchall(c)
            return Response({'Success' : True, 'Message' : "Data ADDED SUCCESSFULLY"}, status=200)      

            #exception
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)
        

#GET operation
class getFeedback(APIView):
    def post(self, request):
        try:
            
            query = '''
                SELECT *, (select name from agentmaster where recno=agentrecno)as agent, (select name from productmaster where recno=productsrecno)as product FROM feedbackmaster;
            '''
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = dictfetchall(cursor)

            return Response({'Success': True, 'Message': row}, status=200)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)

#-------------------------------------------------------------------------------------


# ------------------------------------ AGENT NAMES ----------------------------------------------------------------------------
class AgentMasterList(APIView):
    def post(self, request):
        try:
            request_data = request.data
            name = request_data['name']
            active = request_data.get('active', None)
            designation = request_data.get('designation', None)

            
            checkDuplicateQuery = ' SELECT recno, name FROM agentmaster WHERE name=%s'
            checkDuplicateValues = [name]
            
            with connection.cursor() as c:
                c.execute(checkDuplicateQuery, checkDuplicateValues)
                duplicateEntry = dictfetchall(c)
                
                if len(duplicateEntry) > 0:
                    raise Exception('Agent with the same name already exists')

           
            with connection.cursor() as c:
                addQuery = ' INSERT INTO agentmaster (name, active, designation) VALUES (%s, %s, %s) '
                c.execute(addQuery, [name, active, designation])

            return Response({'Success': True, 'Message': "Added Successfully"}, status=200)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)

        
class GetAgentMasterList(APIView):
    def post(self, request):
        try:
            query = 'SELECT * FROM agentmaster ORDER BY recno DESC'

            with connection.cursor() as c:
                c.execute(query)
                row = dictfetchall(c)

            return Response({'Success': True, 'Message': row}, status=200)
        

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)
        
# ------------------------------------ PRODUCT NAMES ----------------------------------------------------------------------------

class ProductMasterList(APIView):
    def post(self, request):
        try:
            request_data = request.data
            name = request_data['name']
            active = request_data.get('active', None)

            checkDuplicateQuery = ' SELECT recno, name FROM productmaster WHERE name=%s'
            checkDuplicateValues = [name]
            
            with connection.cursor() as c:
                c.execute(checkDuplicateQuery, checkDuplicateValues)
                duplicateEntry = dictfetchall(c)
                
                if len(duplicateEntry) > 0:
                    raise Exception('Product with the same name already exists')
            
            with connection.cursor() as c:
                add = 'INSERT INTO productmaster (name, active) VALUES ( %s, %s)'
                c.execute(add, [name,active])

            return Response({'Success': True, 'Message': "Added Successfully"}, status=200)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)
        
        
class GetProductMasterList(APIView):
    def post(self, request):
        try:
            query = 'SELECT * FROM productmaster ORDER BY recno DESC'

            with connection.cursor() as c:
                c.execute(query)
                row = dictfetchall(c)

            return Response({'Success': True, 'Message': row}, status=200)
        

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=400)



