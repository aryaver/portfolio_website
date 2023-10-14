# %pip install dash-iconify
# %pip install dash-mantine-components

import dash
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = dash.Dash(external_stylesheets=[dbc.themes.MORPH]) #CYBORG, MATERIA, MINTY, MORPH, QUARTZ, SKETCHY, SLATE, LUMEN   

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
                       
        html.Div([  #dbc.Button("Contact Me", id = 'contact-button', n_clicks = 0),
                    dbc.Offcanvas(html.Div(id = 'offcanvas-body', 
                                #    children = [ html.Div([html.A([DashIconify(icon="logos:google-gmail", width=30,)], target = 'Blank', href = "https://mail.google.com/mail/u/0/#inbox?compose=new")], style = {'padding': '20px'}), 
                                #                 html.Div([html.A([DashIconify(icon="skill-icons:instagram", width=30,)], target = 'Blank', href = "https://www.instagram.com/aryya__a/")], style = {'padding': '20px'}), 
                                #                 html.Div([html.A([DashIconify(icon="skill-icons:linkedin", width=30,)], target = 'Blank', href = "https://www.linkedin.com/in/arya-verma-a18719279/")], style = {'padding': '20px'}),
                                #                 html.Div([ dbc.Input(id='name_input', type='text', placeholder='Enter your name...', style={'width': '36vw'})]),
                                #                 html.Div([ dbc.Input(id='sender_email_input', type='text', placeholder='Enter your email...', style={'width': '36vw'})]),
                                #                 #html.Div([ dmc.TextInput( label="Email id", style={"width": 200 }, placeholder="Enter your email id here...", icon=DashIconify(icon="ic:round-alternate-email"))]),                                              
                                #                 html.Div([ dbc.Input(id='sender_password_input', type='password', placeholder='Enter your password...', style={'width': '36vw'})]), 
                                #                 dbc.Tooltip("This is a tooltip", id="tooltip", is_open=False, target="sender_password_input", trigger=None),
                                #                 html.Div([ dbc.Input(id='message_input', type='text', placeholder='Enter your message...', style={'width': '36vw'})]),
                                #                 html.Div([dbc.Button('Send Mail', id = 'send_info_mail', n_clicks = 0, color="warning", className = 'text-center')]),                                                   
                                #                 html.Div(id='confirmation-section'),], 
                                        className = 'fw-bold'),
                                        id = 'offcanvas', is_open = False, keyboard = True, 
                                        scrollable = True, title = "About Plotly Dash"),
                                                  
                ]),

        html.Div([dmc.Group([
                html.Div(html.A("HOME", href='#home-section', className='nav-link fw-bold')),
                html.Div(html.A("ABOUT", href='#about-section', className='nav-link fw-bold')),
                html.Div(html.A("SKILLS", href='#skills-section', className='nav-link fw-bold')),
                # html.Div(html.A("CLUBS and ACTIVITIES", href = '#clubs-section')), 
                html.Div(html.A("EXPERIENCE", href='#experience-section', className='nav-link fw-bold')),
                html.Div(html.A("PROJECTS", href='#projects-section', className='nav-link fw-bold')),
                html.Div(html.A("CONTACT ME", href='#contact-section', className='nav-link fw-bold')),
                html.Div(html.A("DASH", href='#dash-section', id='dash-button', className='nav-link fw-bold')),
        ])], style = {'position': 'fixed', 'padding': '20px'}),
                        
        html.Div([  html.Div(id = 'home-section'),
                    html.Br(),
                    html.Br(),
                    html.H1("ARYA VERMA", className = 'fw-bold text-center display-3')], 
                    style = {'height':'50vh','align-items': 'center'}),#, 'padding': '100px'}),#
                        
        html.Div(id = 'photo-gallery'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.Div([  html.Div(id = 'about-section'),
                    html.Br(),
                    html.Br(),
                    html.H1("ABOUT", className = 'fw-bold text-center display-3'),
                    html.Div([html.H6("Hi there.")], style = {'text-align' : 'center', 'font-weight': 'bold'}),
                    html.Div([html.P("""I am a dedicated AI/ML enthusiast actively seeking an internship in the field of computer science 
                                        and related technologies. What sets me apart is not just my technical acumen but also my outgoing nature, 
                                        excellent communication skills, and knack for building meaningful connections. Beyond the world of algorithms 
                                        and data, I have a deep passion for music, and I love to sing. This creative outlet not only adds harmony to 
                                        my life but also enhances my problem-solving skills, offering a unique perspective to approaching challenges. 
                                        I am genuinely excited to connect with like-minded professionals, learn from diverse perspectives, and 
                                        contribute to the ever-evolving landscape of AI, ML and Data Science.""")], className = 'px-5'),   
                ], style = {'height':'50vh','align-items': 'center'}),
                        
        html.Div(id = 'skills-section'),
        html.Br(),
        html.Br(),
        html.H1("SKILLS", className = 'fw-bold text-center display-3'),


        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.Div(id = 'experience-section'),
        html.Br(),
        html.Br(),
        html.H1("EXPERIENCE", className = 'fw-bold text-center display-3'),

        # html.H1("EXPERIENCE", id = 'experience-section', className = 'fw-bold text-center display-3'),

        html.Div([dbc.Row([
                            dbc.Col(html.Div([   html.H2("Data Analysis Intern"),#, className="display-3"),
                                                 html.Hr(className="my-2"),
                                                 html.P("Clevered")
                                            ],className="h-100 p-5 text-black rounded-3 justify-content-center")),
                            dbc.Col(html.Div([   html.H2("General Secretary"),#, className="display-3"),
                                                 html.Hr(className="my-2"),
                                                 html.P("Sangam")
                                            ],className="h-100 p-5 text-black rounded-3 justify-content-center")),
                            dbc.Col(html.Div([   html.H2("Technical Department"),#, className="display-3"),
                                                 html.Hr(className="my-2"),
                                                 html.P("IEEE WIE Student Chapter")
                                            ],className="h-100 p-5 text-black rounded-3 justify-content-center")),
                        ])
                ]),

        html.Div(id = 'experience'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.H1(id = 'projects-section'),
        html.Br(),
        html.Br(),
        html.H1("PROJECTS", className = 'fw-bold text-center display-3'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        

        html.Div(id = 'contact-section'),
        html.Br(),
        html.Br(),
        html.H1("CONTACT ME", className = 'fw-bold text-center display-3'),

        html.Div([              html.Div([ dbc.Input(id='name_input', type='text', placeholder='Enter your name...', style={'width': '36vw'})]),

                                html.Div([ dbc.Input(id='sender_email_input', type='text', placeholder='Enter email...', style={'width': '36vw'})]),

                                html.Div([      dbc.Input(id='sender_password_input', type='password', placeholder='Enter app password...', style={'width': '36vw'}), 
                                                dbc.Tooltip("""Please note: Google no longer allows access to less secure apps. To use your Gmail account, you'll need to 
                                                                generate a 'Less Secure App Password' from your Google Account settings. Rest assured, this app password is unique to this 
                                                                application, does not provide login access to your account, and helps keep your account secure. Now go ahead and type in your message ;) """, 
                                                            id="tooltip", is_open=False, target="sender_password_input", trigger="hover", placement = 'right')]), 

                                                                        

                                html.Div([ dbc.Input(id='message_input', type='text', placeholder='Your message to me...', style={'width': '36vw'})]),

                                html.Div([dbc.Button('Send Mail', id = 'send_info_mail', n_clicks = 0, color="warning", className = 'text-center')]),
                                                                        
                                html.Div(id='confirmation-section'),], style = {'padding':'20px'}),
        
        html.Div([
                    html.Div([html.A([DashIconify(icon="logos:google-gmail", width=50,)], target = 'Blank', href = "https://mail.google.com/mail/u/0/#inbox?compose=new")], style = {'padding': '20px'}), 

                    html.Div([html.A([DashIconify(icon="skill-icons:instagram", width=40,)], target = 'Blank', href = "https://www.instagram.com/aryya__a/")], style = {'padding': '20px'}), 

                    html.Div([html.A([DashIconify(icon="skill-icons:linkedin", width=45,)], target = 'Blank', href = "https://www.linkedin.com/in/arya-verma-a18719279/")], style = {'padding': '20px'}),
                ],  style = {'justify-content': 'center','display':'flex'}
            ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div(["designed and developed by Arya", DashIconify(icon="meteocons:pollen-flower-fill", width=30)], className = 'fst-italic text-center'),
                        
], style={
            #'display': 'flex',
            'justify-content': 'center',  # Center horizontally
            'align-items': 'center',      # Center vertically
            'height': '100vh',            # Optional: Make the div fill the viewport height
        })  


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
        
        recipient_email = 'arya.verma2021@vitstudent.ac.in'
  
        if send_email(sender_email, password, recipient_email, f"Message from {name}!", message) == 1:
            return dbc.Alert('Email sent successfully!', color = 'success', style = {'width':'30vw'}) 
        else:
            return dbc.Alert('Error: Incorrect password or authentication failed.', color = 'danger', style = {'width':'30vw'}) 
    else:
        return ''#dbc.Alert('No emails to send.', color = 'danger', style = {'width':'30vw'})   
    
@app.callback(
    Output('offcanvas', 'is_open'),
    Input('dash-button', 'n_clicks'),
    State('offcanvas', 'is_open'),
)
def open_offcanvas(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug = True, port = 8060)