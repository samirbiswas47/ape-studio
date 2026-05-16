def replace_email_keywords(content, data):
    for key, value in data.items():
        content = content.replace(key, str(value))

    return content