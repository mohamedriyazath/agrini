import random,string
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response,render
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import and_

from ..models import MyModel
from ..models import pwdgen,complaint
from pyramid.session import SignedCookieSessionFactory


@view_config(route_name='fpwd',renderer='../templates/FPWD.jinja2')
def random_pwd(request):
    try:

        def rand_pass(size):
            generate_pass = ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits)for n in range(size)])

            return generate_pass

        pwd = rand_pass(6)
        print("errorcheck")
        if request.POST.get('button1'):
           fl_id= request.params['flat_id']
           print('fl_id',fl_id)
           obj=pwdgen()
           obj.flat_id=fl_id
           obj.pwd=pwd
           obj.email_id='NA'
           request.dbsession.add(obj)
           return()
        else:
             return()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)




@view_config(route_name='signin', renderer='../templates/signup.jinja2')
def update_signin(request):
    try:
        if request.POST.get('signup'):
            print("check")
            fl_id= request.params['flat_id']
            print('fl_id',fl_id)
            em_id= request.params['email_id']
            print('email_id',em_id)
            upwd= request.params['upwd']
            print('upwd',upwd)
            obj=pwdgen()
            print("before_query")
            result=request.dbsession.query(pwdgen).filter(pwdgen.flat_id==fl_id)
            for row in result:
                print(row.pwd)
                row.pwd=upwd
                row.email_id=em_id

            #session.query(User).filter(User.id==3).update({'name': 'user'})
            #request.dbsession.query(pwdgen).filter(and_(=u_id,obj.flat_id==fl_id)).update({obj.email_id:em_id,obj.pwd:upwd})
            print("After_query")
            #getname=request.dbsession.query(login_models)
            #name=getname.name
            #pasword=getname.password
            #Sreturn Response('saved')
            #return render_to_response('../templates/login.jinja2',{}, request=request)
            return()
        else:
            return()


    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)











@view_config(route_name='complaint',renderer='../templates/raisecomplaints.jinja2')
def complaint_issue(request):
    try:


        if request.POST.get('button1'):
            fl_id= request.params['flat_id']
            print('fl_id',fl_id)
            title= request.params['title']
            print('title',title)
            dept= request.params['department']
            print('dept',dept)
            issue= request.params['issue']
            print('issue',issue)
            obj=complaint()
            obj.flat_id=fl_id
            obj.title=title
            obj.department=dept
            obj.issue=issue
            obj.allocate_by='NA'
            obj.complaint_status='NA'
            obj.replay='NA'
            request.dbsession.add(obj)
            print("entry_sucessfully")
            return()

        else:
            print("enery_failed")
            return()

        #getname=request.dbsession.query(login_models)
        #name=getname.name
        #pasword=getname.password
        #Sreturn Response('saved')


    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)


'''def login(request):
    try:
        if request.POST.get('button1'):
            fl_id= request.params['flat_id']
            print('fl_id',fl_id)
            pas= request.params['password']
            print('pas',pas)
            result=request.dbsession.query(pwdgen).filter(and_(pwdgen.pwd==pas,pwdgen.flat_id==fl_id))
            for row in result:
                print(row.pwd)
                print("login s")
            #return Response('login_sucessfull.............')
            if result=={}:
                return()
            else:
                return render_to_response('../templates/complaint.jinja2',{'foo':1, 'bar':2},request=request)
            #print('result.pwd',result.pwd)
            #print("login_sucessfull")
            #return Response('login_sucessfull.............')
        else:
            #return Response('login_failed.............please enter valied ')
            return()


    except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)'''


@view_config(route_name='alloc', renderer='../templates/alloc.jinja2')
def alloc(request):
    try:
        if request.POST.get('admin'):
            print("check")
            fl_id= request.params['flat_id']
            print('fl_id',fl_id)
            alloc= request.params['aloc_by']
            print('alloc',alloc)
            state= request.params['status']
            print('state',state)
            areplay= request.params['replay']
            print('areplay',areplay)
            #obj=complaint()
            print("before_query")
            result=request.dbsession.query(complaint).filter(complaint.flat_id==fl_id)
            for row in result:
                print(row.complaint_status)
                row.complaint_status=state
                row.allocate_by=alloc
                row.replay=areplay

            #session.query(User).filter(User.id==3).update({'name': 'user'})
            #request.dbsession.query(pwdgen).filter(and_(=u_id,obj.flat_id==fl_id)).update({obj.email_id:em_id,obj.pwd:upwd})
            print("After_query")
            #getname=request.dbsession.query(login_models)
            #name=getname.name
            #pasword=getname.password
            #Sreturn Response('saved')
            #return render_to_response('../templates/login.jinja2',{}, request=request)
            return()
        else:
            return()


    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

@view_config(route_name='fpass', renderer='../templates/forgotpass.jinja2')
def admin(request):
    try:
        if request.POST.get('button1'):
            print("check")
            fl_id= request.params['flat_id']
            print('fl_id',fl_id)
            em_id= request.params['email_id']
            print('em_id',em_id)
            upwd= request.params['upwd']
            print('upwd',upwd)
            #obj=complaint()
            print("before_query")
            result=request.dbsession.query(pwdgen).filter(and_(pwdgen.flat_id==fl_id,pwdgen.email_id==em_id))
            for row in result:
                print(row.pwd)
                #row.complaint_status=state
                row.pwd=upwd

            #session.query(User).filter(User.id==3).update({'name': 'user'})
            #request.dbsession.query(pwdgen).filter(and_(=u_id,obj.flat_id==fl_id)).update({obj.email_id:em_id,obj.pwd:upwd})
            print("After_query")
            #getname=request.dbsession.query(login_models)
            #name=getname.name
            #pasword=getname.password
            #Sreturn Response('saved')
            #return render_to_response('../templates/login.jinja2',{}, request=request)
            return()
        else:
            return()


    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)




@view_config(route_name='status', renderer='../templates/issue status.jinja2')
def issue_record(request):
    details=[]
    try:
        query = request.dbsession.query(complaint).all()
        for row in query:
            det=[]
            det.append(row.id)
            det.append(row.time_created)
            det.append(row.allocate_by)
            det.append(row.title)
            det.append(row.flat_id)
            det.append(row.issue)
            det.append(row.department)
            det.append(row.complaint_status)
            det.append(row.time_updated)
            det.append(row.replay)
            details.append(det)

            row.flat_id


    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'project': details}

@view_config(route_name='login',renderer='../templates/login.jinja2')
def login(request):
      if request.POST.get('button1'):
        login = request.dbsession.query(pwdgen)
        x = request.params['flat_id']
        z = request.params['password']
        for n in login:
            if n.flat_id == x and n.pwd == z :
               #session = request.session
               #session['user'] = x
               return Response(render('../templates/complaint.jinja2',{'user':n.flat_id},request=request))
        '''for n in prof:
            if n.email == x and n.password == z:
               session = request.session
               session['user'] = x
               return Response(render('../templates/professor-chapters.jinja2',{'user':n.username},request=request))
        for n in admin:
            if n.username == x and n.schoolname == y and n.password == z:
               session = request.session
               session['user'] = x
               return Response(render('../templates/admin-link.jinja2',{},request=request))'''
        return Response(render('../templates/login.jinja2',{'error':'Username or password is incorrect !'},request=request))
      else:
        return {}
@view_config(route_name='adminlogin',renderer='../templates/adlogin.jinja2')
def adlogin(request):
    if request.POST.get('button1'):

        x = request.params['username']
        z = request.params['password']
        user="admin"
        pwd="adminpass"
        if user == x and pwd == z :
            #session = request.session
            #session['user'] = x
            return Response(render('../templates/admin.jinja2',{'user':'flat_id'},request=request))
        return Response(render('../templates/adlogin.jinja2',{'error':'Username or password is incorrect !'},request=request))
    else:
        return {}



@view_config(route_name='l3',renderer='../templates/index.jinja2')
def l3(request):
    print("button function")

    return()
@view_config(route_name='l2',renderer='../templates/main.jinja2')
def button(request):
    print("button function")

    return()


@view_config(route_name='ui',renderer='../templates/userissue.jinja2')
def ui(request):

    details=[]
    try:
        query = request.dbsession.query(complaint).all()
        for row in query:
            det=[]
            det.append(row.id)
            det.append(row.time_created)
            det.append(row.allocate_by)
            det.append(row.title)
            det.append(row.flat_id)
            det.append(row.issue)
            det.append(row.department)
            det.append(row.complaint_status)
            det.append(row.time_updated)
            det.append(row.replay)
            details.append(det)

            row.flat_id

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'project': details}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_Agrini_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
