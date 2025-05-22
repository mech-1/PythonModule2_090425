# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ",Произвольный, текст.."

num_comma = text.count(",")
num_points = text.count(".")

if num_comma > num_points:
    print(",")
elif num_comma < num_points:
    print(".")
else:
    print("одинаково")

