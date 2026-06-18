from database import engine, Base, SessionLocal
from models import Fragrance, Clone

# Rebuild the database tables
Base.metadata.create_all(bind=engine)
db = SessionLocal()

if db.query(Fragrance).count() == 0:
    sample_data = [
        # Men's / Unisex
        {
            "brand": "Creed", "name": "Aventus", "notes": "Pineapple, Bergamot, Birch, Musk", "accords": "Fruity, Woody, Smoky", "price_estimate": "$475",
            "clones": [
                {"clone_brand": "Armaf", "clone_name": "Club de Nuit Intense Man", "similarity_score": 92.0, "price_estimate": "$35", "notes_match": "Lemon, Pineapple, Birch, Musk"},
                {"clone_brand": "Montblanc", "clone_name": "Explorer", "similarity_score": 85.0, "price_estimate": "$60", "notes_match": "Bergamot, Vetiver, Patchouli"},
                {"clone_brand": "Lattafa", "clone_name": "Qaed Al Fursan", "similarity_score": 82.0, "price_estimate": "$25", "notes_match": "Pineapple, Saffron, Jasmine"}
            ]
        },
        {
            "brand": "Maison Francis Kurkdjian", "name": "Baccarat Rouge 540", "notes": "Saffron, Jasmine, Amberwood, Fir Resin", "accords": "Amber, Woody, Warm Spicy", "price_estimate": "$425",
            "clones": [
                {"clone_brand": "Armaf", "clone_name": "Club de Nuit Untold", "similarity_score": 95.0, "price_estimate": "$45", "notes_match": "Saffron, Jasmine, Amberwood"},
                {"clone_brand": "Lattafa", "clone_name": "Ana Abiyedh Rouge", "similarity_score": 88.0, "price_estimate": "$25", "notes_match": "Saffron, Bitter Almond, Amber"},
                {"clone_brand": "Zara", "clone_name": "Red Temptation", "similarity_score": 85.0, "price_estimate": "$30", "notes_match": "Saffron, Coriander, Praline"}
            ]
        },
        {
            "brand": "Tom Ford", "name": "Oud Wood", "notes": "Oud, Sandalwood, Cardamom, Sichuan Pepper", "accords": "Woody, Oud, Warm Spicy", "price_estimate": "$295",
            "clones": [
                {"clone_brand": "Maison Alhambra", "clone_name": "Woody Oud", "similarity_score": 90.0, "price_estimate": "$30", "notes_match": "Oud, Sandalwood, Amberwood"}
            ]
        },
        {
            "brand": "Tom Ford", "name": "Tobacco Vanille", "notes": "Tobacco Leaf, Vanilla, Cacao, Tonka Bean", "accords": "Vanilla, Sweet, Tobacco", "price_estimate": "$295",
            "clones": [
                {"clone_brand": "Maison Alhambra", "clone_name": "Tobacco Touch", "similarity_score": 92.0, "price_estimate": "$30", "notes_match": "Tobacco, Vanilla, Spicy Notes"},
                {"clone_brand": "Al Haramain", "clone_name": "Amber Oud Tobacco Edition", "similarity_score": 89.0, "price_estimate": "$50", "notes_match": "Tobacco, Cinnamon, Vanilla"}
            ]
        },
        {
            "brand": "Dior", "name": "Sauvage EDT", "notes": "Calabrian Bergamot, Pepper, Lavender, Ambroxan", "accords": "Fresh Spicy, Amber, Citrus", "price_estimate": "$145",
            "clones": [
                {"clone_brand": "Armaf", "clone_name": "Ventana", "similarity_score": 87.0, "price_estimate": "$30", "notes_match": "Bergamot, Grapefruit, Lavender, Ambroxan"},
                {"clone_brand": "Afnan", "clone_name": "Modest Une", "similarity_score": 91.0, "price_estimate": "$35", "notes_match": "Lavender, Mint, Pepper, Ambroxan"}
            ]
        },
        {
            "brand": "Kilian", "name": "Angels' Share", "notes": "Cognac, Cinnamon, Tonka Bean, Oak", "accords": "Warm Spicy, Vanilla, Woody", "price_estimate": "$245",
            "clones": [
                {"clone_brand": "Lattafa", "clone_name": "Khamrah", "similarity_score": 85.0, "price_estimate": "$40", "notes_match": "Cinnamon, Praline, Vanilla"},
                {"clone_brand": "Maison Alhambra", "clone_name": "Kismet Angel", "similarity_score": 94.0, "price_estimate": "$35", "notes_match": "Cognac, Cinnamon, Tonka Bean"}
            ]
        },
        {
            "brand": "Le Labo", "name": "Santal 33", "notes": "Sandalwood, Leather, Papyrus, Virginia Cedar", "accords": "Woody, Powdery, Leather", "price_estimate": "$320",
            "clones": [
                {"clone_brand": "Zara", "clone_name": "Energetically New York", "similarity_score": 80.0, "price_estimate": "$30", "notes_match": "Cardamom, Jasmine, Sandalwood"},
                {"clone_brand": "Dossier", "clone_name": "Woody Sandalwood", "similarity_score": 88.0, "price_estimate": "$49", "notes_match": "Violet Leaves, Sandalwood, Musk"}
            ]
        },
        
        # Women's
        {
            "brand": "Parfums de Marly", "name": "Delina", "notes": "Litchi, Rhubarb, Turkish Rose, Vanilla", "accords": "Rose, Floral, Fruity", "price_estimate": "$355",
            "clones": [
                {"clone_brand": "Maison Alhambra", "clone_name": "Delilah", "similarity_score": 92.0, "price_estimate": "$30", "notes_match": "Rhubarb, Litchi, Rose"},
                {"clone_brand": "Afnan", "clone_name": "Souvenir Floral Bouquet", "similarity_score": 89.0, "price_estimate": "$45", "notes_match": "Litchi, Rose, Vanilla"}
            ]
        },
        {
            "brand": "Yves Saint Laurent", "name": "Black Opium", "notes": "Coffee, Vanilla, White Flowers, Patchouli", "accords": "Vanilla, Coffee, Sweet", "price_estimate": "$155",
            "clones": [
                {"clone_brand": "Zara", "clone_name": "Gardenia", "similarity_score": 85.0, "price_estimate": "$25", "notes_match": "Coffee, Orange Blossom, Vanilla"},
                {"clone_brand": "Dossier", "clone_name": "Ambery Vanilla", "similarity_score": 90.0, "price_estimate": "$29", "notes_match": "Pear, Coffee, Vanilla"}
            ]
        },
        {
            "brand": "Byredo", "name": "Gypsy Water", "notes": "Juniper Berries, Lemon, Bergamot, Pine Needles", "accords": "Woody, Citrus, Aromatic", "price_estimate": "$225",
            "clones": [
                {"clone_brand": "Zara", "clone_name": "Waterlily Tea Dress", "similarity_score": 75.0, "price_estimate": "$35", "notes_match": "Bergamot, Mint, Musk"},
                {"clone_brand": "Oakcha", "clone_name": "Morning Rain", "similarity_score": 88.0, "price_estimate": "$40", "notes_match": "Lemon, Juniper, Sandalwood"}
            ]
        }
    ]

    for item in sample_data:
        frag = Fragrance(brand=item["brand"], name=item["name"], notes=item["notes"], accords=item["accords"], price_estimate=item["price_estimate"])
        db.add(frag)
        db.commit()
        db.refresh(frag)
        
        for c in item["clones"]:
            clone_obj = Clone(original_id=frag.id, clone_name=c["clone_name"], clone_brand=c["clone_brand"], similarity_score=c["similarity_score"], price_estimate=c["price_estimate"], notes_match=c["notes_match"])
            db.add(clone_obj)
    db.commit()
    print("Vel Archive V2 successfully seeded!")
db.close()
