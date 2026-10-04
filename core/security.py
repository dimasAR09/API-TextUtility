from fastapi import Header, HTTPException, Security

RAPIDAPI_SECRET = "rahasia-proxy"

def verify_rapidapi_header(x_rapidapi_proxy_secret: str = Header(None)):
    """Mencegah akses langsung dari luar instruksi RapidAPI,"""

    if x_rapidapi_proxy_secret != RAPIDAPI_SECRET:
        raise HTTPExceptio(status_code=403, detail="Akses di tolak, gunakan RapidAPI Gateway.")
    return x_rapidapi_proxy_secret