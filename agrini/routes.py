def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('alloc', 'alloc')
    config.add_route('login', 'login')
    config.add_route('complaint', 'complaint')
    config.add_route('fpwd', 'fpwd')
    config.add_route('signin', 'signin')
    config.add_route('fpass', 'fpass')
    config.add_route('status', 'status')
    config.add_route('adminlogin', 'adlogin')
    config.add_route('l3', 'l3')
    config.add_route('l2', 'choise')
    config.add_route('ui', 'ui')
