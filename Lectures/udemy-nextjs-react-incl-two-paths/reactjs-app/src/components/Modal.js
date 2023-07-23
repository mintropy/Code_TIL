function Modal(props) {
  function cancelHandler() {
    props.onCancel();
  }
  function confirmHandler() {
    props.onConfirm();
  }

  return (
    <div classname="modal">
      <p>Are You Sure?</p>
      <button classname="btn btn--alt" onClick={cancelHandler}>
        Cancle
      </button>
      <button classname="btn" onClick={confirmHandler}>
        Confirm
      </button>
    </div>
  );
}

export default Modal;
