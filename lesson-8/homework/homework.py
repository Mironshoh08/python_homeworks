# ---- Homework

# n = 5
# for i in range(n):
#     for a in range(i, n):
#         print(' ', end=' ')
#     for a in range(i):
#         print('*', end=' ')
#     for a in range(i + 1):
#         print('*', end=' ')
#     print()

# -----

# n = 5
# for i in range(n-1):
#     for a in range(i, n):
#         print(' ', end=' ')
#     for a in range(i):
#         print('*', end=' ')
#     for a in range(i + 1):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     for a in range(i + 1):
#         print(' ', end=' ')
#     for a in range(i, n - 1):
#         print('*', end=' ')
#     for a in range(i, n):
#         print('*', end=' ')
#     print()

# ----

# n = 5
# for i in range(n):
#     for a in range(i + 1):
#         print('*', end=' ')
#     for a in range(n-1, i, -1):
#         print(' ', end=' ')
#     for a in range(i+1, n):
#         print(' ', end=' ')
#     for b in range(i+1):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     for a in range(i, n):
#         print('*', end=' ')
#     for a in range(i):
#         print(' ', end=' ')
#     for a in range(i):
#         print(' ', end=' ')
#     for a in range(i, n):
#         print('*', end=' ')
#     print()