"""This module implements examples of SOLID principles in Python."""
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
