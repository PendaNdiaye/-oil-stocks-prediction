import re
def process_text(text):
    # removed all the special characters 
    processed_feature = re.sub(r'\W', ' ', str(text))

    # remove all single characters 
    processed_feature = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

    # remove single characters from start 
    processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature)

    # substuting multiple spaces with single space
    processed_feature = re.sub(r'\s+', ' ', processed_feature, flags = re.I)

    # removing prefixed b
    processed_feature = re.sub(r'^b\s+', ' ', processed_feature) 

    processed_feature = processed_feature.lower()
    return processed_feature