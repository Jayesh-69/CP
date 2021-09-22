for _ in range(int(input())):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w, h = map(int, input().split())

    ans = 999999999999999

    if x2 - x1 + w <= W:
        ans = min(ans, max(0, w - x1))
        ans = min(ans, max(0, x2 - (W - w)))

    if y2 - y1 + h <= H:
        ans = min(ans, max(0, h - y1))
        ans = min(ans, max(0, y2 - (H - h)))

    if ans == 999999999999999:
        print(-1)
    else:
        print(float(ans))
