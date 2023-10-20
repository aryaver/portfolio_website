# %pip install dash-iconify
# %pip install dash-mantine-components

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = dash.Dash(external_stylesheets=[dbc.themes.MORPH]) #CYBORG, MATERIA, MINTY, MORPH, QUARTZ, SKETCHY, SLATE, LUMEN   
server = app.server

about_me = """I am a dedicated AI/ML enthusiast actively seeking an internship in the field of computer science 
            and related technologies. What sets me apart is not just my technical acumen but also my outgoing nature, 
            excellent communication skills, and knack for building meaningful connections. Beyond the world of algorithms 
            and data, I have a deep passion for music, and I love to sing. This creative outlet not only adds harmony to 
            my life but also enhances my problem-solving skills, offering a unique perspective to approaching challenges. 
            I am genuinely excited to connect with like-minded professionals, learn from diverse perspectives, and 
            contribute to the ever-evolving landscape of AI, ML and Data Science."""



def send_email(sender_email, password, recv_email, subject, message):

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recv_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server1 = smtplib.SMTP("smtp.gmail.com", 587)
        server1.starttls()
        login_result = server1.login(sender_email, password)
        #print("login successful")

        if login_result[0] == 235:  # Check if login was successful -> 235 is the code for successful login
            server1.sendmail(sender_email, recv_email, msg.as_string())
            server1.quit()
            return 1
        else:
            return 'Error: Incorrect password or authentication failed.'
        
    except smtplib.SMTPException as e:
        return f"Error: Unable to send email - {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"


app.layout = html.Div(
    id='page-content',
    children = [
                       
        html.Div([
            dbc.Offcanvas(id = 'offcanvas', is_open = False, 
                        keyboard = True, scrollable = True, title = "App Password Information",
                        children = [html.H6("What is an App Password?"),
                                    dcc.Markdown("""An "App Password" is a unique, application-specific password generated within your Google Account 
                                           settings. This password is exclusively used for specific applications or services, like ours, and **does 
                                           not provide access to your Google Account**."""),
                                    html.H6("How to Generate an App Password:"),
                                    dcc.Markdown('''
                                                 * Log in to your Google Account.
                                                 * Navigate to your Google Account settings.
                                                 * Select the "Security" tab.
                                                 * Select "2-step verification and locate the "App Passwords" section.
                                                 * Generate a new App Password for Mail.
                                                 * Use this App Password to contact me through my website.                                                 
                                                '''),
                                    html.H6("Your Account's Security Remains Intact"),
                                    html.P("""Rest assured, using an App Password ensures that your primary Gmail account remains secure. This App 
                                           Password is unique to our application and won't compromise your login credentials."""),]),
                                    
                
            ]),

        html.Div([
            dmc.Group([
                html.Div(html.A("HOME", href='#home-section', className='nav-link fw-bold')),
                html.Div(html.A("ABOUT", href='#about-section', className='nav-link fw-bold')),
                html.Div(html.A("SKILLS", href='#skills-section', className='nav-link fw-bold')), 
                html.Div(html.A("EXPERIENCE", href='#experience-section', className='nav-link fw-bold')),
                html.Div(html.A("CLUBS", href='#clubs-section', className='nav-link fw-bold')),
                html.Div(html.A("PROJECTS", href='#projects-section', className='nav-link fw-bold')),
                html.Div(html.A("CONTACT ME", href='#contact-section', className='nav-link fw-bold')),
                # html.Div(dmc.Burger(html.A(href='#offcanvas', id='fyi-button', className='nav-link fw-bold'), opened=False)),
                html.Div(html.A("FYI :)", href='#offcanvas', id='fyi-button', className='nav-link fw-bold')),
                ])
            ], style = {'position': 'fixed', 'padding': '20px'}),
        # dmc.Burger(id="burger-button"),                
        html.Div([  
            html.Div(id = 'home-section'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1("ARYA VERMA", className = 'fw-bold text-center display-3')
            ],style = {'height':'50vh','align-items': 'center'}),#, 'padding': '100px'}),#
                        
        html.Div(id = 'photo-gallery'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
          
        html.Div(id = 'about-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("ABOUT", className = 'fw-bold text-center display-3'),
        html.Br(),

        # html.Div([html.H6("Hi there.")], style = {'text-align' : 'center', 'font-weight': 'bold'}),
        dmc.Tabs([
            dmc.TabsList([
                dmc.Tab("Education",icon=DashIconify(icon="carbon:education"),value="education",),
                dmc.Tab("Languages",icon=DashIconify(icon="uil:language"),value="languages",),
                    ],position="right", style = {'margin-right':'250px', 'margin-left':'250px'},
                ),
            ],
            id="tabs",
            value="education",
        ), 
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col([html.Div([
            dmc.Paper(
                children = [about_me],
                shadow="xl", style = {'padding':'40px', 'margin-left':'80px'}),
            ], style = {'height':'50vh','align-items': 'center'})]),
                                
        
        html.Br(),
        html.Br(),      
        dbc.Col([html.Div(id="tabs-content", style={'display':'flex', 'align-items': 'center', "justifyContent": "center"})])]),  

        html.Div(id = 'skills-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("SKILLS", className = 'fw-bold text-center display-3'),
        html.Br(),
        html.Br(),
        html.Div([
            DashIconify(icon = "devicon:java",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "devicon:python",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "simple-icons:plotly",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "devicon:pandas",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "vscode-icons:file-type-excel",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "devicon:git",width = 100, style={'margin-right': '20px'}),
            DashIconify(icon = "devicon:github",width = 100, style={'margin-right': '20px'}),
        ],style={"display": "flex", 'justify-content': 'center'}),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.Div(id = 'experience-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("EXPERIENCE", className = 'fw-bold text-center display-3'),
        html.Br(),
        html.Br(),
        html.Br(),
        
        dbc.Row([dbc.Col(
            dbc.Card([
                dbc.CardImg(src='/assets/clevered.png',
                            alt="Clevered Image",
                            top=True,
                            # style={"opacity": 0.3},
                        ),
            ],
            style={"width": "18rem"},
        ),),
        dbc.Col([html.H4("Data Analysis Intern", className = 'fw-bold'),
        html.Div("Clevered"),
        html.A(["Visit website"], target = 'blank', href = "https://clevered.com/"),]),], style  = {'margin-left':'250px'}),
            


        html.Div(id = 'clubs-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("CLUBS", className = 'fw-bold text-center display-3'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src='/assets/sangamLogo.jpg',
                                alt="Sangam Image",
                                top=True,
                                style={"opacity": 0.4},
                            ),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H4("General Secretary", className="card-title fw-bold text-dark"),
                            html.P("Sangam, VIT Chennai", className="card-text fw-bold text-dark"),
                            html.A(["Visit"], target = 'blank', href = "https://www.linkedin.com/in/sangam-vit-chennai-a83b1827a/"),
                            ],
                        ),
                    ),
                ],
                style={"width": "18rem"},
            ),]),
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src='/assets/ieeewie.png',
                                alt="IEEE Image",
                                top=True,
                                style={"opacity": 0.4},
                            ),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H4("Technical Team", className="card-title fw-bold text-dark"),
                            html.P("IEEE Women in Engineering, VIT Chennai", className="card-text fw-bold text-dark"),
                            html.A(["Visit"], target = 'blank', href = "https://wie.ieee.org/"),
                            ],
                        ),
                    ),
                ],
                style={"width": "18rem"},
            ),]),
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src='/assets/uddeshya1.png',
                                alt="Uddeshya Image",
                                top=True,
                                style={"opacity": 0.4},
                            ),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H4("Design Team", className="card-title fw-bold text-dark"),
                            html.P("Uddeshya, VIT Chennai", className="card-text fw-bold text-dark"),
                            html.A(["Visit"], target = 'blank', href = "https://www.linkedin.com/in/uddeshya-vit-chennai/?originalSubdomain=in"),
                            ],
                        ),
                    ),
                ],
                style={"width": "18rem"},
            ),]),], style  = {'margin-left':'100px'}),
        
    
        html.Div(id = 'experience'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.H1(id = 'projects-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("PROJECTS", className = 'fw-bold text-center display-3'),

        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col(
                html.Div([   
                    html.H2("HR Dashboard"),
                    html.Hr(className="my-2"),
                    html.A("View Project", target = 'blank', href = "https://github.com/aryaver/dashboard_launch.git")
                    ],className="h-100 p-5 rounded-3 justify-content-center")),
            dbc.Col(
                html.Div([   
                    html.H2("Lead Analysis Dashboard"),
                    html.Hr(className="my-2"),
                    html.A("View Project", target = 'blank', href = "https://github.com/aryaver/clevered_sales_dash.git")
                    ],className="h-100 p-5 rounded-3 justify-content-center")),
            dbc.Col(
                html.Div([   
                    html.H2("Portfolio Website"),
                    html.Hr(className="my-2"),
                    html.A("Visit website", href = "/")
                    ],className="h-100 p-5 rounded-3 justify-content-center")),
            ]),

        html.Div(id = 'contact-section'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("CONTACT ME", className = 'fw-bold text-center display-3'),
        html.Br(),
        html.Br(),#
        html.Div([  
            html.Div([
                dbc.Row([   
                        dbc.Col([ 
                            dbc.Input(id='name_input', type='text', placeholder='Enter your name...', style={'width': '36vw', 'margin-right':'50px'}),
                            dbc.Input(id='sender_email_input', type='text', placeholder='Enter email...', style={'width': '36vw'}),
                            ],style={"display": "flex", 'justify-content': 'center'})
                        ])
                    ]),                                                   
                html.Br(),
                html.Br(),
                html.Div([
                    dbc.Row([   
                        dbc.Col([ 
                            dbc.Input(id='message_input', type='text', placeholder='Your message to me...', style={'width': '36vw', 'margin-right':'50px'}),
                            dbc.Input(id='sender_password_input', type='password', placeholder='Enter app password...', style={'width': '36vw'}),
                            dbc.Tooltip( """Please note: Google no longer allows access to less secure apps. To use your Gmail account, you'll need to 
                                                  generate a 'Less Secure App Password' from your Google Account settings. Rest assured, this app password is unique to this 
                                                  application, does not provide login access to your account, and helps keep your account secure. Now go ahead and type in your message ;) """, 
                                              id="tooltip", is_open=False, target="sender_password_input", trigger="hover", placement = 'right')
                            ],style={"display": "flex", 'justify-content': 'center'}), 
                        ]),                                             
                    ]),
                html.Br(),
                html.Br(),  
                dbc.Row(dbc.Col([dbc.Button('Send Mail', id = 'send_info_mail', n_clicks = 0, color="warning", className = 'text-center')], style = {'display':'flex', 'justify-content':'center'})),
                                                                    
                ]),
        html.Br(),
        html.Div(id='confirmation-section', style = {'display':'flex', 'justify-content':'center'}),
        html.Br(),
        html.Br(),
        html.Div([
            html.Div([
                html.A([
                    DashIconify(id = "gmail-icon",icon="logos:google-gmail", width=48,)
                    ], target = 'Blank', href = "https://mail.google.com/mail/u/0/#inbox?compose=new"),
                    dbc.Tooltip( """arya.verma.923@gmail.com""", 
                                              id="tooltip2", is_open=False, target="gmail-icon", trigger="hover", placement = 'left')], style = {'padding': '20px'}), 
            html.Div([
                html.A([
                    DashIconify(icon="skill-icons:instagram", width=40,)
                    ], target = 'Blank', href = "https://www.instagram.com/aryya__a/")], style = {'padding': '20px'}), 
            html.Div([
                html.A([
                    DashIconify(icon="skill-icons:linkedin", width=40,)
                    ], target = 'Blank', href = "https://www.linkedin.com/in/arya-verma-a18719279/")], style = {'padding': '20px'}),
            html.Div([
                html.A([
                    DashIconify(icon="devicon:github", width=40,)
                    ], target = 'Blank', href = "https://github.com/aryaver")], style = {'padding': '20px'}),
                ],  style = {'justify-content': 'center','display':'flex'}
            ),

        html.Br(),
        html.Br(),
        html.Div(["designed and developed by Arya", DashIconify(icon="meteocons:pollen-flower-fill", width=30)], className = 'fst-italic text-center'),
        html.Div(["using Python"], className = 'fst-italic text-center'),
        # html.Br(),
                        
], style={'height': '100vh',})             
         
@app.callback(Output("tabs-content", "children"), 
              Input("tabs", "value"))
def render_content(active):
    if active == "education":
        ed = html.Div([
            dmc.Timeline(
                    active=1,
                    bulletSize=15,
                    lineWidth=2,
                    children=[
                        dmc.TimelineItem(
                            title="B.Tech. CSE (Spl. in AI and ML)",
                            children=[
                                dmc.Text(
                                    [
                                        html.Div("Vellore Institute of Technology, Chennai"),
                                        html.Div("Current CGPA: 8.99"),
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            title="CBSE XII AISSCE",
                            children=[
                                dmc.Text(
                                    [
                                        html.Div("Sunbeam School"),
                                        html.Div("98.4% | 2020"),
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            title="CBSE X SSC",
                            lineVariant="dashed",
                            children=[
                                dmc.Text(
                                    [
                                        html.Div("Sunbeam School"),
                                        html.Div("96.4% | 2018"),
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            [
                                dmc.Text(
                                    [
                                        html.Div("Sunbeam School"),
                                        html.Div("2006 - 2017"),
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                            title="CBSE KG - IX",
                        ),
                    ],
                )
        ]),
        return ed
    else:
        lang = html.Div([
            html.Div("English",),
            dcc.Slider(
                id='english-slider',
                min=0,
                max=100,
                step=10,
                value=100,
                # marks={0: 'Basic', 50: 'Intermediate', 100: 'Full Proficiency'},
                tooltip={'placement': 'bottom', 'always_visible': True},
                disabled=True, 
            ),
            html.Div("Hindi",),
            dcc.Slider(
                id='hindi-slider',
                min=0,
                max=100,
                step=10,
                value=100,
                # marks={0: 'Basic', 50: 'Intermediate', 100: 'Native Language'},
                tooltip={'placement': 'bottom', 'always_visible': True},
                disabled=True,  
            ),
            html.Div("French",),
            dcc.Slider(
                id='french-slider',
                min=0,
                max=100,
                step=10,
                value=30, 
                marks={0: 'Basic', 50: 'Intermediate', 100: 'Full Proficiency'},
                tooltip={'placement': 'bottom', 'always_visible': True},
                disabled=True,
            ),
        ], style = {'width':'30vw'}),
        return lang
        
@app.callback(
    Output('confirmation-section', 'children'), 
    Input('send_info_mail', 'n_clicks'),
    Input('message_input', 'value'),
    Input('name_input', 'value'),
    Input('sender_email_input', 'value'),
    State('sender_password_input', 'value'),
    prevent_initial_callback = True
)
def send_bday_anni_info(n_clicks, message, name, sender_email, password):
    if n_clicks > 0  and password is not None:
        
        recipient_email = 'arya.verma.923@gmail.com'
  
        if send_email(sender_email, password, recipient_email, f"Message from {name}!", message) == 1:
            return dbc.Alert('Email sent successfully!',dismissable=True, color = 'success', style = {'width':'30vw'}) 
        else:
            return dbc.Alert('Error: Incorrect password or authentication failed.', dismissable=True, color = 'danger', style = {'width':'30vw'}) 
    else:
        return ''   
    
@app.callback(
    Output('offcanvas', 'is_open'),
    Input('fyi-button', 'n_clicks'),
    State('offcanvas', 'is_open'),
)
def open_offcanvas(n_clicks, is_open):
    if n_clicks:
        html.P("Dash is a Python framework for building web applications."),
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug = True, port = 8060)