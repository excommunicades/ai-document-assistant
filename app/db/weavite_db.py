import weaviate

from app.config import settings


def connect_weaviate():

    if not settings.weaviate_url.startswith("http://"):
        raise ValueError("weaviate_url must start with http:// for local connection")

    host_port = settings.weaviate_url.replace("http://", "")

    try:
        host, port_str = host_port.split(":")
        port = int(port_str)
    except ValueError:
        raise ValueError(f"Invalid weaviate_url format: {settings.weaviate_url}")

    client = weaviate.connect_to_local(host=host, port=port)
    return client
