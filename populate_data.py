"""Script to populate the database with acolyte data from the provided table."""

import data_manager
from models import Acolyte, Absence, Suspension, BonusMovement, ScheduleHistoryEntry

# Data from the table
acolytes_data = [
    {
        "name": "Andrew",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Augusto",
        "schedule": ["01/01", "03/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 1,
        "bonus_used": []
    },
    {
        "name": "Daniel",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Edmilson",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Flavio",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 1,
        "bonus_used": []
    },
    {
        "name": "Francisco",
        "schedule": ["01/01", "04/01"],
        "absences": [{"date": "04/01/2026", "description": "Escala/Terço (E/T)"}],
        "suspensions": [{"reason": "Ausência sem justificativa", "start_date": "01/01/2026", "duration": "01/01 - 25/01", "is_active": False}],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Gabriel Castro",
        "schedule": ["01/01", "02/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 2,
        "bonus_used": []
    },
    {
        "name": "Gabriel Teixeira",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 1,
        "bonus_used": []
    },
    {
        "name": "Guilherme",
        "schedule": ["01/01", "04/01"],
        "absences": [{"date": "04/01/2026", "description": "Escala/Terço (E/T)"}],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Gustavo",
        "schedule": ["01/01", "03/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Igor",
        "schedule": ["01/01", "03/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 3,
        "bonus_used": []
    },
    {
        "name": "João Ferreira",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Joaquim",
        "schedule": ["01/01", "02/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Jonas",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [{"reason": "Ausência sem justificativa", "start_date": "01/01/2026", "duration": "01/01 - 11/01", "is_active": False}],
        "bonus_available": 1,
        "bonus_used": []
    },
    {
        "name": "Jorge",
        "schedule": ["01/01", "04/01"],
        "absences": [{"date": "04/01/2026", "description": "Escala/Terço (E/T)"}],
        "suspensions": [],
        "bonus_available": 1,
        "bonus_used": []
    },
    {
        "name": "Júlio César",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Júnior",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Lucas Gonçalves",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 3,
        "bonus_used": []
    },
    {
        "name": "Lucas Ribeiro",
        "schedule": ["01/01", "04/01", "04/01"],  # 2x on 04/01
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Matheus Castro",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Matheus Magalhães",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Miguel",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": []
    },
    {
        "name": "Natalino",
        "schedule": ["01/01", "04/01", "04/01"],  # 2x on 04/01
        "absences": [],
        "suspensions": [],
        "bonus_available": 0,
        "bonus_used": [{"date": "04/01/2026", "description": "Escala/Terço (E/T)"}]
    },
    {
        "name": "Sandro",
        "schedule": ["01/01", "04/01"],
        "absences": [],
        "suspensions": [],
        "bonus_available": 3,
        "bonus_used": []
    },
]

def populate_database():
    """Populate the database with all acolyte data."""
    print("=" * 60)
    print("POPULATING DATABASE WITH ACOLYTE DATA")
    print("=" * 60)
    
    acolytes = []
    
    for data in acolytes_data:
        print(f"\nCreating acolyte: {data['name']}")
        
        # Create acolyte
        acolyte = Acolyte(name=data['name'])
        
        # Add schedule history
        for date_str in data['schedule']:
            full_date = f"{date_str}/2026"
            # Detect weekday
            parts = date_str.split("/")
            day_name = "Quarta-feira"  # Default, should be calculated properly
            
            entry = ScheduleHistoryEntry(
                schedule_id=f"historical-{date_str}",
                date=full_date,
                day=day_name,
                time="18:00",  # Default time
                description="Missa"
            )
            acolyte.schedule_history.append(entry)
            acolyte.times_scheduled += 1
        
        print(f"  ✓ Added {len(data['schedule'])} schedule entries")
        
        # Add absences
        for absence_data in data['absences']:
            absence = Absence(
                date=absence_data['date'],
                description=absence_data['description']
            )
            acolyte.absences.append(absence)
        
        if data['absences']:
            print(f"  ✓ Added {len(data['absences'])} absences")
        
        # Add suspensions
        for suspension_data in data['suspensions']:
            suspension = Suspension(
                reason=suspension_data['reason'],
                start_date=suspension_data['start_date'],
                duration=suspension_data['duration'],
                is_active=suspension_data.get('is_active', False)
            )
            acolyte.suspensions.append(suspension)
            if suspension_data.get('is_active', False):
                acolyte.is_suspended = True
        
        if data['suspensions']:
            print(f"  ✓ Added {len(data['suspensions'])} suspensions")
        
        # Add bonus (earned)
        if data['bonus_available'] > 0:
            bonus_movement = BonusMovement(
                type='earn',
                amount=data['bonus_available'],
                description='Bônus disponível inicial',
                date='01/01/2026'
            )
            acolyte.bonus_movements.append(bonus_movement)
            acolyte.bonus_count = data['bonus_available']
            print(f"  ✓ Added {data['bonus_available']} bonus points")
        
        # Add used bonus
        for bonus_use in data['bonus_used']:
            bonus_movement = BonusMovement(
                type='use',
                amount=1,
                description=bonus_use['description'],
                date=bonus_use['date']
            )
            acolyte.bonus_movements.append(bonus_movement)
            acolyte.bonus_count -= 1
            print(f"  ✓ Used 1 bonus point on {bonus_use['date']}")
        
        acolytes.append(acolyte)
    
    # Save all data to the database
    print("\n" + "=" * 60)
    print("Saving to database...")
    data_manager.save_data(acolytes, [], [])
    print("✓ Database saved successfully!")
    
    # Verify
    loaded_acolytes, _, _ = data_manager.load_data()
    print(f"✓ Verified: {len(loaded_acolytes)} acolytes loaded from database")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for acolyte in sorted(acolytes, key=lambda a: a.name):
        print(f"{acolyte.name:20} - Escalas: {acolyte.times_scheduled:2}, "
              f"Faltas: {acolyte.absence_count}, "
              f"Suspensões: {acolyte.suspension_count}, "
              f"Bônus: {acolyte.bonus_count}")
    
    print("\n" + "=" * 60)
    print("✓ DATABASE POPULATION COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    populate_database()
