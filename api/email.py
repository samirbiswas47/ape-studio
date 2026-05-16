def email_body(content):
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                padding: 20px;
            }}

            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
            }}

            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: gray;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            {content}

            <div class="footer">
                © 2026 APE Studio
            </div>

        </div>
    </body>
    </html>
    """