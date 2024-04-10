from surrealdb import Surreal


async def main():
    """Example of how to use the SurrealDB client."""
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        await db.create(
            "person",
            {
                "user": "me",
                "pass": "safe",
                "marketing": True,
                "tags": ["python", "documentation"],
            },
        )
        print(await db.select("person"))
        print(
            await db.update(
                "person",
                {
                    "user": "you",
                    "pass": "very_safe",
                    "marketing": False,
                    "tags": ["Awesome"],
                },
            )
        )
        print(await db.delete("person"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
