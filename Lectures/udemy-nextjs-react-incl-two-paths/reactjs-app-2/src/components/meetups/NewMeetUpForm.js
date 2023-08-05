import Card from "../ui/Card";
import styles from "./NewMeetUpForm.module.css";

function NewMeetUpForm() {
  return (
    <Card>
      <from className={styles.from}>
        <div className={styles.control}>
          <label htmlFor="title">MeetUp Title</label>
          <input type="text" required id="title" />
        </div>
        <div className={styles.control}>
          <label htmlFor="image">MeetUp Image</label>
          <input type="url" required id="image" />
        </div>
        <div className={styles.control}>
          <label htmlFor="address">Address</label>
          <input type="text" required id="address" />
        </div>
        <div className={styles.control}>
          <label htmlFor="description">Description</label>
          <textarea id="description" required rows="5"></textarea>
        </div>
        <div className={styles.actions}>
          <button>Add MeetUp</button>
        </div>
      </from>
    </Card>
  );
}
export default NewMeetUpForm;
