def main(x):
    import re
    w="had"
    w1="bought"
    w2="got"
    w3="has"
    ww="wins"
    www="won"
    w4="have"
    w5="gives you"
    w6="finds"
    w7="gave you"
    word1 = "Gained"
    word2 = "Acquired"
    word3 = "Received"
    word4 = "Obtained"
    word5 = "Collected"
    word6 = "Added"
    word7 = "Inherited"
    word8 = "Deposited"
    word9 = "Accumulated"
    word10 = "Won"
    word11 = "Earned"
    word12 = "Attained"
    word13 = "Secured"
    word14 = "Procured"
    word15 = "Garnered"
    word16 = "Scored"
    word17 = "Achieved"
    word18 = "Found"
    word19 = "Discovered"
    word20 = "Mined"
    word21 = "Claimed"
    word22 = "Gathered"
    word23 = "Realized"
    word24 = "Captured"
    word25 = "Achieved"
    word26 = "Grabbed"
    word27 = "Took"
    word28 = "Attained"
    word29 = "Netted"
    word30 = "Bagged"
    word31 = "Obtained"
    word32 = "Derived"
    word33 = "Produced"
    word34 = "Assumed"
    word35 = "Earned"
    word36 = "Obtained"
    word37 = "Acquired"
    word38 = "Confiscated"
    word39 = "Snagged"
    word40 = "Received"
    word41 = "Pulled in"
    word42 = "Procured"
    word43 = "Snatched"
    word44 = "Secured"
    word45 = "Reaped"
    word46 = "Hauled in"
    word47 = "Found"
    word48 = "Accumulated"
    word49 = "Nailed"
    word50 = "Seized"
    word51 = "Fetched"
    word52 = "Landed"
    word53 = "Caught"
    word54 = "Raked in"
    word55 = "Gathered in"
    word56 = "Claimed"
    word57 = "Derived"
    word58 = "Took home"
    word59 = "Hit"
    word60 = "Stumbled upon"

    # Define the variable a
    a=x

    # Define a pattern to match any of the words followed by a numeric value
    pattern = r"\b(" + "|".join(re.escape(word) for word in [w,ww,www,w1,w2,w3,w4,w5,w6,w7,word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17, word18, word19, word20, word21, word22, word23, word24, word25, word26, word27, word28, word29, word30, word31, word32, word33, word34, word35, word36, word37, word38, word39, word40, word41, word42, word43, word44, word45, word46, word47, word48, word49, word50, word51, word52, word53, word54, word55, word56, word57, word58, word59, word60]) + r")\s+(\d+)\b"

    # Use regular expression to find matches
    matches = re.findall(pattern.lower(), a.lower())

    # Print the matches
    if matches:
        for match in matches:
            word, value = match
            lis=[]
            lis.append(value)
    else:
        return 0
    lisa = [int(items) for items in lis]
    result = sum(lisa)
    return result