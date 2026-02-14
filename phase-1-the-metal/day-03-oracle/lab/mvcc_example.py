class OracleRow:
    def __init__(self, data, scn):
        self.data = data
        self.scn = scn  # System Change Number (Timestamp)
        self.undo_segment = []  # History of changes

    def update(self, new_data, new_scn):
        # 1. Save current state to Undo
        self.undo_segment.append((self.scn, self.data))
        # 2. Update current state
        self.data = new_data
        self.scn = new_scn

    def read_consistent(self, query_scn):
        """Reconstruct the row as it looked at query_scn"""
        # If current row is old enough, return it
        if self.scn <= query_scn:
            return self.data

        # Otherwise, go back in time (Undo)
        # print(f"   [MVCC] Row SCN {self.scn} is too new. Checking Undo...")
        for old_scn, old_data in reversed(self.undo_segment):
            if old_scn <= query_scn:
                return old_data
        return None  # Row didn't exist then


# --- The Simulation ---
row = OracleRow(data="Salary=1000", scn=100)

# 1. User A starts a long query at SCN 105
query_scn_A = 105
print(f"User A sees (Time 105): {row.read_consistent(query_scn_A)}")

# 2. User B updates the row at SCN 110
row.update(new_data="Salary=2000", new_scn=110)
print("User B committed Update to 2000 (Time 110).")

# 3. User A reads AGAIN (Should still see 1000, not 2000)
print(f"User A sees (Time 105): {row.read_consistent(query_scn_A)}")