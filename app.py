import argparse
import secrets
import string


def generate_password(length=16, use_digits=True, use_symbols=True):
    """Generate a password containing at least one character from each enabled group."""
    if length < 1:
        raise ValueError("Password length must be positive")
    groups = [string.ascii_lowercase, string.ascii_uppercase]
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append("!@#$%^&*()-_=+")
    if length < len(groups):
        raise ValueError(f"Length must be at least {len(groups)} for selected character groups")
    chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)
    chars.extend(secrets.choice(all_chars) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main():
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=16)
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    args = parser.parse_args()
    try:
        print(generate_password(args.length, not args.no_digits, not args.no_symbols))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
