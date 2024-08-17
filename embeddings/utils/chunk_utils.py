
def get_headings(content):
    elements = []
    for heading in content["headings"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":heading["slug"],
            "type":"heading",
            "text":heading["label"]
        })
    return elements

def get_tables(content):
    elements = []
    for table in content["tables"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":table["heading"],
            "type":"table",
            "text":table["text"],
            "sid": table["sid"]
        })
    return elements

def get_images(content):
    elements = []
    for image in content["images"]:
        if(len(image["text_list"]) > 0):
            text = ' '.join(image["text_list"])
            meta = "url="+image["url"] + " "
            if(image["title"] is not None):
                meta += "title="+image["title"] + " "
            if(image["alt"] is not None):
                meta += "alt="+image["alt"] + " "
            elements.append({
                "doc_sid":content["sid"],
                "doc_path":content["path"],
                "heading":image["heading"],
                "type":"diagram",
                "text":text,
                "meta":meta,
                "sid": image["sid"]
            })
    return elements

def get_codes(content):
    elements = []
    for code in content["code"]:
        meta = "language="+code["language"]
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":code["heading"],
            "type":"code",
            "text":code["text"],
            "meta":meta,
            "sid": code["sid"]
        })
    return elements

def get_paragraphs(content):
    elements = []
    for paragraph in content["paragraphs"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":paragraph["heading"],
            "type":"paragraph",
            "text":paragraph["text"]
        })
    return elements

def split_chunk(text, max_length, overlap):
    """
    Splits a text into chunks, each with a maximum length of max_length.
    Each chunk will overlap with the next by 'overlap' characters.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_length, len(text))
        if end < len(text):
            # Extend the chunk to include overlap, ensuring not to exceed text length
            overlap_end = min(end + overlap, len(text))
            chunk_end = text.rfind(' ', end, overlap_end)
            if chunk_end == -1 or chunk_end - start > max_length:
                # No space found in overlap range, or chunk too large, so use hard limit
                chunk_end = end
        else:
            chunk_end = end
        chunks.append(text[start:chunk_end])
        start = chunk_end
    return chunks

def split_chunk_text(text, max_length, overlap):
    """
    Splits a text into two sets of data:
    1. Chunks: Each with a maximum length of max_length, overlapping with the next by 'overlap' characters.
       Chunks avoid splitting words unless it requires dropping more than 20 characters.
    2. Non-overlapping Texts: Corresponding segments of the chunks without any redundancy.
    """
    chunks = []
    non_overlapping_texts = []
    start = 0
    non_overlap_start = 0

    while start < len(text):
        end = min(start + max_length, len(text))
        chunk_end = end

        if end < len(text):
            # Extend the chunk to include overlap, ensuring not to exceed text length
            overlap_end = min(end + overlap, len(text))
            proposed_end = text.rfind(' ', end, overlap_end)

            if (proposed_end != -1) and ((overlap_end - proposed_end) <= 40):
                # If a space is found within a reasonable range, use it to avoid splitting a word
                chunk_end = proposed_end
            else:
                # No suitable space found or the chunk would be too short, so use the hard limit
                chunk_end = overlap_end

        # Append the chunk
        chunks.append(text[start:chunk_end])

        # Calculate non-overlapping text end
        # It should end where the next chunk will start
        non_overlap_end = min(start + max_length, len(text))

        # Append the non-overlapping text
        non_overlapping_texts.append(text[non_overlap_start:non_overlap_end])

        # Update the start for the next iteration
        start = non_overlap_end
        non_overlap_start = start

    combined_list = [{"chunk": chunk, "text": non_overlap_text} for chunk, non_overlap_text in zip(chunks, non_overlapping_texts)]
    return combined_list
