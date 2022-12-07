import { useNavigate, useSearchParams } from "react-router-dom";

const Edit = () => {
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();

  const id = searchParams.get("id");
  const mode = searchParams.get("mode");

  return (
    <div>
      <h1>Edit</h1>
      <p>this is page for Edit one</p>
      <button onClick={() => navigate("/home")}>home</button>
      <button onClick={() => navigate(-1)}>back</button>
    </div>
  );
};

export default Edit;
