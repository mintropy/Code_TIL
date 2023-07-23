function Modal(props) {
  function cancelHandler() {
    props.onCancle();
  }
  function confirmHandler() {
    props.onConfirm();
  }

  return (
    <div className="modal">
      <p>Are You Sure?</p>
      <button className="btn btn--alt" onClick={cancelHandler}>
        Cancle
      </button>
      <button className="btn" onClick={confirmHandler}>
        Confirm
      </button>
    </div>
  );
}

export default Modal;
