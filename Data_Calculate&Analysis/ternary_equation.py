def cal_3x3(args=[[0,0,0],
                  [0,0,0],
                  [0,0,0]]):
    # --------- 1  1       2  2       3  3       1  2       2  3      3  1        2  1       3  2       1  3
    basic = args[0][0] * args[1][1] * args[2][2] + args[0][1] * args[1][2] * args[2][0] + args[1][0] * args[2][1] * \
                                                                                          args[0][2]
    # ----------       1  3         2  2         3  1         1  1         2  3         3  2         3  3         1  2       2  1
    temp=0-args[0][2] * args[1][1] * args[2][0] - args[0][0] * args[1][2] * args[2][1] - args[2][2] * args[0][1] * \
                                                                                           args[1][0]
    return basic+temp

def get_x1_x2_x3(args=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]):
    common_val=cal_3x3([
                        [args[0][0],args[0][1],args[0][2]],
                        [args[1][0],args[1][1],args[1][2]],
                        [args[2][0],args[2][1],args[2][2]]
                       ]);
    #print("Start-----------------------get_x1_x2_x3")
    result_dict={}
    temp_val=cal_3x3([
                    [args[0][3],args[0][1],args[0][2]],
                    [args[1][3],args[1][1],args[1][2]],
                    [args[2][3],args[2][1],args[2][2]]
                   ])
    result_dict["X1"]=temp_val/common_val
    #print("X1:{}/{}".format(temp_val,common_val))


    temp_val=cal_3x3([
                      [args[0][0], args[0][3], args[0][2]],
                      [args[1][0], args[1][3], args[1][2]],
                      [args[2][0], args[2][3], args[2][2]]
                     ])
    result_dict["X2"]=temp_val/common_val
    #print("X2:{}/{}".format(temp_val,common_val))

    temp_val=cal_3x3([
                      [args[0][0], args[0][1], args[0][3]],
                      [args[1][0], args[1][1], args[1][3]],
                      [args[2][0], args[2][1], args[2][3]]
                     ])
    result_dict["X3"]=temp_val/common_val
    #print("X3:{}/{}".format(temp_val,common_val))

    #print("End-------------------------get_x1_x2_x3")

    return result_dict


