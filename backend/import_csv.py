import csv
import os
from database import SessionLocal, engine, Base
from models import Fragrance, Clone

def import_csv_to_db(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    # Ensure tables are built
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print(f"Opening {file_path} for ingestion...")
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        count = 0
        for row in reader:
            # Check if the original fragrance exists; if not, create it
            frag = db.query(Fragrance).filter_by(name=row['name'], brand=row['brand']).first()
            if not frag:
                frag = Fragrance(
                    brand=row['brand'],
                    name=row['name'],
                    notes=row['notes'],
                    accords=row['accords'],
                    price_estimate=row['price_estimate']
                )
                db.add(frag)
                db.commit()
                db.refresh(frag)

            # Check if there is clone data attached to this row
            if row.get('clone_name') and row.get('clone_brand'):
                clone_exists = db.query(Clone).filter_by(original_id=frag.id, clone_name=row['clone_name']).first()
                if not clone_exists:
                    try:
                        similarity = float(row['similarity_score']) if row['similarity_score'] else 0.0
                    except ValueError:
                        similarity = 0.0
                        
                    clone = Clone(
                        original_id=frag.id,
                        clone_brand=row['clone_brand'],
                        clone_name=row['clone_name'],
                        similarity_score=similarity,
                        price_estimate=row['clone_price'],
                        notes_match=row['notes_match']
                    )
                    db.add(clone)
                    db.commit()
            count += 1
            
    db.close()
    print(f"Successfully processed {count} rows and injected them into the Vel Archive!")

if __name__ == "__main__":
    import_csv_to_db("fragrance_data.csv")
